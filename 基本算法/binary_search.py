def binary_search(alist,item):
    """递归"""
    n = len(alist)
    if n>0:
        mid = n//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid],item)
        else:
            return binary_search(alist[mid+1:],item)
    return False

def binary_search_2(alist,item):
    """非递归"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first+last)//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid -1
        else:
            first = mid + 1
    return False

if __name__ == '__main__':
    li = [17,4,5,6,6,7,7,88]
    print(binary_search_2(li,8))

