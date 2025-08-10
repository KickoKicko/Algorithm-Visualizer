from algorithms import bubble_sort, merge_sort, quick_sort, insertion_sort
from sorting_visualizer import sorting_visualizer
import random
import sys

#LIST_SIZE = 200

def main(sort,list_size):
    list = [i for i in range(1,list_size+1)]
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
    sv.display(5)
    print(sv.list)


if __name__ == "__main__":
    if len(sys.argv)==3:
        main(sys.argv[1], int(sys.argv[2]))
