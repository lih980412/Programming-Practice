nums = [4,5,6,7,8,9,0,1,2]
target = 0

'二分法'
'https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/'
'https://leetcode-cn.com/circle/discuss/rFK9HC/view/tDWDHh/'


'Method 2'
left, right = 0, len(nums)-1
while left<=right:
    mid = (right+left) // 2
    if nums[mid] == target:
        print(mid)
    if nums[left]<=nums[mid]:             # 需要注意加等号，即left和mid重合的情况下，[3, 1] target为1
        if nums[left]<=target<=nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if nums[mid]<=target<=nums[right]:
            left = mid + 1
        else:
            right = mid - 1
print(-1)



'Method 1'
left, right = 0, len(nums) - 1
while left < right:
    mid = (right + left) // 2
    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid

if nums[0] < nums[len(nums) - 1]:
    left, right = 0, len(nums) - 1
else:
    if target == nums[-1]:
        print(len(nums) - 1)
    if target < nums[-1]:
        left, right = left, len(nums) - 1
    else:
        left, right = 0, left - 1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        print(mid)
    if nums[mid] > target:
        right = mid - 1
    else:

        left = mid + 1
print(-1)