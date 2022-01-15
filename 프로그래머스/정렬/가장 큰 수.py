# from itertools import permutations

# def solution(numbers):
#     answer = 0
#     combinations = list(permutations(numbers, len(numbers)))
#
#     for case in combinations:
#         tmp = ''
#         for item in case:
#             tmp += str(item)
#         answer = max(answer, int(tmp))
#
#     return str(answer)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0,0,0]))
