#gen_random.py

import random

def gen_random(count, min, max):
    for i in range(count):
        yield random.randint(min, max)

if __name__ == '__main__':
    for number in gen_random(5, 1, 3):
        print(number)