from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    # 코스 요리를 구성하는 갯수 각각에 대해 구함
    for n in course:
        combination_list = []
        for order in orders:
            combination_list.extend(list(combinations(sorted(order), n)))

        # 가장 많이 주문한 단품메뉴들 구하기 (단, 최소 2명이상)
        count_combination = Counter(combination_list).most_common();
        course_menu = [''.join(k) for k, v in count_combination if v > 1 and v == count_combination[0][1]]
        answer.extend(list(course_menu))

    answer.sort()
    return answer
