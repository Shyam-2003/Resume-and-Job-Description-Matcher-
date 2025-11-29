The Resume and Job Description Matcher is a Streamlit based web application designed to help job seekers and recruiters quickly evaluate how well a resume aligns with a specific job description.
Users can upload their resume in PDF format and either upload or paste a job description. The app extracts text from both documents using PyPDF2 and then leverages LangChain with Ollama to analyze the match.
The analysis is returned in a structured JSON format, covering:
•	Job Title Match – alignment between the resume’s title and the job role.
•	Roles & Responsibilities Match – comparison of duties listed in the resume vs. the job description.
•	Years of Experience Match – evaluation of experience requirements.
•	Keywords Match – overlap of important skills and keywords.
•	Scores – numeric ratings (out of 10) for each category.
•	Summary & Suggestions – overall assessment and recommendations to improve the resume.
This tool provides a fast, AI powered way to identify gaps and strengths in a resume relative to a job posting, making it useful for candidates preparing applications and recruiters screening resumes.
