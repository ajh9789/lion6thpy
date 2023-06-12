class CustomException(Exception):
    def __init__(self, mesage):
        self.message = mesage

try:
    raise CustomException("This is a custom exception")
except CustomException as e:
    print(f"Error:{e.message}")


# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Error : Division by zero")
#
# print("Program continues.")


# from python.MyApp.Handlers.text_handler import handle_text
#
# #패키지 추가 빨간 밑줄 alt+엔터로 편하게 할수있다
# input_text = "python package pratice"
# handle_text(input_text)

# class Engine:
#     def start(self):
#         return "Engine started"
#     def stop(self):
#         return "Engine stopped"
#
# class Wheels:
#     def rotate(self):
#         return "Whells are rotating"
#
# #다중 상속
# class Car(Engine, Wheels):
#     pass
# #인스턴스 생성
# my_car =Car()
# # 부모 클래스의 메소드 사용
# print(my_car.start())
# print(my_car.rotate())

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make =make
#         self.model=model
#         self.year=year
#
#     def start_engine(self):
#         return "The engine is running!"
#
# class Car(Vehicle):
#     def start_engine(self):
#         return  super().start_engine() + " It's a car engine."
#
# my_car = Car("Toyotam", "Corolla", 2020)
#
# print(my_car.start_engine())

# class Car:
#     # 클래스 속성
#     wheels = 4
#
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#     # 매소드
#     def drive(self):
#         return "The car is moving!"
#
#     def stop(self):
#         return f"The car has stopped."
#
#
# my_car = Car("Kia", "Morning", "Blue")
#
# # 속성 사용
# print(my_car.make)
#
# # 메소드 호출
# print(my_car.drive())
# print(my_car.stop())