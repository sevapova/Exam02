'''3. Tax Calculator
🧠 Vazifa: Maoshga qarab soliqni hisoblang va sof maoshni chiqaring.

Shart:

Maosh 5,000,000 dan katta bo‘lsa → soliq 20%
Aks holda → soliq 13%
➡️ Kirish:

Maosh: 6_000_000
⬅️ Chiqish:

Soliq: 1_200_000
Sof maosh: 4_800_000
🔧 Funksiyalar:

def calculate_tax(salary): ...
def calculate_net_salary(salary): ...
'''

def calculate_tax(salary): 
    if salary > 5000000:
        return salary * 0.2
    else: 
        return salary * 0.13

def calculate_net_salary(salary): 

    tax = calculate_tax(salary)
    net_salary = salary - tax
    return tax, net_salary

def main():
   
        salary = int(input("Maoshni kiriting: "))
        tax, x = calculate_net_salary(salary)
        print(f"Soliq: {tax:,}")
        print(f"Maosh: {x:,}")

    
main()