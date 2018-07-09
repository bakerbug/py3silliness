"""
Iterators and generators
"""

MAX_SEQ = 42

def fibonacci_generator():
    index = 2
    first = 0
    second = 1

    if MAX_SEQ == 1:
        yield first
    elif MAX_SEQ == 2:
        yield second
    else:
        while index < MAX_SEQ:
            third = first + second
            first = second
            second = third
            index += 1
            yield third


if __name__ == '__main__':
    fibonacci_iterator = fibonacci_generator()
    while True:
        try:
            the_number = next(fibonacci_iterator)
            #print(the_number)
        except StopIteration:
            print("I'm done!")
            break

    print('The {} Fibonacci number is:'.format(MAX_SEQ))
    print(the_number)

