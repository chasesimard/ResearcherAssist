

✅ Full Copy-Paste README.md

# 📚 ResearcherAssist

AI-powered assistant for academic papers. Upload a PDF, ask deep questions, and get accurate answers — powered by LangChain, OpenAI, Supabase, Flask, and React.

> Ideal for students, researchers, and developers looking to understand papers faster and interactively.

---

## 🔍 Demo Screenshots
![image](https://github.com/user-attachments/assets/91d0869d-03cd-4aaa-80fa-03ca3904c33a)



### 🖼️ Upload PDF
reen![image](https://github.com/user-attachments/assets/b50059e6-10ac-46fe-a28f-ba75a9c54d93)


### 💬 Ask Questions
![qa](screenshots/qa.png)

---

## 🚀 Features

- 📄 Upload any PDF file (research paper, contract, article)
- 🧠 Automatic chunking, embedding via LangChain
- 🔎 Ask natural language questions — get contextual answers
- 💾 Supabase VectorStore for persistent retrieval
- ⚡ Modern React UI with Flask backend

---

## 🛠 Tech Stack

| Tech | Description |
|------|-------------|
| **React** | Lightweight frontend built with Vite |
| **Flask** | Fast backend for API endpoints |
| **LangChain** | Handles document chunking, embeddings, RAG |
| **OpenAI** | GPT-4 or 3.5 for answering queries |
| **Supabase** | Vector store for retrieval QA |
| **FAISS** | In-memory vector store for local dev (fallback) |

---

## 📦 Local Setup

### 1. Clone the repo

```bash
git clone git@github.com:chasesimard/ResearcherAssist.git
cd ResearcherAssist

2. Setup Python backend

cd backend
python -m venv .venv
source .venv/bin/activate  # or .venv\\Scripts\\activate on Windows
pip install -r requirements.txt
touch .env

Paste into .env:

OPENAI_API_KEY=sk-...
SUPABASE_URL=https://<your-project>.supabase.co
SUPABASE_API_KEY=ey...

python app.py



⸻

3. Setup React frontend

cd ../frontend
npm install
npm run dev

Navigate to http://localhost:5173

⸻

⚠️ Notes
	• Your PDF must be under 10MB and contain extractable text
	• For Supabase: create a documents table and match_documents function (see supabase.sql if included)

⸻

📄 License

MIT

⸻

👋 Contact

Made with 💡 by @chasesimard
Want to contribute? PRs welcome!

---

When you’re ready:
```bash
touch README.md
# paste the code above
git add README.md
git commit -m "Add polished README"
git push
