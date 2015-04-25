print("Please think of a number between 0 and 100!")

low = 0
high = 100

while True:
    ans = (high + low)/2
    print('Is your secret number ' + str(int(ans)) + '?')
    choice = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if choice == 'l' or choice == 'L':
        low = ans
    elif choice == 'h' or choice == 'H':
        high = ans
    elif choice == 'c' or choice == 'C':
        print('Game over. Your secret number was: ' + str(int(ans)))
        break
    else:
        print('Sorry, I did not understand your input')