
def sift(li, low, high):
   i = low
   j = 2 * i + 1
   tmp = li[low]
   while j <= high:
       if j + 1 <= high and li[j+1] > li[j]:
           j += 1
       if li[j] > tmp:
           li[i] = li[j]
           i = j
           j = 2 * i + 1
       else:
           break
   li[i] = tmp
   

def heap_sort(li):
   # build a heap
   n = len(li)
   for i  in range(n//2 -1 , -1, -1):
       sift(li, i, n-1)
   
   for i in range(n-1, -1, -1):
       li[0], li[i] = li[i], li[0]
       sift(li, 0, i-1)
   
