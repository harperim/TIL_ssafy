# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  집합의 부분집합 중에 원소의 합이 10이 되는 경우

def powerset(n, k, cursum):
    ###########################
    # 가지치기 넣기
    if cursum > 10: return
    ###########################


    if n == k:
        if cursum == 10:
            for i in range(n):
                if bit[i]:
                    print(arr[i], end=' ')
            print()
    else:
        bit[k] = 1
        powerset(n, k+1, cursum + arr[k])   # cursum += arr[k] 이렇게 하면 절대 X
        bit[k] = 0
        powerset(n, k+1, cursum)


# cursum += arr[k] 이렇게 하면 절대 X
# = 이 없기 때문에 되돌아왔을 때 값을 사라지기 때문에 사용하지 X
# 정 쓰고 싶다면 되돌아왔을 때 따로 빼줘야함

N = 10
arr = [i for i in range(1, N+1)]
bit = [0] * N
powerset(N, 0, 0)

