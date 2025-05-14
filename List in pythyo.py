#1... 
num=[1.2,1.9,2.8,3.7,4.2]
print(num)                 # for print
print(type(num))           #to find the type
print(len(num))            #to find the length of value
print(num[1])              # to search for index value 
print(num[-4:-1])        # to search for negative index value [1.2=-5,1.9=-4,2.8=-3,3.7=-2,4.2=-1]

#1... List in pythyo.py

 #2.. FUNCTION.APPEND(_)  yo le number or variable add garcha
num=[1,3,4,5,7,8]
num.append(2)       # Aba 2 add huncha list ma 
print(num) 
 
#..
name=['shuvam','kriti']
name.append('samrat')   # Aba samrat add huncha list ma
print(name)

#3...FUNCTION.SORT(_)  yo syntax ko kam  order ma halcha number or kunai pani  kura lai
num=[3,2,5,4,1]   
num.sort()
print(num)

#
chr=['e','d','c','b','a']
chr.sort()
print(chr)

#,..
name=['shuvam','cat','binu','aditay','dipu']
name.sort()
print(name)

#4....LIST.SORT(Reverse =.....)  
# SYNTAX VARIABLE(NUM).sort(reverse=VARIABLE(NUM))
num=[1,2,3,4,5,6,7,8,9]
num.sort(reverse=num)
print(num)

#...
name=['alu','bilu','cilu','dilu','eilu']
name.sort(reverse=name)
print(name)

#..
name=['alu','shuvam','bisal','raj','calu']
name.sort(reverse=name)
print(name)


#5...LIST.REVERSE()  reverse garxa yo syntax le
     #syntax (variable.reverse())
num=[5,4,3,2,1]
num.reverse()
print(num)

#...
chr=[9,8,7,6,5,4,3,2,1]
chr.reverse()
print(chr)

#,,,
name=['anup','bishal','caluu','dipa','emu']
name.reverse()
print(name)

#6....Syntax = list.Insert(1,variable) yo index ko 1 ho ra hamile 1 ko thaou ma kunai naya kura add gare ko ho   
name=['raj','hari','bishal']
name.insert(1,'shuvam')
print(name)

#..
num=[1,2,4,5,7,8]
num.insert(2,'3',)
num.insert(5,'6')
print(num)

#...
name=['shuvam','binu','swikriti']
name.insert(0,'prakriti')
name.insert(2,'mithila')
print(name)


#7...LIST.REMOVE METHOD..
#list.remove(....)

name=['shuvam','prakriti','swikriti','summer','rohit']
name.remove('rohit')
print(name)

#...
chr=['a','s','x','gc','uu','s','f','j']
chr.remove('x')
chr.remove('uu')
chr.remove('j')
print(chr)

#,,,,
num=[1,2,3,4,4,5,6,7,8]
num.remove(4)
print(num)


#8... Tuples in python (...) this is a tuple
#A tuple is an ordered, immutable (unchangeable) collection of elements in Python, 
# enclosed in parentheses ().


# ...tup.index(...) returns index of first occurrence
name=('shuvam','raj','rawan')
print(name.index('raj'))
print(type(name))


#..
num=(1,2,3,4,5,6,7,8)
print(num.index(4))
print(type(num))


#... tupel..Count
num=(1,2,2,3,3,2,2,34,3,2,1,2,2)
print(num.count(2))
print(type(num))

#..
chr=('a','s','a','d','a','a','d','f','s','r','s','a','a',)
print(chr.count('a'))



#..LET'S PRACTICE 
#1..WAP to ask the user to enter names of their 3 
# favorite movies & store in a list
movie=[]
user1=input('movie name:')
user2=input('movie name:')
user3=input('movie name:')

movie.append(user1)
movie.append(user2)
movie.append(user3)
print(movie)

#WAP to ask the user to enter names of their 5 
# favorite movies & store in a list
movie=[]
movie1=input('name of the movie:')
movie.append(movie1)
movie2=input('name of the movie:')
movie.append(movie2)
movie3=input('name of the movie:')
movie.append(movie3)
movie4=input('name of the movie:')
movie.append(movie4)
movie5=input('name of the movie:')
movie.append(movie5)

print(movie)

#...
#WAP to ask the user to enter names of their 5 
# favorite foods & store in a list
food=[]
food1=input('name of the food:')
food.append(food1)
food2=input('name of the food:')
food.append(food2)
food3=input('name of the food:')
food.append(food3)
food4=input('name of the food:')
food.append(food4)
food5=input('name of the food:')
food.append(food5)
print(food)


#WAP to ask the user to enter names of their 5 
# favorite num & store in a list
num=[]
num1=int(input('the favourite number is:'))
num.append(num1)
num2=int(input('the favourite number is: '))
num.append(num2)
num3=int(input('the favourite number is :'))
num.append(num3)
num4=int(input('the favorite number is :'))
num.append(num4)
num5=int(input('the favorite number is :'))
num.append(num5)
print(num)

#2...WAP to check if list contains a palindrome of elements.
#palindrome=A palindrome is a word, phrase, number, or sequence of characters
# that reads the same backward as forward.


#WAP to count the numbers os the students with the 'A' grades in the following tuple.
 #  ['c','d','a','a','b','b','a']

grade=['c','d','a','a','b','b','a']
print(grade.count('a'))


#Store the above values in a list & sort them 
# from "A" to "D" = ['c','d','a','a','b','b','a']

grade=['c','d','a','a','b','b','a']
grade.sort()
print(grade)



   #1...
student=['shuvam',22.5,22,'kathmandu']
print(student[3])  #(YO MA KATHMANDU PRINT HUNCHA KINA KI LIST KO INDEX MA 0='SHUVAM',21=22.5,2=22,& 3='KATHMANDU' TAI BHAYE RA PRINT GARDA KATHMANDU PRINT BHA KO HO )
print(student)  #(YO PRINT GARDA STUDENT KO SABAI PRINT HUNCHA)

 
#2...
num=[12,22,33,44,39]
print(num[0:2])

#3...
num=[12,22,33,44,39]
print(num[-3:-1])

#4...
num=[22,23,24,25,26]
print(num[-4:-2])

#5...
num=[20,21,22,23,24,25,26,27]
print(num[-5:-1])

#6...
list=[2,1,3]
list.append(4)
print(list)

#7...
friends=['ram','sham','hari']
friends.append('girlfriend')
print(friends)

#8
friends=['shuvam','shujan','sujal']
friends.append('raj')
print(friends)

#9... List . short()
num=[3,4,2,1]
num.sort()
print(num)

#10
num=[10,6,2,3,1,4,5,7,8,9]
num.sort()
print(num)

#11.....List.reverse()...
num=[1,2,3,4,5,6,7,8,9,10]
num.reverse()
print(num)

num=[1,2,3,4,5]
num.reverse()
print(num)

chr=['a','b','c','d','e','f','g']
chr.reverse()
print(chr)


#12..List.insert()
fruits=['apple','banana','cherry']
fruits.insert(0,'orange')
print(fruits)

#13..
chr=["shuvam","binu","swirti","prakriti"]
chr.insert(0,"prakash")
chr.insert(1,"mithila")
print(chr)

#14...
num=[1,2,3,4]  #[0,1,2,3] index number python ma 0 bata suru huncha 
num.insert(4,5) #yo index ko 4 ko thaou ma 5 rakhe ko ho
print(num)

#15.. Another example of index number
num=[1,2,3,4,5,6,7,8]
num.insert(8,9)
print(num)




#16...
a=int(input('enter first number:')) 
b=int(input('enter second number:'))
c=int(input('enter third number:'))
if(a>b and a>c):
    print('first number is largest',a)
elif(b>c):
    print('second number is largest',b)
else:
    print('third number is the largest',c)  








