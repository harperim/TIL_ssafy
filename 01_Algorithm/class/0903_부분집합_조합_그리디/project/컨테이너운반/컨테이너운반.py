import sys
sys.stdin = open('컨테이너운반_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 컨테이너, 트럭 용량
    Wi = list(map(int, input().split()))  # 컨테이너
    Ti = list(map(int, input().split()))  # 트럭

    Wi.sort(reverse=True)
    Ti.sort(reverse=True)

    # 투포인터 이용
    w = t = 0  # w: 컨데이너, t: 트럭
    ans = 0
    while w < N and t < M:
        # 트럭에 컨테이너를 실을 수 있으면
        if Wi[w] <= Ti[t]:
            ans += Wi[w]
            w, t = w + 1, t + 1
        else:  # 트럭 용량보다 컨테이너가 더 무거우면
            w += 1  # 다음 컨테이너로 이동
    print(f'#{tc} {ans}')

