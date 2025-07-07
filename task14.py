'''14. “A” bilan boshlanuvchilarni ajratish (Input/students.json)
🧠 Vazifa: name qiymati "A" harfi bilan boshlanuvchi o‘quvchilarni toping va Output/output14.json fayliga yozing.

⬅️ Output (misol):

{
  "a_names": [
    "Ali", "Abdulaziz", "Anvar", "Alisher", "Abdukarim", "Aziza", "Aziz"
  ]
}
'''



import json

with open('Input/students.json', 'r') as file:
    students = json.load(file)

a_names = [student["name"] for student in students if student["name"].startswith("A")]

with open('Output/output14.json', 'w') as file:
    json.dump({"A harfi bilan boshlanuvchi ismlar": a_names}, file, indent=2)
