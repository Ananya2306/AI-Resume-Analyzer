# 📄 AI Resume Analyzer & Job Match System

A web-based AI application that analyzes a candidate’s resume against a given job description to estimate job fit and highlight potential skill gaps.

The system focuses on real-world NLP challenges such as unstructured text, noisy PDF extraction, and low-context job descriptions, while keeping the logic explainable and practical.

🔗 **Live App:**  
```
https://er-ananya-ai-resume-analyzer.streamlit.app/
```


## 🚀 Features

- Upload resume in PDF format  
- Paste any job description  
- Extracts and cleans unstructured text  
- Computes a resume–job match score (%)  
- Identifies missing or weak skill keywords  
- Handles noisy PDFs using character-level NLP  
- Deployed as a live web application  


## 🧠 How It Works

1. **Resume Upload**  
   Resume PDF is parsed using `pdfplumber` to extract raw text.

2. **Text Cleaning**  
   - Lowercasing  
   - Removal of special characters  
   - Stopword filtering  

3. **Vectorization**  
   Resume and job description are converted into numerical vectors using **character-level TF-IDF (n-grams)** to handle broken or noisy text commonly found in PDFs.

4. **Similarity Calculation**  
   Cosine similarity is used to compute a match score between the resume and job description.

5. **Skill Gap Detection**  
   Keywords present in the job description but missing from the resume are highlighted as potential skill gaps, with guardrails to avoid misleading results when overlap is too low.


## 🛠️ Tech Stack

- **Language:** Python  
- **NLP:** TF-IDF, Cosine Similarity  
- **PDF Parsing:** pdfplumber  
- **Web Framework:** Streamlit  
- **Libraries:** scikit-learn, NLTK  


## 📂 Project Structure

```
ai-resume-analyzer/
│── app.py
│── requirements.txt
```

## ⚙️ Local Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Ananya2306/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app
```bash
streamlit run app.py
```

## ⚠️ Known Limitations

- Image-based or Canva-designed resumes do not contain a text layer and cannot be parsed without OCR.

- This version supports text-based PDFs only.

- OCR integration (e.g., Tesseract) is a planned enhancement.


## 💡 Key Learnings

- Real-world resumes are often noisy and inconsistently formatted

- Word-level NLP fails on broken PDF text

- Character-level n-grams significantly improve robustness

- Input quality is as important as model choice

- Explainable ML is crucial for trust and usability


## 🔮 Future Improvements

- OCR support for image-based resumes

- Section-wise scoring (Skills, Experience, Projects)

- Skill normalization using a predefined skill taxonomy

- LLM-based feedback and resume suggestions

## 👩‍💻 Author

Ananya

B.Tech CSE (AI & ML)

Focused on building practical AI systems through hands-on projects

🔗 LinkedIn:
```
 https://www.linkedin.com/in/ananya-61314128b/
```
