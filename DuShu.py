board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

col = [[0] * 9 for _ in range(9)]
row = [[0] * 9 for _ in range(9)]
gird = [[0] * 9 for _ in range(9)]
# print(len(col), len(col[0]))

for i in range(9):
    for j in range(9):

        if board[i][j] != '.':
            # print(i)
            # print(j)

            num = int(board[i][j]) - 1
            print(num)
            row[i][num] += 1
            col[j][num] += 1
            gird[i // 3 * 3 + j // 3][num] += 1
            # print(str(i//3*3) + " " + str(j//3))

            if row[i][num] > 1 or col[j][num] > 1 or gird[i // 3 * 3 + j // 3][num] > 1:
                print(False)
print(True)
