SUGGESTION_MAP = {

    "Python": "Improve your Python programming skills and build more real-world projects.",

    "SQL": "Practice SQL queries including Joins, Window Functions, and CTEs.",

    "Power BI": "Create interactive Power BI dashboards and publish them in your portfolio.",

    "Excel": "Learn advanced Excel including Pivot Tables, Power Query, and XLOOKUP.",

    "Pandas": "Practice data cleaning, filtering, grouping, and analysis using Pandas.",

    "NumPy": "Learn NumPy arrays, indexing, broadcasting, and mathematical operations.",

    "Git": "Learn Git and use it for version control in your projects.",

    "GitHub": "Upload your projects to GitHub and maintain a professional portfolio.",

    "Statistics": "Strengthen your Statistics knowledge and apply it in data analysis projects.",

    "Communication": "Improve communication skills and highlight teamwork or presentation experience in your resume.",

    "Problem Solving": "Practice solving business problems using analytical thinking and real datasets.",

    "Critical Thinking": "Demonstrate critical thinking by explaining your project decisions and business insights."
}


def generate_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:

        if skill in SUGGESTION_MAP:

            suggestions.append(SUGGESTION_MAP[skill])

        else:

            suggestions.append(f"Consider learning {skill} to improve your ATS score.")

    return suggestions