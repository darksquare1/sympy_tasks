#import sympy as sp
from matplotlib import pyplot as plt
#import numpy as np

f = input()
#x, y = sp.symbols("x y")
#a = sp.Eq(y, sp.simplify(f))
#a = sp.Eq(a.lhs.subs(y, x), a.rhs.subs(x, y))
#q = sp.solve(a, y)
#l = [sp.Eq(y, i).rhs for i in q]
#m = np.linspace(-10, 10, 10000)

#for i in l:
   # y = i
    #lambd_expr = sp.lambdify(x, y)
    #output = lambd_expr(m)
    #plt.plot(m, output,'green')
plt.plot(10,5)# --
plt.grid()
plt.savefig('output.png')
