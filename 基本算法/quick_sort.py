"""
快速排序是基于分治法的一种排序算法
空间复杂度： 最坏情况下为 O(n)    平均栈深度为 O(log2n)
时间复杂度： O(nlog2n)
快速排序是所有内部排序算法中平均性能最优的一种排序算法
"""

def quick_sort(arr):
    if len(arr) < 2:
        return arr

    mid = arr[len(arr) // 2]
    left,right = [], []
    arr.remove(mid)
    for i in arr:
        if i >= mid:
            right.append(i)
        else:
            left.append(i)
    return quick_sort(left) + [mid] + quick_sort(right)


ll = [10, 5, 1, 4, 14]
res = quick_sort(ll)
print(ll)
print(res)
