import sorting_visualizer

def sort(sv):
    for i in range(len(sv.list)):
        move_back(sv,i)

def move_back(sv, x):
    list = sv.list
    i=x-1
    while i>=0 and list[i]>list[x]:
        i-=1
    temp = list[x]
    for j in range(x-1,i,-1):
        list[j+1]=list[j]
        sv.update(j,x)
    list[i+1]=temp
