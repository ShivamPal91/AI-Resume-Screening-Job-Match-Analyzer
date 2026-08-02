def match_skills(candidate_skills, job_skills):

    matched = []

    missing = []

    for skill in job_skills:

        if skill in candidate_skills:

            matched.append(skill)

        else:

            missing.append(skill)

            total_required = len(job_skills)
            ats_score = (len(matched) / total_required) * 100

    return matched, missing, ats_score