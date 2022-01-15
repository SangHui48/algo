import sys
s = sys.stdin.readline().strip()

count0, count1 = 0, 0 # 전부 0으로 바꿀때나 전부 1로 바꿀때

if s[0] == '0':
    count1 += 1
else:
    count0 += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))