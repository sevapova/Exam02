'''10. Tartiblash (Input/numbers.txt)
🧠 Vazifa: Fayldagi sonlarni tartiblang va Output/output10.txt fayliga yozing.

⬅️ Output (misol):

-8
-5
0
3
7
10
15
22
'''


f = open('Input/numbers.txt', 'r')
text = f.read()
f.close()

numbers = text.split()
numbers = [int(son) for son in numbers]

numbers.sort()

x = open('Output/output10.txt', 'w')
for son in numbers:
    x.write(str(son) + '\n')
x.close()

print("Tartiblangan sonlar Output/output10.txt fayliga yozildi.")
