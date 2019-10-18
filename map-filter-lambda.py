def temp_convert(c):
    return 9/5 * c + 32

#cel = 35
cel_list = [10,20,30,40,23,34,23,21,34,12]
fah_list = []

#fah = temp_convert(cel)
'''for temp in cel_list:
    fah_list.append(temp_convert(temp))'''

f_list = list(map(temp_convert, cel_list))

#f_list = list(map(lambda a,b,c:a+b+c, cel_list))

#def sum(a,b,c):
#    return a+b+c

f2_list = list(map(lambda c: 9/5 * c + 32, cel_list))

print(f_list)
print(f2_list)


def even(number):
    return number % 2 == 0

#number = int(input("Enter a number: "))

#print('Even') if even(number) else print('odd')

numbers = [12,23,123,4,5,5634,3,324,45,34]

evenNumbers = []

'''for num in numbers:
    if even(num):
        evenNumbers.append(num)'''

evenList = list(filter(even, numbers))
        
evenList2 = list(filter(lambda number: number % 2 == 0, numbers))

print(evenNumbers)
print(evenList)
print(evenList2)















