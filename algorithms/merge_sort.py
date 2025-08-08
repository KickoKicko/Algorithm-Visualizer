def merge_sort(list):
    recursion(list)

def recursion(list):
    if len(list) ==1:
        return
    l1 = [i for i in list[0:len(list)//2]]
    l2 = [i for i in list[len(list)//2:len(list)]]
    recursion(l1)
    recursion(l2)
    merge(list,l1, l2)


def merge(list,l1, l2):
    i1=0
    i2=0
    for i in range(len(list)):
        if i1<len(l1) and i2<len(l2):
            if(l1[i1]<l2[i2]):
                list[i] = l1[i1]
                i1 =i1+1
            else:
                list[i] = l2[i2]
                i2 =i2+1
        else:
            if i1<len(l1):
                list[i] = l1[i1]
                i1 =i1+1
            else:
                list[i] = l2[i2]
                i2 =i2+1
