def add(x,y):
    print(x + y)
def sub(x,y):
    print(x - y)
def mul(x,y):
    print(x * y)
def div(x,y):
    print(x / y)
def terminate(*args):
    print("Going to terminate program")
    quit()
def errorHandler(*args):
    print("Wrong choice")

while True:
    print('''1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit''')
    
    choice = input("Enter your choice: ")

    '''if choice == 5:
        quit()
    elif choice < 1 or choice > 5:
        print("Wrong choice")
        continue'''

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    operations = {'1':add, '2': sub, '3':mul, '4':div, '5':terminate}

    #operations[choice](num1,num2)

    operations.get(choice,errorHandler)(num1,num2,choice)





    
    '''if choice == 1:
        print(add(num1,num2))
    elif choice == 2:
        print(sub(num1,num2))
    elif choice == 3:
        print(mul(num1,num2))
    else:
        print(div(num1,num2))'''


    '''def first():
	print("in first fn")

	
>>> def second():
	print("in second fn")

	
>>> operations = {'1':first(), '2': second()}
in first fn
in second fn
>>> operations
{'1': None, '2': None}
>>> 
>>> 
>>> first()
in first fn
>>> print(first())
in first fn
None
>>> print(first)
<function first at 0x109637f28>
>>> operations = {'1':first, '2': second}
>>> operations
{'1': <function first at 0x109637f28>, '2': <function second at 0x10964f048>}
>>> 
>>> choice = '1'
>>> operations[choice]
<function first at 0x109637f28>
>>> operations[choice]()
in first fn'''
