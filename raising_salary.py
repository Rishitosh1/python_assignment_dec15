def old_salary(salary):

    new_salary=[]

    for each in salary:
        each=0.23*each+each
        new_salary.append(each)
    return new_salary


salary=[15000,20000,17000,18900,30000]
new_salary=old_salary(salary)
print(new_salary)
