# x = "global"

# def newFunc():
#     print("This is local", x)

# newFunc()

# --------

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

# --------

# x = "global "

# def foo():
#     global x 
#     x = x * 2
#     print(x)

# foo()