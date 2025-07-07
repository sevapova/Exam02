''' 6. Baholar tizimi
🧠 Vazifa: Talabalar ro‘yxati dict tarzida berilgan. O‘rtacha bahoni hisoblang. o'rtacha balldan yuqori baho olgan talabalarni chiqarish kerak.

➡️ Kirish:

students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}
'''

students = {
    
    'Ali': 5, 
    'Vali': 4, 
    'Hasan': 5, 
    'Husan': 3

}
def talabalarning_urtacha_bahosi(students):
    x = sum(students.values())
    avg = x / len(students)

    average = {}
    for name in students:
        if students[name] > avg:
            average[name] = students[name]

    print(f"O'rtacha baho: {avg:.2f}")
    return average

students = {}
print("Talabalar ismi va bahosini kiriting: ")

while True:
    name = input("Ism: ")
    if name.lower() == "stop":
        break

    baho = input("Baho: ")
    if baho.isdigit():
        baho = int(baho)
        if 1 <= baho <= 5:
            students[name] = baho
        else:
            print(" Baho 1 dan 5 gacha bo'lishi kerak.")
    else:
        print(" Noto'g'ri kiritish. Raqam kiriting.")

natija = talabalarning_urtacha_bahosi(students)
print("O'rtacha bahodan yuqori baho olgan talabalar:", natija)
