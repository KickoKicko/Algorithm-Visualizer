from algorithms import bubble_sort, merge_sort

list = [5,1,67,9,3,2,0,-66,150]
print("Before: "+ str(list))
merge_sort.merge_sort(list)
#bubble_sort.bubble_sort(list)
print("After: "+ str(list))
