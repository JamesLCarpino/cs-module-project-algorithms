"""
Input: a List of integers
Returns: a List of integers
"""


def product_of_all_other_numbers(arr):

    # Your code here
    # multiply each number in the array excluding 1 each time
    # if the index is the pointer then multiply other numbers in the array together
    # might be a good way to sort them?
    # how do I tell the program to choose any number of the array and ignore that index when multiplying
    # (x * 0)+(all other indicies * looping array)
    multiplier = [1] * len(arr)
    products = 1
    # how do I keep track of my pointer
    # i'm going to move right each time

    # the pointer is what will be removed
    # products will be the array of all the info in the multiplier arrray excluding one
    for i in range(len(arr)):
        multiplier[i] *= products
        products *= arr[i]

    products = 1

    for i in range(len(arr) - 1, -1, -1):
        multiplier[i] *= products
        products *= arr[i]
    return multiplier


if __name__ == "__main__":
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [
    #     2,
    #     6,
    #     9,
    #     8,
    #     2,
    #     2,
    #     9,
    #     10,
    #     7,
    #     4,
    #     7,
    #     1,
    #     9,
    #     5,
    #     9,
    #     1,
    #     8,
    #     1,
    #     8,
    #     6,
    #     2,
    #     6,
    #     4,
    #     8,
    #     9,
    #     5,
    #     4,
    #     9,
    #     10,
    #     3,
    #     9,
    #     1,
    #     9,
    #     2,
    #     6,
    #     8,
    #     5,
    #     5,
    #     4,
    #     7,
    #     7,
    #     5,
    #     8,
    #     1,
    #     6,
    #     5,
    #     1,
    #     7,
    #     7,
    #     8,
    # ]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}"
    )
