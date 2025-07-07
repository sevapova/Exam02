'''4. FISH tartibini o‘zgartirish
🧠 Vazifa: Foydalanuvchi FISH (Familiya Ism Sharif) kiritadi. Siz uni Ism Sharif, Familiya shaklida chiqarishingiz kerak.

➡️ Kirish: "Aliyev Vali G'aniyevich" ⬅️ Chiqish: "Vali G'aniyevich, Aliyev"
'''

def reorder_fish(fish):
    a = fish.strip().split()
    if len(a) < 3:
        return "Xato!"
    familiya = a[0]
    ism_sharif = " ".join(a[1:])
    return f"{ism_sharif}, {familiya}"

def run_fish_reorder():
    fish = input("FISH ni kiriting: ").title()
    result = reorder_fish(fish)
    print("Natija:", result)

run_fish_reorder()
