import streamlit as st
from sentence_transformers import SentenceTransformer
from scorer import extract_resume_text, get_semantic_score, get_categorized_gaps


st.set_page_config(
    page_title = "Resume JD Fit Scorer",
    page_icon = "📄",
    layout = "centered"
)


@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')


model = load_model()


st.title("📄 Resume / JD Fit Scorer")
st.markdown("Upload your resume and paste a job description to see how well your profile matches the role.")
st.divider()


col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Resume")
    uploaded_file = st.file_uploader("Upload PDF or DOCX", type = ["pdf", "docx"])

with col2:
    st.subheader("Job Description")
    jd_text = st.text_area(
        "Paste the JD here",
        height = 300,
        placeholder = "Paste the full job description here..."
    )

st.divider()


if st.button("Analyze Fit", use_container_width = True, type = "primary"):

    if not uploaded_file:
        st.warning("Please upload your resume to continue.")
    elif not jd_text.strip():
        st.warning("Please paste a job description to continue.")
    else:
        with st.spinner("Analyzing your resume against the job description..."):

            resume_text = extract_resume_text(uploaded_file)

            if not resume_text.strip():
                st.error("Could not read text from your file. Please try a different format.")
            else:
                score = get_semantic_score(resume_text, jd_text, model)
                technical_gaps, soft_gaps = get_categorized_gaps(resume_text, jd_text)

                # Show the fit score
                st.subheader("Your Fit Score")

                if score >= 60:
                    st.success(f"### {score}% Match")
                    verdict = "Strong match. Your resume aligns well with this role."
                elif score >= 35:
                    st.warning(f"### {score}% Match")
                    verdict = "Moderate match. A few targeted improvements could boost your chances."
                else:
                    st.error(f"### {score}% Match")
                    verdict = "Low match. There are significant gaps between your resume and this JD."

                st.markdown(f"**{verdict}**")
                st.progress(float(min(score / 100, 1.0)))

                st.divider()

                # Show missing keywords
                st.subheader("Keyword Gap Analysis")
                st.markdown("Specific technical and soft skill keywords from the JD that are absent in your resume. A clean result here means the JD uses non-standard phrasing, not that your resume is a perfect match.")

                col_t, col_s = st.columns(2)

                with col_t:
                    st.markdown("**Technical Skills**")
                    if technical_gaps:
                        for word in technical_gaps[:10]:
                            st.markdown(f"- `{word}`")
                    else:
                        st.success("No tracked keywords missing")

                with col_s:
                    st.markdown("**Soft Skills**")
                    if soft_gaps:
                        for word in soft_gaps[:10]:
                            st.markdown(f"- `{word}`")
                    else:
                        st.success("No tracked keywords missing")

                st.divider()

                with st.expander("View Extracted Resume Text"):
                    st.text(resume_text[:7000])


# Footer
st.markdown("---")
st.caption("Built by Krishna Yuvaraj Phirke")