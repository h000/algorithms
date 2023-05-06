import heapq

def solution(n, works):
    answer = 0
    works = [-work for work in works]
    heapq.heapify(works)
    while works and n > 0:
        work = -heapq.heappop(works)
        work -= 1
        if work > 0:
            heapq.heappush(works, -work)
        n -= 1
    for work in works:
        answer += work * work
    return answer
