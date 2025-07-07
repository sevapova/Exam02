'''18. Sonlarni kvadratga oshirish (map + list[dict])
🧠 Vazifa: Har bir elementning value qiymatini kvadratga oshiring. Natija ham dict ko‘rinishida bo‘lsin.

➡️ Kirish:

numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]
⬅️ Chiqish:

[{'value': 4}, {'value': 9}, {'value': 16}]
'''

numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]

result = list(map(lambda x: {'value': x['value'] ** 2}, numbers))
print(result)
