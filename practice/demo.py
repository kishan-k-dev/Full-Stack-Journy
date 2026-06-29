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

fruits = ["Apple", "Banana", "Mango"]

for i in range(2):
    print(f"--- Iteration {i+1} ---")
    for fruit in fruits:
        print(fruit)
