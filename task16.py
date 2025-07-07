'''16. Bahosi 5 bo‘lganlar soni (Input/grades.csv)
🧠 Vazifa: grades.csv faylidan bahosi 5 bo‘lganlar sonini hisoblang va Output/output16.txt fayliga yozing.

⬅️ Output (misol):

5 baho olganlar soni: 6
'''



import csv

with open('Input/grades.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  

    count = sum(1 for i in reader if int(i[1]) == 5)

with open('Output/output16.txt', 'w') as file:
    file.write(f"5 baho olganlar soni: {count}")
