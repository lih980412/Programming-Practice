nums = [1,1,2]

length = len(nums)
fast = 1
slow = 0
while fast<length:
    if nums[fast] == nums[fast-1]:
        nums[slow] = nums[fast]
        slow += 1
    fast += 1
str = "112"
str.find("2")

print(11)