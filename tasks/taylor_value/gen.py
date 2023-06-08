from random import seed,uniform,randint
seed(242414115)
def gen():
    func=f'x**{randint(-10,10)}'
    n=f'{randint(1,10)}'
    a=f'{uniform(-1000,1000)}'
    return (func,n,a)
counter = 1
def save(tup):
    global counter
    with open(f'{counter:02d}.in','w') as f:
        print(tup[0],file=f)
        print(tup[1],file=f)
        print(tup[2],file=f)
    counter+=1
for i in range(7):
    save(gen())