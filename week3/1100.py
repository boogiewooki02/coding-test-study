# 하얀 칸

board = [list(input()) for _ in range(8)]
result = 0

for i in range(8):
    for j in range(8):
        if ((i+j) % 2 == 0) and board[i][j] == 'F':
            result += 1

print(result)

# 2차원 리스트 입력 받기