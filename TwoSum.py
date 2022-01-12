# nums = [3, 3]
# target = 6
#
# for i in range(len(nums)):
#     if target - nums[i] in nums:
#         if i != nums.index(target - nums[i]):
#             print( i, nums.index(target - nums[i]))
#             break

# s = "abacb"
# k = -1
# dict = {}
# res = 0
# for i, value in enumerate(s):
#     if value in dict and dict[value] > k:
#         k = dict[value]
#         dict[value] = i
#     else:
#         dict[value] = i
#         res = max(i - k, res)
# print(res)

# nums = [1, 3, 5, 7, 9, 11, 19, 21]
# query = 5
# left = 0
# right = len(nums) - 1
# while left <= right:
#     mid = (left+right) // 2
#     if left == right:
#         if nums[left] == query:
#             print(left)
#             break
#         else:
#             print("None")
#             break
#     elif query == nums[mid]:
#         print(mid)
#         break
#     elif query > nums[mid]:
#         left = mid + 1
#     else:
#         right = mid - 1

# nums = [1, 3, 5, 7, 9, 11, 19, 21]
# query = 5
# left = 0
# right = len(nums) - 1
# while left <= right:
#     mid = (left+right) // 2
#     if left == right:
#         if nums[left] == query:
#             print(left)
#             break
#         else:
#             print("None")
#             break
#     elif query == nums[mid]:
#         print(mid)
#         break
#     elif query > nums[mid]:
#         left = mid + 1
#     else:
#         right = mid - 1

# num1 = [2, 4]
# num2 = [1, 3]
# for key in range(len(num2)):
#     left = 0
#     right = len(num1)
#     while left <= right:
#
#         mid = (left + right) // 2
#         if num1[mid] == key:
#             num1.insert(mid, key)
#             break
#         elif num1[mid] > key:
#             right = mid - 1
#         else:
#             left = mid + 1

# nums1 = []
# nums2 = []
# def QuickSort(left1, right1, nums2):
#     left = left1
#     right = right1
#     if left < right:
#         tmp = nums2[left]
#         while left != right:
#             while tmp <= nums2[right] and left < right:
#                 right = right - 1
#             if left < right:
#                 nums2[left] = nums2[right]
#                 left = left + 1
#
#             while nums2[left] <= tmp and left < right:
#                 left = left + 1
#             if left < right:
#                 nums2[right] = nums2[left]
#                 right = right - 1
#         nums2[left] = tmp
#         QuickSort(left1, left - 1, nums2)
#         QuickSort(right + 1, right1, nums2)
#     return nums2
# for key in range(len(nums1)):
#     nums2.append(nums1[key])
# left = 0
# right = len(nums2) - 1
# nums2 = QuickSort(left, right, nums2)
# if len(nums2) % 2 == 1:
#     print(nums2[right//2])
# else:
#     print((nums2[right//2] + nums2[right//2+1]) / 2)

# nums = [8, 9, 5, 10, 79, 52, 37]
# def QuickSort(left: int, right: int, nums2: list):
#     left1 = left
#     right1 = right
#     if left1 < right1:
#         tmp = nums2[left1]
#         while left1 != right1:
#             while tmp <= nums2[right1] and left1 < right1:
#                 right1 = right1 - 1
#             if left1 < right1:
#                 nums2[left1] = nums2[right1]
#                 left1 = left1 + 1
#             while tmp >= nums2[left1] and left1 < right1:
#                 left1 = left1 + 1
#             if left1 < right1:
#                 nums2[right1] = nums2[left1]
#                 right1 = right1 - 1
#             nums2[left1] = tmp
#             QuickSort(left, left1 - 1, nums2)
#             QuickSort(right1 + 1, right, nums2)
#     return nums2
# print(QuickSort(0, len(nums) - 1, nums))

# class Student():
#     name = ''
#     age = 0
#     def solution(self):
#         print("调用类内的函数，需要加 self")
#     def print_file(self):
#         print('name:' + self.name)
#         print('age:' + str(self.age))
#         self.solution()
# student = Student()
# student.print_file()

# nums1 = [1, 2]
# nums2 = [3, 4]
# n1, n2 = len(nums1), len(nums2)
# def get_kth_element(k: int) -> int:
#     i1, i2 = 0, 0
#     while k != 0:
#         if i1 == n1:        # 表示数组 nums1 已都完成计算
#             return nums2[i2 + k - 1]
#         if i2 == n2:        # 表示数组 nums2 已都完成计算
#             return nums1[i1 + k - 1]
#         if k == 1:          # 1//2 = 0 所有也要判断一下
#             return min(nums1[i1], nums2[i2])
#         new_i1 = min(i1 + k // 2 - 1, n1 - 1)  # 每个数组贡献 k//2
#         new_i2 = min(i2 + k // 2 - 1, n2 - 1)
#         pivot_1, pivot_2 = nums1[new_i1], nums2[new_i2]
#         if pivot_1 <= pivot_2:  # 把小的那段扔掉
#             k -= (new_i1 - i1 + 1)  # 做好index的更新    # 每删掉一个数
#             i1 = new_i1 + 1
#         else:
#             k -= (new_i2 - i2 + 1)
#             i2 = new_i2 + 1
# n = n1 + n2
# if n % 2 == 1:
#     print(get_kth_element((n + 1) // 2))  # 0 1 2 3 4  n=5 取第3个
#     print(111)
# else:
#     print((get_kth_element(n // 2) + get_kth_element((n + 2) // 2)) / 2.0)  # 0 1 2 3 n=4 取第2个，第3个的aver
#     print(222)

# s = 'abaca'
# n = len(s)
# if n < 2:
#     print(s)
# max_len = 1
# begin = 0
# # dp[i][j] 表示 s[i..j] 是否是回文串
# dp = [[False] * n for _ in range(n)]
# for i in range(n):
#     dp[i][i] = True
# # 递推开始
# # 先枚举子串长度
# for L in range(2, n + 1):
#     # 枚举左边界，左边界的上限设置可以宽松一些
#     for i in range(n):
#         # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
#         j = L + i - 1
#         # 如果右边界越界，就可以退出当前循环
#         if j >= n:
#             break
#         if s[i] != s[j]:
#             dp[i][j] = False
#         else:                   # j-i<3 代表下标相减小于3，即枚举长度为2和3的子串，如果有回文串就标记为true。
#             if j - i < 3:
#                 dp[i][j] = True
#             else:               # 如果子串长度大于3，那么这个子串的子串也必是回文串
#                 dp[i][j] = dp[i + 1][j - 1]
#         # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
#         if dp[i][j] and j - i + 1 > max_len:
#             max_len = j - i + 1
#             begin = i
# print(s[begin:begin + max_len])

# arr = [4, 5, 2, 1, 3, 6]
# swap = 0
# comp = 0
# for i in range(1, len(arr)):
#     for j in range(0, len(arr) - i):
#         comp = comp + 1
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             swap = swap + 3
# print(swap+comp)

# s = "tmmzuxt"
# dict = {}
# res = 0
# k = -1
# for i in range(len(s)):
#     value = s[i]
#     if value in dict and dict[value]>k:
#         k = dict[value]
#         dict[value] = i
#     else:
#         dict[value] = i
#         res = max(res, i-k)

# nums1 = [0, 0, 0, 0, 0]
# nums2 = [-1, 0, 0, 0, 0, 0, 1]
# n1, n2 = len(nums1), len(nums2)
# def find_kth_element(k: int):
#     i1, i2 = 0, 0
#     while k > 0:
#
#         if n1 == i1:
#             return nums2[i2 + k - 1]  # 下标 1
#         if n2 == i2:
#             return nums1[i1 + k - 1]  # 下标
#         if k == 1:
#             return min(nums1[i1], nums2[i2])
#
#         key1 = min(i1 + k // 2 - 1, n1 - 1)
#         key2 = min(i2 + k // 2 - 1, n2 - 1)   # min函数判断越界 2
#         value1 = nums1[key1]
#         value2 = nums2[key2]
#         if value1 >= value2:
#             k -= (key2 - i2 + 1)
#             i2 = key2 + 1
#         else:
#             k -= (key1 - i1 + 1)
#             i1 = key1 + 1
# n = n1 + n2
# if n % 2 == 1:
#     print(find_kth_element((n // 2) + 1))
# else:
#     print(((find_kth_element(n // 2) + find_kth_element((n // 2) + 1))) / 2.0)

# s = "babad"
# n = len(s)
# begin = 0
# max_len = 0
# if n == 1:
#     print(s)
# dp = [[False] * n for _ in range(0, n)]
# for i in range(n):
#     dp[i][i] = True
# for L in range(2, n + 1):
#     for i in range(0, n):
#         j = i + L - 1
#         if j < n:
#             if s[i] != s[j]:
#                 dp[i][j] = False
#             else:
#                 if j - i < 3:
#                     dp[i][j] = True
#                 else:
#                     dp[i][j] = dp[i + 1][j - 1]
#                 if dp[i][j] and L > max_len:
#                     max_len = max(L, max_len)
#                     begin = i
# print(s[begin:begin + max_len])

# s = "aa"
# p = "a"
#
# m, n = len(s), len(p)
#
#
# def match(self, i: int, j: int):
#     if i == 0:
#         return False
#     if p[j - 1] == ".":
#         return True
#     return s[i - 1] == p[j - 1]
#
#
# f = [[False] * (n + 1) for _ in range(m + 1)]
# f[0][0] = True
# for i in range(m+1):
#     for j in range(1, n+1):
#         if p[j-1] == '*':
#             f[i][j] |= f[i][j-2]
#             if match(i, j-1):
#                 f[i][j] |= f[i-1][j]
#
#         else:
#             if match(i, j):
#                 f[i][j] |= f[i-1][j-1]
#
# print(f[m][n])

# def sort(nums, i, j):
#     left = i
#     right = j
#     if left >= right:
#         return
#     if i < j:
#         temp = nums[i]
#         while (i < j):
#             while i < j and temp <= nums[j]:
#                 j = j - 1
#             if i < j:
#                 nums[i] = nums[j]
#                 i = i + 1
#             while i < j and temp >= nums[i]:
#                 i = i + 1
#             if i < j:
#                 nums[j] = nums[i]
#                 j = j - 1
#         nums[i] = temp
#     sort(nums, left, i - 1)
#     sort(nums, i + 1, right)
#     return nums
#
#
# nums = [-1, 0, 1, 2, -1, -4]
# length = len(nums)
# i = 0
# j = len(nums) - 1
# sort_nums = sort(nums, i, j)
# ans = []
# for first in range(length):  # 第一个下标
#     if first < length - 1 and nums[first] == nums[first + 1]:
#         continue
#     else:
#         second = length - 1  # 第二个下标
#         while second > first + 1 and nums[second] == nums[second - 1]:
#             second = second - 1
#         if second == first + 1:
#             break
#         else:
#             for third in range(first + 1, second):
#                 # if third < second and nums[third] == nums[third + 1]:
#                 #     continue
#                 target = -(nums[first] + nums[second])
#                 if nums[third] == target:
#                     ans.append([nums[first], nums[second], nums[third]])
# print(ans)

digits = "23"
DIG2LETTER = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
str_ans = []
def combination(tar_list, digits):
    if len(digits) == 0:
        str_ans.append(tar_list)
    else:
        for i in DIG2LETTER[digits[0]]:
            combination(tar_list+i, digits[1:])

if digits:
    combination('', digits)
print(str_ans)