#paycheck_generator.py
#October 23, 2022
#This program will generate for the user a copy of his/her current paycheck.


    

      

def employee_paycheck(regular_hours, holiday_hours, overtime_hours):
    #To calculate the pay and taxes of the employees based on hours worked.

    #hours worked during the week
    hours_worked = regular_hours + holiday_hours + overtime_hours
    
    #The hourly rate is $20.00 per hour
    hourly_rate = 20.00
    regular_pay = regular_hours * hourly_rate

    #Holiday and overtime hourly is the regular hourly multiplied by 1.5.
    overtime_rate = hourly_rate * 1.50
    overtime_pay = (overtime_hours + holiday_hours) * overtime_rate

    #Gross pay of the employee before taxes are taken out
    gross_pay = regular_pay + overtime_pay


    #federal income tax rate is %15
    fed_rate = 0.15
    federal_tax = gross_pay * fed_rate

    #State income tax rate is %10
    state_rate = 0.10
    state_tax = gross_pay * state_rate

    #FICA rate is %2
    fica_rate = 0.02
    fica = gross_pay * fica_rate
    
    #Net pay of the employee after taxes
    net_pay = gross_pay - (federal_tax + state_tax + fica)


    print(f"Hourly Rate: ${hourly_rate}")
    print(f"Hours Worked: {hours_worked}hrs")
    print(f"Regular Pay: ${regular_pay}")

    print(f"Overtime Pay: ${overtime_pay}")

    print(f"Gross Pay: ${gross_pay}")
    print(f"Federal Tax: ${federal_tax}")
    print(f"State Tax: ${state_tax}")
    print(f"FICA: ${fica}")
    print(f"Net Pay: ${net_pay}")
    

def main():

    #intro
    print('\nWELCOME TO THE PAYCHECK GENERATOR!\n')

    #number of employees whose paycheck you want to look at
    employees = int(input('Enter how many employees paycheck you would like to check: '))

    while employees >= 1:
        employee_name = str(input('\nWhat is the name of the employee? '))

        total_hours = float(input('\nHow many hours did the employee work for the week? '))

        if total_hours > 40:

            #normal hours are hours worked before getting to 40
            normal_hours = 40
            overtime_hours = total_hours - 40

        else:
            normal_hours = total_hours
            overtime_hours = 0.00

        #holiday hours calculation
        holiday_hours = float(input('\nHow many of the normal hours were during a holiday? '))

        if holiday_hours > 0:
            regular_hours = normal_hours - holiday_hours

        else:
            regular_hours = normal_hours
            holiday_hours = 0.00


        employees = employees - 1

        print(f'\n\nEmployee Name: {employee_name}')

        employee_paycheck(regular_hours, holiday_hours, overtime_hours)




main()

        

        

        

            

    

    


























    
    
