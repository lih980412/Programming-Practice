nums = [3, 4, 5, 1, 2]

left, right = 0, len(nums) - 1

while right > left:
    # mid = (left+right) // 2
    mid = left + (right - left) // 2
    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid

print(nums[left])
