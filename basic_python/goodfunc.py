def get_name_and_age():
    name = "john"
    age = 30
    return name,age

person = get_name_and_age()


print(person)
print(person[0])
print(person[1])
name,age = person
print(name,age)