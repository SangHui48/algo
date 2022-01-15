n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]

answer = min(cards[0])
for row in cards:
    answer = max(answer, min(row))

print(answer)