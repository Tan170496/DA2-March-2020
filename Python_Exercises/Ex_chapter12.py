#Functions:

def reverse(astring):
    return astring[::-1]
print(reverse('please reverse this sentence'))

def num_test(n):
    if int(n)>10:
        return 'Greater than 10'
    elif int(n) < 10:
        return 'Less than 10'
    else: 
        return 'Equal to 10'
print(num_test(1))

#return digits of input:
def numDigits(n):
    for d in str(n):
        result = len(str(n))
    return result

print(numDigits(3004543))

#remove letters:
def remove_letter(theLetter, theString):
    new = theString.replace(theLetter, '')
    return new
   
print((remove_letter('a', 'ngay mai toi di hoc')))

#
from test import testEqual
def replace(s, old, new):
    cut_old = s.split(old)
    temp = new
    new = temp.join(cut_old)
    return new
print(replace('hom nay la thu ba cua thang ba', 'a', 'o'))

#find max vulue number:
import random

def max(lst):
    max = 0
    for e in lst:
        if e > max:
            max = e
    return max

lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(max(lst))

# sum of squares:
def sum_of_squares(xs):
    sum = 0
    for n in xs:
        sum = sum + n*n
    return sum
print(sum([3,4,5]))

# count odd numbers:
def countOdd(lst):
    count = 0
    for n in lst:
        if n %2 == 1:
            count = count +1
    return count

#sum up all even numbers in list:
def sumEven(lst):
    sum = 0
    for n in lst:
        if n % 2==0:
            sum = sum + n
    return sum

#sum up all negative numbers:
def sumNegatives(lst):
    sum = 0
    for n in lst:
        if n < 0:
            sum = sum + n
    return sum

print(sumNegatives([-2, -15, -56]))

#tinh canh huyen cua tam giac vuong:

def findHypot(a,b):
    c = (a + b)**0.5
    return c
print(findHypot(17,8))

#compute pow:
def pow_answer(base, exponent):
    c = base**exponent
    return c
print(pow_answer(5,5))

#
def generate_odd_numbers(lst):
    new = []
    for n in lst:
        if n %2 == 1:
            new.append(n)
    return new
print(generate_odd_numbers([2, 3, 4, 5, 6, 7, 8, 9 ,10]))
        




