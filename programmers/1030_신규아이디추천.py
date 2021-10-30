def solution(new_id):
    new = ""
    # 1,2
    for c in new_id:
        if c.isalnum() or c in ['-', '_', '.']:
            if c.isupper():
                c = c.lower()
            new += c
    # 3 4
    answer = ""
    for i, c in enumerate(new):
        if c == '.' and (i == 0 or i == len(new) - 1 or new[i - 1] == '.'):
            continue
        answer += c
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    # 5 6
    if not answer:
        answer = "a"
    elif len(answer) > 15:
        if answer[14] == '.':
            answer = answer[:14]
        else:
            answer = answer[:15]
			# 7
    while (len(answer) < 3):
        answer += answer[-1]

    return answer
