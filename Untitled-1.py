def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n* fact(n-1)
print(fact(5))
    









age = 22
print("age")
print(age)
print(str(age))

A,B=5,50
C=A/B
print(C)

A,B=1.5,3
C=A//B
print(C,A/B)

a,s=-12,3
q=a//s
print(q)

#this is the line of comment
""" thie is a multi line comment i guess"""

#Taking input from user & printing it.
name=input("name:")
lastname=input("lastname:")
age=int(input("age :"))
print("My name is",name,lastname,"and i am", age,"years old")

  





def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    
show (5)
    
