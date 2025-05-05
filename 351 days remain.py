print('351 Days remain for my first internship')

# Create a set...
#1..
fruits = {"apple", "banana", "cherry"}
print("fruits:", fruits)
fruits.clear()
print("After clear():", fruits)  

#2..
bikes={'suzuki','honda','ducati','fz'}
print('bikes:',bikes)
bikes.clear()
print(bikes)

#3...
chr={'shuvam','shija','raja'}
chr.clear()

#4..
chr={'shuvam','baku','lalla','kajun'}
print(chr.pop())

#5..
a={1,2,3}
b={3,4,5}
c={5,6}
num=a.union(b,c)
print(num)
 
#6...
chr1={'shuvam','shuvam','binu','binu','swikriti'}
chr2={'shuvam','praktiti','prakash','swikriti'}
print(chr1.union(chr2))

#7..intersection
set1={1,2,3}
set2={2,3,4}
set3={4,5,6,7}
set4={7,8,9}
print(set1.union(set2,set3,set4))

#8..

chr={
    'table':['a piece of furniture','list of facts and figures'],
    'cat':'a small animal'
}
print(chr)

#9..
subjects={
    'python','java','c++','python',
    'javascript','java','c++','c'
    }
print(subjects)
print(len(subjects))

#10..
marks={}
x=int(input('enter phy: '))
marks.update({'phy': x})
x=int(input('enter math: '))
marks.update({'math': x})
x+int(input('enter chem: '))
marks.update({'chem': x})
print(marks)

#11...

