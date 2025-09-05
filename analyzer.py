import re
import csv

# Job description
job_description = """
We are looking for a backend developer with experience in Python, Django, SQL, AWS, Kubernetes, Azure. 
Knowledge of Docker and good teamwork skills are a plus.
""".lower()

# Resumes
resumes = {
    "Rahul Sharma": """
    Java, SpringBoot, SQL, Kubernetes, Azure, Python, AWS, Teamwork
    """.lower(),
    "Riya Shinde": """
    Python, Django, SQL, AWS, Docker, Teamwork , Communication, 
    kubernetes
    """.lower()
}

def extract_words(text):
    """
    Extract words/phrases from text. Remove punctuation and split by comma or whitespace.
    """
    text = re.sub(r"[,\-/]", " ", text)
    words = text.split()
    words = [w for w in words if len(w) > 1]
    return set(words)

# Extract words from job description
job_words = extract_words(job_description)

# Prepare CSV file
with open("resume_analysis.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Skills Found in Resume", "Skills Matched with Job", "Match Score (%)"])
    
    results = []

    # Analyze resumes
    for name, text in resumes.items():
        resume_words = extract_words(text)
        matched_skills = resume_words.intersection(job_words)
        score = len(matched_skills)/len(job_words)*100 if job_words else 0
        score = round(score, 2)
        results.append((name, resume_words, matched_skills, score))

    # Sort results by match score descending
    results.sort(key=lambda x: x[3], reverse=True)

    # Write to CSV
    for name, resume_words, matched_skills, score in results:
        writer.writerow([
            name,
            ", ".join(resume_words),
            ", ".join(matched_skills),
            score
        ])

print("Analysis saved to 'resume_analysis.csv'")
