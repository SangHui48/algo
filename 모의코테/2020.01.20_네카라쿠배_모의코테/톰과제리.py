from collections import deque

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

tom_x, tom_y = map(int, input().split())
jerry_x, jerry_y = map(int, input().split())

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0

def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] == 0:
                    if dx[i] != 0:
                        for j in range(nx, n):
                            if data[j][ny] == 1:
                                break
                            if visited[j][ny] == 0:
                                visited[j][ny] = visited[x][y] + 1
                                q.append([j, ny])

                    elif dy[i] != 0:
                        for k in range(ny, n):
                            if data[nx][k] == 1:
                                break
                            if visited[nx][k] == 0:
                                visited[nx][k] = visited[x][y] + 1
                                q.append([nx, k])

    return visited[jerry_x-1][jerry_y-1]

result = bfs(tom_x-1, tom_y-1)
if result == 0:
    print(-1)
else:
    print(result - 1)
