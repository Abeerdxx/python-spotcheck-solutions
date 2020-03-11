def get_squares_dictionary(n):
    return {x: x ** 2 for x in range(1, n + 1)}


print(get_squares_dictionary(5))
