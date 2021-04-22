
def insert_sort(list):
    for i in range(1,len(list)):
        tmp = list[i]
        j = i - 1
        while j>=0 and list[j]>tmp:
            list[j+1] = list[j]
            j-=1
        list[j+1] = tmp        
