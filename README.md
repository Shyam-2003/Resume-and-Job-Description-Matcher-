# Resume and Job Description Matcher

This project is a **Streamlit web application** that analyzes how well a resume matches a given job description.  
It uses **LangChain + Ollama** for LLM‑powered analysis and **PyPDF2** for PDF text extraction.

---

## Features
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

# To install dependencies
  pip install -r requirements.txt

# To Run a Application in web
  streamlit run main.py

PROJECT HIERARCHY
-- App.py
-- main.py
-- requirements.txt
