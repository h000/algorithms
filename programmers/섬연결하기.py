parent = [i for i in range(100)]

def solution(n, costs):

    costs.sort(key=lambda x : x[2])
    answer = 0
    for x, y, c in costs:
        if find(x) == find(y):
            continue
        union(x, y)
        answer += c
    return answer

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]
