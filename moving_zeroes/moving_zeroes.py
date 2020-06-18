"""
Input: a List of integers
Returns: a List of integers
"""


def moving_zeroes(arr):
    # move each non-zero integer to the left side
    # move zero to the right...
    # if arr[i] == 0 move it
    # need to pop and insert it
    # Your code here

    for i in range(len(arr) - 1):
        print("this is i", i)

        if i == 0:
            arr.pop(i)
            arr.insert(-1, i)
            i += 1

        else:
            return arr


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
