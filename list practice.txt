s="python"
rev=""
for ch in s:
    rev=ch+rev
print(rev)

s="programming"
for ch in s:
    if s.count(ch)==1:
     print(ch)
     break

s="madam"
if (s==s[::-1]):
    print("True")
#Find the Maximum and Minimum Elements in a List
s=[3, 1, 4, 1, 5, 9]
print(max(s))
print(min(s))
#Remove Duplicates from a List
s=[1, 2, 2, 3, 4, 4, 5]
#1
s = [10, 20, 30, 40, 50]
for num in s:
    print(s)
#2
s = [10, 25, 7, 40, 15]
print(max(s))
#3
s = [10, 25, 7, 40, 15]
print(min(s))
#4
s = [10, 25, 7, 40, 15]
print(len(s))
#5
s = [10, 20, 30, 40]
print(sum(s))
#6
s = [10, 20, 30, 40, 50]
print(s[0])
#7
s = [10, 20, 30, 40, 50]
print(s[-1])
#8
s = [1, 2, 3, 4, 5]
s.reverse()
print(s)
#9
s = [1, 2, 2, 3, 4, 4, 5]
unique=list(set(s))
print(unique)
#10
s = [40, 10, 30, 20, 50]
s.sort()
print(s)
#11
s = [1, 2, 2, 3, 2, 4]
print(s.count(2))
#12
s = [10, 20, 30, 40]
print(30 in s)
#13
s = [1, 2, 3, 4, 5, 6, 7, 8]
for i in s:
    if i % 2 != 0:
        print(i)
#14
s = [1, 2, 3, 4, 5, 6, 7, 8]
for i in s:
    if i%2==0:
        print(i)
#15
s = [10, 25, 7, 40, 15]
s.sort()
print(s[-2])
#16
s = [10, 25, 7, 40, 15]
s.sort()
print(s[1])
#17
s = [1, 2, 2, 3, 3, 3, 4]
for i in s:
  s.count(i)
  print(i)
