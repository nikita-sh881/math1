import math

def module(): 
    z = read_complex()
    z[0] = math.abs(z[0]) 
    z[1] = math.abs(z[1])
    return math.sqrt((z[0]*z[0])+(z[1]*z[1])) 

def argument():
    z = read_complex()
    return math.atan2(z[0], z[1]) 

def sum_complex():
    z1 = read_complex()
    z2 = read_complex() 
    return [z1[0]+z2[0], z1[1]+z2[1]]

def sub_comlex():
    z1 = read_complex()
    z2 = read_complex()
    return [z1[0]-z2[0], z1[1]-z2[1]]

def mul_complex():
    z1 = read_complex()
    z2 = read_complex()
    return [(z1[0]*z2[0])-(z1[1]*z2[1]), (z1[0]*z2[1])-(z2[0]*z1[1])]

def div_complex():
    z1 = read_complex()
    z2 = read_complex()
    return [(z1[0]*z2[0] + z1[1]*z2[1])/(z2[0]*z2[0] + z2[1]*z2[1]), (z2[0]*z1[1] - z1[0]*z2[1])/(z2[0]*z2[0] + z2[1]*z2[1])]

def read_natural(prompt):
    while True:
        s = input(prompt).strip()
        if not s.isdigit() or int(s) == 0:
            print("  Ошибка: нужно натуральное число (целое > 0). Попробуйте снова.")
            continue
        return int(s)

def read_complex():
    C = [] 
    print("\nВведите значения действительной и мнимой частей комплексного числа (2 натуральных числа):")
    C.append(read_natural(f"  X = "))
    C.append(read_natural(f"  Yi = "))
    return C 

def show_complex(z): 
    if z[1] < 0:
        print(f"z = {z[0]} - {z[1]}i")
    else:
        print(f"z = {z[0]} + {z[1]}i")

def show_trig():
    z = read_complex() 
    r = module(z) 
    a = argument(z) 
    print(f"{r}(cos({a}) + isin({a}))")

print("Калькулятор операций с комплексными числами (ввод — только натуральные числа)")

while True:
    print("\nМеню:")
    print("  1 — Вычислить модуль")
    print("  2 — Вычислить аргумент")
    print("  3 — Вычислить сумму")
    print("  4 — Вычислить разность")
    print("  5 — Вычислить произведение")
    print("  6 — Вычислить частное")
    print("  7 — Показать тригонометрическую форму")
    print("  0 — выход")
    choice = input("Выбор: ").strip()

    if choice == "0":
        break
    elif choice == "1":
        show_complex(module())
    elif choice == "2":
        show_complex(argument())
    elif choice == "3":
        show_complex(sum_complex())
    elif choice == "4":
        show_complex(sub_comlex())
    elif choice == "5":
        show_complex(mul_complex())
    elif choice == "6":
        show_complex(div_complex())
    elif choice == "7":
        show_trig()
    else:
        continue 


    