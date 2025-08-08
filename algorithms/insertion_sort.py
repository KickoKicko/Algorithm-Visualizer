def sort(list):
    for i in range(len(list)):
        move_back(list,i)

def move_back(list, x):
    i=x-1
    while(list[i]>list[x]):
        i-=1
    temp = list[x]
    for i in range(i+1,x)[::-1]:
        list[i+1]=list[i]
    list[i]=temp

def swap(list,i1,i2):
    list[i1],list[i2]=list[i2],list[i1]
