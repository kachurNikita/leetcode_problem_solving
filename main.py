
arr = [2, 5, 5, 11]


def two_sum( nums, target):
    visited_nums = {}
    for i in range(len(nums)):
        visited_nums[i] = nums[i]
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target and j not in visited_nums.keys():
                return [i, j]


two_sum(arr, 10)

# Speed n**2
# sum = num + value_2
# num = sum - value_2
# value_2 = sum - num


def is_palindrome(x):
    str_x = str(x)
    str_x_reverse = str_x[::-1]
    if str_x == str_x_reverse:
        return True
    else:
        return False


is_palindrome(101)
