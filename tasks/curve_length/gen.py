import random

random.seed(50)


def generate_f_x():
    poly = f'{random.randint(-100, 100)}*x**{random.randint(0, 10)} + {random.randint(-100, 100)}*x**' \
           f'{random.randint(0, 10)}+'f'{random.randint(-100, 100)}'

    return poly


def gen_segment():
    left = random.randint(-1000, 1000)
    right = random.randint(left, 1000)
    segm = f'{left} {right}'
    return segm


if __name__ == "__main__":
    counter = 1


    def save(f_x, segment):
        global counter
        with open(f'{counter:02d}.in', 'w') as file:
            print(f_x, file=file)
            print(segment, file=file)
        counter += 1


    for i in range(17):
        save(generate_f_x(), gen_segment())
