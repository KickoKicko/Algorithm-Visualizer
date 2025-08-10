import sorting_visualizer

def sort(sv):
    recursion(sv,0,len(sv.list)-1)

def recursion(sv,start,end):
    if start-end==1:
        return
    pivot = partition(sv,start,end)
    #sv.update(pivot)
    recursion(sv,start,pivot-1)
    recursion(sv,pivot+1,end)

def partition(sv, low, high):
    i1=low-1
    for i2 in range(low,high):
        #sv.update(pivot)
        if sv.list[i2]<sv.list[high]:
            i1+=1
            swap(sv,i1,i2)
    i1+=1
    swap(sv,i1,high)
    return i1

def swap(sv,i1,i2):
    sv.list[i1], sv.list[i2] = sv.list[i2],sv.list[i1]
    #sv.update(i1,i2)
    sv.update(i1)
    