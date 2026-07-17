import re

resume = """
Name: Varun Reddy
Email: varunreddy@gmail.com
Mobile: 9876543210
Skills: Python, Java, SQL, Machine Learning, NLP
Experience: 3 years
"""

name = re.search(r"Name:\s*(.*)", resume)
if name:
    name = name.group(1)

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", resume)

mobile = re.findall(r"\b[6-9]\d{9}\b", resume)

skills = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
found_skills = []

for skill in skills:
    if re.search(skill, resume, re.IGNORECASE):
        found_skills.append(skill)

exp = re.search(r"(\d+)\s+years", resume)
experience = int(exp.group(1)) if exp else 0

print("Candidate Summary")
print("--------------------")
print("Name:", name)
print("Email:", emails)
print("Mobile:", mobile)
print("Skills:", found_skills)
print("Experience:", experience, "years")

if experience >= 2 and "Python" in found_skills:
    print("Eligible for Shortlisting")
else:
    print("Not Eligible")