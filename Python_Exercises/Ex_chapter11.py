#Dictionaries


medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
events = []
for key in medal_events.keys():
    events.append(key)
print(events)    

#count words in sentence:
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
words = sentence.split()
word_counts ={}
for word in words:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] = word_counts[word] + 1
for word in word_counts:
    print(word + ": " + str(word_counts[word]) + " occurrences")
    

stri = "what can I do"
char_d ={}

for word in stri:
    for char in word:
        if char not in char_d:
            char_d[char] = 0
        char_d[char] = char_d[char] +1
print(char_d)

#Count value of dictionaries:
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total = 0
for country in travel:
    total = total + travel[country]
print(total)

# key has the highest value:
d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
max_value = 0
max_key ='' 
# initialize variable best_key_so_far to be the first key in d
for k in ks:
    if d[k] > max_value:
        max_value = d[k]
        max_key = k
    else: 
        max_value = max_value
        max_key = max_key
      
    # check if the value associated with the current key is
    # bigger than the value associated with the best_key_so_far
    # if so, save the current key as the best so far

print("key " + max_key + " has the highest value, " + str(max_value))


f = open('scarlet3.txt', 'r')
dic = {}
lines = f.readlines()
for line in lines:
    for word in line:
        for char in word:
            if char not in dic:
                dic[char] = 0
            dic[char] = dic[char]+1
sorted(dic.items(), key=lambda x: x[1], reverse=True)

print(dic)
#for n in final_list:
 #   print(final_list.key() + 'appears' + str(final_list.value()) + 'times')

 
sentence = input('enter your sentence: ')
words = sentence.split(' ')
dic = {}
for word in words:
    for char in word:
        if char not in dic:
            dic[char] = 0
        dic[char] = dic[char] + 1
for n in dic:
    print(n  +" : "+ str(dic[n]) +'\n')

