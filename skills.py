SKILLS = [
    "Python",
    "SQL",
    "Power BI",
    "Excel",
    "Tableau",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Scikit-learn",
    "Statistics",
    "MySQL",
    "Git",
    "GitHub",
    "Streamlit"
]

SKILL_ALIASES = {
    "Power BI": ["power bi", "powerbi"],
    "GitHub": ["github", "git hub"],
    "Scikit-learn": ["scikit-learn", "sklearn"],
    "NumPy": ["numpy"],
    "MySQL": ["mysql"]
}

def extract_skills(resume_text):

    found_skills = []

    resume_text = resume_text.lower()

    for skill in SKILLS:

        # Default keyword
        keywords = [skill.lower()]

        # Agar aliases hain to unhe bhi add karo
        if skill in SKILL_ALIASES:
            keywords.extend(SKILL_ALIASES[skill])

        # Kisi bhi keyword se match ho jaye
        for keyword in keywords:
            if keyword in resume_text:
                found_skills.append(skill)
                break

    return found_skills