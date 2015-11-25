#enter a sentence
#Return something about this sentence

letter = space = num = other = 0
word = 1
list = {0:letter,1:space,2:word,3:num,4:other}
name =['letter','space','word','num','other']
str = input("Please enter a sentence:")
for i in str:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        list[0] = list[0] + 1  #letter
    elif i>='0' and i<='9':
        list[3] = list[3] + 1 #num
    elif i==' ':
        list[1] = list[1] + 1   #space
        list[2] = list[2] + 1   #word
    else:
        list[4] = list[4] + 1 #others
n = 0
while n<5:
    print(name[n])
    print(list[n])
    n = n + 1
input('press enter to finish')
