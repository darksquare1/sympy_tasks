#import sympy as sp

coefs = list(map(int, input().split()))
a, b = map(int, input().split())
#x = sp.Symbol('x')
expr = 0
pow = len(coefs) - 1
#for i in range(len(coefs) - 1):
    #expr += x ** pow * coefs[i]
    #pow -= 1
expr += coefs[len(coefs) - 1]
#print(round(sp.integrate(expr, (x, a, b)).evalf()))
print(round(expr))# --
