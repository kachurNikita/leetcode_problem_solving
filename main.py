

arr = [2, 4, 3, 11, 0, 1]
#
#
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


def two_num_sum(array, target):
    hash_table = {}
    for num in array:
        if target - num in hash_table:
            return [target - num, num]
        else:
            hash_table[num] = True
    return []


print(two_num_sum(arr, 5)
)

