# File: backend/app.py

import os
import tempfile
import traceback
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader, YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.vectorstores import SupabaseVectorStore
from langchain.chains import RetrievalQA
from supabase import create_client

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# ENV variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

# Supabase client
supabase_client = create_client(SUPABASE_URL, SUPABASE_API_KEY)

# LangChain components
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

def load_document(source_type, source):
    if source_type == "pdf":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(source.read())
            loader = PyPDFLoader(tmp.name)
    elif source_type == "url":
        loader = WebBaseLoader(source)
    elif source_type == "youtube":
        loader = YoutubeLoader.from_youtube_url(source)
    else:
        raise ValueError("Unsupported source type")
    return loader.load()

def process_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(docs)

def create_vectorstore(chunks):
    return SupabaseVectorStore.from_documents(
        chunks,
        embeddings,
        client=supabase_client,
        table_name="documents",
        query_name="match_documents",
        chunk_size=500
    )

def build_qa_chain():
    vectorstore = SupabaseVectorStore(
        embedding=embeddings,
        client=supabase_client,
        table_name="documents",
        query_name="match_documents",
    )
    retriever = vectorstore.as_retriever()
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

@app.route("/upload", methods=["POST"])
def upload():
    source_type = request.form.get("source_type")
    file = request.files.get("file")
    url = request.form.get("url")

    source = file if file else url
    if not source_type or not source:
        return jsonify({"error": "Missing source_type or source"}), 400

    try:
        docs = load_document(source_type, source)
        chunks = process_documents(docs)
        create_vectorstore(chunks)
        return jsonify({"message": "Document processed and stored."})
    except Exception:
        trace = traceback.format_exc()
        print("UPLOAD TRACEBACK:")
        print(trace)
        return jsonify({"error": trace}), 500

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        qa = build_qa_chain()
        answer = qa.run(question)
        return jsonify({"answer": answer})
    except Exception as e:
        print("ASK ERROR:", e)
        traceback.print_exc()
        return jsonify({"error": repr(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)