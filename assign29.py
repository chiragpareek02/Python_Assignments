'''Create a function to take 2 value and check the datatype
- If the data type is int then
    create the number raise to power of second number and return the value'''
def pow(a,b):
    if(type(a) is int and type(b) is int):
        power=a**b
    print("Power is:",power)
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
pow(a,b)

'''Create a function taking a string as a input
    if the word in the string contain any vowel remove that word from
the string'''

def func(x):
    char="aeiouAEIOU"
    mod_string=''.join([i for i in x if i not in char])
    return mod_string
x=input("Enter a string:")
func(x)

'''Take a input as string if the word contain letter "a" and "e" then adding "ing"
in the last of the word otherwise add letter "RA" at the starting of the word
'''
def add_str(x):
    if 'a' in x and 'e' in x:
        x=x+'ing'
    else:
        x='RA'+x
    return x
x=input("Enter string:")
add_str(x)

'''create square and pyramid
****
*  *
*  *
****
'''
def pattern(x):
    for i in range(x):
        if i == 0 or i == x - 1:
            print("*" * x)
        else:
            print("*" + " " * (x - 2) + "*")
x = int(input("Enter size:"))
pattern(x)

'''
   *
  * *
 * * *
* * * *
'''
def pattern_triangle(x):
    for i in range(1, x + 1):
        spaces = " " * (x - i)
        stars = "* " * i
        print(spaces + stars)
x=int(input("Enter size:"))
pattern_triangle(x)

''' Take 2 input from the user as parameter and find it's LCM of two numbers
    And return the LCM of both the numbers
    3,5
'''
def lcm(a, b):
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
lcm(a,b)

'''Find the HCF of two number and return the value
'''
def hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
hcf(a,b)