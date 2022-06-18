import math

PI = math.pi
x = 4

print(x*PI)

print(math.ceil(x))

x = 9.81
print(math.floor(x))

x = 225
print(math.sqrt(x))

x=10
print(math.log(x))

x=3
print(math.factorial(x))

xn = [0,PI/6,PI/4,PI/2,PI]

for i in range(0,len(xn)):
     print(math.sin(xn[i]))
     print(math.cos(xn[i]))
     print(math.tan(xn[i]))

print(math.acos(0))
print(math.asin(1))
print(math.acos(1))

r = 2
x = r*math.cos(PI)
y = r*math.sin(PI)

print(x**2 + y**2)
