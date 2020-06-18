"""
Input: a List of integers
Returns: a List of integers
"""


# def moving_zeroes(arr):
# move each non-zero integer to the left side
# move zero to the right...
# if arr[i] == 0 move it
# destructure it, match it, append it to a new list
# need to pop and insert it
# Your code here

# zeros = []
# non_zero = []

# for i in range(len(arr)):
#     if arr[i] == 0:
#         zeros.append(arr[i])
# for j in range(len(arr)):
#     if arr[j] != 0:
#         non_zero.append(arr[j])
# new_list = non_zero + zeros
# return new_list


# 1. The return statement will always execute after the first non-zero element it incounters. oh no! Move this after the for loop.
# 2. Now that we're looping more than once... but we're actually missing the last element. You don't have to subtract 1, range already does not include the upper limit as it's starting from 0.
# 3. I already increments. you do not neeed to increment it!
# 4 i is the index, not the value. the index of the value of 0 will not always be 0! So don't insert it lol and don't evaluate by it in your if statement
# 5. Python's list insert inserts the item at that index, and shifts all elements after it to the right. You want to append to the end
# 6. Now you've got a problem where whenever you pop, you're actually shifting the rest of the elements DOWN and therefore skipping the next one. Let's use a while loop instead to track how many elements we've evalueated so we can track index separately.
def moving_zeroes(arr):
    elem = 0
    i = 0
    while elem < len(arr):
        elem += 1
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
        else:
            i += 1
    return arr


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
