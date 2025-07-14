'''2. Simple ATM Simulation
🧠 Vazifa: Foydalanuvchi quyidagi amallardan birini bajaradi:

Pul qo‘yish (deposit)
Pul yechish (withdraw)
Balansni ko‘rish (check balance)
➡️ Kirish:

Boshlang‘ich balans: 100000
Amal: deposit
Miqdor: 50000
⬅️ Chiqish:

Yangi balans: 150000
🔧 Funksiyalar:

def deposit(balance, amount): ...
def withdraw(balance, amount): ...
def check_balance(balance): ...
'''


def deposit(balance, amount): 
    if amount <= 0:
        return balance, "Xato!"
    balance += amount
    return balance, f"Yangi balans: {balance}"
def withdraw(balance, amount): 
    if amount <= 0:
        return balance, "Xatolik!"
    if amount > balance:
        return balance, "Xatolik!"
    balance -= amount
    return balance, f"Yangi balans: {balance}"

def check_balance(balance): 
        return balance, f"Joriy balans: {balance}"

def main():
    balance = 100000 
    print("Xush kelibsiz!")
    print("Amallar: deposit, withdraw, check")
    x = input("Amalni tanlang: ").strip().lower()

    if x == "deposit":
        amount = float(input("Miqdor: "))
        balance, x = deposit(balance, amount)
        print(x)
    elif x == "withdraw":
        amount = float(input("Miqdor: "))
        balance, x = withdraw(balance, amount)
        print(y)
    elif x == "check":
        y = check_balance(balance)
        print(y)
    else:
        print("Xato!")

main()


