import streamlit as st
from PyPDF2 import PdfReader
from App import chat

st.set_page_config(page_title="RESUME ANALYSER")
st.title("Resume and Job Description Matcher")
st.markdown("Upload your resume and the job description to see how well they match!")

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += (page.extract_text() or "") + "\n"
    return text

uploaded_resume = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
uploaded_jd = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])
paste_jd = st.text_area("Or paste the Job Description here", height=200)

job_description = ""

# Priority: use pasted text if provided, else use uploaded JD PDF
if paste_jd.strip():
    job_description = paste_jd
elif uploaded_jd:
    job_description = extract_text_from_pdf(uploaded_jd)

if uploaded_resume and job_description:
    resume_text = extract_text_from_pdf(uploaded_resume)
    if st.button("Analyze Match"):
        with st.spinner("Analyzing..."):
            result = chat(resume_text, job_description)
        st.subheader("Match Analysis Result")
        st.json(result)