# accepting inputs 
annual_salary = float(input("Enter your annual salary: "))

portion_saved = float(input("Enter the percentage of the salary to save, as decimal: "))

Total_cost = float(input("Enter the cost of your dream home: "))

semi_annual_raise = float(input("Enter semi-annual raise, as a decimal: "))

# initialisation

portion_down_payment = 0.25*Total_cost

month = 0

current_savings = 0

r = 0.04

# the main logic

while current_savings < portion_down_payment :
    
    increase = annual_salary * semi_annual_raise

    monthly_salary = annual_salary/12
    
    monthly_save = portion_saved * monthly_salary

    additional_money = current_savings*r/12
    
    current_savings += monthly_save + additional_money
    
    month += 1
    
    if month % 6 == 0:
        annual_salary += increase
        
# printing outputs

print("Number of months:",int(month))


