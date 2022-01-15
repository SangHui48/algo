n = int(input())
plans = input().split()
x, y = 1, 1
vector = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

for plan in plans:
    nx = x + vector[plan][0]
    ny = y + vector[plan][1]

    if 1 <= nx <= 5 and 1 <= ny <= 5:
        x = nx
        y = ny

print(x, y)