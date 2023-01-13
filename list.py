# Lists
# Lists are used to store items. 

# We can create a list by using square brackets with commas separating items. Like this:

# words = ["Hello", "world", "!"]
# nums = [4, 3, 7, 1]

# If you want to access a certain item in the list, you can do this by using its index in square brackets.

# In our example, that would look like this:

# words = ["Hello", "world", "!"]
# print(words[0])
# print(words[1])
# print(words[2])

# nums = [5, 4, 3, 2, 1]

# print(nums[2])
# Lists can hold different data types, such as strings and numbers.

# x = ["a", "b", "c"]
# y = [1, 2, 3, 4, 5]
# print(x[1])
# print(y[3])

# things = ["text", 0, [1, 2, 8], 4.56]
# print(things[2][2])

# x = "Python"
# print(x[1] + x[4])

# str = "Hello world!"
# print(str[7])

# List Operations
# The item at a certain index in a list can be reassigned.

# For example:

# nums = [5, 8, 2]
# nums[1] = 42
# print(nums)
# nums = [1, 2, 3, 4, 5]
# nums[3] = nums[1]
# print(nums[3])
# x = [2, 4]
# x += [6, 8]
# print(x[2]//x[0])
# x = [2, 4]
# x = x * 3
# print(x[3])
# List Operations
# To check if an item is in a particular list, we can use the in operator.

# It returns True if the item occurs one or more times in the list, and False if it doesn't. Like this:

# words = ["spam", "egg", "spam", "sausage"]
# print("spam" in words)
# print("egg" in words)
# print("tomato" in words)

# nums = [10, 9, 8, 7, 6, 5]

# nums[0] = nums[1] - 5

# if 4 in nums:

#   print(nums[3])

# else:

#   print(nums[4])

# Similarly, to check if an item is not in a list, you can use the not operator in one of the following ways:

# nums = [1, 2, 3]
# print(not 4 in nums)
# print(4 not in nums)
# print(not 3 in nums)
# print(3 not in nums)
# for Loop:
# We have learned about the while loop in the previous lessons. Now it's time to learn about the for loop.

# The for loop is used to iterate over a given sequence, such as lists or strings.

# The code below outputs each item in the list and adds an exclamation mark at the end:

# words = ["hello", "world", "spam", "eggs"]
# for word in words:
#   print(word + "!")
# nums = [4, 7, 3, 1]
# for x in nums:
#     print(x*2)

# for Loop
# A for loop can be used to iterate over strings.

# For example:

# str = "testing for loops"
# count = 0

# for x in str:
#   if(x == 't'):
#     count += 1

# print(count)
# Similar to while loops, the break and continue statements can be used in for loops, to stop the loop or jump to the next iteration.

# text = "some text"
# for x in text:
#   if x == 'e':
#     break
#   print(x)
# Similar to while loops, the break and continue statements can be used in for loops, to stop the loop or jump to the next iteration.

# text = "some text"
# for x in text:
#   if x == 'e':
#     break
#   print(x)


# list = [2, 3, 4, 5, 6, 7]

# for x in list:

#    if(x%2==1 and x>4):

#       print(x)

    #   break
    # list numbers:

# nums = [1, 2, 3, 4]

# res = 0

# for x in nums:

#     if(x%2==0):

#         continue

#     else:

#         res += x

        

# print(res)
# Range:
# Python makes it super easy to create number sequences using the range() function.

# By default, it starts from 0, increments by 1 and stops before the specified number.

# The following code generates a list containing all of the integers, up to 10.

# numbers = range(10)

# In order to output the range as a list, we need to explicitly convert it to a list, using the list() function.

# numbers = list(range(10))
# print(numbers)

# nums = list(range(5))
# print(nums[4])

# print(range(20) == range(0, 20))
# numbers = list(range(5, 20, 2))
# print(numbers)
# nums = list(range(3, 15, 3))
# print(nums[2])

# x = list(range(7, 3, -1))
# print(x)
# numbers = list(range(5, 10, 2))




# List Slices:
# List slices allow you to get a part of the list using two colon-separated indices. This returns a new list containing all the values between the indices.

# Example:

# squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(squares[2:6])
# print(squares[3:8])
# print(squares[0:1])

# sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
# print(sqs[4:7])
# squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(squares[:7])

# sq = [0, 1, 4, 9, 16, 25, 36, 49, 64]

# print(sq[4:])
# squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(squares[::2])
# print(squares[2:8:3])
# sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 

#

# Using [::-1] as a slice is a common and idiomatic way to reverse a list.

# nums = [5, 42, 7, 1, 0]
# res = nums[::-1]
# print(res)

# nums = [1, 2, 3, 4, 5, 6]
# res = nums[::-1]
#print(res[2])


# list = [1, 1, 2, 3, 5, 8, 13]
# print(list[list[4]])

# for i in range(10):

#   if not i % 2 == 0:

#     print(i+1)

# x = [6, 4, 2, 9]

# x = x[::-1]

# print(x[0]+x[2])



# List Functions
# Python has a bunch of useful built-in functions for lists.

# len() lets you get the number of items in a list. Like this:

# nums = [1, 3, 5, 2, 4]
# print(len(nums))

# letters = ["a", "b", "c"]

# letters += ["d"]

# # print(len(letters))
# str = "some text"
# x = len(str)
# # print(x)
# x ="abc"

# x *= 2

# print(len(x))
# nums = [9, 8, 7, 6, 5]

# nums.append(4)

# nums.insert(2, 11)

# print(len(nums))

# x = [2, 4, 5, 7, 4]

# y = x.index(4)

# print(y)

# nums = [1, 3, 5, 2, 4]

# res = min(nums) + max(nums)

# print(res)

# list = [8, 4, 2, 6]

# list.remove(2)

# print(len(list)+list.count(6))

# nums = [2,4,8,9,5]


# nums.insert(1, 3)

# nums.remove(9)

# nums.insert(0, nums.count(8))

# print(nums[3])


# print("{0}{1}{0}".format("abra", "cad"))
txt = "hello"

print(max(txt))