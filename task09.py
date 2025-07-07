'''9. Eng katta son (Input/numbers.txt)
🧠 Vazifa: Fayldagi eng katta sonni toping va Output/output09.txt fayliga yozing.

⬅️ Output (misol):

Eng katta son: 22

'''

with open('Input/numbers.txt', 'r') as file:
    data = file.read()

numbers = list(map(int, data.split()))

max_number = max(numbers)

with open('Output/output09.txt', 'w') as file:
    file.write(f"Eng katta son: {max_number}")
    