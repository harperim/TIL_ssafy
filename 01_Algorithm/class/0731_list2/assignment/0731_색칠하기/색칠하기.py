import sys
sys.stdin = open('색칠하기_input.txt')

T = int(input())

# 빨강 +1, 파랑 +2, 해서 겹치는 부분은 +3이 될 것
# 3 되는 값 찾기!

for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]
    n = int(input())

    # 색칠하기
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color

    # 확인하기
    # for lst in arr:
    #     print(*lst)

    # 겹쳐진 칸수 카운팅
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1
    print(f'#{tc} {cnt}')
