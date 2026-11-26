import numpy as np
import matplotlib.pyplot as plt

f = lambda x, y: -2.0 * y          
x0, y0 = 0.0, 1.0                  
h = 0.1                           
x_end = 2.0                        
n = int(round((x_end - x0) / h))  

def euler(f, x0, y0, h, n):
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    x[0], y[0] = x0, y0
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
        x[i + 1] = x[i] + h
    return x, y

exact = lambda x: np.exp(-2.0 * x)

x_e, y_e = euler(f, x0, y0, h, n)
y_exact = exact(x_e)

print("=" * 78)
print("ЗАДАЧА КОШИ: y' = -2y,  y(0) = 1")
print(f"Отрезок: [{x0}, {x_end}], шаг h = {h}, число шагов N = {n}")
print(f"Точное решение: y(x) = exp(-2x)")
print("=" * 78)

print("\n--- ПОШАГОВЫЙ РАСЧЁТ МЕТОДОМ ЭЙЛЕРА ---")
print(f"{'i':>3} {'x_i':>8} {'y_i':>12} {'f(x_i,y_i)':>14} {'y_(i+1)':>14}")
print(f"{0:>3} {x_e[0]:>8.3f} {y_e[0]:>12.6f} {f(x_e[0], y_e[0]):>14.6f} {'—':>14}")
for i in range(n):
    fi = f(x_e[i], y_e[i])
    print(f"{i+1:>3} {x_e[i+1]:>8.3f} {y_e[i+1]:>12.6f} {fi:>14.6f} {y_e[i+1]:>14.6f}")

print("\n" + "=" * 78)
print("СРАВНЕНИЕ С ТОЧНЫМ РЕШЕНИЕМ")
print("=" * 78)
print(f"{'x':>6} {'Эйлер':>14} {'Точное':>14} {'Абс. ошибка':>16} {'Отн. ошибка, %':>16}")
print("-" * 70)
for i in range(n + 1):
    abs_err = abs(y_e[i] - y_exact[i])
    rel_err = abs_err / y_exact[i] * 100 if y_exact[i] != 0 else 0.0
    print(f"{x_e[i]:>6.2f} {y_e[i]:>14.6f} {y_exact[i]:>14.6f} "
          f"{abs_err:>16.6e} {rel_err:>16.4f}")

abs_err = np.abs(y_e - y_exact)
print("-" * 70)
print(f"Максимальная абсолютная ошибка: {abs_err.max():.6e}")
print(f"Ошибка в конечной точке x = {x_end}: {abs_err[-1]:.6e}")
print("Вывод: глобальная погрешность метода Эйлера имеет порядок O(h).")

plt.figure(figsize=(8, 5))
plt.plot(x_e, y_e, 'o-', label=f'Эйлер, h={h}')
plt.plot(x_e, y_exact, '-', label='Точное решение')
plt.xlabel('x'); plt.ylabel('y')
plt.title("Метод Эйлера vs точное решение")
plt.legend(); plt.grid(True)
plt.tight_layout(); plt.show()