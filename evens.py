def even_number_of_evens(numbers):
    """
    Should raise a TypeError if a list is not passed into the function
    error message: "A list was not passed into the function"
    if numbers are empty return False
    if the number of evens is odd, return False
    if the number of evens is zero, return False
    if the number of evens is even, return True
    """

    if isinstance(numbers, list):
        return True
    else:
        raise TypeError("A list was not passed into the function")


if __name__ == '__main__':
    print(even_number_of_evens(5))
