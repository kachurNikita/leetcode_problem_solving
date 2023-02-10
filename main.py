
arr = [1, 2, 3, 10]
test_1 = [7,1,5,3,6,4]
test_2 = [3,2,6,5,0,3]
test_3 = [2,1,2,1,0,1,2]

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


# def max_profit(prices):
#     if len(prices) == 1:
#         return
#     left_end = 0
#     right_end = len(prices) - 1
#     min_price = min(prices)
#     max_price = max(prices)
#     min_price_index = prices.index(min_price)
#     max_price_index = prices.index(max_price)
#     if min_price_index == right_end:
#         prices.remove(min_price)
#         case_1 = max_profit(prices)
#         return case_1
#     elif max_price_index == left_end:
#         prices.remove(max_price)
#         case_2 = max_profit(prices)
#         return case_2
#     elif max_price_index > min_price_index:
#         res = max_price - min_price
#         return res
#
#
# solution = Solution()
# print(solution.max_profit([2, 1, 11,]))

def max_profit(array):
    min_value = min(array)
    max_value = max(array)
    while len(array) > 1:
        if min_value == 0:
            array.remove(min_value)
            min_value = min(array)
        if array.index(min_value) == len(array) - 1:
            if len(array) > 1:
                array.remove(min_value)
                min_value = min(array)
        if array.index(max_value) < array.index(min_value):
            if len(array) > 1:
                array.remove(max_value)
                max_value = max(array)
        else:
            return max_value - min_value
    else:
        return 0


print(max_profit(test_2))

