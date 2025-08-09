import time
import sorting_visualizer

def sort(sv):
    recursion(sv,0,len(sv.list)-1)

def recursion(sv,start,end):
    if start-end==1:
        return
    pivot = partition(sv,start,end)
    recursion(sv,start,pivot-1)
    recursion(sv,pivot+1,end)

def partition(sv, low, high):
    i1=low-1
    for i2 in range(low,high):
        sv.update(i2)
        time.sleep(0.1)
        if sv.list[i2]<sv.list[high]:
            i1+=1
            swap(sv.list,i1,i2)
    i1+=1
    swap(sv.list,i1,high)
    return i1

def swap(list,i1,i2):
    list[i1], list[i2] = list[i2],list[i1]