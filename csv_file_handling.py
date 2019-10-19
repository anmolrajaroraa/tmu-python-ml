#comma-separated values

#Ram,BTech,12345

#tab-separated values

#Ram   BTech  12345

import csv

#file = open('file_1.csv', 'w')

'''students = [
    {'name':'Ram', 'id':101, 'contact': '12345'},
    {'name':'Shyam', 'id':102, 'contact': '12345'},
    {'name':'Mohan', 'id':103, 'contact': '12345'}
    ]

with open('file_1.csv', 'w') as file:
    writer = csv.writer(file)
    for student in students:
        writer.writerow(student.values())'''

students = []

with open('file_1.csv') as file:
    data = csv.reader(file)
    for row in data:
        student = {'name': row[0], 'id': row[1], 'contact': row[2]}
        students.append(student)
        print(row)


print(students)





















