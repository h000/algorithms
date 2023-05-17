def solution(user_id, banned_id):
    arr = []
    for b in banned_id:
        lst = []
        for u in user_id:
            if len(b) != len(u):
                continue
            for i in range(len(b)):
                if b[i] == u[i] or b[i] == '*':
                    continue
                break
            else:
                lst.append(u)
        arr.append(lst)
    case = set()
    getCase(0, len(banned_id), arr, case, set())
    return len(list(case))

def getCase(cnt, n, arr, case, tmp):
    if cnt == n:
        tmplst = list(tmp)
        tmplst.sort()
        case.add(str(tmplst))
        return
    
    for a in arr[cnt]:
        if a in tmp:
            continue
        tmp.add(a)
        getCase(cnt + 1, n, arr, case, tmp)
        tmp.remove(a)
