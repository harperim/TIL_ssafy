import sys
sys.stdin = open('특별한정렬_input.txt')

T = int(input())

# 짝수 idx : max 값 거꾸로
# 홀수 idx : min 값 순서대로

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    # 비교할 숫자 중 앞의 숫자
    for i in range(n-1):
        # 짝수번째 idx에는 최대값이 내림차순으로 배치
        if i % 2 == 0:
            max_idx = i
            # 비교할 숫자 중 뒤의 숫자
            for j in range(i+1, n):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            # 구간의 최대값을 현재 위치로 이동
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        # 홀수번째 idx에는 최대값이 오름차순으로 배치
        else:
            min_idx = i
            # 비교할 숫자 중 뒤의 숫자
            for j in range(i + 1, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            # 구간의 최소값을 현재 위치로 이동
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    answer = ' '.join(map(str, arr[:10]))
    print(f'#{tc} {answer}')



