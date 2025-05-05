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




