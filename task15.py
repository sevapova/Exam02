'''15. Eng yuqori bahoni topish (Input/grades.csv)
🧠 Vazifa: grades.csv faylidan eng yuqori baho olgan o‘quvchini aniqlang va Output/output15.txt fayliga yozing.

⬅️ Output (misol):

Bahosi eng yuqori o‘quvchi: Ali - 5
'''


import csv

with open('Input/grades.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  

    max_grade = -1
    student = ""

    for i in reader:
        name = i[0]
        grade = int(i[1])
        if grade > max_grade:
            max_grade = grade
            student = name

with open('Output/output15.txt', 'w') as file:
    file.write(f"Bahosi eng yuqori o'quvchi: {student} - {max_grade}")
