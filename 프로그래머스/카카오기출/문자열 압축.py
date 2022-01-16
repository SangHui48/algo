def solution(s):
    answer = len(s)
    mid = len(s) // 2
    for i in range(1, mid+1):
        tmp = ''
        token = s[:i]
        count = 1
        for j in range(i, len(s), i):
            if token == s[j : j + i]:
                count += 1
            else:
                tmp += str(count) + token if count >= 2 else token
                token = s[j:j+i]
                count = 1
        tmp += str(count) + token if count >= 2 else token
        answer = min(answer, len(tmp))
    return answer


print(solution("aabbaccc"))
