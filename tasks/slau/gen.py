from random import seed, randint

seed(15501851)


def gen():
    n, m = randint(1, 10), randint(1, 10)
    slau = []
    for i in range(n):
        eq = ''
        counter = 0
        while counter != m:
            eq += f'{randint(1, 100)}*x{counter}'
            eq += " + " if counter != (m - 1) else ""
            counter += 1
        eq += f' = {randint(1, 100)}'
        slau.append(eq)
    return (n, m, slau)


cnt = 1


def save(a):
    global cnt
    with open(f'{cnt:02d}.in', 'w') as f:
        print(a[0], a[1], sep=' ', file=f)
        for i in a[2]:
            print(i, file=f)
    cnt += 1


for i in range(10):
    save(gen())