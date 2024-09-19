# 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
negative = -3
print(abs(negative))

# 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
empty_list = []
print(bool(empty_list))

# 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
my_list = [1, 2, 3, 4, 5]
print(sum(my_list))

sum_v = 0
for item in my_list:
    sum_v += item
print(sum_v)


# 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
unsorted_list = ['하', '교', '캅', '의', '지', '가']

print(sorted(unsorted_list))  # 비파괴적 함수
print(unsorted_list)

unsorted_list.sort()       # 파괴적 메소드
print(unsorted_list)

