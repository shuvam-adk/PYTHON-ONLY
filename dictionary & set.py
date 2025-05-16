#Lets do it for you're self for better future of your own..

#Dictionary and set ..
# In Python, the comma (,) is used to separate elements in a list, tuple, dictionary, or set.
#1...
info={
    'first_name':['shuvam','raj'],
    'last_name':['adhikari'],
    'class':['14'],
    'cgpa':9.3,
    'college':['himalaye college'],
    'hobby':['watching movies'],
    'age':22
}
print(info['first_name'])
print(info['age'])
print(info['college'])
print(info['class'])

print(type('first_name'))
print(type('class'))
print(type(info['cgpa']))
print(type('age'))
print(type(info))
print(type(info['last_name']))

# 2...Nested Dictionaries==
student = {
    'student':'shuvam_adhikari',
    'books': {
            'dsa':'34',
            'sad':'29',
            'prob':'31',
            'java':'29',
            'web':'29',
    },
    'gpa' : {
    'books': {
        'dsa':2.3,
        'sad':3.3,
        'prob':2.4,
        'java':2.0,
        'web':2.3
    
        }
   }
}
print(student)
print(type(student))

# 3..

student={
    'name':'shuvam_adhikari',
    'subject name':{
        'dsa':29,
        'sab':25,
        'pro':29,
        'web':29,
        'jave':24,
    }
}
print(student['subject name'])


# 4..
student= {
    'name':'shuvam',
    'marks':{
        'math':22,
        'science':23,
        'dsa':34,
        
    }
}

print(student['name'],student['marks'])

# 5..
bike= {
    'type':'two wheel',
    'kawasaki ninja':{
        'engine':'998cc',
        'power':'310 hp',
        'top speed':'400+km',
    }
    
}
print(bike['type'])
print(bike['kawasaki ninja']['engine'])
print(bike)

# 6..
info = {
    'chr':{
        'name':'shuvam',
        'work':'studying',
        'age':22,
        'location':'ktm', 
    }
    
}
print(info['chr'])

# 7..
father= {
    'work': {
        'police': 'retired',
        'money':{
            'salary':203000,   
        }
    }
}
print(father['work'])




#1...
info={
    "name":"shuvam",
    "subject":"python.py",
    "topics":"dict",
    "age":22,
    "is_adult":True,
    "marks":98.7,
}

print(info)

#2...
dict={
    'name':'shuvam',
    'last_name':'adhikari',
    'cgpa':'5.5',
    'marks':'99,97',
    
    }
print(dict)

#3....
info={
    'name':'shuvam',
    'class':'14',
    'college':'himalaye college of bca',
    'studing':'bca',
}
print(info)

#4..
info={
    "name":"shuvam",
    "last_name":"adhikari",
    "college":"himalaye college of engineering",
    "sem":"3rd sem",
}
print(info)

#5...
null_dict={}
null_dict["name"]="shuvam adhikari"
print(null_dict)

#6...
info={
    "name":"shuvam",
    "last_name":"adhikari",
    "college":"himalaye college of engineering",
    "sem":"3rd sem",
}
print(info)
null_dict={}
null_dict["name"]="Binu"
print(null_dict,info)

#7...NESTED DICTIONARIES =
student={
    'name':'shuvam adhikari',
    'sub':{
        'maths':35,
        'dsa':45,
        'web':55,
    }
}
print(student["sub"])

#8...
college={
    "subject":{
        "probality":"45",
        "dsa":"50",
        "java":"25",
    } 
}
print(college)

  
  
