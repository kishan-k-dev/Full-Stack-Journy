#x = 10
#print(id(x))

# a = [1, 2, 3]
# b = a

# b.append(4)

# print(a)

# students = ["Pavan", "Rahul", "Manoj"]

# marks = {
#     "Math": 95,
#     "Science": 90
# }

# 
# arr = [10,20,30]

# arr[0] = 2200

# print(arr)
# arr = [10,20,30,40,50]

# for p in arr:
#     print(p)

# arr = [10,20,30,40,50]

# target = 10

# for i in range(len(arr)):
#     if arr[i] == target:
#         print("Found at index", i)

# fruits = ["Apple", "Banana", "Mango"]

# for _ in range(3):
#   for fruit in fruits:
#     print(fruit)

# fruits = ["Apple", "Banana", "Mango"]

# for i in range(2):
#     print(f"--- Iteration {i+1} ---")
#     for fruit in fruits:
#         print(fruit)


# class Student:

#     name = "Pavan"
#     age = 22

# student=Student()
# for i in range(len(student.name)):
#     print(i)
# print(student.name)


# Student=[kishan,pavan,rhaa,khaa,ghh,shaa,jeee,ram,room,]


class car:
    EVcar=None
    print("this is EV cars=",EVcar)
    def __init__(self,name,brand,model):
        self.K=name
        self.A=brand
        self.P=model
        self.price=0

kishan=car("BMW","AUDI","hello")
print(kishan.K)
print(kishan.A)
print(kishan.P)
print(kishan.price)

instructor_1=car("Swift","MS","world")
print(instructor_1.A,instructor_1.K)