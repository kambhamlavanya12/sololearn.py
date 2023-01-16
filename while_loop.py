# i=1
# while i<=5:
#    print(i)
#    i=i+1

# print("Finished!")

'''we can also use other statements, such as if statements in loops'''

# x=1
# while x<10:
#   if x%2==0:
#     print(str(x)+" is even")
#   else:
#     print(str(x) +" is odd")
#   x+=1

'''break statement'''

# i=0
# while True:
#   print(i)
#   i=i+1
#   if i>=5:
#     print("Breaking")
#     break

# print("Finished")

# i=5
# while True:
#   print(i)
#   i=i-1
#   if i<=2:
#     break

'''continue statement'''

# i=0
# while i<5:
#   i+=1
#   if i==3:
#     print("Skipping 3")
#     continue
#   print(i)

'''break and continue'''

# i=0
# while True:
#     i+=1
#     if(i==2):
#         continue
#     if(i==5):
#         break
#     print(i)

'''You are making a ticketing system.
The price of a single ticket is $100.
For children under 3 years of age, the ticket is free.
Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.'''

# total = 0
#your code goes here
# i=0
# while i<5:
#     age=int(input())
#     i+=1
#     if age<3:
#         continue
#     total+=100
# print(total)

# i = 0
# x = 0
# while i < 4:
#     x+=i
#     i+=1
# print(x)

# x = int(input())
# if x > 5:
#     if x < 8:
#         print(x+1)
#     else:
#         print(x-1)
# else:
#     print(x)

'''Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. 
It’s calculated using a person's weight and height, using this formula: weight / height²
The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more'''

# w=int(input())
# h=float(input())

# BMI=w/(h*2)

# if BMI<18.5:
#     print("Underweight")
# elif BMI>=18.5 and BMI<25:
#     print("Normal")
# elif BMI>=25 and BMI<30:
#     print("Overweight")
# elif BMI>30: 
#     print("Obesity")
