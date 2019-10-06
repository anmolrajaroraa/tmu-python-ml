'''number = int(input("Enter a number to check if it's prime or not"))
numberIsPrime = True
if number <= 1:
    print("Number is not prime")
else:
    for i in range(2, ((number // 2) + 1)  ):
        if number % i == 0:
            print('Number is not prime')
            numberIsPrime = False
            break
    if numberIsPrime:
        print('Number is prime')'''

number = int(input("Enter a number to check if it's prime or not"))

if number <= 1:
    print("Number is not prime")
else:
    for i in range(2, ((number // 2) + 1)  ):
        if number % i == 0:
            print('Number is not prime')
            break
    else:
        print('Number is prime')

