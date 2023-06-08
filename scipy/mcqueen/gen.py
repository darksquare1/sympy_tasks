import random

random.seed(5918591814)


def gen_m_n():
    return [random.randint(1, 15),random.randint(1, 15)]


def gen_matrix(m_n):
    matrix = [[random.uniform(-100000, 100000) for i in range(int(m_n[1]))] for i in range(int(m_n[0]))]
    return matrix


start_index = 1


def save(matrix):
    global start_index
    with open(f'{start_index:02d}.in', 'w') as file:
        print(len(matrix), len(matrix[0]), file=file)
        for i in range(len(matrix)):
            print(*matrix[i], file=file)
    start_index += 1


for i in range(18):
    save(gen_matrix(gen_m_n()))