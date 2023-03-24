# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]


input_str = input("Enter a list of integers separated by space: ")
input_list = list(map(int, input_str.strip().split()))
def square(num):
    return num ** 2
square_list = list(map(square, input_list))
print("Square of list numbers:")
print(square_list)

#output
# Enter a list of integers separated by space: 4 5 2 9
# Square of list numbers:
# [16, 25, 4, 81]
