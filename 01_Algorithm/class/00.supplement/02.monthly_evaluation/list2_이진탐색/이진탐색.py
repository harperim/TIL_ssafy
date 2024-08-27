import sys
sys.stdin = open('이진탐색_input.txt')

T = int(input())

for tc in range(1, T+1):
    total, a, b = map(int, input().split())

    # a, b의 시작점, 끝점, 도전 횟수 변수 설정
    start_a = start_b = 1
    end_a = end_b = total

    a_cnt = b_cnt = 0  # a, b의 도전 횟수

    # A의 도전 횟수 구하기
    while start_a <= end_a:
        mid_a = int((start_a + end_a)//2)
        a_cnt += 1

        if a > mid_a:
            start_a = mid_a
        elif a < mid_a:
            end_a = mid_a
        else:
            break

    # B의 도전 횟수 구하기
    while start_b <= end_b:
        mid_b = int((start_b + end_b)//2)
        b_cnt += 1

        if b > mid_b:
            start_b = mid_b
        elif b < mid_b:
            end_b = mid_b
        else:
            break

    # 이긴 사람 찾기
    if a_cnt < b_cnt:
        answer = 'A'
    elif a_cnt > b_cnt:
        answer = 'B'
    else:
        answer = 0

    print(f'#{tc} {answer}')
