full_name = input("Enter your full name: ")
name = full_name.split()
count = len(name)

if count == 2:
    first_name, last_name = name
    print(" The first name is {0} and the last name is {1}".format(first_name,last_name))
if count>2:
    first_name, middle_name, last_name = name
print("The first name is {0}, the middle name is {1} and the last name is {2}".format(first_name,middle_name,last_name))