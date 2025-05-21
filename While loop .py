
# ##while loop

#1.
i=1
while i<= 6 :
    print('shvam')
    i+=1
        
#2.. multiple while loop
i=1
a=1
while i<=6 :
 while a<=3 :
    print('adhikari')
    print('shuvam')
    a+=1
    i+=1
    
    
# #3..
a=1
s=1
q=1
while a<=3 :
  print('shuvvam')
  a+=1
while s<=2 :
  print('adhikari')
  s+=1
while q<=2 :
  print('ashu')
  q+=1

#4..
i=1
while i<=4 :
    print('shuvam')
    i+=1
    
###5..
name=input('enter your name :')
while name =='':
    print('you have to enter your name')
    name=input('enter your name :')
print(f'hello {name}')


#6..
 
name=input('enter your name :')
age=(input('enter  age :'))
location=input('location :')
while name == '':
  print('you did not enter  your name')
  name=input('enter your name :')
print(f'hello {name}')
while age == '':
  print('you didnot enter your age:')
  age=(input('enter your age :'))
  age=int(age)
print(f'your age is {age}')
while location=='':
  print('you have to locate your place as well')
  location=input('location :')
print(f'your location is {location}')    
