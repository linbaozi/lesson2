#enter a sentence
#Return something about this sentence

letter = space = num = other = 0
word = 1
dat = {'letter':letter,'space':space,'word':word,'num':num,'other':other}
sentence = input("Please enter a sentence:")
for i in sentence:
    if i.isalpha():
        dat['letter'] = dat['letter'] + 1  #letter
    elif i.isdigit():
        dat['num'] = dat['num'] + 1 #num
    elif i==' ':
        dat['space'] = dat['space'] + 1   #space
        dat['word'] = dat['word'] + 1   #word
    else:
        dat['other'] = dat['other'] + 1 #others
for i in dat:
    print (i,'=',dat[i])
input('press enter to finish')
