class Engine:
    def start(self):
        return "Engine started"
    def stop(self):
        return "Engine stopped"

class Wheels:
    def rotate(self):
        return "Whells are rotating"
#다중 상속
class Car(Engine, Wheels):
    pass
#인스턴스 생성
my_car =Car()
# 부모 클래스의 메소드 사용
print(my_car.start())
print(my_car.rotate())

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