def solution(routes):
    routes.sort(key=lambda x : x[0])
    answer = 1
    time = routes[0][1]
    for s, e in routes[1:]:
        if s <= time:
            time = min(time, e)
            continue
        time = e
        answer += 1
    return answer
