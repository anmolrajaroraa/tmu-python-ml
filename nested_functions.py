def outer():
    print('Outer called')
    def inner_1():
        print('Inside inner_1 fn')
    def inner_2():
        print('Inside inner_2 fn')
    #print(inner_1())
    #print(inner_2())
    return inner_1, inner_2

result = outer()
print(result)
result[0]()
result[1]()
#print(inner_1())
