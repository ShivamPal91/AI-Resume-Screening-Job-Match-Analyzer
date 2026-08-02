from job_parser import read_job_description
from matcher import match_skills
from parser import extract_resume_text
from skills import extract_skills
from candidate_info import extract_candidate_info

# Resume path
pdf_path = "resumes/sample_resume.pdf"

# Extract resume text
resume = extract_resume_text(pdf_path)

# Extract candidate information
candidate = extract_candidate_info(resume)

# Extract skills
skills = extract_skills(resume)

job_skills = read_job_description("job_description/google_data_analyst.txt")

matched, missing = match_skills(skills, job_skills)

print("=" * 40)
print("Candidate Information")
print("=" * 40)

print("Email :", candidate["email"])
print("Phone :", candidate["phone"])
print("GitHub :", candidate["github"])
print("LinkedIn :", candidate["linkedin"])

print("\nDetected Skills")
print("----------------")

for skill in skills:
    print(skill)

print(f"\nTotal Skills Found: {len(skills)}")

print("\nMatched Skills")
print("----------------")

for skill in matched:
    print("✅", skill)

print("\nMissing Skills")
print("----------------")

for skill in missing:
    print("❌", skill)

score = (len(matched) / len(job_skills)) * 100

print("\n" + "=" * 40)
print(f"ATS Match Score : {score:.2f}%")
print("=" * 40)