def countBobs(s):
    bob = ' '
    bobNumber = 0
    for letter in s:
        if letter == 'o':
            if bob == 'b':
                bob = 'bo'
            elif bob == 'bo':
                bob = ' '
        elif letter == 'b':
            if bob == ' ' or bob == 'b':
                bob = 'b'
            elif bob == 'bo':
                bobNumber += 1
                bob = 'b'
        else:
            bob = ' '

    print('Number of times bob occurs is: ' + str(bobNumber))
    
countBobs('bobblboobbobx')
#should be 2
countBobs('obobpbobbbobboboobbsnbobrkcobobooboozd')   
#should be 6 
countBobs('goboboobbobbsgbotbobcobobobcb')  
#should be 5
countBobs('lfobajoboboobobobobbwbobbebobobbobbb')
#should be 8
countBobs('gobanobobgbooobobzobooobbo')
#should be 2          
                