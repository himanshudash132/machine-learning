name = input("Enter your name:")
age = int(input("Enter your age:"))
weight = float(input("Enter your weight (in kg):"))
is_student = input("Are you a student? (yes/no):").lower()

if is_student == "yes":
    is_student = True
else:
    is_student = False    


print("Name:", name)
print("Age:", age)
print("weight:", weight)
print("Is a student:", is_student)