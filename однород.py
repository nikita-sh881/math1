import math

def solve_homogeneous(C, x):
    assert x > 0
    return x * (math.log(x) + C)

def f_homogeneous(x, y):
    return y / x + 1.0

def check_numeric(C, x, h=1e-6):
    y = solve_homogeneous(C, x)
    y_plus = solve_homogeneous(C, x + h)
    y_minus = solve_homogeneous(C, x - h)
    y_prime_num = (y_plus - y_minus) / (2 * h)
    return y_prime_num, f_homogeneous(x, y)

C = 0.5
x0 = 2.0
yp, r = check_numeric(C, x0)
print(f"y({x0}) = {solve_homogeneous(C, x0):.6f}")
print(f"y' численно = {yp:.6f},  y/x + 1 = {r:.6f},  разность = {abs(yp-r):.2e}")