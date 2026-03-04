# FUNCTION RETURNING A SINGLE VALUE
# 1- Write a function square(num) that returns the square of a number
# def square(num):
#     return num ** 2
#
# ans = square(3)
# print(ans)


# MULTIPLE RETURN VALUES
# 1- Write a function min_and_max(numbers) that returns both the minimum and maximum values in a list.
def min_and_max(nums):
    min_value = min(nums)
    max_value = max(nums)
    return min_value, max_value

nums = [-2, 4, -5, 8, 11, 1]
minimum, maximum = min_and_max(nums)
print(minimum, maximum)