# 26.2 List Comprehension

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# This new list will only contain the even numbers from the list numbers.
result = [num for num in numbers if num % 2 == 0]
print(result) # [2, 8, 34]