''' 1. Calculator (Kalkulyator)
🧠 Vazifa: Foydalanuvchi ikkita son va amal kiritadi (+, -, *, /). Siz tegishli natijani hisoblab chiqaring.

➡️ Kirish:

Son 1: 8
Amal: *
Son 2: 5
⬅️ Chiqish:

Natija: 40
🔧 Funksiyalar:

def add(a, b): ...
def subtract(a, b): ...
def multiply(a, b): ...
def divide(a, b): ...
'''

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Xatolik: 0 ga bo'lish mumkin emas!"
    return a / b

def main():
    
        a = float(input("Birinchi son: "))
        op = input("Amal (+, -, *, /): ")
        b = float(input("Ikkinchi son: "))

        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)
        else:
            result = "Xato!"

        print("Natija:", result)


main()
