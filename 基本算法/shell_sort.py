def shell_sort(alist):
    n = len(alist)
    gap = n // 2


    i = 1
    if alist[i]<alist[i-gap]:
        alist[i],alist[i-gap] = alist[i-gap],alist[i]
    else:
        pass
if __name__ == '__main__':
    pass

