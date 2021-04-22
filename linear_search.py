
def linear_search(list, val):
    for ind, v in enumerate(list):
        if v == val:
            return ind
    else: 
        return None
