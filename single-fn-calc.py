def calc(x,y,operator):
    print( eval(x + operator + y) )
    #10 + '+' + 5

while True:
    print('''1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit''')
    
    choice = input("Enter your choice: ")

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    operators = {'1':'+', '2':'-', '3': '*', '4':'/'}

    operator = operators.get(choice)

    calc(num1,num2,operator)

    
