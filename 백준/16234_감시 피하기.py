from collections import deque

n = int(input())
room = [list(input().split()) for _ in range(n)]
check = False
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

def bfs():
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if room[i][j] == 'T':
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            temp_x, temp_y = x, y
            while True:
                nx = temp_x + dx[i]
                ny = temp_y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if room[nx][ny] == 'X' and visited[nx][ny] == False:
                        visited[nx][ny] = True
                    elif room[nx][ny] == 'S':
                        return False
                    elif room[nx][ny] == 'O':
                        break
                    temp_x, temp_y = nx, ny
                else:
                    break
    return True

def recursive(index):
    global check
    if index == 3:
        if bfs():
            check = True
        return

    for i in range(n):
        for j in range(n):
            if room[i][j] == 'X':
                room[i][j] = 'O'
                recursive(index + 1)
                room[i][j] = 'X'
recursive(0)

if check:
    print('YES')
else:
    print('NO')