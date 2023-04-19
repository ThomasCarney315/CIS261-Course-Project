
# Thomas Carney
# CIS 261 - Object-Oriented Computer Programming
# Course Project Phase 1

### Create function GetEmpName that will input a value into variable empname and return the value
def GetEmpName():
    empname = input('Enter employee name:  ')
    return empname
### This function shows how to enter a value that is numeric and return the value.
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours

### Create a function GetHourlyRate that will input a numeric value into variable hourlyrate and return the value
def GetHourlyRate():
    hourlyrate = float(input('Enter hourly rate:  '))
    return hourlyrate

### Create a function GetTaxRate that will input a numeric value into variable taxrate and return the value
def GetTaxRate():
    taxrate = float(input('Enter tax rate:  '))
    return taxrate

def CalcTaxAndNetPay(hours,  hourlyrate, taxrate):
    ## complete the code to calculate grosspay, incometax, and net pay
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours:,.2f}")
    ## complete the code to display hourlyrate, grosspay, taxrate, incometax, and netpay with appropriate labels and formatting
    print(f'Hourly Rate:  {hourlyrate:.2f}')
    print(f'Gross Pay:  {grosspay: .2f}')
    print(f'Tax Rate:  {taxrate: .0%}')
    print(f'Income Tax:  {incometax: .2f}')
    print(f'Net Pay:  {netpay: .2f}')

    print()

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    ## complete the code to display TotGrossPay, TotTax, and TotNetPay with appropriate lables and formatting
    print(f'Total Gross Pay:  {TotGrossPay: .2f}')
    print(f'Total Income Tax:  {TotTax: .2f}')
    print(f'Total Net Pay:  {TotNetPay: .2f}')


if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        ## call the function GetEmpName and assign the return value to empname
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break

        ## call the function GetHoursWorked and assign the return value to hours
        hours = GetHoursWorked()

        ## call the function GetHourlyRate and assign the return value to hourlyrate
        hourlyrate = GetHourlyRate()

        ## call the function GetTaxRate and assign the return value to taxrate
        taxrate = GetTaxRate()
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)

        ## call the function printinfo and pass in empname, hours, hourlyrate, grosspay, taxrate, incometax, and netpay
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)

        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
    ## call the function PrintTotals and pass in  TotEmployees, TotHours, TotGrossPay, TotTax, and TotNetPay
    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
