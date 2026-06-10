import pdfplumber
import docx
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


TECHNICAL_KEYWORDS = {
    'python', 'java', 'javascript', 'typescript', 'sql', 'nosql', 'docker',
    'kubernetes', 'aws', 'azure', 'gcp', 'spring', 'react', 'angular', 'vue',
    'node', 'git', 'api', 'rest', 'restful', 'microservices', 'postgresql',
    'mysql', 'mongodb', 'redis', 'tensorflow', 'pytorch', 'scikit', 'pandas',
    'numpy', 'hadoop', 'spark', 'kafka', 'jenkins', 'linux', 'bash', 'html',
    'css', 'flask', 'django', 'fastapi', 'streamlit', 'hibernate', 'maven',
    'gradle', 'junit', 'selenium', 'graphql', 'grpc', 'agile', 'scrum',
    'devops', 'mlops', 'nlp', 'deep', 'machine', 'neural', 'algorithm',
    'database', 'cloud', 'serverless', 'distributed', 'concurrent', 'orm',
    'jpa', 'golang', 'rust', 'kotlin', 'android', 'ios', 'embedded',
    'microservice', 'container', 'backend', 'frontend', 'fullstack', 'tableau',
    'powerbi', 'excel', 'data', 'structure', 'network', 'learning', 'cicd'
}

SOFT_KEYWORDS = {
    'communication', 'leadership', 'teamwork', 'collaborate', 'analytical',
    'problem', 'solving', 'management', 'stakeholder', 'presentation',
    'adaptability', 'creativity', 'critical', 'thinking', 'organization',
    'initiative', 'proactive', 'motivated', 'mentor', 'negotiate', 'flexible',
    'attention', 'detail', 'interpersonal', 'resilience', 'ownership'
}

NOISE_WORDS = {
    'bengaluru', 'india', 'mumbai', 'delhi', 'bangalore', 'intern', 'interns',
    'academic', 'building', 'company', 'high', 'core', 'good', 'strong',
    'basic', 'ability', 'work', 'role', 'team', 'using', 'understanding',
    'experience', 'knowledge', 'skills', 'year', 'years', 'degree', 'apply',
    'products', 'systems', 'design', 'enterprise', 'leader', 'actively',
    'comprehensive', 'actively', 'applications', 'qualifications', 'preferred'
}

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text


def extract_text_from_docx(file):
    doc = docx.Document(file)
    paragraphs = [para.text for para in doc.paragraphs]
    return "\n".join(paragraphs)


def extract_resume_text(file):
    file_name = file.name.lower()
    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif file_name.endswith(".docx"):
        return extract_text_from_docx(file)
    return ""


def clean_text(text):
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

    text = text.lower()

    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def split_into_chunks(text, min_length=20):
    chunks = re.split(r'[\n.•\-*]', text)
    clean_chunks = [chunk.strip() for chunk in chunks if len(chunk.strip()) >= min_length]
    return clean_chunks


def get_semantic_score(resume_text, jd_text, model):

    resume_chunks = split_into_chunks(resume_text)
    jd_chunks = split_into_chunks(jd_text)

    if not resume_chunks:
        resume_chunks = [resume_text]
    if not jd_chunks:
        jd_chunks = [jd_text]

    resume_embeddings = model.encode(resume_chunks, show_progress_bar=False)
    jd_embeddings = model.encode(jd_chunks, show_progress_bar=False)

    best_match_scores = []
    for jd_embedding in jd_embeddings:
        similarities = cosine_similarity([jd_embedding], resume_embeddings)[0]
        best_match_scores.append(np.max(similarities))

    raw_score = np.mean(best_match_scores)

    normalized_score = (raw_score - 0.2) / (0.9 - 0.2)
    final_score = max(0, min(1, normalized_score)) * 100

    return round(final_score, 2)


def get_categorized_gaps(resume_text, jd_text):
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(jd_text)

    vectorizer = TfidfVectorizer(stop_words='english', max_features=40)
    vectorizer.fit([cleaned_jd])
    jd_keywords = set(vectorizer.get_feature_names_out())

    resume_words = set(cleaned_resume.split())
    missing_keywords = jd_keywords - resume_words

    missing_keywords = {
        word for word in missing_keywords
        if len(word) > 2 and not word.isnumeric()
    }

    technical_gaps = sorted([w for w in missing_keywords if w in TECHNICAL_KEYWORDS])
    soft_gaps = sorted([w for w in missing_keywords if w in SOFT_KEYWORDS])
    domain_gaps = sorted([
        w for w in missing_keywords
        if w not in TECHNICAL_KEYWORDS
        and w not in SOFT_KEYWORDS
        and w not in NOISE_WORDS
    ])

    return technical_gaps, soft_gaps