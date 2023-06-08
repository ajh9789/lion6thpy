b = (10)
c = (10,)

print(type(b))
print(type(c))

d = (10, 20, 30, 40)
e = (10, 20, -50, 21.3, '멋쟁이사자')
f = 10, 20, -50, 21.3, '멋쟁이사자'

print(d, e, f, sep="\n")

print(f[1])
print(f[2])
print(f[3])
print(f[4])
print(f[:3])
print(f[1:4])
print(f[3:])
g = c + f
print(g)
print(f * 5)
print(-10 in f)
print("========")
h = (10, 20, -50, 20)
print(min(h), max(h))
print(h.count(20))
print(h.index(20))
sorted_a = sorted(h)
print(sorted_a)

a = (10, 20, -50)
x, y, z = a #튜플 해체
print(x, y, z)

a = 1
b = 2
print(a, b)

tmp = a
a = b
b = tmp

print(a, b)

a, b = b, a #스압

print(a, b)

list_h = list(h) #튜플을 리스트화

print(list_h, type(list_h))

tuple_h = tuple(list_h)

print(tuple_h, type(tuple_h))

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(nested_tuple)


# def generate_alphabet(start_letter,end_letter):
#     start = ord(start_letter)
#     end= ord(end_letter)
#     while start<=end:
#         yield chr(start)
#         start +=1
# # ord() ord() 함수는 한 문자의 아스키코드 값을 정수형으로 반환해준다.
# runner = generate_alphabet('A','F')
#
# for letter in runner:
#     print(letter)

# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
#
# runner = fibonacci(100)
#
# print(next(runner))
#
# print("======")
# print(runner)
# print(next(runner))
# print("======")
#
# for num in runner:
#     print(num)

# fruits = ["apple", "bananan", "cherry", "orange"]
# vegetables =["carrot","cucumber"]
#
# grocery =fruits+vegetables
# print(grocery)
#
# numbers=[10,5,7,1,9]
# numbers.sort()
# print(numbers)
#
# slice_numbers = numbers[1:4]
# print(slice_numbers)
#
# numbers_copy = numbers.copy() #그냥 쓰면 원본변수가 바뀐다
# print(numbers_copy)
#
# numbers_clone =numbers[:]
# print(numbers_clone)

# fruits = ["apple", "bananan", "cherry", "orange"]
#
# print(fruits)
#
# fruits.append("grape")
#
# print(fruits)
#
# fruits.insert(2, "kiwi")
#
# print(fruits)
#
# print(fruits.pop())
# print(fruits.pop(1))
#
# print(fruits)
# fruits.remove("apple")
# print(fruits)
# a = 50
#
#
# def show():
#     a = 10
#     print("show-A: ", a)
#
#
# show()
# print("A:", a)
#
#
# def show2():
#     global a
#     print("show2-A: ", a)
#     a = 20
#     print("show2-A2: ", a)
#
#
# show2()
# print("A: ", a)
#
#

# def show():
#     x = 10
#     print(x)
#
#
# show()
#
#
# def add(y):
#     x = 10
#     print(x)
#     print(x + y)
#
#
# add(20)
#
# a = 50
#
#
# def show():
#     x = 10
#     print(x)  # local
#     print(a)  # global
#
#
# show()
#
# print("Gobal Variable a:", a)
# i = 0
#
#
# def myfun():
#     a = i + 1
#     print("My Function a:", a)
#
#
# myfun()
# print("Gobal Variable a:", a)

# def add(x, y):
#     z = x + y
#     print("Addition: ", z)
#
#
# add(5, 2)
#
#
# def add(*num):
#     z = num[0] + num[1] + num[2]
#     print("Addtition *: ", z)
#
#
# add(5, 2, 4)
#
#
# def add(x, *num):
#     z = x + num[0] + num[1]
#     print("Addition x *: ", z)
#
#
# add(5, 2, 4)
#
# def add(**num): #**이면 가변키워드도 변경이가능하다
#     z = num['a']+ num['b']+num['c']
#     print("Addition: ",z)
#
# add(a=2,b=3,c=4,d=2)
# def pw(x,y):
#     z = x ** y
#     print(z)
#
# pw(2,5)
# # pw(5,2,3)
# def show(name='홍길동', age=99): # 디폴트값설정으로 인수없을때 오류방지
#     print(f"name: {name} Age: {age}")
#
# show(name="멋쟁이사자",age=27)
# # show(name="멋쟁이사자")


# print("인자가 없는 함수 정의")
# def disp():
#     name = "멋쟁이사자"
#     print("Welcom to", name)
#
# print("함수 실행")
# disp()
#
# def add():
#     x = 10
#     y = 20
#     c = x+y
#     print(c)
# add()
#
#
# def add(y):
#     x = 10.2334
#     print(x + y)
#     print(f"formatted Output {x+y:6.2f}") #뒷부분은 소수점 앞부분은 문자 전체 길이(. 과 소수점 포함)
# add(20)
#
# def add():
#     x = 10
#     y = 20
#     return x+y
#
# sum1 = add()
# print(sum1)
#
# def add(y):
#     x=10
#     return x+y
#
# sum3=add(20)
# print(sum3)
#
# def add(y):
#     x=10
#     c=x+y
#     d=y-x
#     return  c,d,50 #튜플로반환
#
# sum4,sub1,a=add(20)
# print(sum4)
# print(sub1)
# print(a)
#
# def disp():
#     def show():
#         return "Show Function"
#     result = show() + "Disp Function"
#     return result
# print(disp())
#
# def disp(sh):
#     print(type(sh))
#     print("Disp Funtion"+sh()) #sh가 함수라서 sh()
#
# def show():
#     return  " Show Funtion"
# disp(show) #괄호없이 사용하면 함수를 변수처럼 사용
#
#
# def disp():
#     def show():
#         return  " Show Funtion"
#     print("Disp Function")
#     return  show
# r_sh=disp()
# print(r_sh(),type(r_sh))
#
# def disp(sh):
#     print("Disp Funtion")
#     return sh
#
# def show():
#     return "Show Funtion"
# print(r_sh())
# print(show())


# s=" Hello, World  "
#
# print(s.upper())#모두 대문자
# print(s.lower())#모두 소문자
# print(s.swapcase())#대문자 소문자 바꾸기
# print(s.upper().title())#첫글자 대문자 나머지 소문자
# print(s.isupper())#모두 대문자 확인
# print(s.islower())#모두 소문자 확인
# print(s.istitle())#첫글자대문자 나머지 소문자
# print(s.isdigit())#숫자인지 확인
# print(s.isalpha())#알파벳인지 확인
# print(s.lstrip())#공백을 String의 왼쪽에서 제거
# print(s.rstrip())#공백을 String의 오른쪽에서 제거
# print(s.strip())#공백을 String의 왼쪽과 오른쪽에서 제거
# print(s.replace("world".title(),"there"))#문자 바꾸기
# print(s.split(","))#문자열을 리스트로 저장
# print("".join(s.split(",")))#리스트를 붙여서 반환
# print(s.startswith("Hello"))#문자열이 다음으로 시작하는지 boolean값으로 확인

# str1 = 'likeLion'
# str2 = "likeLion"
# str3 = '''
# 동해물과 백두산이 마르고 닳도록
# 하느님이 보우하사
# 우리나라 만세
# '''
# print(str1)
# print(str2)
# print(str3)
#
# str5='Hello "Like Lion" How are you'
# str6="Hello 'Like Lion' How are you"
#
# print(str5)
# print(str6)
#
# str7="Hello \nHow are you"
# str8="Hello \\nHow are you"
# str9=r"Hello \nHow are you"
#
# print(str7)
# print(str8)
# print(str9)


# from array import *
# stu_roll =array('i',[101,102,103,104,105,106,107])
# print("5까지 찍기")
# a=stu_roll[0:5]
# for i in a:
#     print(i)
# print("1:5까지")
# a=stu_roll[1:5]
# for i in a:
#     print(i)
# print("처음부터 전부출력")
# b=stu_roll[0:]
# for i in b:
#     print(i)
# print("처음부터 5번쨰까지")
# c=stu_roll[:5]
# for i in c:
#     print(i)
# print("마지막 요소 4개 출력")
# d=stu_roll[-4:]
# for i in d:
#     print(i)
# print("0붙 6번쨰까지 건너뛰어 출력")
# e=stu_roll[0:7:2]
# for i in e:
#     print(i)
# print("마지막 5개 요소 중 오른쪽 부터 2개의 요소를 출력")
# f=stu_roll[-5:-3]
# for i in f:
#     print(i)

#
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
#
# print("배열 pop() 함수 실습")
#
# element = stu_roll.pop(0)
# print('element:', element)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1


# n=len(stu_roll)
# i=0
# while i<n:
#     print(stu_roll[i])
#     i +=1
#
#
# print("Array After Insert")
# stu_roll.insert(1, 106)
# stu_roll.insert(3, 107)
# n= len(stu_roll)
# i=0
# while i<n:
#     print(stu_roll[i])
#     i+=1
#
# print("배열 요소 삭제")
#
# stu_roll.remove(107)
# n=len(stu_roll)
# i=0
# while i<n:
#     print(stu_roll[i])
#     i +=1

# # 틀만 만들어두고 TODO를 사용하면 협업할때 좋음
# a = 5
# if a < 6:
#     pass #
# else:
#     print("6 보다 큼")


# # for in
# st = "멋쟁이 사자"
# for ch in st:
#     print(ch)
# else:
#     print("Else")
#
# print("코드 종료")


# for i in range(5):
#     print(i)
#
# for i in range(2,7):
#     print(i)
#
# for i in range(1, 10, 2):
#     print(i)
#
# for i in range(-1, -10, -2):
#     print(i)
#
# a = range(5)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
#
# print("Reverse Rage with Start, stop, step")
# r = range(5, 0, -1)
# print(r[0])
# print(r[1])
# print(r[2])
# print(r[3])
# print(r[4])


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
