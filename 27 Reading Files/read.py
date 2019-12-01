employees_file = open("employees.txt", "r+")   #w write, r read, r+ all, a append

for employee in employees_file.readlines():
    print(employee)

employees_file.close()