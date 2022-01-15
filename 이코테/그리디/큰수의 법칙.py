n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

a, b = divmod(m, k)

answer = (a * data[-1] * k) + (b * data[-2])

print(answer)
