import sorting_visualizer

def sort(sv):
    while True:
        flag = False
        for i in range(len(sv.list)-1):
            if(sv.list[i]>sv.list[i+1]):
                swap(sv, i,i+1)
                flag = True
        if(not flag):
           break


def swap(sv, i1, i2):
    sv.list[i1], sv.list[i2] = sv.list[i2],sv.list[i1]
    sv.update()
