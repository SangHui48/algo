def solution(n, m):
    gcd = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
    return [gcd, gcd * (n // gcd) * (m // gcd)]

print(solution(3, 12))
print(solution(2, 5))