n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] #맵 정보
info = []

# 사과 정보
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

#방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c= input().split()
    info.append((int(x), c))

#처음에는 오른쪾 보고 있었으므로 시계방향 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 #뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 #처음은 동쪽
    time = 0 #경과 시간
    index = 0 #다음에 회전할 정보
    q = [(x, y)] #뱀이 차지하고 있는 위치 정보
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 몸통이 늘어나야 한다.
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪힐때
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1

        if index < l and time == info[index][0]: #회전할 시간인 경우
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())