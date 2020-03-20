#10

fileref = open("school_prompt2.txt", "r")
a = fileref.read()
num_char = 0
for char in a:
    num_char = num_char + 1
print(a)

fileref.close()

# Read and count lines:
fileref = open('travel_plans2.txt', 'r')
num_lines = 0
a = fileref.readlines()
for n in a:
    num_lines = num_lines + 1
print(num_lines)
fileref.close()

#10:

# Hint: first see if you can write a program that just prints out the number of scores on each line
# Then, make it print the number only if the number is at least six
# Then, switch it to printing the name instead of the number
filevar = open('studentdata.txt', 'r')

for line in filevar:
    b = line.split()
   
    if len(b[1:]) > 6:
        print(b[0])
filevar.close()

#
filevar = open('emotion_words.txt', 'r')
a = filevar.readlines()
c =[]
j_emotions = []

print(a)
for line in filevar:
    lin = line.split()
    for w in lin:
        words = w.split()
        c.append(words)
        for char in words:
            if char[0] == 'j':
                j_emotions.append(words)
                    
print(j_emotions)

#write data to new file:
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
month = open('months.txt', 'w')
for n in months:
    month.write(n +'\n')


# count 

filevar = open('travel_plans.txt', 'r')
num = 0
a = filevar.readlines()
for n in a:
    for m in n:
        num = num +1

print(num)

# select the third word of each sentence:
filen = open('school_prompt.txt','r')
lines = filen.readlines()
three = []
for line in lines:
    words = line.split(" ")
    three.append(words[2])   
print(three)

## select the first word of each sentence:
file = open('emotion_words.txt','r')
lines = file.readlines()
emotions =[]
for line in lines:
    c = line.split(" ")
    emotions.append(c[0])
print(emotions)
    



    

    

