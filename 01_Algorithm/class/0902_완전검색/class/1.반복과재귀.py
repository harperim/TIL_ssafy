# 11 12 13 21 ...
path = []
N = 3

def run(lev):
    if lev == N:
        print(path)
        return

    for i in range(1, 4):
        path.append(i)
        run(lev + 1)
        path.pop()

N = int(input())
run(0)

# --------------------------------------------------------------------

def func(x):
    x[0] += 1


x = [10]
func(x)
print(x)

# --------------------------------------------------------------------

def BBQ(x):
    x += 10
    print(x)


def KFC(x):
    print(x)
    x += 3
    BBQ(x+2)
    print(x)


x = 3
KFC(x+1)
print(x)

# --------------------------------------------------------------------

# def func(x):
#     x[0] += 1
#
# x = [10]
# func(x)
# print(x)

# -------------------------------------------------------------------

def KFC(x):
    KFC(x+1)

KFC(0)

# --------------------------------------------------------------------

def func(x):
    # 1. 기저 조건(종료 조건)
    if x == 6:
        return

    # 2. 다음 재귀 호출 전
    print(x, end=' ')
    # 3. 재귀 호출 (현재 값에 무슨 수식을 적용해서 넘겨줄까?)
    func(x+1)  # 다음 재귀 호출에서는 현재보다 x 값이 1이 커야한다.
    # 4. 호출하고 돌아왔을 때
    print(x, end=' ')


start = 0
func(start)

# --------------------------------------------------------------------

def KFC(x):
    if x == 3:
        return
    for i in range(2):
        KFC(x+1)


KFC(0)

# --------------------------------------------------------------------

# 중복순열 [1, 1, 1] ~ [6, 6, 6]
# path = []  # 경로를 기록할 리스트
#
# def recur(x):
#     if x == 3:
#         print(path)
#         return
#     for i in range(1, 7):
#         path.append(i)
#         recur(x + 1)
#         path.pop()
# recur(0)

# 중복순열 [1, 1, 1, 1, 1] ~ [4, 4, 4, 4, 4]
# path = []  # 경로를 기록할 리스트
#
# def recur(x):
#     if x == 5:
#         print(path)
#         return
#     for i in range(1, 5):
#         path.append(i)
#         recur(x + 1)
#         path.pop()
# recur(0)


# 1을 뽑음 -> 앞으로는 1을 뽑지 않겠다. 같은 숫자를 뽑지 않는 경우
path = []  # 경로를 기록할 리스트
used = [0] * 8  # 1~7 숫자의 사용 여부를 기록할 리스트

# 0부터 시작, 3개를 뽑은 경우 종료
def recur(level):
    if level == 3:
        print(*path)
        return
# 2. 후보군을 반복하면서
    for i in range(1, 6):
        # i가 이미 뽑혔다면, continue 해라
        # 아래 코드의 단점 : "in" = O(len(path))
        # 시간 초과 위험도가 높다.
        # if i in path:
        #     continue

        # 조건이 많아지면 코드가 난잡해짐 => continue로 가독성 해결
        # i가 이미 뽑혔다면, continue 해라
        # == 방문했다면 실행하지 마라
        # i가 이미 뽑혔다면, continue 해라.
        if used[i]:
            continue

        # 2.1 재귀호출 전 - 경로 기록 + 사용 기록
        used[i] = 1
        path.append(i)
        # 2.2 다음 재귀 호출 (파라미터 전달)
        recur(level + 1)
        # 2.3 돌아왔을 때 - 사용했던 경로 삭제
        path.pop()
        used[i] = 0
recur(0)  # 호출 : 시작점을 같이 전달해주는 경우가 많다.

