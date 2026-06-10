<<<<<<< HEAD
---
title: Resume JD Fit Scorer
emoji: 📄
colorFrom: blue
colorTo: indigo
sdk: streamlit
app_file: app.py
pinned: false
---

# 📄 Resume / JD Fit Scorer

An AI-powered tool that analyzes how well your resume matches a Job Description using **TF-IDF vectorization** and **cosine similarity**.

## Features
- Upload your resume as PDF or DOCX
- Paste any Job Description
- Get an instant fit score with verdict
- See exactly which JD keywords are missing from your resume

## How It Works
1. Extracts and cleans text from your resume and the JD
2. Vectorizes both using **TF-IDF** (Term Frequency-Inverse Document Frequency)
3. Computes **cosine similarity** between the two vectors as the fit score
4. Identifies high-value JD keywords absent from your resume

> Note: Scores are relative, not absolute. A score of 20–40% indicates strong alignment in this model. TF-IDF cosine similarity naturally produces lower values due to vocabulary sparsity between resume and JD text.

## Tech Stack
`Python` · `Scikit-learn` · `Streamlit` · `pdfplumber` · `python-docx`

## Run Locally
```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/resume-jd-scorer
cd resume-jd-scorer
pip install -r requirements.txt
streamlit run app.py
```

## Built By
**Krishna Yuvaraj Phirke**  
B.E. Computer Engineering, TSEC Mumbai (2025–2029)  
Minor in AI & Data Science, IIT Mandi  
[LinkedIn](https://linkedin.com/in/krishnayuvarajphirke) · [GitHub](https://github.com/krishnaphirke)

=======
# resume-jd-scorer
>>>>>>> f64d9e2d50f1323333b3a08844c2c9069c78e49d
