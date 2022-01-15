def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr1[0])
    answer = [[] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))