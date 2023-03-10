# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


sample_list1 =[(2,5),(1,2),(4,4),(2,3),(2,1)]
# By using lambda inside sorted()
sorted_list1=sorted(sample_list1,key=lambda x:x[-1])
print(sorted_list1)

# Output
# [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
