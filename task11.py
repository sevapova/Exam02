''' 11. Ismlar soni (Input/students.json)
🧠 Vazifa: students.json faylidagi o‘quvchilar sonini hisoblang va natijani Output/output11.json fayliga yozing.

⬅️ Output (misol):

{
  "count": 20
}
'''


import json

with open('Input/students.json', 'r') as file:
    students = json.load(file)

count = len(students)

with open('Output/output11.json', 'w') as file:
    json.dump({"count": count}, file,indent=2)
