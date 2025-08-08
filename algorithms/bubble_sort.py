def sort(list):
    while True:
        flag = False
        for i in range(len(list)-1):
            if(list[i]>list[i+1]):
                switch_values(list, i,i+1)
                flag = True
        if(not flag):
           break


def switch_values(list, i1, i2):
    t = list[i1]
    list[i1] = list[i2]
    list[i2] = t
