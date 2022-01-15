def solution(food_times, k):
    answer = -1
    one_rotate_duration = len(food_times) # 테이블을 한바퀴 도는데 필요한 시간
    can_rotate = k // one_rotate_duration # 총 몇바퀴 돌수있는지

    array = [] # 돌수있는만큼 다 돌고 남은 food의 양

    for food in food_times:
        array.append(food - can_rotate)

    idx = 0
    need_rotate = k % one_rotate_duration  # 끝까지 다 돌고 다시 방송이 꺼지기 전까지 다시 돌떄
    # 남은 시간 처리
    while need_rotate > 0:
        if array[idx] <= 0:
            idx += 1
            continue
        else:
            array[idx] -= 1
            idx += 1
            need_rotate -= 1

    # 다시 시작하면 되는 위치 찾기
    for idx ,food in enumerate(array):
        if food != 0:
            answer = idx + 1
    return answer

print(solution([3,1,2], 5))