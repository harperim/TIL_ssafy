# 1. 숫자가 입력 되면 절대치를 구하시오.
num = -1
if num < 0:
    num = num * -1
print(num)  # 절대값


# 2. 정수가 입력되면 짝수나 홀수를 출력하시오.
num = 11
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')
# 출력: 짝수

# 3. 성적을 입력하면 수, 우, 미, 양, 가를 출력하시오.
score = 90
if score >= 90:
    print('수')
elif score >= 80:
    print('우')
elif score >= 70:
    print('미')
elif score >= 60:
    print('양')
else:
    print('가')
# 출력 : 수