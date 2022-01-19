def solution(s):
    words = s.split(' ')
    for i in range(len(words)):
        tmp = ''
        for j in range(len(words[i])):
            if j % 2 == 0:
                tmp += words[i][j].upper()
            else:
                tmp += words[i][j].lower()
        words[i] = tmp
    return " ".join(words)

print(solution("try hello world"))
