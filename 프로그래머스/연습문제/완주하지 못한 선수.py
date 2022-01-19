# from collections import defaultdict
#
# def solution(participant, completion):
#     answer = ''
#     completion_map = defaultdict(int)
#
#     for com in completion:
#         completion_map[com] += 1
#
#     for person in participant:
#         if person not in completion_map:
#             return person
#         completion_map[person] -= 1
#
#     for k, v in completion_map.items():
#         if v != 0:
#             return k

from collections import Counter

def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))