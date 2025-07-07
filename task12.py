'''12. Ismlarni alfavit bo‘yicha tartiblash (Input/students.json)
🧠 Vazifa: students.json faylidagi barcha name maydonlarini alfavit bo‘yicha tartiblang va Output/output12.json fayliga yozing.

⬅️ Output (misol):

{
  "sorted_names": [
    "Abdukarim", "Abdulaziz", "Ali", "Alisher", "Anvar", "Aziza", "Aziz",
    "Diyor", "Jasurbek", "Kamola", "Lola", "Madina", "Muhammad", "Olim",
    "Ravshan", "Rustam", "Sardor", "Sherzod", "Umida", "Ziyoda"
  ]
}'''


import json

with open('Input/students.json', 'r') as file:
    students = json.load(file)

names = [student["name"] for student in students]

names.sort()

with open('Output/output12.json', 'w') as file:
    json.dump({"Tartiblangan ismlar": names}, file, indent=2)
