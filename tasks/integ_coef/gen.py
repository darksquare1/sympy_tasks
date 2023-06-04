import random

random.seed(1053530)


def gen_coefs():
    length = random.randint(1, 10)
    return [random.randint(-10000, 10000) for i in range(length)]


def gen_semg():
    start = random.randint(-100000, 100000)
    return start, random.randint(start, 100000)


counter = 1


def save(f_x, segment):
    global counter
    with open(f'{counter:02d}.in', 'w') as file:
        print(*f_x, file=file)
        print(*segment, file=file)
    counter += 1


for i in range(18):
    save(gen_coefs(), gen_semg())
