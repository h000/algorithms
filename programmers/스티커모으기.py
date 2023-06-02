def solution(sticker):
    answer = 0
    # 첫번째것을 체크한 경우
    dp1 = [sticker[0], max(sticker[:2])]
    # 첫번째것을 체크하지 않은 경우
    dp2 = [0, sticker[1] if len(sticker) > 1 else 0]
    
    for i in range(2, len(sticker) - 1):
        tmp = dp1[i - 2] + sticker[i]
        dp1.append(tmp if tmp > dp1[i - 1] else dp1[i - 1])
        tmp = dp2[i - 2] + sticker[i]
        dp2.append(tmp if tmp > dp2[i - 1] else dp2[i - 1])

    return dp1[-1] if dp1[-1] > dp2[-2] + sticker[-1] else dp2[-2] + sticker[-1]
