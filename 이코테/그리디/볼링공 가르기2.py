n, m = map(int, input().split())
balls = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for ball in balls:
    #각 무게에 해당하는 볼링공의 개수 카운트
    array[ball] += 1

result = 0

# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수 제외(A가 선택한 케이스)
    result += array[i] * n # A가 선택할 수 있는 케이스 x B가 선택할 수 있는 케이스

print(result)