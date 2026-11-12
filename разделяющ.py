import math

def solve_separable(C, x):
    return C * math.exp(x * x / 2.0)

def rhs(x, y):
    return x * y

def check_numeric(C, x, h=1e-6):
    y = solve_separable(C, x)
    y_plus = solve_separable(C, x + h)
    y_minus = solve_separable(C, x - h)
    y_prime_num = (y_plus - y_minus) / (2 * h)
    return y_prime_num, rhs(x, y)

C = 2.0
x0 = 1.0
yp, r = check_numeric(C, x0)
print(f"y({x0}) = {solve_separable(C, x0):.6f}")
print(f"y' численно = {yp:.6f},  x*y = {r:.6f},  разность = {abs(yp-r):.2e}")