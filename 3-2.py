import numpy as np
import matplotlib.pyplot as plt

f = lambda x, y: -2.0 * y
x0, y0 = 0.0, 1.0
h = 0.1
x_end = 2.0
n = int(round((x_end - x0) / h))
exact = lambda x: np.exp(-2.0 * x)

def euler(f, x0, y0, h, n):
    x = np.zeros(n + 1); y = np.zeros(n + 1)
    x[0], y[0] = x0, y0
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
        x[i + 1] = x[i] + h
    return x, y

def heun(f, x0, y0, h, n):
    x = np.zeros(n + 1); y = np.zeros(n + 1)
    x[0], y[0] = x0, y0
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h, y[i] + h * k1)
        y[i + 1] = y[i] + h * (k1 + k2) / 2
        x[i + 1] = x[i] + h
    return x, y

def rk4(f, x0, y0, h, n):
    x = np.zeros(n + 1); y = np.zeros(n + 1)
    x[0], y[0] = x0, y0
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + h * k1 / 2)
        k3 = f(x[i] + h / 2, y[i] + h * k2 / 2)
        k4 = f(x[i] + h, y[i] + h * k3)
        y[i + 1] = y[i] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x[i + 1] = x[i] + h
    return x, y

x_e, y_e = euler(f, x0, y0, h, n)
x_h, y_h = heun(f, x0, y0, h, n)
x_r, y_r = rk4(f, x0, y0, h, n)
y_exact = exact(x_e)

print("=" * 96)
print("ЗАДАЧА КОШИ: y' = -2y,  y(0) = 1")
print(f"Отрезок: [{x0}, {x_end}], шаг h = {h}, число шагов N = {n}")
print("Методы: Эйлер (порядок 1), Хойн (порядок 2), Рунге-Кутта 4 (порядок 4)")
print("=" * 96)

print("\n--- ПОШАГОВЫЙ РАСЧЁТ (первые 5 шагов) ---")
print(f"{'i':>3} {'x_i':>7} {'Эйлер':>13} {'Хойн':>13} {'RK4':>13} {'Точное':>13}")
print("-" * 66)
show = min(5, n)
for i in range(show + 1):
    print(f"{i:>3} {x_e[i]:>7.2f} {y_e[i]:>13.6f} {y_h[i]:>13.6f} "
          f"{y_r[i]:>13.6f} {y_exact[i]:>13.6f}")
print("...")

print("\n" + "=" * 96)
print("СРАВНЕНИЕ ПО ТОЧКАМ (все узлы сетки)")
print("=" * 96)
print(f"{'x':>6} {'Эйлер':>12} {'err_E':>12} {'Хойн':>12} {'err_H':>12} "
      f"{'RK4':>12} {'err_R':>12} {'Точное':>12}")
print("-" * 96)
for i in range(n + 1):
    e_E = abs(y_e[i] - y_exact[i])
    e_H = abs(y_h[i] - y_exact[i])
    e_R = abs(y_r[i] - y_exact[i])
    print(f"{x_e[i]:>6.2f} {y_e[i]:>12.6f} {e_E:>12.3e} {y_h[i]:>12.6f} "
          f"{e_H:>12.3e} {y_r[i]:>12.6f} {e_R:>12.3e} {y_exact[i]:>12.6f}")

err_E = np.abs(y_e - y_exact)
err_H = np.abs(y_h - y_exact)
err_R = np.abs(y_r - y_exact)
print("\n" + "=" * 96)
print("СВОДКА ПОГРЕШНОСТЕЙ")
print("=" * 96)
print(f"{'Метод':<20} {'макс. ошибка':>18} {'ошибка в x=2':>18} {'порядок':>10}")
print("-" * 70)
print(f"{'Эйлер':<20} {err_E.max():>18.6e} {err_E[-1]:>18.6e} {'O(h)':>10}")
print(f"{'Хойн':<20} {err_H.max():>18.6e} {err_H[-1]:>18.6e} {'O(h^2)':>10}")
print(f"{'RK4':<20} {err_R.max():>18.6e} {err_R[-1]:>18.6e} {'O(h^4)':>10}")

print("\nПроверка порядка при уменьшении шага вдвое (h -> h/2):")
print("  Эйлер: ошибка должна уменьшиться примерно в 2 раза;")
print("  Хойн:  примерно в 4 раза;")
print("  RK4:   примерно в 16 раз.")

print("\n" + "=" * 96)
print("ВЛИЯНИЕ ШАГА (ошибка в конечной точке x = 2)")
print("=" * 96)
print(f"{'h':>10} {'Эйлер':>16} {'Хойн':>16} {'RK4':>16}")
print("-" * 62)
for hh in [0.2, 0.1, 0.05, 0.025]:
    nn = int(round((x_end - x0) / hh))
    _, ye = euler(f, x0, y0, hh, nn)
    _, yh = heun(f, x0, y0, hh, nn)
    _, yr = rk4(f, x0, y0, hh, nn)
    ye_true = exact(x0 + nn * hh)
    print(f"{hh:>10.4f} {abs(ye[-1]-ye_true):>16.3e} "
          f"{abs(yh[-1]-ye_true):>16.3e} {abs(yr[-1]-ye_true):>16.3e}")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x_e, y_e, 'o--', label='Эйлер')
plt.plot(x_h, y_h, 's--', label='Хойн')
plt.plot(x_r, y_r, '^--', label='RK4')
plt.plot(x_e, y_exact, '-', label='Точное')
plt.xlabel('x'); plt.ylabel('y')
plt.title(f"Решения, h = {h}")
plt.legend(); plt.grid(True)

plt.subplot(1, 2, 2)
plt.semilogy(x_e, err_E, 'o-', label='Эйлер')
plt.semilogy(x_h, err_H, 's-', label='Хойн')
plt.semilogy(x_r, err_R, '^-', label='RK4')
plt.xlabel('x'); plt.ylabel('|y_числ - y_точн| (log)')
plt.title("Абсолютная ошибка")
plt.legend(); plt.grid(True, which='both')

plt.tight_layout(); plt.show()