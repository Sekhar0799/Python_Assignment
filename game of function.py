# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
# Explanation:
# Summation should like 8+2+3+0+7 = 20


def sum_list():
    num1_list = []
    n = int(input("Enter the number of elements in the list: "))
    for i in range(n):
        num = int(input("Enter a number: "))
        num1_list.append(num)
    sum_of_list = sum(num1_list)
    return sum_of_list
print(sum_list())

# output
# Enter the number of elements in the list: 5
# Enter a number: 8
# Enter a number: 2
# Enter a number: 3
# Enter a number: 0
# Enter a number: 7
# 20
