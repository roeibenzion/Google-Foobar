def solution(data: list, n: int) -> list:
    count_app = dict()

    for num in data:
        count_app[num] = count_app.get(num, 0) + 1
    len_data = len(data)
    i = 0
    while i < len_data:
        if count_app[data[i]] > n:
            data = data[:i] + data[i+1:]
            len_data-=1
        else:
            i+=1
    return data

print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 2))
