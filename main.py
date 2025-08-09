from algorithms import bubble_sort, merge_sort, quick_sort, insertion_sort
from sorting_visualizer import sorting_visualizer
import random
import sys

LIST_SIZE = 200

list = [5,1,67,9,3,2,0,-66,150]
#print("Before: "+ str(list))
#insertion_sort.sort(list)
#quick_sort.sort(list)
#merge_sort.sort(list)
#bubble_sort.sort(list)
#print("After: "+ str(list))
#list = [i for i in range(1,LIST_SIZE+1)]
#random.shuffle(list)
#sv = sorting_visualizer(list)
#bubble_sort.sort(sv)
#print(sv.list)
#quick_sort.sort(sv)
#sorting_visualizer.visualize_list(list,LIST_SIZE)

def main(sort):
    list = [i for i in range(1,LIST_SIZE+1)]
    random.shuffle(list)
    sv = sorting_visualizer(list)

    if sort=="insertion":
        insertion_sort.sort(sv)
    elif sort=="quick":
        quick_sort.sort(sv)
    elif sort=="merge":
        merge_sort.sort(sv)
    elif sort=="bubble":
        bubble_sort.sort(sv)
    else:
        print("Faulty first arguement")
    sv.display(20)
    print(sv.list)


if __name__ == "__main__":
    if len(sys.argv)==2:
        main(sys.argv[1])
