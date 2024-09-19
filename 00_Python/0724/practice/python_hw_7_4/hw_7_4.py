# 아래 클래스를 수정하시오.
class Person:
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name # 인스턴스 변수
        self.age = age
        Person.number_of_people += 1

    def introduce(self): # 인스턴스 메서드
        print(f'제 이름은 {self.name}이고, 저는 {self.age} 살 입니다.')

person1 = Person("Alice", 25)
p2 = Person('kim', 20)
person1.introduce()
p2.introduce()
print(Person.number_of_people)
