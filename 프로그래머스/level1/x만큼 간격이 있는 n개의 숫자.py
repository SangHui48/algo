# def solution(x, n):
#     answer = []
#     for i in range(x, x * (n + 1), x):
#         answer.append(i)
#     return answer

def solution(x, n):
    return [x * i for i in range(1, n + 1)]

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))
print(solution(-4, 0))