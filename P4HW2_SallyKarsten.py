#Karsten Sally
#11/21/23
#Use if/else to determine an employee pay

#Create variables to hold totals paid to employee
num_em = 0
total_reg = 0
total_OT = 0
total_gross = 0

emp_name = input("Enter employee Name or type Done to quit")
#Loops to control adding employees
while emp_name !="Done":
    num_em += 1
    emp_hours = int(input("Enter employee hours: "))
    emp_pay =float(input("Enter employee pay rate: "))

    #Calculations
    if emp_hours > 40:
        OT_hours = emp_hours - 40
        reg_hours = 40

    else: #This represents if emp_hours is 40 hours or less
        OT_hours = 0
        reg_hours = emp_hours

    #Calculate pay
    OT_pay = (emp_pay * 1.5) * OT_hours
    total_OT += OT_pay

    reg_pay = emp_pay * reg_hours
    total_reg += reg_pay

    gross_pay = OT_pay + reg_pay
    total_gross += gross_pay
        
    print(f"Employee Name: {emp_name}")
    print(f"Regular Hours: {reg_hours}")
    print(f"OT Hours: {OT_hours}")
    print(f"OT Pay: {OT_pay}")
    print(f"Regular Pay: {reg_pay}")
    print(f"Gross Pay: {gross_pay}")
    print()
    emp_name = input("Enter Employee Name or type done to quit")
    

#This code executes after look break
print("Done adding employee")
print()
print(f"Total number of employee: {num_em}")
print(f"Total regular pay to employee: {reg_pay}")
print(f"Total OT pay to employee: {OT_pay}")
print(f"Total gros pay to employee: {gross_pay}")

      
