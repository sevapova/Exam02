'''20. Eng qisqa ismli o‘quvchini topish (min + list[dict])
🧠 Vazifa: Quyidagi o‘quvchilar ro‘yxatidan ismi eng qisqa bo‘lgan o‘quvchini toping.

➡️ Kirish:

students = [
    {'name': 'Ali', 'age': 18},
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Muhammad', 'age': 21}
]
⬅️ Chiqish:

Ali
'''

students = [
    {'name': 'Ali', 'age': 18},
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Muhammad', 'age': 21}
]

name = min(students, key=lambda x: len(x['name']))['name']
print(name)
