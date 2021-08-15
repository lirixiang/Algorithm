# def reverse(pHead):
#     if pHead is None:
#         return pHead
#     last = None
#     while pHead:
#         tmp = pHead.next
#         pHead.next = last
#         last = pHead
#         pHead = tmp
#     return last
#
# ll = [1,2,3,4,5,3,6]
# def f(n):
#     print(n)
#     if n < 0:
#         return
#     a = f(n - 1)
#     print(n)
#
#     #print(n)
#
# f(7)
nums = [3,4,3,5,6,3,78,1,2]

size = len(nums)
def maxheap(i):
    l = 2*i + 1
    r = 2*i + 2
    large = i
    if l < size and nums[l] > nums[large]:
        large = l
    if r < size and nums[r] > nums[large]:
        large = r
    if large != i:
        nums[large],nums[i] = nums[i],nums[large]
        maxheap(large)

for i in range(size//2,-1,-1):
    maxheap(i)
print(nums)
for i in range(size-1,-1,-1):
    nums[0],nums[i] = nums[i],nums[0]
    size -= 1
    maxheap(0)
print(nums)

class Singletion():
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

s1 =Singletion()
print(s1)
s2 =Singletion()
print(s2)
s3 =Singletion()
print(s3)


def FindPath(self, root):
    # write code here
    if root == None:
        return []

    def DFS(root, path):
        if root.left == None and root.right == None :
            result.append(path)
        if root.left != None:
            DFS(root.left, path + [root.left.val])
        if root.right != None:
            DFS(root.right, path + [root.right.val])

    result = []
    DFS(root, [root.val])

    return result