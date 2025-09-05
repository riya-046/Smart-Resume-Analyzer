Smart Resume Analyzer

A simple Python project that analyzes resumes against a given job description and calculates a **match score** based on skills. It extracts relevant skills from resumes, compares them with job requirements, and exports the results into a CSV file for easy viewing in Excel.

Features:-
- Extracts skills from job descriptions and resumes  
- Calculates a match percentage for each candidate  
- Displays matched skills  
- Saves results into a CSV file for Excel analysis  
- Easy to extend with more skills or new resumes  

Structure:
smart_resume_analyzer/
│── .venv/              # already created
│── resumes/            # put sample resume in te xt formathere
│── skills.json         # list of skills to check
│── analyzer.py         # main script
|── job.txt             # put job description
|── resume_analysis.csv # open in excel
