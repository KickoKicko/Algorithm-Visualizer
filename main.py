from algorithms import bubble_sort, merge_sort, quick_sort, insertion_sort
from sorting_visualizer import sorting_visualizer
import random

LIST_SIZE = 50

list = [5,1,67,9,3,2,0,-66,150]
#print("Before: "+ str(list))
#insertion_sort.sort(list)
#quick_sort.sort(list)
#merge_sort.sort(list)
#bubble_sort.sort(list)
#print("After: "+ str(list))
list = [i for i in range(1,LIST_SIZE+1)]
random.shuffle(list)
sv = sorting_visualizer(list)
quick_sort.sort(sv)
#sorting_visualizer.visualize_list(list,LIST_SIZE)

