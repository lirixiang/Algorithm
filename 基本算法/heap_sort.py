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