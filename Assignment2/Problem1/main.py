### 1. Question: Merge and Sort Two Lists
#Description:** Given two lists of integers
# merge them into one list and sort the result in ascending order.
# Do not use Python's built-in sort() function or other sorting functions.
s1=[2,4,6]
s2=[1,3,5]
merged_list=s1+s2
sortedList=[]
for i in range(len(merged_list)):
    smallest = merged_list[0]
    for j in range(len(merged_list)):
        if merged_list[j] < smallest:
            smallest = merged_list[j]
    sortedList.append(smallest)
    merged_list.remove(smallest)

print(sortedList)