"""
5
45 15 10 56 23
96 98 99 40 69
96 84 49 46 34
16 64 81 4 11
10 66 85 55 14
"""

# 연습문제 1-2
# 25개의 각 요소에 대해 그 요소와 이웃한 요소와의 차의 절대값 구하고, 합으로 출력하기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

# 우, 하, 좌, 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

total = 0
for i in range(N):
    for j in range(N):  # NxN 배열의 모든 원소에 대해 => 라는 문장이 있으면 for문 일단 2개 쓰기
        sum_val = 0  # 원소와 인접원소 차 절댓값의 합
        # i, j 원소의 4 방향
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                sum_val += abs(arr[i][j] - arr[ni][nj])    # 실존하는 인접원소 ni, nj
        total += sum_val
print(total)  # 2430



