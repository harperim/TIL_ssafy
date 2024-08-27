import sys
sys.stdin = open('회문2_input.txt')

T = 10

# 거꾸로 카운팅 시작하기
cnt = 0
for tc in range(1, T+1):
    trash = input()  # 버리는 변수
    N = 100
    arr = [list(map(str, input())) for _ in range(N)]
    # print(arr)

    max_len = 100
