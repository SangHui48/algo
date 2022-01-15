# 행 1~8, 열 a~8
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0]) - ord('a') + 1)

vectors = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

result = 0
for r, c in vectors:
    nrow = row + r
    ncol = col + c

    if 1 <= nrow <= 8 and 1 <= ncol <= 8:
        result += 1

print(result)