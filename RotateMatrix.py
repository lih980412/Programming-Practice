# 要求不额外开辟矩阵

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

n = len(matrix)
'先水平画线折叠换位 matrix[row][col] = matrix[n-row-1][col],'
'再主对角线换位 matrix[row][col] = matrix[col][row]'
'这样只需要一半的矩阵换位'
for i in range(n // 2):
    for j in range(n):
        matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

for i in range(n):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

'通过推导得到关键等式：matrix[row][col] = matrix[col][n-row-1]'
# for i in range(n//2):
#     for j in range((n+1)//2):
#         temp = matrix[i][j]
#         matrix[i][j] = matrix[n-j-1][i]
#         matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
#         matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
#         matrix[j][n-i-1] = temp
