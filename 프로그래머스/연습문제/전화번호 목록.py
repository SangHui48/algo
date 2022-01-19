# from collections import defaultdict
#
# def solution(phone_book):
#     phone_map = defaultdict(int)
#
#     for number in phone_book:
#         phone_map[number] +=1
#
#     for number in phone_book:
#         tmp = ''
#         for num in number:
#             tmp += num
#             if tmp in phone_map and tmp != number:
#                 return False
#     return True

def solution(phone_book):
    phone_book = sorted(phone_book)

    # for p1, p2 in zip(phone_book, phone_book[1:]):
    #     print(p1, p2)



    answer = True
    return answer


print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123","456","789"]))
# print(solution(["12","123","1235","567","88"]))

