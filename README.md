# 📄 PDF Chat Agent

_A zero‑cost, end‑to‑end AI agent that lets you **chat with any PDF** in plain English._

---

## ⚡ Key Highlights

- **Retrieval‑Augmented Generation (RAG)**: Combines TF‑IDF retrieval with a DistilBERT QA model  
- **100% Open Source & CPU‑Only**: No paid APIs or GPUs required  
- **Clean, Modular Python Code**: Demonstrates best practices in Python, NLP, and CLI tooling  
- **Universal Utility**: Instantly “chat” with whitepapers, reports, resumes, or any document  

---

## 🎥 Demo

1. **Upload** a PDF (e.g. `sample.pdf` on “Large Language Models…”).  
2. **Run** the CLI and ask:


3. **Get** instant, precise answers—no manual reading required!

---

## 🚀 Features

- **📄 PDF Parsing & Chunking**  
- Extracts text via PyPDF2  
- Splits into 1,000‑character chunks for efficient context management  

- **🔍 Smart Retrieval**  
- Builds a TF‑IDF index (scikit‑learn) over all chunks  
- Retrieves the top 5 most relevant segments per query  

- **🤖 Precise Q&A**  
- DistilBERT‑SQuAD (Hugging Face) for free‑form answers  
- Regex fallbacks for structured data (email, phone, numeric scores)  
- Section‑scoped extraction for list‑style sections (use cases, applications, evolution, references, challenges)  

- **💬 Interactive CLI**  
- Simple prompt: enter PDF name → ask any question → receive formatted answers  
- Easily swap in **any** PDF: whitepapers, business reports, resumes, and more  

---

## 🛠️ Tech Stack

- **Language**: Python 3.8+  
- **Libraries**:  
- PDF parsing: PyPDF2  
- Retrieval: scikit‑learn  
- NLP & QA: transformers (DistilBERT‑SQuAD), torch  
- **Environment**: Virtualenv, cross‑platform CLI  

---

## 📥 Installation

```bash
git clone https://github.com/your-username/pdf-chat-agent.git
cd pdf-chat-agent

python3 -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows (PowerShell)
# .\venv\Scripts\Activate.ps1

pip install -r requirements.txt

▶️ Usage
python app.py

Enter your PDF filename when prompted (e.g. sample.pdf)

Ask any question in natural language

Receive an instant, formatted answer



📂 Project Structure
pdf-chat-agent/
├── app.py             # CLI entry point
├── pdf_utils.py       # PDF extraction & chunking
├── retriever.py       # TF‑IDF retrieval logic
├── qa_pipeline.py     # QA model + regex & section extraction
├── sample.pdf         # Demo PDF
├── requirements.txt   # Python dependencies
├── README.md          # Project overview & instructions
├── LICENSE            # Open‑source license (MIT)
└── .gitignore         # Ignore venv, caches, etc.

🤝 Contributing
Contributions are welcome! Feel free to:

Add new file‑format support (e.g. DOCX, HTML)

Integrate a GUI (Streamlit, Flask)

Enhance retrieval (FAISS, semantic embeddings)

Improve QA accuracy or add new fallbacks


