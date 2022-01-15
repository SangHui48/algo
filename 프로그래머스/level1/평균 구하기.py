def solution(arr):
    answer = sum(arr) / len(arr)
    if answer % 10 != 0:
        return answer
    else:
        return int(answer)

print(solution([1,2,3,4]))
print(solution([5,5]))