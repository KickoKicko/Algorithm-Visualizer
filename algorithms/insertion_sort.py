import sorting_visualizer

def sort(sv):
    for i in range(len(sv.list)):
        move_back(sv,i)

def move_back(sv, x):
    list = sv.list
    i=x-1
    while(list[i]>list[x]):
        i-=1
    temp = list[x]
    for i in range(i+1,x)[::-1]:
        list[i+1]=list[i]
        sv.update(x)
    list[i]=temp
    #sv.update(x)
