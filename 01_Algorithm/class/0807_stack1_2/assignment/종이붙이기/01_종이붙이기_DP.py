import sys
sys.stdin = open('종이붙이기_input.txt')

# 20*10i 채우는 리스트
m = [1, 1]      # 빈 공간을 채우는 경우 = 1 (아무것도 없는 경우 1가지로 카운트)
for i in range(2, 31):
    m.append(m[i-1] + 2*m[i-2])

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 10의 배수
    print(f'#{tc} {m[N//10]}')
