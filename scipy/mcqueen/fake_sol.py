#from scipy.optimize import minimize
#from scipy.optimize import rosen
m, n = map(int, input().split())
s = 0
for i in range(m):
    xi = [float(i) for i in input().split()]
    #b = minimize(rosen, xi, method='Nelder-Mead')
    #s += b.fun
print(round(s))