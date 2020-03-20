#9:
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []
for n in verbs:
    ing.append(n + "ing")
print(ing)
verbs = ing
print(verbs)

myList = [76, 92.3, 'hello', True, 4, 76]

myList.append('apple')
myList.append(76)
myList.insert(3, 'cat')
myList.insert(0, 99)
print(myList.index( 'hello' ))

#9:
myList = [76, 92.3, 'hello', True, 4, 76]

myList.append('apple')
myList.append(76)
myList.insert(3, 'cat')
myList.insert(0, 99)
myList.remove(76)
print(myList.index('hello'))
count = 0
for n in myList:
    if n == 76:
        count = count + 1
for a in myList:
    if a ==True:
        myList.pop(a)
print(count)
print(myList)

# check for keywords:
import keyword
test = ["else", "integer", "except", "elif"]
keyword_test = []
for n in test:
    if keyword.iskeyword(n) == True:
        keyword_test.append(True)
    else:
        keyword_test.append(False)
print(keyword_test)    

# return squares:
numbers = [71, 96, 88, 76, 39, 34, 17, 88, 40, 69, 51, 23, 84, 74, 14, 84, 20, 63, 37]
sqrts = []
for n in numbers:
    sqrts.append(n**2)

# 
municipalities = ['Morgantown', 'Star City', 'Westover', 'Granville', 'Blacksville']
cities = municipalities
towns = cities[:]
municipalities = [n.replace('Blacksville', 'Town of Blacksville')for n in municipalities]
print(municipalities)
print(cities)
print(towns)
    
