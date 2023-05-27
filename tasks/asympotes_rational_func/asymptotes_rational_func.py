import sympy as sp


def n_p_inf(q):  # +- бесконечность
    return q == sp.oo or q == -sp.oo


x = sp.Symbol('x')

f = sp.simplify(input())  # наша функция
denom = f.as_numer_denom()[1]  # знаменатель
denom_zeros = sp.solve(denom, x)  # ищем точки бесконечного разрыва
vertical_asymptotes = []
for i in denom_zeros:
    # если один из пределов слева или справа в точке разрыва бесконечен то i является вертикальной ассимптотой
    if n_p_inf(sp.limit(f, x, i, '-')) or n_p_inf(sp.limit(f, x, i, '-')):
        vertical_asymptotes.append(i)
k = sp.limit(f / x, x, sp.oo)

b = sp.limit(f - k * x, x, sp.oo)
horizontal_asymptote = f'y = {k * x + b} ' if not (n_p_inf(k) or n_p_inf(b)) else '-'
ans = [f'x = {i}' for i in sorted(vertical_asymptotes)]
print(', '.join(ans) if ans else '-')
print(horizontal_asymptote)
