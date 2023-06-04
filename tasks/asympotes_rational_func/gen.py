import random

if __name__ == '__main__':
    random.seed(100)


    def generate_fraction():
        numerator = f"{random.randint(1, 100)}*x**{random.randint(0, 2)} + {random.randint(1, 100)}*x + {random.randint(1, 100)}"
        denominator = f"{random.randint(1, 100)}*x**{random.randint(0, 2)} + {random.randint(1, 100)}*x + {random.randint(1, 100)}"
        poly = f"({numerator})/({denominator})"
        return poly


    start_index = 1


    def save(poly):
        global start_index

        with open(f'{start_index:02d}.in', 'w') as file:
            print(poly, file=file)
        start_index += 1


    for i in range(16):
        save(generate_fraction())
