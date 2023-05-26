def solution(n, stations, w):
    answer = 0
    start = 1
    for station in stations:
        tmp = station
        while tmp - w - 1 >= start:
            tmp = tmp - 2 * w - 1
            answer += 1
        start = station + w + 1
    if start <= n:
        count = n - start + 1
        one = w * 2 + 1
        answer += count // one + (1 if count % one else 0)

    return answer
