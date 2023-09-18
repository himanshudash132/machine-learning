
# while loop
count = 0
while count < 5: 
      print("count:",count)
      count+=1

# Nested loop
for i in range(1, 4):
      for j in range(1,4):
            print(i,"*",j, "=",i*j)

# Loop Control Statements
numbers = [0,1,2,3,4,5]
for num in numbers:
      if num ==3:
          continue # skip no. 3
      if num ==3:
          break    # Exit the loop
      print(num)


      