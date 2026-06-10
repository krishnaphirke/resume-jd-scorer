# 📄 Resume / JD Fit Scorer

> An AI-powered tool that analyzes how well a resume matches a Job Description using NLP techniques, semantic similarity, and keyword gap analysis.

---

## 🚀 Features

* 📤 Upload resumes in **PDF** or **DOCX** format
* 📝 Paste any **Job Description**
* 📊 Get an instant **Resume–JD Fit Score**
* 🎯 Receive a clear match verdict
* 🔍 Identify important keywords missing from your resume
* 🤖 Semantic matching powered by **all-MiniLM-L6-v2**
* ⚡ Clean and interactive Streamlit interface

---

## 🧠 How It Works

1. 📄 Extracts text from the uploaded resume
2. 🧹 Cleans and preprocesses resume and JD text
3. 📊 Uses **TF-IDF** to identify keyword overlap
4. 🤖 Uses **Sentence Transformers** to measure semantic similarity
5. 📐 Calculates cosine similarity scores
6. 🔍 Highlights keywords present in the Job Description but absent from the resume
7. 📈 Generates an overall Resume–JD Fit Score

---

## 🛠️ Tech Stack

* 🐍 Python
* 🎈 Streamlit
* 🤖 Scikit-learn
* 🧠 Sentence Transformers
* 📄 pdfplumber
* 📝 python-docx

---

## 📂 Project Structure

```text
resume-jd-scorer/
│
├── app.py
├── scorer.py
├── requirements.txt
├── README.md
```

---

## 💻 Run Locally

```bash
git clone https://github.com/krishnaphirke/resume-jd-scorer.git
cd resume-jd-scorer
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Project Highlights

* Combines keyword-based and semantic analysis for resume evaluation
* Helps job seekers identify gaps between their resume and a target role
* Provides actionable insights for improving ATS compatibility
* Lightweight, practical, and easy to use
* Deployed using Hugging Face Spaces

---

## 👨‍💻 Built By

**Krishna Yuvaraj Phirke**

🎓 B.E. Computer Engineering, TSEC Mumbai (2025–2029)

🤖 Minor in AI & Data Science, IIT Mandi

🔗 [LinkedIn](https://linkedin.com/in/krishnayuvarajphirke)

---

⭐ If you found this project useful, consider giving the repository a star.
