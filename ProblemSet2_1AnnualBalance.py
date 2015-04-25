balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
total = 0

for num in range(1,13):
    minPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minPayment
    interest = (annualInterestRate/12) * unpaidBalance
    balance = unpaidBalance + interest
    total = total + minPayment
    print('Month: ' + str(round(num, 2)))
    print('Minimum monthly payment: ' + str(round(minPayment, 2)))
    print('Remaining Balance: ' + str(round(balance, 2)))
    
print('Total paid: ' + str(round(total, 2)))
print('Remaining Balance: ' + str(round(balance, 2)))