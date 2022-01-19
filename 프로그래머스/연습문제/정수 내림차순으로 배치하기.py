def solution(n):
    tmp = [int(i) for i in str(n)]
    tmp.sort(reverse=True)
    answer = ''
    for i in tmp:
        answer += str(i)
    return int(answer)

print(solution(118372))
