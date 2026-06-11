import re

def analyze_resume(text: str):
    skills = []

    skill_keywords = [
        "python",
        "java",
        "c++",
        "sql",
        "machine learning",
        "deep learning",
        "html",
        "css",
        "javascript",
        "react",
        "mongodb",
        "nodejs",
        "data structures",
        "algorithms"
    ]

    text_lower = text.lower()

    for skill in skill_keywords:
        if skill in text_lower:
            skills.append(skill)

    score = min(len(skills) * 10, 100)

    if score >= 80:
        feedback = "Excellent resume profile."
    elif score >= 50:
        feedback = "Good profile. Add more projects and skills."
    else:
        feedback = "Needs improvement. Include more technical skills."

    return {
        "skills": skills,
        "ats_score": score,
        "feedback": feedback
    }
