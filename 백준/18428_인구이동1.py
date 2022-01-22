from collections import deque

n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]

result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    print(a, b)
    queue = deque()
    queue.append((a, b))
    visited = [[0] * n for _ in range(n)]
    visited[a][b] = countries[a][b]
    move = False
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if l <= abs(countries[nx][ny] - countries[x][y]) <= r and visited[nx][ny] == 0:
                    visited[nx][ny] = countries[nx][ny]
                    move = True
                    count += 1
                    queue.append((nx, ny))

    if move:
        total = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j] != 0:
                    total += visited[i][j]

        move_result = total // count

        for i in range(n):
            for j in range(n):
                if visited[i][j] != 0:
                    countries[i][j] = move_result
        return True
    else:
        return False

for i in range(n):
    for j in range(n):
        if bfs(i, j):
            result += 1

print(countries)
print(result)