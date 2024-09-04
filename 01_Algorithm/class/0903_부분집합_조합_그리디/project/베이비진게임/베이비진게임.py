import sys
sys.stdin = open('베이비진게임_input.txt')

def baby_test(cnts):
    for i in range(10):  # triplet
        if cnts[i] >= 3:
            return True
    for i in range(8):  # run
        if cnts[i] >= 1 and cnts[i + 1] >= 1 and cnts[i + 2] >= 1:
            return True


def game(arr):
    cnts1 = [0] * 10
    cnts2 = [0] * 10
    for i in range(12):
        n = arr[i]

        if i % 2 == 0:  # player1
            cnts1[n] += 1
        else:  # player2
            cnts2[n] += 1

        # 3장 이후부터
        if i > 4:
            if i % 2 == 0:
                if baby_test(cnts1):
                    return 1
            else:
                if baby_test(cnts2):
                    return 2
    return 0  # 승자가 없는 경우


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    print(f'#{tc} {game(arr)}')
