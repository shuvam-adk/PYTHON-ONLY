print('Day 11 for Better life of my one')

   #1...
student=['shuvam',22.5,22,'kathmandu']
print(student[3])  #(YO MA KATHMANDU PRINT HUNCHA KINA KI LIST KO INDEX MA 1='SHUVAM',2=22.5,3=22,& 4='KATHMANDU' TAI BHAYE RA PRINT GARDA KATHMANDU PRINT BHA KO HO )
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








