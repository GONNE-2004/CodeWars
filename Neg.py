# changing number to negative
def make_negative(number):
    if number == 0:
        return 0
    elif number < 0:  # numbers below 0 are automatically negative
        return number
    else:
        return -number  # just added the minus to change to neg


# i would only say order makes it sensible
# saw many clever variations in the platform


# example
# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
# def grow(arr):
#     total = 1
#     for num in arr:
#         total *= num
#     return total


# had to set total to 1 so that it could accumulates
# then loop through each while adding it total