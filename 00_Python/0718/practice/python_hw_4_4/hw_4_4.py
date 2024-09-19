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

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]


# missing_book = []
# for rental in rental_book:
#     if rental not in list_of_book:   # 내부적으로 for
#         missing_book.append(rental)

missing_book = [rental for rental in rental_book if rental not in list_of_book]

if missing_book: # 리스트가 비어있지 않으면 len(missing_book) > 0
    for book in missing_book:
        print(f'{book}을/를 보충해야 합니다.')
else:
    print('모든 도서가 대여 가능함')