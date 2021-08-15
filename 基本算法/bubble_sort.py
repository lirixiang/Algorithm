def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        for i in range(n-1-j):
           if  alist[i]>alist[i+1]:
               alist[i],alist[i+1] = alist[i+1],alist[i]


        


if __name__ == '__main__':
    li = [1,233,4,5,56,66,7]
    print(li)
    bubble_sort(li)
    print(li)
