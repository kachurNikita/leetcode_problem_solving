
arr = [3, 3]

# def two_num_sum(array, target):
#     for i in range(len(array)):
#         for j in range(1, len(array)):
#             if array[i] + array[j] == target:
#                 return 1
#     else:
#         return -1
#
# print(two_num_sum(arr, 12))
# Speed n**2
# sum = num + value_2
# num = sum - value_2
# value_2 = sum - num



# Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.


def is_palindrome(x):
    str_x = str(x)
    left_side = 0
    right_side = len(str_x) - 1
    while left_side <= right_side:
        if str_x[left_side] != str_x[right_side]:
            return False
        else:
            left_side += 1
            right_side -= 1
    return True



print(is_palindrome(101))