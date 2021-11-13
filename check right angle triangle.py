print("Write a program to check a triangle is right angle or not")
h=int(input("enter height of triangle:"))
b=int(input("enter base of triangle:"))
hyp=int(input("enter the length of hyp:"))
print("A triangle will be called as right angle triangle if it satisfy pytheogoras theorem")
if (hyp**2==h**2+b**2):
     print("triangle is right angle triangle")
else:
     print("triangle is not a right angle triangle")
