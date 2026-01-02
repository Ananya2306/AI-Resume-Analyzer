import streamlit as st
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words('english'))



def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in STOP_WORDS]
    return " ".join(words)


def calculate_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer(
        analyzer="char",
        ngram_range=(3, 5)
    )
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    return similarity * 100


def extract_missing_skills(resume_text, jd_text, similarity_score):
    if similarity_score < 5:
        return ["Insufficient overlap between resume and job description"]

    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())

    missing = jd_words - resume_words
    return list(missing)[:10]




st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and paste a job description to get a match score.")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description here")

if st.button("Analyze"):
    if resume_file is None or job_description.strip() == "":
        st.warning("Please upload resume and enter job description.")
    else:
        resume_text = extract_text_from_pdf(resume_file)

        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(job_description)
        
        score = calculate_similarity(clean_resume, clean_jd)
        missing_skills = extract_missing_skills(clean_resume, clean_jd,score)

        st.success(f"✅ Match Score: {score:.2f}%")

        st.subheader("Skill Gaps Based on Job Description")
        if missing_skills:
            st.write(", ".join(missing_skills))
        else:
            st.write("No major missing skills detected.")
