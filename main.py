for i in range(5):
    print(i)

for i in range(2,7):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(-1, -10, -2):
    print(i)

a = range(5)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

print("Reverse Rage with Start, stop, step")
r = range(5, 0, -1)
print(r[0])
print(r[1])
print(r[2])
print(r[3])
print(r[4])



# # 예제 1 : 간단한 if 문
# x=5
# if x > 3:
#     print("x는 3보다 큽니다.")
#
# age=18
# if age>= 18:
#     print("성인입니다.")
# else:
#     print("미성년자입니다")
#
# # 중첩된 if else 중첩된 if문은 가독성을 떨어뜨리니 되도록 사용하지말기
# score = 85
# if score >= 90:
#     print("A 등급")
# else :
#     if score >= 80:
#         print("B 등급")
#     else:
#         if score >= 70:
#             print("C 등급")
#         else:
#             print("D 학점")
#
# # 예제4 : if else
# marks = 75
# if marks >= 90:
#     print("A 등급")
# elif marks >=80:
#     print("B 등급")
# elif marks >=70:
#     print("C 등급")
# else:
#     print("D등급")
#
# a = int(input("Enter Number Greater then 2:"))
# if a > 2:
#     print("Corret!! You have Entered: ",a)
# else:
#     print("Wrong!! You have Entered", a)
#
# day = input("요일을 입력하세요: ")
# if day == "Mon":
#     print("오늘은 월요일")
# elif day == "Tue":
#     print("오늘은 화요일")
# elif day == "Wed":
#     print("오늘은 수요일")
# else :
#     print("오늘은 휴일")
#
# # 다른 언어와 다르게 else를 넣으면 마지막에 else문을 실행한다.
# i=0
# while(i<10):
#     i+=1
#     print("i: ",i)
# else :
#     print("else")
#
# # 무한 루프 while문 break이 있으면 else가 실행이 안된다.
# while True:
#     a = int(input("Enter Menu Number:"))
#     if a=='0':
#         break
#     print("i: ",i)
# else:
#     print("else")
#
# #첫번째 while 루프 디버깅할떄 while
# a = 1
# while a<= 10:
#     print(a)
#     a +=1
# else:
#     print("While 조건이 거짓이므로 Else 부분 실행됨")
# print("코드 종료")
#
# # 무한 루프 컨트롤+C 누르면 인터럽트 시스템콜로 종료된다.
# while True:
#     print("멋쟁이 사자")
# print("코드 종료")
#
# i = 0
# while True:
#     i += 1
#     print(i)
#     if i == 5:
#         break
# print("코드 종료")

# # 출력함수
# data = [10, 20, -50, 21.3, 'LikeLion']
# print(data)
#
# print("Like", "Share", "Subscribe", sep='')
# print("Like", "Share", "Subscribe", sep='***')
#
# print("Like", "Share", "Subscribe", sep='***', end='\t')
# print("Like", "Share", "Subscribe", sep='***', end='\n')
#
# m = 27
# print("value: ", m)
#
# name = "주현"
# age = 42
# print("My name is", name, "and My age is", age, sep=' ')
#
# print("Welcome", end='\t')
# print("to", end='\t')
# print("LikeLion")
#
#
# #줄바꿈 없이 입력
# print("1")
# print("2", end='')
# print("3")
# print("4")
#
#
# #타입 변환
# n5 = ("Kim", "Bae", "Park", "Lee")
# vn5 = list(n5)
#
# print(n5, type(n5))
# print(vn5, type(vn5))


# #튜플 변환
# n5 = "멋쟁이 사자"
# vn5 = tuple(n5)
#
# print(vn5, type(vn5))


# # 명시적 타입 변환2
# q = 20
# u = '10'
# print(type(u))
# r = q + int(u)
# print(r, type(r))
# r = str(q) + u
# print(r, type(r))
#
# # 명시적 타입 변환
# a = 5
# b = 2
# value = a / b
# print(value, type(value))
# int_value = int(value)
# print(int_value, type(int_value))


# # 암시적 타입 변환
# a = 5
# b = 2
# print(b, type(b))
# value = a / b
# print(value)
# print(type(value))
#
# x = 10
# y = 5.5
# total = x + y
# print(total)
# print(type(total))
#
# j = "Hello"
# k = "like lion"
# p = j + k
# print(p)
# print(type(p))
#
# q = 20
# u = '10'
# r = q + u # 오류
# print(r)

# # is 연산자
#
# a = 10
# b = 10
# print(a is not b)
#
# a = 10
# b = '10'
# print(a is not b)



# # 멤버 in 연산자
#
# st1 = "Welcome to 멋쟁이 사자"
# print("to" not in st1)
#
# st2 = "Welcome top 멋쟁이 사자"
# print("to" not in st2)
#
# st3 = "Welcome to 멋쟁이 사자"
# print("subs" not in st3)



# # 비트 연산자 실습
#
# a = 10
# b = 15
#
# print('a: ', bin(a))
# print('b: ', bin(b))
# print('a & b: ', a & b)
# print('a << 2: ', a << 2)
# print('a >> 2: ', a >> 2)


# # 할당 연산자 =
# a = 10
# b = 20
# m = 15
#
# y = a + b
# print(y)
#
# m += 10 # m = m + 10
# print(m)
#
# m **= 2
# print(m)
#
# m //= 10
# print(m)

# # 논리 연산자
# a = 5
# b = 2
# c = 3
# d = 200
#
# print('AND 연산자')
# print('a > b and a < c:', a > b and a < c)
#
# print("OR 연산자")
# print('a > b or a < c:', a > b or a < c)
#
# print('NOT 연산자')
# print('not(a < b): ', not(a < b))

# print('Hello, World!')
#
# # 비교 연산자
# a = 5
# b = 2
# print('a:', a, 'b:', b)
#
# print('a < b: ', a < b)
#
# print('a <= b: ', a <= b)
#
# print('a == b: ', a == b)
#
# print('a != b: ', a != b)


# # 덧셈
# a = 4
# b = 2
# total = a + b
# print('total = a + b:', total)
#
# #뺄셈
# a = 4
# b = 2
# total = a - b
# print('total = a - b: ', total)
#
# #곱셈
# total = a * b
# print('total = a * b: ', total)
#
# #나눗셈
# print('a / b: ', a / b)
#
# #나머지
# a = 5
# b = 2
# print('a % b: ', a % b)
#
# #거듭제곱
# print('a ** b: ', a ** b)
#
# # 몫 (양수)
# print('a // b : ', a // b)
#
# # 몫 (음수)
# a = -5
# print('a // b(음수) :', a // b)



# # 변수 선언
# a=10
# b=3.14
# c="hello, world"
# d=[1,2,3]
# e=(4,5,6)
# f={7,8,9}
# g={"apple":1,"bananan":2,"orange":3}
#
# # 데이터 타입 출력
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))