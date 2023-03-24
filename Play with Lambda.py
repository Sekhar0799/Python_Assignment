# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# sample input: 10
# sample output: 35

add_25 = lambda num: num + 25
num = int(input("Enter a number: "))
result = add_25(num)
print(f"The result of adding 25 to {num} is {result}")

#output
# Enter a number: 10
# The result of adding 25 to 10 is 35
