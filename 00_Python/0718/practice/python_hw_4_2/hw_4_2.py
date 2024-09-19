list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    # '난중일기',
    '홍길동전',
    '만복자서포기',
]

# 1. 이중 for
for rental in rental_list:   # 난중일기
    flag = False # 대여 불가능한 경우
    for book in list_of_book:
        if rental == book:
            flag = True # 대여 가능한 경우
            break
    # 리스트에 대여 책이 없는 경우
    if not flag:
        print(f'{rental}은/는 보유하고 있지 않습니다.')
        break
        
# 전체 목록에 대여 가능한 책들이 모두 존재
if flag:
    print('모든 도서가 대여 가능한 상태입니다.')


#  2. for + in
for rental in rental_list:
    flag = True             # 대여가능
    if rental not in list_of_book:
        print(f'{rental}은/는 보유하고 있지 않습니다.')
        flag = False
        break
if flag:
    print('모든 도서가 대여 가능한 상태입니다.')


# 3. for ~ else
for rental in rental_list:
    if rental not in list_of_book:
        print(f'{rental}은/는 보유하고 있지 않습니다.')
        break
else: # break로 빠져나가지 않고 for문을 다 돌았을 때
    print('모든 도서가 대여 가능한 상태입니다.')
