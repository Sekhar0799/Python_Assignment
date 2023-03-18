# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


def count_upper_lower():
    user_str1 = input("Enter a string: ")
    upper_count = 0
    lower_count = 0
    for char in user_str1:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("No. of Upper case characters : ", upper_count)
    print("No. of Lower case characters : ", lower_count)
count_upper_lower()

# Output
# Enter a string: The quick Brow Fox
# No. of Upper case characters :  3
# No. of Lower case characters :  12
