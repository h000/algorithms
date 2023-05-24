def solution(n, times):
    start = 0
    end = n * max(times)
    
    while start < end - 1:
        mid = (start + end) // 2
        mid_done = 0
        for time in times:
            mid_done += mid // time
        if mid_done < n:
            start = mid
        else:
            end = mid
    
    return end
