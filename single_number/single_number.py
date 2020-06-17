"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""


def single_number(arr):
    # each element increments by 1, checks to see if current element is equal to previous element, if it is move on.
    #  if it isn't check the next element to see if it is the same, if it isn't check the next to see if it is the same as the previous, if it is move on
    # if it checks the next element and it is different return that number since it can't be the same
    # issues to think about:
    # how does it know it is looking at a new number
    # what does the program do to get out of loop.
    # can I break this down so it checks index 0,1 then index 2,3 and so on?
    # what if the array is unsorted.

    # Your code here

    for i in arr:
        if i == 0:
            
    
        


if __name__ == "__main__":
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
