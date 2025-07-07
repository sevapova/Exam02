'''7. Mahsulotlar savatchasi
🧠 Vazifa: Har bir mahsulot uchun narx va miqdor berilgan. Umumiy narxni hisoblang.

➡️ Kirish:

cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}
Tushuntirish: 3000*2 + 8000*1 + 5000*5 = 37000
⬅️ Chiqish:

Umumiy summa: 37000
'''

def umumiy_narx(cart):
    total = 0
    for item in cart.values():
        total += item['price'] * item['quantity']
    return total

cart = {
    'non': {'price': 3000, 'quantity': 2},
    'sut': {'price': 8000, 'quantity': 1},
    'olma': {'price': 5000, 'quantity': 5}
}

umumiy_summa = umumiy_narx(cart)
print(f"Umumiy narx: {umumiy_summa}")
