S = input()

head = []
tail = []

for i in range(len(S)):
    if S[i].isdigit():
        tail.append(int(S[i]))
    else:
        head.append(S[i])

head.sort()
print("".join(head) + str(sum(tail)))