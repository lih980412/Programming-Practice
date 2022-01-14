# 两数相除，不适用乘法、除法和 mod 运算符

dividend = 10
divisor = 3

MAX, MIN = 2 ** 31 - 1, -2 ** 31
# if dividend == 0:
#     return 0
if dividend == MIN and divisor == -1:
    print(MAX)

flag = 0
if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
    flag = 1
    if divisor < 0:
        divisor = -divisor
    else:
        dividend = -dividend
if dividend < 0 and divisor < 0:
    divisor = -divisor
    dividend = -dividend


def compute(a, b):
    count = 1
    tb = b
    if a < b:
        return 0
    while tb + tb <= a:
        count += count
        tb += tb
    return count + compute(a - tb, b)


ans = compute(dividend, divisor)
if flag:
    ans = -ans
print(ans)
