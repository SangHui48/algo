N = list(map(int, list(input())))
left = N[: len(N) // 2]
right = N[len(N) // 2:]

print('LUCKY' if sum(left) == sum(right) else 'READY')