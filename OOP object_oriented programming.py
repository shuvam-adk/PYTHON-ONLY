#NEW CHAPTER OOP object_oriented programming.py

print('learn untile you get a job')
#348 day remain only..

#1..string
name='shuvam'
gretting='nameste'
print(name+' '+gretting)

#2..string
name=('shuvam adhikari')
age=(22)
print('my name is:',name)
print('my age is:',age)

#3..float
a=12.2
s=22.32
sum=(a+s)
print(sum)

#4..dictionary, key value
person={'name':'shuvam','age':22}
print(person['name'])

 #5(sets)
unique_number={1,2,3,3,4,5}
print(unique_number)
 
 
 
 #6..file input and output chapter..7
f=open('DAY8.py', 'r')
data=f.read()
print(data)
print(type(data))
f.close()


with open('practice.txt','w') as f:
    f.write('hi my name is  shuvam adhikari ')
    f.write('using python')
    
#7..
class car:
    color='blue'
    brand='mustang' 
car1=car()
print(car1.color)
print(car1.brand)     

#8. 
class Student:
 def __init__(self,name,age):
       self.name = name
       self .age= age
 def show(self):
    print(f'name: {self.name},age:{self.age}')
s1 = Student('shuvam',22)
s2 = Student('kriti',22)
s1.show()
s2.show()
    
    
#9
class car:
  color='red'
car1=car()
print(car1.color)
    
#10
class Car:
    name=('mustang')
    name=('gtr')
    def __init__(self, name, price ):
       self.name= name
       self.price=price
s1=Car('mustang',2000000)
print(s1.name,s1.price)

#11
 #practice again and agaim all type of code you almost forget this commen oscode so try but don't cry 
a=10
s=10
sum=a+s
print(sum)
        
#12..

class Car:
    brand={
        'mustang':{'price':2000,'type':'sport'},
        'gtr':{'price':3000,'type':'super'},
        'porsche':{'price':4000,'type':'classic'}
    }
    def __init__(self , name , color = 'red', year=2020):
       self.name=name
       self.color=color
       self.year=year
       self.price=self.brand[name]['price']
       self.type=self.brand[name]['type']
mustang=Car('mustang')
gtr=Car('gtr',color='blue',year=2021)
porsche=Car('porsche',year=2020)
print(f'{mustang.name}:{mustang.price}')
print(f'{gtr.name} {gtr.type} {gtr.year}')

#13
#347 days left to goo

#1...
name='shuvam'
last_name='adhikari'
sum=(name+' '+last_name)
print(sum)

#2...
 
class Student:
    college_name='hemal college'
    def __init__(self , name , marks):
        self.name=name
        self.marks=marks
        print('new student in data base')
s1=Student('shuvam',22)
print(s1.name,s1.marks)
        
        
s2=Student('kritik',12)
print(s2.name,s2.marks)



#3
class Student:
    def __init__(self,name,marks):   #[99,34,54]
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print('Hi',self.name,'your avg score is:',sum/3 )

s1=Student('shuvam adhikari',[54,86,93])
s1.get_avg()








 
 
 
 
