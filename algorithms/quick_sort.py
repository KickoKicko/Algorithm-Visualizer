import time
import sorting_visualizer

def sort(list):
    recursion(list,0,len(list)-1)

def recursion(list,start,end):
    if start-end==1:
        return
    pivot = partition(list,start,end)
    recursion(list,start,pivot-1)
    recursion(list,pivot+1,end)

def partition(list, low, high):
    i1=low-1
    for i2 in range(low,high):
        sorting_visualizer.visualize_list(list,len(list))
        time.sleep(1)
        if list[i2]<list[high]:
            i1+=1
            swap(list,i1,i2)
    i1+=1
    swap(list,i1,high)
    return i1

def swap(list,i1,i2):
    list[i1], list[i2] = list[i2],list[i1]