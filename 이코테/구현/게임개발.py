# 열 A 행 B
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북 동 남 서

n, m = map(int, input().split())
a, b, direction = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * m for _ in range(n)] # 방문정보 위치 저장
d[a][b] = 1

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    # 왼쪽 회전
    turn_left()
    na = a + dx[direction]
    nb = a + dy[direction]

    # 회전 후 이동할 수 있으면 전진
    if d[na][nb] == 0 and map[na][nb] == 0:
        d[na][nb] = 1
        a = na
        b = nb
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1 #회전 이후 정면에 가보지 않은 칸이 없거나 바다인 경우

    if turn_time == 4:
        # 네방향 모두 가봣을 경우
        na = a - dx[direction]
        nb = b - dy[direction]

        # 뒤로 갈수 있다면 이동하기
        if map[na][nb] == 0:
            a = na
            b = nb
        else:
            break
        turn_time = 0

print(count)