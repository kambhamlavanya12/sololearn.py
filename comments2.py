# Comments:
# We’re so close to the finish line! Well done for making it this far!

# Comments are annotations to code used to make it easier to understand. They don't affect how code is run. 

# In Python, a comment is created by inserting an octothorpe (otherwise known as a number sign or hash symbol: #). All text after it on that line is ignored.

# For example:

# x = 365
# y = 7
# print(x % y) # find the remainder


# x = 5
# #x += 1
# x += 2 #increment
# print(x)

# Docsstrings:
# Docstrings (documentation strings) are similar to comments, in that they’re designed to explain code. But, they’re more specific and have a different syntax.

# They’re created by putting a multiline string containing an explanation of the function below the function's first line. Like this:

# def shout(word):
# """
# Print a word with an
# exclamation mark following it.
# """
# print(word + "!")

# shout("spam")


# def print_nums(x):
#   for i in range(x):
#     print(i)
#     return
# print_nums(10)


def func(x):

  res = 0

  for i in range(x):

     res += i

  return res

print(func(3))

