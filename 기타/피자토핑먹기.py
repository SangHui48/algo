def solution(topping, tasting):
    answer = len(topping) # 최악의 경우 피자한판 다 돌아야 하므로
    for i in range(len(topping)):
        # 해당 지점부터 시계방향, 반시계방향으로 돌며 모든 경우를 탐색해본다.
        clock = topping[i:] + topping[:i] # 시계방향
        reverse_clock = topping[i::-1] + topping[-1:i:-1] #반시계 방향

        for start in clock:


    return answer

print(solution([2,1,3,1,2,4,4,3], [1, 2, 3, 4]))
# print(solution([2,1,3,1,2,4,4,3], [3,1,2,4]))