from collections import deque

def solution(n, roads, sources, destination):
    answer = [-1 for _ in range(n + 1)]
    answer[destination] = 0
    
    road = {}
    for s, d in roads:
        a = road.get(s, [])
        b = road.get(d, [])
        a.append(d)
        b.append(s)
        road[s] = a
        road[d] = b
    
    answer[destination] = 0
    q = deque()
    q.append([destination, 1])
    while q:
        tmp, dist = q.popleft()
        for r in road.get(tmp, []):
            if answer[r] != -1:
                continue
            answer[r] = dist
            q.append([r, dist + 1])
    
    ret = []
    for s in sources:
        ret.append(answer[s])
    
    return ret
