#7reverse a string:

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

s = input("enter your message: ")
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using loops) is : ",end="") 
print (reverse(s)) 

#months of year
for amonth in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December']:
    print("One of the months of the year is", amonth)

#use loop to print a number square of that number:
for i in [12, 10, 32, 3, 66, 17, 99, 20]:
    square = i**2
    print('number is:',i, ' and square of', i, 'is', square)
       
# mutilpy by using for loop"
lst = [1, 2, 3, 4]
mult = 1
for n in lst:
    mult = mult * n
print(mult) 

#print odd numver from 1 to 101:
for n in range(1, 102):
    if n % 2 == 1:
        print(n)

#compute to 100:
tong = 0
for i in range(1,101):
    tong = tong + i
print(tong)

# compute square:
ls = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
for n in ls:
    a = n**2
    print(a)

#7:
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# Write your code here.
for n in str_list:
    print(len(n)

#7:
several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
for n in several_things:
    print(n)
for n in several_things:
    print(type(n))
