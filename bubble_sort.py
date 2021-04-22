
def bubble_sort(list):
    n = len(list)
    for i in range(n-1):
        exchange = False
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                exchange = True
        if not exchange:
            return
