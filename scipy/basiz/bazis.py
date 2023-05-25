from scipy.linalg import solve, det

# задаем координаты векторов в некотором базисе
e1 = list(map(int, input().split()))
e2 = list(map(int, input().split()))
e3 = list(map(int, input().split()))
x = list(map(int, input().split()))
M = [e1, e2, e3]
if det(M) == 0:
    print('Не является базисом')
else:
    x_n = solve(M, x)
    c = 1
    s = 'x = '
    for i in x_n:
        s += str(int(i)) + f'e{c}'
        if c != 3:
            s += ' + '
        c += 1
    print(s)
