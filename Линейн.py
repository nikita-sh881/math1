import math

def p(x):
    return 1.0

def q(x):
    return math.exp(x)

def mu(x):
    integral_p = x          
    return math.exp(integral_p)

def solve_linear(C, x):
    integral_mu_q = math.exp(2 * x) / 2.0   
    return (integral_mu_q + C) / mu(x)

def check_numeric(C, x, h=1e-6):
    y = solve_linear(C, x)
    y_plus = solve_linear(C, x + h)
    y_minus = solve_linear(C, x - h)
    y_prime_num = (y_plus - y_minus) / (2 * h)
    lhs = y_prime_num + p(x) * y
    return lhs, q(x)

C = 1.0
x0 = 0.5
lhs, rhs_val = check_numeric(C, x0)
print(f"y({x0}) = {solve_linear(C, x0):.6f}")
print(f"y' + y = {lhs:.6f},  e^x = {rhs_val:.6f},  разность = {abs(lhs-rhs_val):.2e}")