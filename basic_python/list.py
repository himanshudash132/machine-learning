# [List] ---->is mutable


# lst = [61, 2, 3, 4, 6, 41]
# var = type(lst)
# lst[2] = 45
# var = lst[2]
# lst.append(100)
# lst.insert(0, 100)
# lst.remove(61)
# lst.pop()
# del lst[3]
# del lst
# lst.clear()
# var = lst
# var = len(lst)
# var = lst[1:4]
# print(var)

#=============>slicing<==================== 

        #  0 1 2 3 4 5 6 7 8 9 
# my_list = [1,2,3,4,5,6,7,8,9,10]

# sliceed_list = my_list[2:6]
# print(sliceed_list)

# sliceed_list = my_list[:5]
# print(sliceed_list)

# sliceed_list = my_list[5:]
# print(sliceed_list)

# sliceed_list = my_list[1:8:2]
# print(sliceed_list)

#concatennation

# my_list1 = [1,2,3,4,5]
# my_list2 = [6,7,8,9,10]

# concatenated_list = my_list1 + my_list2
# print(concatenated_list)


# my_list = [1,200,3,4,50,6,7,118,9,10]

# my_list.sort()
# print(my_list)


# sorted_list = sorted(my_list, reverse = True)
# print(sorted_list)


numbers =[1,2,3,4,5]

squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)

even_numbers = [x  for x in numbers if x % 2 ==0]
print(even_numbers)