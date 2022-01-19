def solution(topping, tasting):
    length = len(topping)
    for i in range(length):
        topping.append(topping[i] + length)


    for i in range(n * 2):
        if i < n:
            if topping[i] == tasting[idx]:
                idx += 1
        # i >= n
        else:
            if topping[i] == tasting[idx] + n:
                idx += 1
        # 전부 다 돌았을 경우
        if idx == len(tasting) - 1:
            answer = min(answer, hour)
            hour = 0
            continue
        hour += 1
    return answer

print(solution([2,1,3,1,2,4,4,3], [1, 2, 3, 4]))