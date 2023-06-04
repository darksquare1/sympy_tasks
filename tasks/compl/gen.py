from random import seed, uniform

seed(162135125)


def gen_a_b():
    return (uniform(-10 ** 6, 10 ** 6), uniform(-10 ** 6, 10 ** 6))


start_index = 1


def save(a_b):
    global start_index
    with open(f'{start_index:02d}.in', 'w') as file:
        print(f'{a_b[0]} + {a_b[1]}*I', file=file)
    start_index += 1


for i in range(18):
    save(gen_a_b())
