
#8 
percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []
for i in percent_rain:
    if i > 90 and i <=100:
        resps.append('Bring an umbrella')
    elif i > 80 and i <=90:
        resps.append('Good for the flowers')
    elif i > 50 and i <=80:
        resps.append('Watch out for the clouds')
    elif i <= 50: 
        resps.append('Nice day!')
print(resps)

# show grade:

a = input("enter your score: ")
n = float(a)
if n<60:
        print("you get a grade F")
elif n < 70:
        print("you get a grade D")
elif n < 80:
        print("you get a grade C")
elif n < 90:
        print("you get a grade B")
elif n <= 100:
          print("you get a frade F")
else: 
    print("wrong input")

# is_even:
num_lst = [3, 20, -1, 9, 10]
is_even =[]
for i in num_lst:
    if i % 2 == 0:
        is_even.append(True)
    else:
        is_even.append(False)
print(is_even)

#8:
students = ['Ruth', 'Karla', 'Mercedez', 'Mariam', 'Mahak', 'Luisa', 'Kimberly', 'Brytanya', 'Perla', 'Gabriella', 'Marissa']
a = len(students)
print("The number of students in this course is", a)
inp = input("Enter student name:")
for n in students:
    if inp == n:
        print('Studen_is attending this course')
    else:
        print('Studen_is not attending the course')
        
        