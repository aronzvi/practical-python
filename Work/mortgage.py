# mortgage.py
#
# Exercise 1.11

principal = 500000.0
rate = 0.05
regular_payment = 2684.11
total_paid = 0.0
month_count = 0
extra_payment = 1000

""" 
How much will Dave pay if he pays an extra $1000/month for 4 years starting in year 5 of the mortgage?
"""
extra_payment_start_month = 49
extra_payment_end_month = 96

print('Start month of extra', extra_payment_start_month)
print('End month of extra', extra_payment_end_month)

while principal > 0:
    month_count += 1 
    if (month_count >= extra_payment_start_month) and (month_count <= extra_payment_end_month):
        payment = regular_payment + extra_payment
    else:
        payment = regular_payment

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(month_count, total_paid, principal)

if principal < 0:
        print('Correcting last month overpayment by', abs(principal))
        total_paid = total_paid - abs(principal)
print('Total paid', total_paid)
print('Months', month_count)