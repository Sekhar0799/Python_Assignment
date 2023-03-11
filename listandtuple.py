# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#By using input user

tup_list = []
n = int(input("Enter the number of tuples:"))
for i in range(n):
    tup_input = input("Enter the tuple separated by comma:")
    tup_val = tuple(map(int,tup_input.split(',')))
    tup_list.append(tup_val)
sorted_tup_list = sorted(tup_list,key=lambda x:x[-1])
print(sorted_tup_list)

#Output

# Enter the number of tuples:5
# Enter the tuple separated by comma:2,5
# Enter the tuple separated by comma:1,2
# Enter the tuple separated by comma:4,4
# Enter the tuple separated by comma:2,3
# Enter the tuple separated by comma:2,1

# [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

#Method 2
sample_list1 =[(2,5),(1,2),(4,4),(2,3),(2,1)]
# By using lambda inside sorted()
sorted_list1=sorted(sample_list1,key=lambda x:x[-1])
print(sorted_list1)

# Output
# [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
