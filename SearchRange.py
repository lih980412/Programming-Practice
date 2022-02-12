nums = [5, 7, 7, 8, 8, 10]
target = 8

if not nums:
    print(-1, -1)
left, right = 0, len(nums) - 1


def findLeft(nums, left, right):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if left < len(nums) and nums[left] == target:
        return left
    else:
        return -1


def findRight(nums, left, right):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
            # left = mid + 1
        else:
            left = mid + 1
            # right = mid - 1
    if right < len(nums) and nums[right] == target:
        return right
    else:
        return -1


l = findLeft(nums, left, right)
r = findRight(nums, left, right)
print(l, r)
