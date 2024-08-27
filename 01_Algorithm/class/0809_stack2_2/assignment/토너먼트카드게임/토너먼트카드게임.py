# 재귀인데 return하는 경우
import sys
sys.stdin = open('토너먼트카드게임_input.txt')


def win(r1, r2):
    if arr[r1] == arr[r2]:
        return r1
    else:
        if arr[r1] == 1 and arr[r2] == 2:  # 가위 vs 바위
            return r2
        elif arr[r1] == 1 and arr[r2] == 3:  # 가위 vs 보
            return r1
        elif arr[r1] == 2 and arr[r2] == 1:  # 바위 vs 가위
            return r1
        elif arr[r1] == 2 and arr[r2] == 3:  # 바위 vs 보
            return r2
        elif arr[r1] == 3 and arr[r2] == 1:  # 보 vs 가위
            return r2
        elif arr[r1] == 3 and arr[r2] == 2:  # 보 vs 바위
            return r1


def game(l, r):  # l과 r의 해당범위의 인덱스
    if l == r:  # 카드가 하나 남았을 때
        return l
    else:
        r1 = game(l, (l + r) // 2)
        r2 = game((l + r) // 2 + 1, r)
        return win(r1, r2)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {game(0, N - 1) + 1}')


