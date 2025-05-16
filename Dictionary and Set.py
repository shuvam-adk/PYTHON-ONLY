
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


