import sys
sys.stdin = open('스도쿠검증_input.txt')


def solve(arr):
    # 행 우선
    for i in range(9):
        cnts = [0] * 10
        for j in range(9):
            cnts[arr[i][j]] += 1
            # 현재 카운트한 인덱스의 값이 1 이상이면 return
            if cnts[arr[i][j]] > 1:
                return 0
    # 열 우선
    for i in range(9):
        cnts = [0] * 10
        for j in range(9):
            cnts[arr[j][i]] += 1
            # 현재 카운트한 인덱스의 값이 1 이상이면 return
            if cnts[arr[i][j]] > 1:
                return 0

    # 3 x 3
    for i in range(0, 9, 3):  # step 3 : 0 ~ 9까지 간격이 3
        for j in range(0, 9, 3):
            cnts = [0] * 10  # cnts 초기화
            for x in range(3):
                for y in range(3):
                    cnts[arr[i+x][j+y]] += 1
                    if cnts[arr[i+x][j+y]] > 1:
                        return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = solve(arr)
    print(f'#{tc} {ans}')

# 2. 내장 함수를 이용해서 만들기
def solve(arr):
    # 행우선
    for lst in arr:
        if len(set(lst)) != 9:  # set으로 중복제거 2후 len
            return 0

    # 열우선
    arr_t = list(zip(*arr))  # 전치행렬을 이용
    for lst in arr_t:
        if len(set(lst)) != 9:  # set으로 중복제거 2후 len
            return 0

    # 3 X 3
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            lst = arr[i][j:j + 3] + arr[i + 1][j:j + 3] + arr[i + 2][j:j + 3]
            if len(set(lst)) != 9:
                return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]  # 9 X 9
    ans = solve(arr)
    print(f'#{tc} {ans}')

