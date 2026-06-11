from resume_tool import analyze_resume

print("\nAI Resume Analyzer MCP\n")

resume_text = input("Paste Resume Text:\n\n")

result = analyze_resume(resume_text)

print("\n===== RESULT =====")

print(f"\nATS Score: {result['ats_score']}")

print("\nSkills Found:")
for skill in result["skills"]:
    print("-", skill)

print("\nFeedback:")
print(result["feedback"])
