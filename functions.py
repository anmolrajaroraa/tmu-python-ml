x = 10
y = 20

# def name_of_fn ( arguments_list  )
 
def add(a,b):
    #print(a + b)
    return a + b
def subtract(a = 0,b = 0):
    print(b - a if b > a else a - b)
def multiply(a = 0,b = 0):
    print(a * b)
def divide(a=0,b=1):
    print(a / b)

def calc(a,b):
    #result = [a+b, a-b, a*b, a/b]
    #return result
    return a+b, a-b, a*b, a/b, a%b    #packing
    '''print("Going to return something else")
    return a-b
    return a*b
    return a/b'''

#print(add)
total = add(50,60) #positional arguments
print(total)
diff = subtract(100)  #default arguments , if we dont supply value for b, default value is used
print(diff)
multiply(x,y)  #variables used as arguments
divide(b=100)  #keyword arguments
#divide(y=100)

result = calc(23,3)
#m,n,o,p = calc(23,3)    #unpacking     #      *args  (multiple args)
m,n,o,*p = calc(23,3)
print("Result is ", result)
print("Diff is ", result[1])
print(m,n,o,p)


