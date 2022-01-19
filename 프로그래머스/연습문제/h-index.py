def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    if n == 1:
        if citations[0] != 1:
            return 1
        else:
            return 0

    for i in range(n + 1):
        bigger = len([x for x in citations if x >= i])
        smaller = len([x for x in citations if x <= i])
        if bigger >= i >= smaller:
            answer = max(answer, i)
    return answer

# def solution(citations):
#     answer = 0
#     citations.sort()
#     n = len(citations)
#     for i in range(n):
#        h_index =
#     return answer

print(solution([3, 0, 6, 1, 5]))
print(solution([22, 42]))
print(solution([3]))