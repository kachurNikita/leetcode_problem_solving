
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

# 104. Maximum Depth of Binary Tree

class Node(object):
    def __init__(self, val,  left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Vertex {self.val}'


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
#
parent_node = Node(3)
parent_node.left = Node(9)
parent_node.right = Node(20)
parent_node.right.left = Node(15)
parent_node.right.right = Node(7)


# 104. Maximum Depth of Binary Tree
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            l_nodes = self.maxDepth(root.left)
            r_nodes = self.maxDepth(root.right)

            if l_nodes > r_nodes:
                return l_nodes + 1
            else:
                return r_nodes + 1


sol = Solution()
print(sol.maxDepth(parent_node))


# 989. Add to Array-Form of Integer

def add_to_array_form(array, k):
    array = ''.join(str(number) for number in array)
    array = int(array) + k
    array = [int(i) for i in str(array)]
    return array


print(add_to_array_form([2, 7, 4],  181))
