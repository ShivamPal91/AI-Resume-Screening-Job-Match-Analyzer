import re


def extract_candidate_info(resume_text):

    info = {
        "email": None,
        "phone": None,
        "github": None,
        "linkedin": None
    }

    # Email
    email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', resume_text)

    if email:
        info["email"] = email.group()

    # Phone Number
    phone = re.search(r'(\+91[- ]?)?[6-9]\d{9}', resume_text)

    if phone:
        info["phone"] = phone.group()

    # GitHub
    github = re.search(
    r'(https?://)?(www\.)?github\.com/\S+',
    resume_text
    )
    if github:
        info["github"] = github.group()

    # LinkedIn
    linkedin = re.search(
    r'(https?://)?(www\.)?linkedin\.com/in/\S+',
    resume_text
    )

    if linkedin:
        info["linkedin"] = linkedin.group()

    return info