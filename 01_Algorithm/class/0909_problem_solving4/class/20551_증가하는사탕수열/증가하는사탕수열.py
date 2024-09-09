import sys
sys.stdin = open('증가하는사탕수열_input.txt')

# 사탕을 먹어치워서 조건을 만족시킬 수 없다면 -1을 출력한다.

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())  # 굳이 리스트를 쓸 필요가 없다.

    if B < 2 or C < 3:  # A는 1보다 크다는 조건 있어서 A < 1 생략 가능 / A < B < C 구조를 만들 수 없는 케이스를 처리
        print(f'#{tc} -1')
        continue

    eat = 0  # 먹은 사탕 개수
    # 설계: B가 C 이상일 때, B = C - 1 이라면 최소 개수 (뒤에서부터 B 먼저 처리, A 먼저 처리하면 X)
    if B >= C:
        eat += B - (C - 1)  # 차이만큼 먹음
        B = C - 1  # 먹고 초기화
    #      A가 B 이상일 때, A = B - 1 이라면 최소 개수
    if A >= B:
        eat += A - (B - 1)
        A = B - 1

    print(f'#{tc} {eat}')
