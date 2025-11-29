# 📄 Resume and Job Description Matcher

This project is a **Streamlit web application** that analyzes how well a resume matches a given job description.  
It uses **LangChain + Ollama** for LLM‑powered analysis and **PyPDF2** for PDF text extraction.

---

## 🚀 Features
- Upload your **resume (PDF)**.
- Upload or paste a **job description (PDF or text)**.
- Analyze the match using an LLM (via Ollama).
- Get structured JSON output with:
  - Job Title match
  - Roles & Responsibilities match
  - Years of Experience match
  - Keywords match
  - Scores (out of 10)
  - Summary
  - Suggestions for improvement

---

## 📦 Installation

1. **Clone or download** this repository into your local machine.

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
