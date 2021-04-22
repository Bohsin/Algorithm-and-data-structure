
def binary_search(list, value):
    left = 0
    right = len(list)-1
    while left<=right:
        mid = (left + right) // 2
        if list[mid] == value:
            return mid
        elif list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return None
