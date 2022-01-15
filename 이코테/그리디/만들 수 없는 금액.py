n = int(input())
data = list(map(int, input().split()))

data.sort()

target = 1

for coin in data:
    if target >= coin:
        target += coin
    else:
        break

print(target)