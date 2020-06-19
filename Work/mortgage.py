# mortgage.py
#
# Exercise 1.8

principal = 500000.0
rate = 0.05
regular_payment = 2684.11
total_paid = 0.0
number_of_months = 0
extra_payment = 1000
number_of_extra_payments = 12

while principal > 0:
    if number_of_extra_payments > 0:
        payment = regular_payment + extra_payment
        number_of_extra_payments -= 1
    else:
        payment = regular_payment

    principal = principal * (1+rate/12) - payment 
    total_paid = total_paid + payment
    number_of_months += 1    

print('Total paid', total_paid, 'Number of months', number_of_months)