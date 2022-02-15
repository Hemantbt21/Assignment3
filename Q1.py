x=str(input('enter string:'))#take input string from user
list=x.split()#split elements of string into list
dict1={}#initializing an empty dictionary
if len(list)==1:
    for i in list[0]:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    print(dict1)
else:
    for i in list:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    print(dict1)
print('\n')

