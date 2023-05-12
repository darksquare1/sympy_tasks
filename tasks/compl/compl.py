import sympy as sp

z = sp.simplify(input())  # на вход комплексное число не равное нулю
a = sp.re(z)  # действительная часть x
b = sp.im(z)  # мнимая часть y
r = sp.sqrt(a ** 2 + b ** 2)  # радиус комплексного числа
if a == 0 or b == 0:
    if b < 0:
        arg = (3 * sp.pi) / 2
    elif b > 0:
        arg = sp.pi / 2
    elif a > 0:
        arg = 0
elif a < 0:
    arg = sp.pi
elif a > 0 and b > 0:
    arg = sp.atan(b / a)  # аргумент пренадлежит первой четверти
elif a < 0 and b > 0:
    arg = sp.pi - sp.atan(abs(b / a))  # аргумент пренадлежит второй четверти
elif a < 0 and b < 0:
    arg = sp.pi + sp.atan(b / a)  # аргумент пренадлежит третьей четверти
elif a > 0 and b < 0:
    arg = 2 * sp.pi - sp.atan(abs(b / a))  # аргумент пренадлежит четвертой четверти
ans = str(r) + '(' + f'cos({arg}) + i sin({arg})' + ')'
print(ans)
