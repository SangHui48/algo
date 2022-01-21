from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
pan = [list(map(int, input().split())) for _ in range(n)]
sx, sy = map(int, input().split()) #톰 위치
ex, ey = map(int, input().split()) #제리 위치

q = deque()
q.append([sx-1, sy-1])
pan[sx-1][sy-1] = 2 # 톰위치 초기화
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < n and 0 <= ny < n and pan[nx][ny] != 1:
            if pan[nx][ny] == 0:
                q.append([nx, ny])
                pan[nx][ny] = pan[x][y] + 1
            nx += dx[i]
            ny += dy[i]

if pan[ex-1][ey-1] == 0:
    print(-1)
else:
    print(pan[ex-1][ey-1] - 3)

