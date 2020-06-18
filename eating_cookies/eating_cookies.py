"""
Input: an integer
Returns: an integer
"""


def eating_cookies(n):
    # Your code here

    for num_ways in range(int(n)):
        # base case is if there were no cookies in the jar you wouldn't have anysort of anything
        if n <= 0:
            num_ways = 0
            return num_ways
        elif n > 0:
            
            #if he eats one cookie he can do so 3 times
            #if he eat 1 cookie than 2 cookies
            #if he eats 2 cookies, then 1
            #if he eats 3 cookies all at once
            #num_ways = some recursive way of adding them for multiple options


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies"
    )
