"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""


def sliding_window_max(nums, k):
    # Your code here
    # need the array to be viewed only as set of 3
    # need the array to have a max that gets printed
    # nums is the array
    # k is the window size
    # probably need to use slice(0:2) -> to get the first 3 items in the array

    # check first 3 items in array, return the largest
    # add 2 to the index and from that new section return the largest to newly made array
    # continue this until hitting the end of the array
    # slice(0:2)
    # window = slice(0:2)+2 ?? something like that mabye

    # could take everything out of the array append those to a new array and then find the max of that and print it

    max_value = []
    for i in range(0, len(nums) - (k - 1)):
        max_value.append(max(nums[i : k + i]))
    return max_value


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
