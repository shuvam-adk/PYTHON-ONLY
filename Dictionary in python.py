#Dictionary in python...
#1...
str='shuvam adhikari'
chr=str[6:15]
print(chr)

#2..
movie = {
    'chr':{
    'word':'pasaa',
    'looks':'sexy',
    'villain':'chettri,don',
}
  }
print(movie)

#A book with items (key) & price(value):::
book={
    'death note': 550,
    'one piece':1120,
    'bleach':500,
    'high school dxd':50,
}
price=book.values()
print(price)

#Dict.items()...

book={
    'death note': 550,
    'one piece':1120,
    'bleach':500,
    'high school dxd':50,
}
print(book.items())


friends={
    'age':22,
    'height':'6ft',
    'weight':81,
}
print(friends.items())


family={
    'members':4,
    'names':['shuvam','prakriti','swikriti','mithila',],
    'age':{
        'shuvam':22,
        'prakriti':28,
        'swikriti':24,
        'mithila':51
    },
    'weight':{
        'shuvam':81,
        'prakriti':90,
        'swikriti':50,
        'mithila':50,
    }
}

print(family.items())







