from collections import defaultdict
from collections import deque

def solution(topping, tasting):
    topping_length = len(topping)
    topping_dict = defaultdict(list) # topping별로 idx 저장
    for i, item in enumerate(topping):
        topping_dict[item].append(i)

    queue = deque()
    queue.append((0, 0, 0))
    result = []

    # start bfs
    while queue:
        current, distance, taste_idx = queue.popleft()
        key = tasting[taste_idx]
        # 시계 방향
        for target in topping_dict[key]:
            dis = 10000000
            idx = current
            if target >= current:
                if (target - current) < dis:
                    dis = target - current
                    idx = target
            else:
                if (topping_length - current + target) < dis:
                    dis = (topping_length - current + target)
                    idx = target

            if taste_idx == len(tasting) - 1:
                result.append(dis+distance)
            else:
                queue.append((idx, dis + distance, taste_idx+1))

        # 반시계 방향
        for target in topping_dict[key]:
            dis = 10000000
            idx = current
            if current >= target:
                if (current - target) < dis:
                    dis = current - target
                    idx = target
            else:
                if dis > (current - target + topping_length):
                    dis = (current - target + topping_length)
                    idx = target

            if taste_idx == len(tasting) -1:
                result.append(dis + distance)
            else:
                queue.append((idx, dis + distance, taste_idx+1))

    return min(result)

print(solution([2,1,3,1,2,4,4,3], [1, 2, 3, 4]))
print(solution([2,1,3,1,2,4,4,3], [3,1,2,4]))
print(solution([2,1,3,1,2,4,4,3],[1,1,1,1]))