'''13. Uzun ismlar (Input/students.json)
🧠 Vazifa: name uzunligi 5 harfdan oshadigan o‘quvchilarni aniqlang va Output/output13.json fayliga yozing.

⬅️ Output (misol):

{
  "long_names": [
    "Jasurbek", "Muhammad", "Abdulaziz", "Sherzod", "Alisher",
    "Kamola", "Rustam", "Ravshan", "Abdukarim", "Ziyoda"
  ]
}
'''


import json

with open('Input/students.json', 'r') as file:
    students = json.load(file)

names = [student["name"] for student in students if len(student["name"]) > 5]

with open('Output/output13.json', 'w') as file:
    json.dump({"Uzun ismlar": names}, file, indent=2)
