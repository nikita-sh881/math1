def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

def print_matrix(A, b, title="Система"):
    print(f"\n{title}:")
    print(f"  | {A[0][0]:>4}  {A[0][1]:>4} |   | x1 |   | {b[0]:>4} |")
    print(f"  | {A[1][0]:>4}  {A[1][1]:>4} | * | x2 | = | {b[1]:>4} |")

def cramer2_detailed(A, b):
    a11, a12 = A[0]
    a21, a22 = A[1]
    b1, b2 = b

    print("\n")
    print("ШАГ 1. Главный определитель Δ")
    print(f"  Δ = | {a11}  {a12} |")
    print(f"      | {a21}  {a22} |")
    print(f"  Δ = ({a11}) * ({a22}) - ({a12}) * ({a21})")
    D = a11 * a22 - a12 * a21
    print(f"  Δ = {a11 * a22} - {a12 * a21} = {D}")

    if D == 0:
        raise ValueError("Δ = 0 → система не имеет единственного решения "
                         "(либо несовместна, либо бесконечно много решений).")
    print("\n")
    print("ШАГ 2. Определитель Δ1 (столбец 1 заменён на b)")
    print(f"  Δ1 = | {b1}  {a12} |")
    print(f"       | {b2}  {a22} |")
    print(f"  Δ1 = ({b1}) * ({a22}) - ({a12}) * ({b2})")
    D1 = b1 * a22 - a12 * b2
    print(f"  Δ1 = {b1 * a22} - {a12 * b2} = {D1}")

    print("\n")
    print("ШАГ 3. Определитель Δ2 (столбец 2 заменён на b)")
    print(f"  Δ2 = | {a11}  {b1} |")
    print(f"       | {a21}  {b2} |")
    print(f"  Δ2 = ({a11}) * ({b2}) - ({b1}) * ({a21})")
    D2 = a11 * b2 - b1 * a21
    print(f"  Δ2 = {a11 * b2} - {b1 * a21} = {D2}")

    print("\n")
    print("ШАГ 4. Находим x1 и x2 по формулам Крамера")
    print(f"  x1 = Δ1 / Δ = {D1} / {D} = {D1 / D:.6g}")
    print(f"  x2 = Δ2 / Δ = {D2} / {D} = {D2 / D:.6g}")

    return D1 / D, D2 / D

def read_natural(prompt):
    while True:
        s = input(prompt).strip()
        if not s.isdigit() or int(s) == 0:
            print("Ошибка: нужно натуральное число (целое > 0). Попробуйте снова.")
            continue
        return int(s)

def read_matrix():
    A = []
    print("\nВведите коэффициенты матрицы A (2 строки по 2 натуральных числа):")
    for i in range(2):
        row = []
        for j in range(2):
            row.append(read_natural(f"  A[{i + 1}][{j + 1}] = "))
        A.append(row)

    print("Введите столбец свободных членов b (2 натуральных числа):")
    b = [read_natural(f"  b[{i + 1}] = ") for i in range(2)]
    return A, b

print("Решение СЛАУ 2×2 методом Крамера (ввод — только натуральные числа)")
print("Для выхода введите 'q' на любом шаге ввода.")

while True:
    try:
        cmd = input("\nНажмите Enter для ввода новой системы или 'q' для выхода: ").strip().lower()
        if cmd == "q":
            break

        A, b = read_matrix()
        print_matrix(A, b, "Исходная система")

        x1, x2 = cramer2_detailed(A, b)

        print("\n")
        print("ОТВЕТ")
        print("")
        print(f"  x1 = {x1:.6g}")
        print(f"  x2 = {x2:.6g}")

    except ValueError as e:
        print("\n⚠ Ошибка:", e)
        print("Попробуйте ввести систему заново.")
    except (KeyboardInterrupt, EOFError):
        print("\n\nПрервано пользователем. Выход.")
        break