import sympy as sp

coefs = list(map(int, input().split()))  # коэффиценты
a, b = map(int, input().split())  # отрезок интегрирования
x = sp.Symbol('x')
expr = 0
pow = len(coefs) - 1
for i in range(len(coefs) - 1):
    expr += x ** pow * coefs[i]
    pow -= 1
expr += coefs[len(coefs) - 1]  # наш многочлен
print(sp.integrate(expr, (x, a, b)))  # выводим интеграл от а до б
