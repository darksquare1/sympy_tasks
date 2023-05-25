from scipy.linalg import solve
from scipy.linalg import inv

n = int(input())
A = [[float(i) for i in input().split()] for j in range(n)]
A = inv(A)
b = [input(float(i)) for i in range(n)]
x = solve(A, b)
print(*map(lambda i: round(i),x),sep=' ,')