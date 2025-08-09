from algorithms import bubble_sort, merge_sort, quick_sort, insertion_sort
import sorting_visualizer
import random

LIST_SIZE = 20

list = [5,1,67,9,3,2,0,-66,150]
#print("Before: "+ str(list))
#insertion_sort.sort(list)
#quick_sort.sort(list)
#merge_sort.sort(list)
#bubble_sort.sort(list)
#print("After: "+ str(list))
list = [i for i in range(1,LIST_SIZE+1)]
random.shuffle(list)
#quick_sort.sort(list)
sorting_visualizer.visualize_list(list,LIST_SIZE)

