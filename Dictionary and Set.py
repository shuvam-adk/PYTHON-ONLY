## Now Sets in python  ..

# Lets practice
##1..store following word meaning in python dictionary:
table={
    'futniture':'a piece of furniture',
    'list ':'of facts and figures',
    'animal':{
    'cat':'a small animal',
    }
}
print(table)

##2..You are given a list of subject for students. assume one classroom is required
# for 1 subject how many classroom are needed by all students ..

cls1= {
    'python','java','c++','python','java'
    'python','java','c++','c' }
print(len(cls1))


#3.. WAP to enter marks of 3 students from the user and store them in dictionary. start with an empty dictionary and add one
# bye one use subject name as key &marks as value 
marks={}
a=(int(input('enter the marks :')))
marks.update({'math':a })
b=(int(input('enter the marks: ')))
marks.update({'dsa':b })
c=(int(input('enter the marks : ')))
marks.update({'sad': c })
print(marks)


##4.. Figure out a way to store 9 & 9.0 as seprated values in the set
# (you can take help of built in data types)
num=(9,'9.0')
print(num)


## 1..
# num={1,2,3,4,5}
# um={1,2,2,3,2}
# print(num-um)


#2..replaced elements stored only once .
num={1,2,3,4,5}
print(num)
print(type(num))
print(len(num))

#3..Set methods:--  We have to do curle brackets on sets
#set.add(..)
chr={'a','s','d','q'}
print(chr)
chr.add('v')
print(chr)

marks={}
a=(int(input('enter the num:')))
marks.update({'maths': a})
s=(int(input('enter the number :')))
marks.update({'sad':s})
d=(int(input('enter the num :')))
marks.update({'web':d})
print(marks)

#WAP to enter marks of 3 students from the user and store them in 
# dictionary. start with an empty dictionary and add one
# bye one use subject name as key &marks as value 

marks={}
shuvam=('enter the marks :')
marks.update({'java':shuvam})
shuvam=('enter the marks :')
marks.update({'pro':shuvam})
shuvam=('enter the marks :')
marks.update({'web':shuvam})
print(marks)
print(type(marks))








#4..
num={1,2,3,4,5,6}
print(num)
num.add(7)
print(num)

##5...SET.remove(..)
chr={'a','s','d','f','g'}
print(chr)
chr.remove('a')
chr.remove('d')
chr.remove('g')
print(chr)

#6...
num={1,2,3,4,5,6,7,8,9,0}
print(num)
num.remove(0)
num.remove(5)
num.remove(1)
num.remove(9)
print(num)

##.7..SET.CLEAR() it remove all the elements from the code ..
chr={'a','s','z','x','c'}
print(chr)
chr.clear()
print(chr)

#8..
element={1,2,3,4,5,6,7}
print(element)
element.clear()
print(element)

## 9..Set.pop() It runs the random value frome code..
chr={'q','w','e','r'}
chr.pop()
print(chr)

##10..
num = {1,2,3,4,5,6,7,8 }
num.pop()
print(num)

##11..
num={1,2,3,4}
num.pop()
print(num)


#12..      SEt methods  ( number haru combine gare ra print garne  garda cha like 1,2,3,4,5)etc.
# SET.UNION()  this in the combination of the two values

num1={1,2,3,4,5}
num2={2,2,3,4,5,6,7,8}
print(num1.union(num2))

#..
num1={1,2,3}
num2={2,3,4,5}
print(num2.union(num1))

##...
num1={0,9,8,7,6}
num2={0,9,8,6,5,4,3,3,2,1}
print(num1.union(num2))



#.13..Set.intersection  (yo ma common value lai print garcha ) for example;;
#it prints the common value
num1={1,2,3,4,5}
num2={2,4,6,7,8}
print(num1.intersection(num2))

#..
chr={'a','s','d','z'}
ele={'a','s','c','v'}
print(chr.intersection(ele))

##..
n={1,2,3,3,4,5}
q={1,7,5,4,8}
print(n.intersection(q))
# 1..
father= {
    'work': {
        'police': 'retired',
        'money':{
            'salary':203000,   
        }
    }
}
print(father['work'])

#2..
son = {
    'name':'shuvam',
     'studying': {
        'himalaya':'3rdsem',
        'books':{
            'maths':{
                'marks':29,
            'subject': {
                'dsa': {
                'marks':30,
                'subject': {
                'java':{
                    'marks':39,
                        'subject':{
                            'sad':{
                                'marks':28
                            }
                        }
                    }
                }    
            }   
            }
            }
        }
            
    }
        
}

print(son)


# 3...

chr= {
    'name':'shuvam',
    'work':'unemployed',
    'age': '22',
    'hobby':{
        'game':['footbal','cricket','video game'],
        'another hobby':{
            'sketch':'animated drawing',
            'from':'hetaude',
            
        }
    }
    
}
print(chr)
print(type(chr))
print(chr['age'])
print(chr['work'])
print(chr['name'])
print(chr['hobby'])


#1..my dict.update(new dict) topic...
student={
    'name':'shuvam',
    'subject':{
        'phy':29,
        'chem':67,
        'math':30,
    }
}
student.update({'city':'kathmandu','nick name':'kriti','age':22,})
print(student)

#2..
game={
    'name':['gta','hunter x hunter','one piece'],
    }
{
    'level':1,
    'level':2,
    'level':3,
}
game.update({'city':['qu city','aduto','year: 2023']})
print(game)

#3..set in python...
chr={1,2,2,2,'hello','world','world',4}
print(chr)
print(len(chr))

#4.. 
dinner={
    "masu":{"khashi ko masu","khukura ko masu","buffalo ko masu"}
}
invitedguests={"mithila","prakriti","binu","prakash","swikriti"}
dinner["masu"].add("changra ko masu")
invitedguests.add("vanja babu")
print(dinner,invitedguests)


person = {'name': 'Alice', 'age': 25}
del person['name']  # Deletes 'name peae'
print(person)

num={22,25,26,27}
num.remove(25)
print(num)


