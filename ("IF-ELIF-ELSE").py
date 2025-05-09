("IF-ELIF-ELSE")


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





