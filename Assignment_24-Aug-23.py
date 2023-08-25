#WAP to take a input from user and find out how many total vowels are present.
x=input("enter string:")
count=0
for i in x:
  if i in 'aeiou':
    count=count+1
print("Total vowel is:",count)

#WAP to take a input from the user and find out whether "a and e" are both present in the string or not.
x=input("enter string:")
if 'a' in x and 'e' in x:
  print("Both a and e is present in string")
else:
  print("Both a and e is not present in string")
  
#WAP to take three variable(length,breadth,height) values from the user.
#if user provide 1 => area of triangle.
#if 2 => area of square.
#3 => area of recatangle.
#4 => take input and find area of circle.
ch=int(input("enter your choice:"))
l=int(input("enter length:"))
b=int(input("enter breadth:"))
h=int(input("enter height:"))
if(ch==1):
  print("Area of Triangle is:",1/2*(h*b))
elif(ch==2):
  print("Area of square is:",4*(l*b*h))
elif(ch==3):
  print("Area of Rectangle is",l*b)
elif(ch==4):
  pi=3.14
  r=int(input("enter radius:"))
  print("Area  of Circle is:",pi*(r*r))

