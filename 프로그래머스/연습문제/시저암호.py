def solution(s, n):
    answer = ''
    for word in s:
        if word == " ":
            answer += " "
        if word == "z":
            answer += chr(ord("a") - 1 + n)
        if word == "Z":
            answer += chr(ord("A") - 1 + n)
        if word != " " and word != 'z' and word != 'Z':
            if word.isupper():
                answer = answer + chr(ord(word) + n) if ord(word) + n <= 90 else answer + chr(ord('A') + (n + ord(word)) - 91)
            else:
                answer = answer + chr(ord(word) + n) if ord(word) + n <= 122 else answer + chr(ord('a') + (n + ord(word)) - 123)
    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
print(solution("AaZz",25))
print(solution("bC",25))
