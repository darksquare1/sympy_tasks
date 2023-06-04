import sympy as sp

n = int(input())
a = sp.Matrix([[int(i) for i in input().split()] for i in range(n)])
eigenvalues = a.eigenvals()  # находим собственные значения
print(*sorted(eigenvalues))  # выводим в порядке возрастания
