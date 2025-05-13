("IF-ELIF-ELSE")

#if-elif-else (syntax)

  # if('condition'):
  #     statement1
  # elif('condition'):
  #     statement2
  # else('condition'):
  #     stetement3
    
    #1......
light = input('trafic light: ')
if(light=='red'):
    print('stop')
elif(light=='yellow'):       # this code is good but
    print('look')          #this is not the way of do the code professionally
else:(light=='green')
print('go')
    
#The pro way to do code is like this
  #2...
light= input(' the trafic light : ')
if light == 'red':
    print ('stop')
if light == 'yellow':
    print('look')
if light == 'geeen':
    print ('go')
else: 
    print ( ' Invalid input ' )  # yo vane ko chai user le aru kunai
                                 # hawa  color choice garyo bhane run garda invalid input vancha..
                                 
                                 
    
#3..Problem: Ask the user for their age and print:

    
#  >= 4 → Checks if Messi scored 4 or more (highest priority).

# >= 3 → If not 4+, but 3 or more (so just 3, since 4+ is already handled).

# >= 2 → If not 3+, but 2 or more (so just 2).

# >= 1 → If not 2+, but 1 or more (so just 1).

# else → If none of the above, 0 goals.

# Example Runs:   
    
    
#No.1
light= input("light colour:")
if(light=="red"):
  print("stop")
elif(light=="yellow"):
  print("lock")
elif(light=="green"):
  print("go")
else:
   print("light is broken")
 
#No.2
age=int( input ( ' the age is  : ' ) )
if age <= 13 :
    print( ' he is just a kid ')
elif  14<= age <22 :
    print ( ' he is teen ' )
elif 22<= age <40:
    print('he is a man')
elif  40<= age <=75:
    print('old man')
else:
    print('senior')
    
    
#another example:
goals=int(input('goals:'))
if  goals <=0:
    print('no goal ')
elif  goals <=1:
    print(' not bad ')
elif goals   <=2:
    print('wow')
elif goals  <=3 :
    print('wokaka')
else:
    print('WTF')
    
   #ANOTHER EXAMPLE OF IF ELSE  
messi_scores=int(input('goals:'))

if  messi_scores >=5 <6:
    print('awesome')
elif  messi_scores ==4 :
    print('wow')
elif messi_scores  >=3 :
    print('not bad')
elif messi_scores >=2 :
    print(' ok')
else:
    print('meeeesiiii')
        
    
#Conditional Statements 
    #Grades of Students
   marks=input("marks : ")
   if(marks>=90):
     print("A")
   elif(marks>=80 and marks<90):
     print("B")
   
     print("C")
   else:
     print("D")

#NO.3
     marks=85
     if marks>=90:
       print("Grade A")
     elif marks >=80:  # Cheks if marks are 80 or above  BUT less than 90
       print("Grade B") 
     else:
      print("Grade C")


#No.4  #Food 
light=input('light:')
if light == 'red':
    print('stop')
elif light == 'green':
    print('go')
elif light == 'yellow':
    print('look')
else:
    print('this is nepal')

#no5...
marks = int(input('marks:'))
if marks >=90:
    print('A+')
elif marks >=80 <89:
    print('A')
elif marks >70 <=79:
    print('B+')
elif marks >60 <=69:
    print('B')
elif marks >50 <=59:
    print('c+')
elif marks >39 <=49:
    print('just pass')
else:
    print('fail')
#5...
light=input('traffic light:')
if light == 'red':
    print('stop')
    print('check his licence')
elif light == 'yellow':
    print('look')
    print('go carefully')
elif light == 'green':
    print('look')
else:
    print('ckeck his  licence')
  
marks= int(input('marks of students:'))
if marks >=90:
    print('A+')
elif marks >=80 <90:
    print('B+')
elif marks >=70 <80:
    print('C+')
else:
    print('study hard')
      
# A=5&G=M ('Solve the problem')   <<<<< xaina aako ajai ni>>>>>>

# a=int(input('a:'))
# g=input('m/f:')
# if((a==1 or a==2) and g=='m'):
#     print('fee is 100 ')    
# elif(a==3 or a == 4 or  g== 'f'):
#     print('fee is 200')
# elif(a==5 or g == 'm'):
#     print('fee is 300')
# else:
#     print('no fee')
    

money=100
money=money+50
print(money) 


m=20
m= (m+20)
print(m)

num1=int(input('first num:'))
num2=int(input('second num:'))
print('sum:',num1+num2)

name=input('name:')
age=int(input('age:'))
marks=float(input('marks:'))
print('my name is:',name)
print(' i am :', age )
print('marks:',marks)

#sum values=
num1=int(input('first num:'))
num2= int(input('sec num:'))
sum=(num1+num2)
print(sum)

#WAP to input 2int num,a&b. print true if
# a is greater than or equal to b in not. print false ..
a=int(input('a:'))
b=int(input('b:'))
if a >=b:
    print('true')
elif b >=a:
    print('false')
else:
    print('error')





marks=85
if marks>=90:
  print("Grade A")
elif marks >=80:  # Cheks if marks are 80 or above  BUT less than 90
  print("Grade B") 
else:
  print("Grade C")
   


   #WHAT IS THE MISTAKEN ON THIS CODE FINDOUT LATER
   #LEARNING DAY 4.0
num1=int(input("5:"))
num2=int(input("5:"))
sum=num1+num2
print("Sum:",sum)


marks=80
if(marks>=90):
    grade= "A"
elif(marks >=80 and marks < 90):
    grade="B"
elif(marks >=70 and marks < 80):
    grade="C"    

#...

#practice questions 
#1...
name=input('name:')
print(len('name'))

# #2..
chr=' paisa koo sign $,$,$,$ ho k ho $ ho k cha re $ cha ho good'
print(chr.count('$'))

#3...
age=int(input('age : '))
if age >=22:
    print('he can have a bike licence ')
elif age <21:
    print('he cant have licence')
else:
    print(' political back ground ')

#5...
age=int(input('His age is:'))
if age >=21 <=22:
    print('he is older son')
elif age >19 <=20:
    print ( ' yonger son')
elif age  >=17 <=18:
    print(' he is teen')
else:
    print('we have no child')

#no...---
food=input("food:")
eat="yes" if food=="cake"else "no"
print(eat)
 
 
 #short and meaningfullvariable name
num1=int(input("50:"))
num2=int(input("50:"))
sum=num1+num2
print("Sum:",sum)  #ONLY THIS IS GOING TO PRINT ON THE TERMINAL 


#CALCULATE SIMPLE INTEREST
p=float(input("P:"))
r=float(input("r:"))
t=float(input("t:"))
si=(p*r*t)/100
print("SI",si)





