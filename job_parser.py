def read_job_description(file_path):

    with open(file_path, "r") as file:

        skills = []

        for line in file:

            line = line.strip()

            if line:

                skills.append(line)

    return skills