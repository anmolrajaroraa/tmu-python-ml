'''def student(eno = None,name = None,contact = None,address = None, *otherDetails):
    print(f"eno : {eno}, name : {name}, contact : {contact}, address : {address}, otherDetails: {otherDetails}")
'''
def student(eno = None,name = None,contact = None,address = None, **otherDetails):
    print(f"eno : {eno}, name : {name}, contact : {contact}, address : {address}, otherDetails: {otherDetails}")

# *args - > multiple values -> creates a tuple
# **kwargs  (keyword args)  -> multiple keywords arguments -> creates a dictionary


student(101,'Ram', '1233', 'abc')
student(102,'Mohan', address = 'def')
student(103, 'Shyam', '4567', 'xyz', course='BTech', age=21)
