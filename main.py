
arr = [2, 1, 2,  0, 1, 2]


def two_sum(nums, target):
    visited_nums = {}
    for i in range(len(nums)):
        visited_nums[i] = nums[i]
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target and j not in visited_nums.keys():
                return [i, j]


two_sum(arr, 10)


def is_palindrome(x):
    str_x = str(x)
    str_x_reverse = str_x[::-1]
    if str_x == str_x_reverse:
        return True
    else:
        return False


is_palindrome(101)


# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.



# 27. Remove Element
def remove_element(nums, value):
        while value in nums:
            nums.remove(value)
        return nums

# print(remove_element())