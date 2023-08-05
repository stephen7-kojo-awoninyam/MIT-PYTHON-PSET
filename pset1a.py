
annual_salary = float(input("Enter your annual salary: "))

portion_saved = float(input("Enter the percentage of the salary to save, as decimal: "))

Total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25*Total_cost

monthly_salary = annual_salary/12

month = 0

current_savings = 0

r = 0.04

monthly_save = portion_saved * monthly_salary


while current_savings < portion_down_payment :
    
    additional_money = current_savings*r/12
    
    current_savings += monthly_save + additional_money
    
    month += 1


print("Number of months:",int(month))


