age=22      
old=True
a=233
print(type(old))
print(type(a))


a = 5
b = 5
sum = a + b
print(sum) 



#No.4  #Food 
food=input("food:")
eat="yes" if food=="cake"else "no"
print(eat) 


    # Type conversion

a=1
a=int(a)
print(type(a))

# Convert the string "25" to an integer and print its type.
a=25
a=int(a)
print(type(a))
# Convert the string "-100" to an integer and print its type.
b=-100
b=int(-100)
print(type(b))
# Convert the string "0" to an integer and print its type.
a=0
a=int(0)
print(type(0))
# Convert the string "3.14" to an integer. What happens?
a=3.14
a=int(3.14)
print(type(a))
# Convert the string "12a" to an integer. What happens?
a='12a'
a=int(12)     #then i have to remove 'a' and code with 12 insted ?
print(type(a))
# Convert the string " 7 " (with spaces) to an integer. Does it work?
a=7
a=int(7)
print(type(a))
# Convert the string "1_000" to an integer. Does it work?
a=1_000
a=int(1_000)
print(type(a))
# Convert the string "0b1101" (binary) to an integer using base 2.
a=0b1101
a=int(a)
print(type(a))
# Convert the float 10.5 to an integer and print its type.
a=10.5
a=int(10.5)
print(type(a))

# Convert the boolean True to an integer and print its type.
boolean_value=True
integer_value=int(boolean_value)
print(integer_value)
print(type(integer_value))

# Convert the boolean False to an integer and print its type.
boolean_value=False
integer_value=int(boolean_value)
print(integer_value)
print(type(integer_value))

# Convert None to an integer. What happens?

# Convert the string "0xFF" (hexadecimal) to an integer using base 16.
hex_string='0xff'
integer_value=int(hex_string , 16)
print(integer_value)

#Convert the string "00050" to an integer and print its type.
string_value='00050'
integer_value=int(string_value)
print(type(integer_value))

#Level 1: Basic Conversions

# Convert "123" to an integer and print it.
int=123
print(int)

# Convert "45.67" to a float and print it.
float=45.67
print(float)

# Convert 100 to a string and print its type.
number='100'
string_name=str(number)
print(type(string_name))


