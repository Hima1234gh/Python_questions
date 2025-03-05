# To calculate salary of an employee given his basic pay (take as input from
# user). Calculate gross salary of employee. Let HRA be 10 % of basic pay and
# TA be 5% of basic pay. Let employee pay professional tax as 2% of total salary.
# Calculate net salary payable after deductions


basic_pay = float(input("Enter Your Basic Pay: ")) 
hra = basic_pay*0.1 
ta = basic_pay*0.05 
gross_pay = basic_pay+hra+ta 
professional_tax  = gross_pay*0.02 
net_salry = gross_pay-professional_tax 
print("HRA:", hra) 
print("TA: ", ta) 
print("Gross Salary:", gross_pay) 
print("Professional Tax:", professional_tax) 
print("Total Salary: ", net_salry) 