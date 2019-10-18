
a = 10
b = 20

'''print(a)

def add():
    global a
    #a = 100
    a = a + 5
    print(a)
    c = a + b
    print(c)

add()

print(a)'''


'''def add():
    global c
    c = a + b
    return c

def sub():
    global d
    d = c - b

print(add())

sub()

print(c)

print(d)'''







def outer():
    x = 10

    def inner():
        global x
        x = 20
        print("X inside inner() is", x)

    inner()
    print("X outside inner() is", x)

outer()
print("X outside both fns is", x)


























