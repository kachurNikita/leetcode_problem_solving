import re
# arr = [2, 1, 2,  0, 1, 2]


# def two_sum(nums, target):
#     visited_nums = {}
#     for i in range(len(nums)):
#         visited_nums[i] = nums[i]
#         for j in range(1, len(nums)):
#             if nums[i] + nums[j] == target and j not in visited_nums.keys():
#                 return [i, j]
#
#
# two_sum(arr, 10)
#
#
# def is_palindrome(x):
#     str_x = str(x)
#     str_x_reverse = str_x[::-1]
#     if str_x == str_x_reverse:
#         return True
#     else:
#         return False
#
#
# is_palindrome(101)


# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


# 27. Remove Element
# def remove_element(nums, value):
#         while value in nums:
#             nums.remove(value)
#         return nums
#
# # print(remove_element())
#
# # 104. Maximum Depth of Binary Tree
#
# class Node(object):
#     def __init__(self, val,  left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#     def __repr__(self):
#         return f'Vertex {self.val}'


# parent_node = Node(4)
# parent_node.right = Node(6)
# parent_node.right.right = Node(7)
# parent_node.right.right.right = Node(9)
# parent_node.right.right.right.right = Node(8)
# parent_node.right.right.right.right.left = Node(5)
# parent_node.right.right.right.right.right = Node(1)
# parent_node.right.right.right.right.right.left = Node(14)
# parent_node.right.right.right.right.right.right = Node(6)
# parent_node.right.right.right.right.right.right.left = Node(3)
# parent_node.right.right.right.right.right.right.right = Node(2)

# parent_node = Node(1)
# parent_node.left = Node(2)
# parent_node.right = Node(3)
# parent_node.right.right = Node(4)
# parent_node.right.right.left = Node(5)
# parent_node.right.right.right = Node(6)
#
# parent_node = Node(3)
# parent_node.left = Node(9)
# parent_node.right = Node(20)
# parent_node.right.left = Node(15)
# parent_node.right.right = Node(7)


# 104. Maximum Depth of Binary Tree
# class Solution(object):
#     def maxDepth(self, root):
#         depth = 0
#         queue = [root]
#         while queue:
#             temp = []
#             depth += 1
#             for node in queue:
#                 if node.left:
#                     temp.append(node.left)
#                 if node.right:
#                     temp.append(node.right)
#             queue = temp
#         return depth


# sol = Solution()
# print(sol.maxDepth(parent_node))


# 989. Add to Array-Form of Integer

# def add_to_array_form(array, k):
#     array = ''.join(str(number) for number in array)
#     array = int(array) + k
#     array = [int(i) for i in str(array)]
#     return array


# print(add_to_array_form([2, 7, 4],  181))


# 551. Student Attendance Record I
# 'PPALLP

# class Solution:
#     def checkRecord(self, s):
#         return not (s.count('A') > 1 or 'LLL' in s)
#
# solution = Solution()
# print(solution.checkRecord('LALL'))


# Romans to integer

class Solution:
    single_char_res = 0
    patterns_res = 0
    romans_copy = []
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    patterns = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }

    def romans_to_int(self, s):
        for char in self.patterns:
            if char in s:
               self.patterns_res += self.patterns[char]
               s = s.replace(char, '')
        for char in s:
            if char in self.roman_to_int:
                self.single_char_res += self.roman_to_int[char]
        return self.patterns_res + self.single_char_res


solution = Solution()
print(solution.romans_to_int('III'))


# 125. Valid Palindrome

def valid_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    left_pointer = 0
    right_pointer = len(s) - 1
    while left_pointer <= right_pointer:
        if s[left_pointer] != s[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1
    return True


print(valid_palindrome('a.'))

