balance = 3329
annualInterestRate = 0.2
#should generate 310
newbalance = balance

while True:
    newbalance = balance
    for num in range(12):
        minPayment = 10
        interest = annualInterestRate/12
        unpaidBalance = balance - minPayment
        balance = unpaidBalance + (interest * unpaidBalance)
    total = balance
    print('Annual balance is: ' + str(total))
    if total < 0:
        print('Lowest payment: ' + str(minPayment))
        break
    else:
        minPayment = minPayment + 10
        total = 0
        balance = newbalance