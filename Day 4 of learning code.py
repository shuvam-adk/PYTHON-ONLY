print("Day 4 of learning code")


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





