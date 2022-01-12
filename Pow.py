# 计算 x 的 n 次方

x = 2.0000
n = 10

'Method 1'
'递归，刚进入 count 时 N=10，但经过递归实际上最开始处理的是 N=0。'
# def count(x, N):
#     if N == 0:
#         return 1.0
#     y = count(x, N // 2)
#     return y * y if N % 2 == 0 else y * y * x
#
# ans = count(x, n) if n >= 0 else 1 / count(x, -n)
# print(ans)

'Method 2'
'迭代，contribition 实际上是遍历了 x 的 n 次方，通过判断将二进制位为1的 contribition 乘入 ans'
def count(x, N):
    ans = 1.
    contribution = x
    while N>0:
        if N%2 == 1:
            ans *= contribution
        contribution *= contribution
        N //= 2
    return ans
ans = count(x, n)
print(ans)