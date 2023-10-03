#! python3

"""
In math, if a quadratic equation is in the format
ax^2 + bx + c = 0, the discriminant can be calculated as
b^2 - 4 * a * c
If the discriminant is a perfect square, the equation can
be factored.  Furthermore, if the discriminant is negative,
then the equation has no solutions (not used in this assignment).
Have the user enter in values for a, b and c and then 
tell them if the equation can be factored.

Inputs:
- 3 numbers (a, b, c)

Outputs:
- "the equation can be factored"
- "the equation can not be factored"

Example:
Enter a: 1
Enter b: 4
Enter c: 4
the equation can be factored

Enter a: 1
Enter b: 4
Enter c: 8
the equation can not be factored

"""

a = input("Enter side a:")
a = int(a)
b = input("Enter side b:")
b = int(b)
c = input("Enter side c:")
c = int(c)
y = b ** 2 - 4 * a * c
x = y ** 0.5
x = str(x)
print(x)
if "." in x :
 print("that can not be factored")
else:
 print("that can be factored")
