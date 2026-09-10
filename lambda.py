#Create a lambda function that takes a number and returns its square.
square=lambda x:x**2
print(square(5))
add=lambda a,b:a+b
print(add(5,7))
sub=lambda a,b:a-b
print(sub(7,5))
mul=lambda a,b:a*b
print(mul(5,7))
cube=lambda x:x**3
print(cube(5))
even= lambda a: a%2==0
print(even(5))
odd=lambda b:b%2 !=0
print(odd(5))
largest=lambda a,b:a if a>b else b
print(largest(10,20))
smallest=lambda a,b:a if a<b else b
print(smallest(10,20))
num=lambda a:a+10
print(num(5))
numbers = [1, 2, 3, 4, 5]
r=list(map(lambda x:x*2,numbers))
print(r)
numbers = [1, 2, 3, 4, 5, 6]
r=list(filter(lambda x:x%2==0,numbers))
print(r)
numbers = [2, 7, 3, 9, 4, 8]
r=list(filter(lambda x:x>5,numbers))
print(r)