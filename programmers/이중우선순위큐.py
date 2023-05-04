import heapq

def solution(operations):
    max_queue = []
    min_queue = []
    heapq.heapify(max_queue)
    heapq.heapify(min_queue)
    
    for operation in operations:
        op, val = operation.split()
        if op == 'I':
            heapq.heappush(max_queue, -int(val))
            heapq.heappush(min_queue, int(val))
        elif op == 'D' and max_queue and min_queue:
            if val.startswith('-'):
                max_queue.remove(-heapq.heappop(min_queue))
            else:
                min_queue.remove(-heapq.heappop(max_queue))
        
    return [0, 0] if not max_queue else [-heapq.heappop(max_queue), heapq.heappop(min_queue)]
