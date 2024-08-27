# 재귀함수 : 수학적 귀납법 f(1) ~ f(n-1) -> f(n)
# (1) 기본파트
# (2) 유도파트

def fact(n):        # 5! = 5 * 4!
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


print(fact(4))
