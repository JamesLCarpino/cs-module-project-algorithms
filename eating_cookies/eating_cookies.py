"""
Input: an integer
Returns: an integer
"""


# def eating_cookies(n):
#     # Your code here

#     # base case is if there were no cookies in the jar you wouldn't have anysort of anything
#     if n < 0:
#         return 0
#     elif n == 0:
#         # because thats what the stupid test says
#         return 1
#     else:
#         return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
#

# if he eats one cookie he can do so 3 times
# if he eat 1 cookie than 2 cookies
# if he eats 2 cookies, then 1
# if he eats 3 cookies all at once
# num_ways = some recursive way of adding them for multiple options


# cache allows us to save our work -> its a data structure
# cache is a dictionary where keys is the n, value is the answer
# runtim now is O(n)
def eating_cookies(n, cache):
    if n < 0:
        return 0
    elif n == 0:
        # because thats what the stupid test says
        return 1
    # add a case to check if answer is in cache
    elif cache[n] > 0:
        return cache[n]
    else:
        # otherwise, our cache doesn't contain the answer so use our recursive logic to calculate it, and then save to cache
        # for furutre uses
        cache[n] = (
            eating_cookies(n - 3, cache)
            + eating_cookies(n - 2, cache)
            + eating_cookies(n - 1, cache)
        )
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    cache = {i: 0 for i in range(num_cookies + 1)}

    print(
        f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to eat {num_cookies} cookies"
    )
