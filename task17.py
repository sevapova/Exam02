'''17. Musbat sonlarni ajratish (filter + list[dict])
🧠 Vazifa: Quyidagi ro‘yxatdan qiymati musbat bo‘lgan sonlarni ajrating (value qiymati bo‘yicha). Har bir element dict ko‘rinishida.

➡️ Kirish:

numbers = [
    {'value': -5}, 
    {'value': 10}, 
    {'value': -1}, 
    {'value': 7}
]
⬅️ Chiqish:

[{'value': 10}, {'value': 7}]
'''



numbers = [
    {'value': -5}, 
    {'value': 10}, 
    {'value': -1}, 
    {'value': 7}
]

x=list(filter(lambda x: x['value'] > 0, numbers))
print("Musbat sonlar:")
for i in x:
    print(i)