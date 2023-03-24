input_str = input("Enter a list of integers separated by space: ")
input_list = list(map(int, input_str.strip().split()))
def square(num):
    return num ** 2
square_list = list(map(square, input_list))
print("Square of list numbers:")
print(square_list)