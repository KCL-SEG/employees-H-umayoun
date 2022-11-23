"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

    def monthly_salary(num):
        print(str() & " is a monthly salaried employee who was paid " & num)
    
    def HourlyContract(hours_worked, hourly_pay):
        print(str() + " is an hourly contracted employee who is paid " + hours_worked*hourly_pay)
    
    def Monthly_Salary_with_Comm(MonthlySalary, CommissionPerContract, NumOfContracts):
        total_salary = MonthlySalary + (CommissionPerContract * NumOfContracts)
        print(str() + " is monthly salaried employee who also gets commision: " + total_salary)

    def Hourly_Pay_With_Comm(hours_worked, hourly_pay, pay_per_contract, num_contracts):
        total_pay = (hours_worked*hourly_pay) + (pay_per_contract*num_contracts)
        print(str() + " is monthly salaried employee who also gets commission: " + total_pay)
    
    def Monthly_salary_with_bonus(monthly_salary, bonus):
        total_pay = monthly_salary+bonus
        print(str() + " is monthly salaried employee who also gets a bonus: " + total_pay)

    def Hourly_plus_bonus(hours_worked, hourly_pay, bonus):
        total_pay = (hours_worked * hourly_pay) + bonus
        print(str() + " is hourly employee who also gets commission: " + total_pay)


##MonthlySalary
##HourlyPay and Hours worked
##MonthlySalary and commission
##HourlyPay and commission
##MonthlySalary and Bonus


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.monthly_salary(4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.HourlyContract(100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.Monthly_Salary_with_Comm(3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.Hourly_Pay_With_Comm(150, 25, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.Monthly_salary_with_bonus(2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
##ariel = Employee('Ariel')
