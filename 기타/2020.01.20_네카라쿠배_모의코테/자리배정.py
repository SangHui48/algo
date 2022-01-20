r, c = map(int, input().split())
k = int(input())

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
direction = 0

seats = [[0] * (c + 2) for _ in range(r + 2)]

for i in range(r + 2):
    seats[i][0] = 1
    seats[i][c+1] = 1

for i in range(c + 2):
    seats[0][i] = 1
    seats[r+1][i] = 1

col = 1
row = 1
wait_num = 1
flag = False

while wait_num <= r * c:
    if wait_num == k:
        flag = True
        break
    seats[col][row] = 1
    ny = col + dy[direction]
    nx = row + dx[direction]

    if seats[ny][nx] == 1:
        direction = (direction + 1) % 4

    col = col + dy[direction]
    row = row + dx[direction]
    wait_num += 1

if flag:
    print(col, row)
else:
    print(0)




