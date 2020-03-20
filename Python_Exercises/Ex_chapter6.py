#6_1
letters = ['A', 'B', 'C', 'D', 'E']
print(letters[0])
print(letters[2:5])
print(letters[0])
print(letters[-1])
grade = letters[2]
print(grade)

#6_3
lst = "It might seem crazy what I'm 'bout to say, Sunshine she's here, you can take a break"
output = lst[-1]
print(output)

#6_
m1 = "Now I know"
m2 = "how to concatenate strings"
m3 = "in Python"
m4 = '!'
print(m1 + m2 + m3 + m4)

#6_
ls = ['who', 'world', 'run', 'lights', '?', 'girls', 'the', 'sea']
#your code here
print(ls[1])
print(ls[2])
print(ls[4])
print(ls[5])
print(ls[3])

message = ls[0] + " " + ls[2]+ " " +  ls[-2]+ " "  + ls[1] + ls[-4]
print(message)
print(message.capitalize())

#6_
ls1 = ['who', 'world', 'run', 'lights', '?', 'girls', '1', 'sea']
print(type(ls1[3]))
print(type(ls1[6]))
#your code here
ls2 = ['who', 'world', 'run', 'lights', '?', 'girls', 1, 'sea']
print(type(ls2[3]))
print(type(ls2[6]))

#6
item_ls = ['milk', 'coca', 'tea', 'coffee', 'beer', 'wine']
then = " then "
print(then.join(item_ls))

#6
str = 'We look at science as something very elite, which only a few people can learn. That’s just not true. You just have to start early and give kids a foundation. Kids live up, or down, to expectations.'
print(str)
x = str.split(". ")
a = x[0]
b = x[1]
c = x[2]
d = x[3]
print(a)
print(b)
print(c)
print(d)