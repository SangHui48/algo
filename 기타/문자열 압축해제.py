def solution(s):
    answer = 0
    stack = []
    for x in s:
        if x != ')':
            stack.append(x)
        else:
            tmp = ''
            while stack:
                c = stack.pop()
                if c == '(':
                    num = ''
                    while stack and stack[-1].isdigit():
                        num = stack.pop() + num
                    res = ''
                    if num == '':
                        num = 1
                    for i in range(int(num)):
                        res += tmp
                    stack.append(res)
                    break
                else:
                    tmp = c + tmp

    answer = "".join(stack)
    return answer

print(solution("2(ab)k3(bc)"))
print(solution("3(a2(b))ef"))