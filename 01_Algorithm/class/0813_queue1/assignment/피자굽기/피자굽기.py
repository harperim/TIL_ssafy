import sys
sys.stdin = open('피자굽기_input.txt')

# 손으로 그려보고 구현하기


def solve():
    Q = []
    # 화덕에 N만큼 넣기
    for i in range(1, N + 1):
        Q.append(i)  # 인덱스를 저장

    idx = N + 1  # 다음에 넣을 피자의 인덱스
    while len(Q) > 1:
        # 피자를 꺼내서 치즈 확인
        pizza = Q.pop(0)
        cheese[pizza] //= 2
        # 치즈가 남아 있으면
        if cheese[pizza] != 0:
            Q.append(pizza)  # 다시 넣기
        # 치즈가 다 녹았으면
        elif idx <= M:  # 남은 피자가 있으면
            Q.append(idx)
            idx += 1
    return Q[0]


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕크기, 피자수
    cheese = [0] + list(map(int, input().split()))  # 0번 인덱스 사용 안 하기
    print(f'#{tc} {solve()}')
