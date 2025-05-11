first=int(input("enter first:"))
second=int(input("enter second:"))
print("sum=",first)

#DICTIONARY 
person={"name":"shuvam","age":22}
print(person["name"])
person["age"]


#TRY this one 
light=input("light:")
if(light=="read"):
   print("stop")
elif(light=="yellow"):
    print("lock")
elif(light=="green"):
    print("go")
else:
    print("light is broken")     
    
    
    
    
    #ALL THIS CODES ARE MISTAKES OR NOT COMPLETED
       num=1
while num<= 5:
    print(num)
    num +=1
    
#3
num+=1
count=0              #MISTAKE CODE 
while  count<5:
    print(num)
    num+=1


#4...
name='shuvam'
count=0
while count<5:
    print(name)
    count+=1

u=1
while u<=3:
    print('shuvam')
    u+=1
      






marks={}
x=int(input('enter phy: '))
marks.update({'phy': x})
x=int(input('enter math: '))
marks.update({'math': x})
x+int(input('enter chem: '))
marks.update({'chem': x})
print(marks)
