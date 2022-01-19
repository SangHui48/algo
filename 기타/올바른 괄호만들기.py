from itertools import combinations

def check(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return False
    if count != 0:
        return False
    else:
        return True

def solution(s):
    for i in range(len(s), 1, -1):
        comb = set(list(combinations(list(s), i)))

        count = 0
        for c in comb:
            if check(c):
                count += 1

        if count != 0:
            return count
    return 0

print(solution("()(()()"))