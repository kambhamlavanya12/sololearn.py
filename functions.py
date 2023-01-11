# Functions
# Just like with if statements, the code block within every function starts with a colon (:) and is indented.

# def my_func():
#   print("spam")
#   print("spam")
#   print("spam")





# Functions
# So once you’ve defined a function, you can call it multiple times in your code.

# Like this:

# def hello():
#   print("Hello world!")

# hello()
# hello()
# hello()

# The function needs to be defined before it can be called. Calling a function before its definition will cause an error.
# For example:

# hello()
# def hello():
#   print("Hello world!")


# def foo():
#     print(1)
#     print(2)
# foo()
# foo()




# Arguments
# Functions can take arguments, which can be used to generate the function output.

# For example:

# def exclamation(word):
#   print(word + "!")

# exclamation("spam")



# def print_double(x):
#     print(2 * x)
# print_double(3)

# Arguments
# You can call the same function with different arguments.

# def exclamation(word):
#   print(word + "!")

# exclamation("spam")
# exclamation("eggs")
# exclamation("python")


# def x(y):
#     print(y+2)
# x(5)

# Even better, you can define functions with more than one argument; separate them with commas. Like this:

# def print_sum_twice(x, y):
#   print(x + y)
#   print(x + y)

# print_sum_twice(5, 8)

# def printBill(text):
#   print("======")
#   print(text)
#   print("======")
# text = input()
# printBill(text)


# def msg(num, ch):
#  print(ch+str(num))
# msg(18, 'A')


# Returning from Functions
# Certain functions, such as int or str, return a value instead of outputting it. 

# The returned value can be used later in the code, for example, by getting assigned to a variable. 

# To do this for your defined functions, you can use the return statement. Like this:

# def sum(x, y):
#   return x+y

# Now we can use our function and assign the result to a variable:

# def sum(x, y):
#   return x+y

# res = sum(42, 7)
# print(res)

# def foo(x, y):
#   if x >= y:
#     return x
#   else:
#     return y
# x = foo(4, 7)
# print(x)



3

# Returning from Functions :
# You can use the returned value in your code, for example, an if statement:

# def max(x, y):
#   if x >=y:
#     return x
#   else:
#     return y

# if(max(6, 4) > 10):
#   print("Yes")
# else:
#   print("Nope")


# Once you return a value from a function, it immediately stops being executed. 

# Any code placed after the return statement won’t be executed.

# For example:

# def add_numbers(x, y):
#   total = x + y
#   return total
#   print("This won't be printed")

# print(add_numbers(4, 5))


# What's the highest number this function prints if called?

# def print_numbers():
#   print(1)
#   print(2)
#   return
#   print(4)
#   print(6)
  
#   A function can only return once, thus, if you need to return multiple values, you can use a list.

# For example:

# def double(a, b):
#   return [a*2, b*2]
# x = double(6, 9)
# # print(x)

# def calc(x, y):
#    return [x+y, x*y]
# res = calc(3, 4)
# print(res[1])


# def sum(x):
#     res = 0
#     for i in range(x):
#         res+=i
#     return res
# print(sum(4))

def sum(x):

    res = 0

    for i in range(x):

        res+=i

    return res

    

print(sum(4))