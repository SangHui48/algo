n = int(input())
data = list(map(int, input().split()))
data.sort()

cnt = 0
idx = 0

while idx < len(data):
    group = data[idx: idx+data[idx]]
    if len(group) >= max(group):
        cnt += 1
    idx += len(group)

print(cnt)