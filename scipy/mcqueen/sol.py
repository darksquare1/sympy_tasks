from scipy.optimize import minimize
from scipy.optimize import rosen
m, n = map(int, input().split())
s = 0
for i in range(m):
    xi = [float(i) for i in input().split()] # считываем значение точки
    b = minimize(rosen, xi, method='Nelder-Mead') # находим ближайшую точку минимума
    s += b.fun # суммируем значения в этих точках
print(round(s))
