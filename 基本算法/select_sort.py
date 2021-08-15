def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n-1):
        min = j
        for i in range(j+1,n):
            if alist[min] > alist[i]:
                min = i
        alist[j],alist[min] = alist[min],alist[j]

if __name__ == '__main__':
    li = [1,233,4,5,56,66,7]
    print(li)
    select_sort(li)
    print(li)
