def word_count(mystring):
  mystring = mystring.lower()
  mywords = mystring.split()
  word_dict = {}
  wordcount = {}
  for word in mywords:
    if word in word_dict:
      wordcount[word] += 1
    else:
      wordcount[word] = 1
    word_dict[word] = wordcount[word]
        
  print(word_dict)

word_count("woah hey hey hey hey hi woah")