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



###
###2...
def person(name,age):
    print(f'my name i {name}')
    print(f'i am {age} years old')   
person('shuvam',23)

###3
def val(luck,plane,name,skills,life,members,topic):
    print(f'i am doing {luck} function today')
    print(f'i am planning to contiuue my {plane} days ')
    print(f'my real name was {name}')
    print(f'what to do to improve my skills on my {skills} ')
    print(f'lets continue our {life} life ')
    print(f'i live with my {members} sister ')
    print(f'i am  starting  this {topic} topic from yestarday ')
val('coding',360,'kriti','coding','happy',1,'function')

###4...
def values (name,age,work, when, hobbies,relation_ship):
    print(f'Hi {name}')
    print(f'You are {age} years  old ')
    print(f'You work as a {work} ')
    print(f'From :{when}')
    print(f'Your hobbies is to play {hobbies}')
    print(f'You are {relation_ship}')
values('shuvam',22,'student',2006,'footbal','single',)

###5...
def value (subject,size,brand):
    print(f'i am studing {subject} from yesterday')
    print(f'i have 2 {size} dog breed .')
    print(f'i want to bye {brand}  bike .')
value('DSA','large','bulldog')

##6..
def display_bill(name,money,date):
    print(f'Hello {name} adhikari.')
    print(f'You have to pay your rent Rs :{money} for your rent and others ')
    print(f' You have to pay your wages till the day of {date} :')
display_bill('shuvam','290000','2084/9/16')

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




