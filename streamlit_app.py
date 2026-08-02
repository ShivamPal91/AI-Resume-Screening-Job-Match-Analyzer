import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from parser import extract_resume_text
from candidate_info import extract_candidate_info
from skills import extract_skills
from job_parser import read_job_description
from matcher import match_skills
from suggestions import generate_suggestions
from report_generator import generate_pdf_report

st.set_page_config(
    page_title="AI Resume Screening & Job Match Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening & Job Match Analyzer")

st.write("Welcome! Upload a resume to analyze ATS score.")

st.divider()

st.subheader("📤 Upload Resume")

uploaded_file = st.file_uploader(
    "Choose your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:
    
    pdf_bytes = uploaded_file.read()

    resume_text = extract_resume_text(pdf_bytes)
    candidate = extract_candidate_info(resume_text)

 #ATS logic
    required_skills = read_job_description(
        "job_description/google_data_analyst.txt"
)
    candidate_skills = extract_skills(resume_text)
    matched_skills, missing_skills, ats_score = match_skills(
    candidate_skills,
    required_skills
)
    suggestions = generate_suggestions(missing_skills)
    st.success("✅ Resume uploaded successfully!")
    #st.subheader("Resume Preview")
    #st.text(resume_text[:500])

    st.divider()
    left_column, right_column = st.columns(2)

    #st.text(f"Data Type: {type(pdf_bytes)}")

    with left_column:
        st.subheader("👤 Candidate Information")
        st.write(f"📧 Email : {candidate['email']}")
        st.write(f"📱 Phone : {candidate['phone']}")      
        st.write(f"💻 GitHub : {candidate['github']}")
        st.write(f"🔗 LinkedIn : {candidate['linkedin']}")
        st.divider()
        st.subheader("🛠 Detected Skills")
        for skill in candidate_skills:
            st.write(f"✅ {skill}")

        st.divider()
        st.subheader("📄 Export Report")
        
        pdf_file = generate_pdf_report(
            candidate,
            ats_score,
            matched_skills,
            missing_skills,
            suggestions
        )
        
        with open(pdf_file, "rb") as file:
                
            st.download_button(
                label="📥 Download ATS Analysis Report",
                data=file,
                file_name="AI_Resume_ATS_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    with right_column:
        st.subheader("📊 ATS Analysis")
        st.subheader("📊 Resume Match")

        if ats_score >= 80:
            gauge_color = "green"
        elif ats_score >= 60:
            gauge_color = "orange"
        else:
            gauge_color = "red"

        if ats_score >= 80:
            match_status = "🌟 Excellent Match"

        elif ats_score >= 60:
            match_status = "🟢 Strong Candidate"

        elif ats_score >= 40:
            match_status = "🟡 Needs Improvement"

        else:
            match_status = "🔴 Bad Match"

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=ats_score,

                number={
                    "suffix": "%",
                    "valueformat": ".2f",
                    "font": {"size": 40}
                },
                title={"text": ""},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": gauge_color}
                }
            )
        )
        gauge.update_layout(
            height=250,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(gauge, use_container_width=True)
        st.markdown(f"### {match_status}")
        #st.progress(ats_score / 100) 
        if ats_score >= 80:
            st.success("🌟 Excellent Match")

        elif ats_score >= 60:
            st.markdown("### 🟢 Good Match")

        elif ats_score >= 40:
            st.warning("⚠️ Average Match")

        else:
            st.error("❌ Poor Match")

        st.divider()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Matched", len(matched_skills))
        
        with col2:
            st.metric("Missing", len(missing_skills))
        
        with col3:
            st.metric("Required", len(required_skills))   

        #pie chart code 
        st.divider()
        labels = ["Matched", "Missing"]
        values = [
            len(matched_skills),
            len(missing_skills)
        ]
        fig = px.pie(
            names=labels,
            values=values,
            title="Skills Distribution",
            hole=0.5
        )
        fig.update_traces(textinfo="percent+label")
        fig.update_layout(
            showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True) 

        st.write("### ✅ Matched Skills")
        for skill in matched_skills:
            st.write(f"✅ {skill}")

        st.write("### ❌ Missing Skills")
        for skill in missing_skills:
            st.write(f"❌ {skill}")

        st.divider()
        
        st.subheader("💡 Resume Improvement Suggestions")
        for suggestion in suggestions:
            st.write(f"👉 {suggestion}")

        