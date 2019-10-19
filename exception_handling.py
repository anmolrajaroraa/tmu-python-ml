
#try - all the code/logic
#except {}  -->  catch error/exception and do some needful handling of error
#finally -> write the code which should run at the end in any case

'''def divide():
    num_1 = input("Enter first number: ")
    num_2 = input("Enter second number: ")
    print(num_1 / num_2)

try:
    divide()
    print('No error occured')
except ZeroDivisionError:
    print('Dont give input as zero for num_2')
    divide()
except ValueError:
    print("Please input only integers")
    divide()
except BaseException as error:
    print("Some error occured", error)'''

'''import csv, io, os
path = 'file_2.csv'
try:
    file = open(path)
    data = file.read()
    print("Done!")
except io.UnsupportedOperation:
    print('Please check the file mode!')
except BaseException as error:
    print(error)
finally:
    print('Going to close the file!')
    if os.path.isfile(path):
        file.close()'''


def atm():
    pin = '1234'
    balance = 10000
    userPin = input("Please enter your pin: ")
    if pin != userPin:
        raise ValueError('Pin Incorrect!')
    transAmount = int(input("How much you want to withdraw: "))
    '''if transAmount > balance:
        raise ValueError('Insufficient Balance!')'''
    assert(transAmount <= balance), 'Insufficient Balance!'
    print('Please collect your cash!')
    balance -= transAmount
    print('Balance is', balance)

try:
    atm()
except AssertionError as error:
    print(error)
except ValueError as error:
    print(error)
except BaseException as error:
    print(error)
else:
    print('Thanks for visiting us!')










































