#function & recursion 
#function is a block of reusable code place() after the function 
### name to invoke it 

##1..
def happy_birthday(name,age):
    print(f'happy birthday {name} bro ')
    print(f'you are {age} years old')
    print('have a nice day')
    print()
happy_birthday('shuvam',22)
happy_birthday('kriti',23) 

##2...
def study(clas,section):
    print(f'Hi i study in class {clas}')
    print(f'Hi i am in {section} section')
study(14,'b')
    
##3..
def family_members(name,age,gender):
    print(f'Hi my name is {name}')
    print(f'i am {age} years old ')
    print(f'i am {gender}')
    print()
family_members('shuvam',22,'male')
family_members('raj',22,'male')  

###4..    
def person(name,work,married,colour,subject):
    print(f'His name is {name} adhikari')
    print(f'He work as a {work}')
    print(f'He is happy and {married}')
    print(f'he is little {colour}')
    print(f'some cubject marks {subject}')
person('shuvam','software deveplopr','single','little dark','subjects')
name = {
    'shuvam':{
    'age':22
    },
    'book': {
        'name':'dsa',
       'name':'probability',
        'name':'web',
    },
    'marks':{
        'dsa':25,
        'probability':28,
        'web':26,
    },
    'colour':'little black',
}
    
print(name)


########


print('my first intern remaning day 349')
#Function and recursion 
#1..
def calc_sum(a, b):
    sum = a + b 
    print(sum)
    return sum
calc_sum(12, 17)


def greet(name):
    print(f"Hello, {name}")

greet("Alice")  # Output: "Hello, Alice!"
def multiply(x, y):
    return x * y

topping = "Ham"  # Changed variable name from 'filling' to 'topping'
message = f"Turkey sandwich with {topping}"  # Still uses f"
print(message)  # Output: "Turkey sandwich with Ham"

#function defination
def calc_mul(a,s): #parameters
    return a*s
multiply = calc_mul(9,2) #function call; arguments
print(multiply)

count=0
def print_hello():
    print('hello')
while count< 5:
    print_hello()
    count+=1


chr='shuvam'
len(chr)
print(len(chr))


def show(a):
    if(a==0):
        return
    print(a)
    show(a-1)
show (5)


#...
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n* fact(n-1)
print(fact(5))
    
    
    
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))




