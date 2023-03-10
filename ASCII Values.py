# Method 1
ascii_dict = {}
for num in range(97, 123):
    ascii_dict[chr(num)] = num
print(ascii_dict)

# Method 2

ascii_dic1={}
for char in range(ord('a'),ord('z')+1):
    ascii_dic1[chr(char)]= char
print(ascii_dic1)