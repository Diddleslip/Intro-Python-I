# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

print()
print()

# YOUR CODE HERE
def f1(num1, num2):
    return num1 + num2

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
def f2(*argv):
    total = 0
    for arg in argv:
        total = total + arg
    return total

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = (7, 6, 5, 4)

# How do you have to modify the f2 call below to make this work?
# def manualFunc(nums):
#     total = 0
    # for i in range(len(nums)):
    #     total = total + nums[i] 
    #     print("This is i",nums[i]) ### Second solution below
    # for num in nums:
    #     if num < 0:
    #     total += num
    #     print("This is i",num)
    # return total

# print(manualFunc(a))

print(f2(sum(a)))    # Should print 22


print()
print()
print()
print()

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE
def f3(num1, num2 = "missing"):
    if num2 == "missing":
        return num1 + 1
    else:
        return num1 + num2

print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE
def f4(**kwargs ):
    for key, value in kwargs.items():
        print(f"key: {key}, value: {value}")
   

# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
f4(d=d) ## To make this work, take off an asterisk and remove the items() method invoked in line 82. The reason is because one asterisk is used for dictionary like objects, while two asterisks means that you will need to assign keywords.

print()
print()