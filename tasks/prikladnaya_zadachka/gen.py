import random

random.seed(100)


def generate_x_y():
    a = [random.uniform(0, 47) for i in range(2)]
    return a


if __name__ == "__main__":
    start_index = 1


    def save(x_y):
        global start_index
        with open(f'{start_index:02d}.in', 'w') as file:
            print(x_y[0], file=file)
            print(x_y[1], file=file)
        start_index += 1


    for i in range(1, 19):
        save(generate_x_y())