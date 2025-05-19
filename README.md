# 📚 ResearcherAssist

AI-powered assistant for academic papers. Upload a PDF, ask deep questions, and get accurate answers — powered by LangChain, OpenAI, Supabase, Flask, and React.

> Ideal for students, researchers, and developers looking to understand papers faster and interactively.

---

## 🔍 Demo Screenshots

![image](https://github.com/user-attachments/assets/3ee749d6-3173-47a4-bcae-98c2e7c9e767)


### 🖼️ Upload PDF
![upload](screenshots/upload.png)

### 💬 Ask Questions
![image](https://github.com/user-attachments/assets/c570f5d3-256e-4eb0-b1ae-8ff61a5a17ac)


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
