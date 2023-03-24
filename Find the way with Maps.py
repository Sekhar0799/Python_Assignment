input_str = input("Enter a list of integers separated by space: ")
input_list = list(map(int, input_str.strip().split()))
def triple(num):
    return num * 3
triple_list = list(map(triple, input_list))
print("Triple of list numbers:")
print(triple_list)