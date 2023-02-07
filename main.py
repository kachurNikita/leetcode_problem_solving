
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



def is_polindrome(x):
    str_x = str(x)
    str_x_reverse = str_x[::-1]
    if str_x == str_x_reverse:
        return True
    else:
        return False


print(is_polindrome(1))