# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]

input_str = input("Enter a list of integers separated by space: ")
input_list = list(map(int, input_str.strip().split()))
def triple(num):
    return num * 3
triple_list = list(map(triple, input_list))
print("Triple of list numbers:")
print(triple_list)

# output
# Enter a list of integers separated by space: 1 2 3 4 5 6 7
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]
