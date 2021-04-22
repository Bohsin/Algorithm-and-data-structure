
def select_sort(list):
    for i in range(len(list)-1):
        min_loc = i
        for j in range(i+1,len(list)):
            if list[j] < list[min_loc]:
                min_loc = j
        list[i], list[min_loc] = list[min_loc], list[i]
        
