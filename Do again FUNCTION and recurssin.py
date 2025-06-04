
###1....
def val(name,age,area):
    print(f'hi {name}.')
    print(f'you are {age} years old .')
    print(f'you are from {area}')
val('shuvam',22,'imadole')

####2..
def valuess (a,s):
    sum=20+2
    print(sum)
    return sum
valuess(20,2)

##3...
def values (a,s,d):
    sum=2+2+1
    print(sum)
    return sum
values('a','s','d')

# ##4..
def sum(a,s,q):
    sum=1+2+1
    print(sum)
    return sum
sum('a','s','q')

# ####4...average of 3 number
def valu(a,s,q):
    sum=a+s+q
    avg=sum/3
    print(avg)
    return avg
valu(2,3,4)

# ###5.. avg number of 6 numbers
def average (a,s,z,x,d,q):
    sum=a+s+z+x+d+q
    avg=sum/6
    print(avg)
average(1,2,3,4,5,6)

# ##5.1.. avg number of 5
def valu(a,s,d,f,g):
    sum=a+s+d+f+g
    avg=sum/5
    print(avg)
valu(1,2,3,4,5,)

# ###5.2...avg number of 3
def num(a,s,d):
    sum=a+s+d
    print(sum)     ##### this is not compelsery but its ok to do no effect on the code 
    avg=sum/3
    print(avg)
num(2,3,4)
    
# ##5.3...
def number(a,s,d,f):
    sum=a+s+d+f
    print(sum)
    avg=sum/4
    print(avg)
number(2,3,4,5)

# ##6... TYPE OF FUNCTION   YO BATA PADNE AGAIN IN FUTURE 
#   # built in function
#   # user define function


# ###7..write a program to print the length of list
chr=['f','d','a','w','q']
value=(len(chr))
print(value)

# ###8... length 
# chr=(1,2,3,4,5,6,7,8,9,0)
# value=(len(chr))
# print(value)

###9...length
num=[1,2,3,4,5]
int=(len(num))
print(int)

# ###10...waf to print the elements of a list in a single line 
element=[d,s,a,q,w,e]
element=['d','s','a','q','w','e']   ## wrong cha yo
def print_len(list):
  print(len(list))
  def print_len(list):
      for item in list :
          print(item,end='')
  print(element)
  print(element)

###11...WAP to find the factorial of n.(n is the parameter)
n=2
def fact(n):
  fact = 1
  for i in range(1,n+1):
    fact *=1
    print(fact)
fact(6)

###12 convert usd value in nrs value 
def convert (usd_value):
    inr_value=usd_value * 102
    print(usd_value,'usd =',inr_value,'inr')
convert(120)

## canvert usd value in nepali value usd 290
def converted (usd_value):
    inr_value=usd_value*102
    print(usd_value,'usd=',inr_value,'inr')
converted(1203)

##convert usd value 20 in nepali nrs 
def value (usd_value):
  inr_value=usd_value *102
  print(usd_value,'usd=',inr_value,'inr')
value(120) 

#####convert usd value in indian money
def indian(usd):
  indian=usd*83
  print(usd,'USD=',indian,'INDIAN')
indian(120)













