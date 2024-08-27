# 삼성시의 버스 노선

import sys
sys.stdin = open("6485_input.txt")

# pypy인 경우 파일 이름 한글이면 안됨
# 각 정류장에 몇 개의 버스 노선이 다니느지 구하는 프로그램 작성
# 1개짜리 tc를 복붙해서 2개의 경우로 만들고, 1개의 tc가 끝나면 엔터처리 되는지 확인하기 (안되는 경우 종종 있음)
T = int(input())

for tc in range(1, T+1):
    N = int(input())        # 노선 수
    counts = [0] * 5001  # 5000번 정류장까지

    # N개의 노선 정보를 모두 읽어놓고 처리 or 읽을 때마다 처리
    for _ in range(N):  # 읽을 때마다 처리
        A, B = map(int, input().split())  # Ai -> Bi 버스 노선의 시점 Ai와 종점 Bi, Ai <= Bi
        for i in range(A, B+1):  # 1 <= Ai <= Bi <= 5,000
            counts[i] += 1

    P = int(input())  # 노선 수를 출력할 P개의 버스 정류장

    # 모두 읽어놓고 처리
    busstop = [int(input()) for _ in range(P)]
    print(f'#{tc}', end=' ')
    for j in busstop:  # 노선 수를 출력할 정류장 번호
        print(counts[j], end=' ')  # 끝에 붙는 빈칸은 무시해도 괜찮음
    print()

