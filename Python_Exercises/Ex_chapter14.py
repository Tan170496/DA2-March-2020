# appends value using while loop
numbers = []
counter = 0
while counter <=35:
    numbers.append(counter)
    counter = counter + 1
print(numbers)


#append value deviable for 10:
tens =[]
counter = 0
while counter <=50:
    if counter % 10==0:
        tens.append(counter)
    counter = counter + 1
print(tens)


def sublist(lst):
    count = 0
    new_lst = lst
    final = []
    while count < len(new_lst):
        if new_lst[count] != 5:
            final.append(new_lst[count]) 
        count = count + 1
        
        break
    return final
print(sublist([1,2,3,4,5,6,7,8,9]))