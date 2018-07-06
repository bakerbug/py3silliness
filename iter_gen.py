"""
Iterators and generators
"""

from random import random
count = 10


def random_generator():
    index = 0
    while index < count:
        index += 1
        result = int(round((random() % 10) * 10))
        yield result


if __name__ == '__main__':
    random_number_iterator = random_generator()
    while True:
        try:
            print(next(random_number_iterator))
        except StopIteration:
            print("I'm done!")
            break

