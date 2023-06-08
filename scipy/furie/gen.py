from random import randint, seed

seed(5151414)


def gen():
    a = randint(-1000, 1000)
    b = randint(a, 1000)
    n = randint(1, 100000)
    poly = f'x**{randint(1, 10)} + {randint(-1000, 1000)}'
    return (a, b, n, poly)


counter = 1


def save(q):
    global counter
    with open(f'{counter:02d}.in', 'w') as f:
        print(q[3], file=f)
        print(q[0], q[1], q[2], file=f)
    counter += 1


for i in range(15):
    save(gen())
