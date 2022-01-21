def clock_dir(start, key, dict, topping_length):
    key_idxs = dict[key]
    result = 150
    idx = start
    for item in key_idxs:
        if item >= start:
            if result > (item - start):
                result = item - start
                idx = item
        else:
            if result > (topping_length - start) + item:
                result = (topping_length - start) + item
                idx = item
    return result, idx

def reverse_dir(start, key, dict, topping_length):
    key_idxs = dict[key]
    result = 150
    idx = start
    for item in key_idxs:
        if item <= start:
            if result > (start-item):
                result = (start-item)
                idx = item
        else:
            if result > (start - item + topping_length):
                result = (start - item + topping_length)
                idx = item
    return result, idx

def solution(topping, tasting):
    topping_length = len(topping)
    topping_dict = {}
    for i in range(topping_length):
        if topping[i] in topping_dict:
            topping_dict[topping[i]].append(i)
        else:
            topping_dict[topping[i]] = [i]

    start_idx = 0
    result = 0
    for item in tasting:
        clock, c_idx = clock_dir(start_idx, item, topping_dict, topping_length)
        reverse_clock, r_idx = reverse_dir(start_idx, item, topping_dict, topping_length)

        if clock <= reverse_clock:
            result += clock
            start_idx = c_idx
        else:
            result += reverse_clock
            start_idx = r_idx

    return result


# print(solution([2,1,3,1,2,4,4,3], [1, 2, 3, 4]))
print(solution([2,1,3,1,2,4,4,3], [3,1,2,4]))