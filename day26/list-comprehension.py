# 26.1 List Comprehension
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# This new list will contain every number in the list numbers but each number should be squared.

squared_numbers = [num * num for num in numbers]
print(squared_numbers)
# [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]