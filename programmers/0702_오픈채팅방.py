def solution(record):
    answer = []
    ans = []
    dictionary = {}
    
    for r in record:
        s = r.split()
        if s[0] == 'Leave':
            answer.append(s[1] + "님이 나갔습니다.")
        else:
            dictionary[s[1]] = s[2]
            if s[0] == 'Enter':
                answer.append(s[1] + "님이 들어왔습니다.")
    
    for a in answer:
        uid = a.split()[0][:-2]
        ans.append(a.replace(uid, dictionary[uid]))

    return ans