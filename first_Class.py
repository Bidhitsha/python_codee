"""name='bidhitsha'
age=20
mark=90
print(name, age, mark)
print(type(name))
#arithmetic operations
a=10
b=20
sum=a+b
sub=a-b
div=b/a
mul=a*b
print(a>b)
print(sum,  sub,  div, mul)
#conditional operator
print(not(a>b))

#function
def Cal_sum(a,b):
    sum=a+b
    return sum
print(Cal_sum(5,8))

#input

#a=input("enter number") 
#print(a)
#print(type(a))

a=int(input("enter first number"))
b=int(input("enter second number"))
sum=a+b
print(sum)

#if else
age=20
if(age>=18):
    print("you can vote")
else:
    print("you cant vote")
   
    
mark=80
if mark>=90:
    print("A")
elif mark>=80:
    print("B")
elif mark>=70:
    print("C")
else:
    print("D")
    
#loop
i=5
while i>=1:
    print(i)
    i-=1
    
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print('end')

#range
for i in range(5):
    print(i**2)
    
for i in range(1,10,2):         # 2 ko diff ma 1 dekhi 10 samma aauxa
    print(i)
    
for i in range(0,10,2):
    print(i)
    
#list
list = [20,30,40,'hari']
print(list)
print(type(list))
list[0]=50
print(list)

list.sort()
print(list)
list.append(80)

list=[50,40,70]
list[0]=80
list.append(90)
list.sort()
list.reverse()
print(list)

tup=(50,50,3,20)
print(tup.count(50))
print(len(tup))
print(tup.index(50))
print(tup)


dict={
    "name":"bidhitsha",
    "age":24,
    "mark":[20,40,10,15]   
}
dict["name"]="bidhitsha khadka"
print(dict)
print(dict["name"])

set1={1,2,2,3,"ram", "hari"}
print(len(set1))
set1.add(6)
set1.add("sita")
set1.remove(2)
set1.clear()
set1.pop()
print(set1)

set1={1,2,3,4,5}
set2={1,2,7,8,5}
print(set1)
print(set2)
print(set1.intersection(set2))
print(set1.union(set2))


set1={1,2,3,4,5}
set2={1,2,7,8,5}
froset1=frozenset(set1)
froset2=frozenset(set2)
print(froset1)
print(froset2)
print(froset1.intersection(froset2))
print(froset1.union(froset2))



from collections import deque
dq=deque([1,2,3,2,4,5])
list=[10,20,30]
dq.append(6)
dq.appendleft(0)
dq.remove(2)
dq.extend(list)
dq.insert(2,20)
dq.extendleft(list)
print(dq)

from collections import defaultdict
d=defaultdict(int)
d['a']+=1
print(d)

from collections import defaultdict
name="bidhitsha"
dd=defaultdict(int)
for ch in name:
    dd[ch]+=1
print(dd)

#traditional way
squares=[]
for x in range(5):
    squares.append(x**2)
print(squares)

#list comprehension
squares=[x**2 for x in range(5)]
print(squares)

#dict comprehension
d={x:x**2 for x in range(5)}
print(d)

gen=(x**2 for x in range(5))
for val in gen:
    print(val)


marks=[60,70,80,90]
def s_grade(marks):
    if marks>=90:
        return "A"
    elif 90>marks>=80:
        return "B"
    elif 80>marks>=70:
        return "C"
    else:
        return "D"
grade=map(s_grade, marks)
print("student marks", marks)
print("student grade", next(grade))
print("student grade", next(grade))
print("student grade", next(grade))
print("student grade", next(grade))

#filter
marks=[60,50,45,35]
def fail(marks):
    return marks<50
result= filter(fail, marks)
print("student marks", list(result))
print("failing marks", list(result))

from functools import reduce
num=[2,4,6,8]
def my_sum(x,y):
    return x+y
sum=reduce(my_sum, num)
print(sum)

num=5
square=num**2
print("square is:",square)#yo code

f=lambda x:x**2 #short banauxa mathi ko code lai
print(f(5))"""

#exception_handle

try:
    num=int(input("enter a number"))
    result=10/num
    print("result is:", result)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("invalid input, please enter a number")
    
class NegativeValueError(Exception):
    pass
try:
    num=int(input("enter a positive number:"))
    if num<0:
        raise NegativeValueError("negative values not allowed")
    print("you entered:", num)
except NegativeValueError as e:
    print(e)
except ValueError:
    print("invalid input, please enter a valid number")