
def function_square(x):
    return x*x


if __name__ == '__main__':
    # function call
    print(function_square(2))

    # lambda - can be used this way, but named function would be preferred here
    lambda_square = lambda x: x*x
    print(lambda_square(2))

    # lambda - preferred usage
    students_tuple = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

    result = sorted(students_tuple, key=lambda x: x[2])
    print(result)

    # The value of the 'key' parameter should be a function that takes a single argument
    # and returns a key to use for sorting purposes.
    # This technique is fast because the key function is called exactly once for each input record.
