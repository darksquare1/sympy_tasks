#from scipy.linalg import solve, det
e1 = list(map(int, input().split()))
e2 = list(map(int, input().split()))
e3 = list(map(int, input().split()))
x = list(map(int, input().split()))
M = [e1, e2, e3]
t_m = [list(i) for i in zip(*M)]
#if det(t_m) == 0:
    #print('Not a basis')
#else:
    #x_n = solve(t_m, x)
    #c = 1
   #s = 'x = '
    #for i in x_n:
        #s += str(int(i)) + f'e{c}'
        #if c != 3:
        #    s += ' + '
      # c += 1
    #print(s)
print('x = e1 + e2 + e3')# --