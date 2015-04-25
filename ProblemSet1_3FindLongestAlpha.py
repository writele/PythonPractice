def findLongestAlpha(s):
    prevLetter = ''
    string1 = ''
    string2 = ''

    for letter in s:
        if string1 == '':
            string1 = string1 + letter
        elif letter >= prevLetter:
            #are we adding to string 1 or 2?
            if len(string2) >= 1 and len(string2)<=len(string1):
                string2 = string2 + letter 
            elif len(string2) >= 1 and len(string2)>len(string1):
                string1 = string2 + letter
                string2 = ''
            else:
                string1 = string1 + letter
#if next letter is NOT alphabetically greater
        else:
           if len(string2) > 1:
                if len(string2) > len(string1):
                    string1 = string2
                string2 = letter
           elif string2 == '':
               string2 = letter
           elif len(string2) == 1:
                string2 = letter

        prevLetter = letter
#compare string1 and string2 after searching through s
    if len(string2) > len(string1):
        answer = string2
    else:
        answer = string1
    print('Longest substring in alphabetical order is: ' + answer)
#Test cases
findLongestAlpha('owhdipdcaumntjvcmsnd')
#should be dip
findLongestAlpha('pxomksyxqts')
#should be ksy
findLongestAlpha('pfvqhunhcamkjlxgwun')
#jlx
findLongestAlpha('tmdrrjymzzaffyzhhhycf')
#affyz