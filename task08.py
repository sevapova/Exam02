'''8. Yig‘indi (Input/numbers.txt)
🧠 Vazifa: Input/numbers.txt faylida berilgan sonlar yig‘indisini hisoblang va Output/output08.txt fayliga yozing.

⬅️ Output (misol):

Yig'indi: 44

'''
with open('Input/numbers.txt', 'r') as file:
    data = file.read()

numbers = list(map(int, data.split()))

total = sum(numbers)

with open('Output/output08.txt', 'w') as file:
    file.write(f"Yig'indi: {total}")
