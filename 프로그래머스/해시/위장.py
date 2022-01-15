from collections import defaultdict

def solution(clothes):
    closet = defaultdict(list)
    for item in clothes:
        closet[item[1]].append(item[0])

    answer = 1

    for items in closet.values():
        answer *= (len(items) + 1)

    answer -= 1

    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))