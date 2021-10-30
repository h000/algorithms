import re

def solution(new_id):
    # 1
    answer = new_id.lower()
    # 2
    answer = ''.join(re.findall(r"[._\-a-z0-9]*", answer))
    # 3
    answer = re.sub(r"\.[\.]+", ".", answer)
    # 4
    answer = re.sub(r"^\.", "", answer)
    answer = re.sub("\.$", "", answer)
    # 5
    if not answer:
        answer = "a"
    # 6
    if len(answer) > 15:
        if answer[14] == '.':
            answer = answer[:14]
        else:
            answer = answer[:15]
    while (len(answer) < 3):
        answer += answer[-1]

    return answer
