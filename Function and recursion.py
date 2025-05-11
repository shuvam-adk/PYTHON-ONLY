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




