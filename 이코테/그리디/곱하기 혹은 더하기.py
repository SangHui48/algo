number = list(map(int, list(input())))

result = 0
for num in number:
    if result != 0 and num != 0 and result <= 2000000000:
        result *= num
    else:
        result += num

print(result)