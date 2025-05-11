#1
print('my name is shuvam','i am don')
a=None
b='shuvam'
print(f'i am {a},my name is {b} adhikari')
print(type(a))
print(type(b),(a))
#2
a=12
b=21
sum=(a+b)
print(sum)
#3
age=23
print(type(age))
#4
a,s=2,3
txt='#'
print(a*txt*s)
#5
a,l,d=2,3,4
sda ='$'
print(a*sda*l*d)
#6
a=21
s=20.2       #float value
z=(a*s)
print(z)
print(type(z))    #type nikale ko ho k ho bhan ra

#7
a,s=12,5
c=a//s
print(c)

#8
a,s=12,2
d=a//s            #12 was divided by 2 (2*6=12)
print(d)
print(type(d))
#9
# STRING INPUT 
name=input('name:')    #aba run garda name bhane ra
                    # ani tya name input garne user le 

# INT INPUT=
age=int(input('age:'))    #aba run garda name bhane ra
                    # ani tya NUM input garne user le 

#9.. FLOAT INPUT
price=float(input('price:'))


#10... Write a program that asks 
# for the user's name and prints "Hello, [name]!"
name=input('name:') 
print(f'hello_{name}')


#11..... Write a program that
# asks for a string and prints its length
# Write a program that asks for a string and prints its length
chr=input('string:')
print(f'the string is,{chr}')

#12... Write a program that takes a word and prints it backwards
text=input('enter the text:')
print(text[::-1])

#13... Write a program that checks if a word is a palindrome backward
text=input('enter the text:')
print(text[::-1])

#14
name=input('name:')
print(name)

#15... string value related thing ' '," "
name=input('name:')
print(name)

#15...
#integer related practice number related like ..1,2,3,4,5,11,etc
age=int(input('age:'))
print(age)

#16... for example more if we have to do like 
# print your age 5 times 
chr=input('name:')
age=int(input('the age is :'))

#17...print name and age of your friend
chr=input("name:")
age=int(input('the age  :'))
print(type(age))

#18..
price=(float(input('the price of the apple is:')))
print(price)

#19
price=float(input('the price of the chicken is :'))
print(price)

#20..
land=float(input('the the price of this land is :'))
print(land)
name=input('my name is :')
age=int(input('the age of the character is :'))
print(name,age)

#21
#20..
land=float(input('the the price of this land is :'))
print(land)
name=input('my name is :')
age=int(input('the age of the character is :'))
banana=float(input('the banana of the price is :'))
print(name,age,banana)
