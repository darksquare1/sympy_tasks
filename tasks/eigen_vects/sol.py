#import sympy as sp

n = int(input())
#a = sp.Matrix([[int(i) for i in input().split()] for i in range(n)])
a=[[int(i) for i in input().split()] for i in range(n)]# --
#eigenvalues = a.eigenvals()
print(*sorted(a[1]))