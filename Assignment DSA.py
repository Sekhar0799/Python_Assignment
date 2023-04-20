# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def find_pairs(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 10
print(find_pairs(arr, target_sum))  

# output
[(1, 9), (2, 8), (3, 7), (4, 6)]

# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

arr = [1, 2, 3, 4, 5, 6]
print(reverse_array(arr)) 

# Output
[6, 5, 4, 3, 2, 1]

# Q3. Write a program to check if two strings are a rotation of each other?
def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    temp = str1 + str1
    if str2 in temp:
        return True
    else:
        return False

str1 = 'abcd'
str2 = 'cdab'
print(are_rotations(str1, str2))  

#Output
True

# Q4. Write a program to print the first non-repeated character from a string?

def first_non_repeated_character(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None

string = "abacddbec"
print(first_non_repeated_character(string)) 

# Output
e

# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)

n = 3
tower_of_hanoi(n, 'A', 'C', 'B')

# output
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod B
Move disk 1 from rod C to rod B
Move disk 3 from rod A to rod C
Move disk 1 from rod B to rod A
Move disk 2 from rod B to rod C
Move disk 1 from rod A to rod C


# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def postfix_to_prefix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for char in expression:
        if char not in operators:
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(char + operand1 + operand2)
    return stack.pop()


expression = "AB+CD-*"
print(postfix_to_prefix(expression))  

# output
*+AB-CD

# Q7. Write a program to convert prefix expression to infix expression.

def prefix_to_infix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for char in reversed(expression):
        if char not in operators:
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append('(' + operand1 + char + operand2 + ')')
    return stack.pop()

expression = "-+AB*CD"
print(prefix_to_infix(expression))  

# output
((A+B)-(C*D))

# Q8. Write a program to check if all the brackets are closed in a given code snippet.

def check_brackets(code):
    stack = []
    opening_brackets = set(['(', '[', '{'])
    closing_brackets = set([')', ']', '}'])
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if bracket_pairs[top] != char:
                return False
    if len(stack) != 0:
        return False
    return True

code_snippet = 'print("Hello, World!")'
print(check_brackets(code_snippet)) 

code_snippet = 'if (x > 0): print("Positive")'
print(check_brackets(code_snippet))  

code_snippet = 'for (i = 0; i < n; i++ { print(i) }'
print(check_brackets(code_snippet))  

# output
True
True
False

# Q9. Write a program to reverse a stack.

def reverse_stack(stack):
    if len(stack) == 0:
        return stack
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)

def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
        return
    temp = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(temp)
    
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)  

# Output
[5, 4, 3, 2, 1]

# Q10. Write a program to find the smallest number using a stack.

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)
        if len(self.min_stack) == 0 or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        item = self.stack.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        return item

    def get_min(self):
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]


stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)
print(stack.get_min())
stack.pop()
stack.pop()
print(stack.get_min()) 

# Output
1
3
