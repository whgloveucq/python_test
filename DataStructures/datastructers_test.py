stack =[3,4,5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.clear()
print(stack)
stack.insert(0,5)
stack.insert(1,4)
stack.insert(2,10)
print(stack)
stack.sort()
print(stack)
stack.reverse()
print(stack)
stack.pop()
print(stack)
stack.append(9)
print(stack)
from collections import deque
queue=deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
print(queue)
squares=[]
for x in range(10):
    squares.append(x**2)
print(squares)
combas=[(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y ]
print(combas)
items =[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            items.append((x,y))
print(items)
vec = [-4, -2, 0, 2, 4,10]
print([x**2 for x in vec ])
print([x for x in vec if x>=0 ])

print([ abs(x) for x in vec if x>=2 ])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
print([num for num in vec ])
from math import pi  # how to explain
print([str(round(pi, i)) for i in range(1, 6)])

matrix =[[1,2,3],[5,7,8,9,10],[5,7,8,9,10,15,16],[5,7,8,9,10,15,16,18]]
# for row in matrix:
#      for i in range(4):
#           print(matrix[row[i]])
test = [[row[i] for row in matrix] for i in range(3)]
print(test)
transposed =[]
for i in range(3):
    transposed.append([row[i] for row in matrix])
print(transposed)
transpose_t=[]
for i in range(3):
    transposed_t_row=[]
    for row in matrix:
        transposed_t_row.append(row[i])
transpose_t.append(transposed_t_row)
print(transpose_t)
a = [-1, 1,  333, 333, 1234.5 ,66.25,]
del a[0]
del a[0]
print(sorted(a))
# print(a.index(2,3))

str1="good morning , hello"
str2=str1.split()
print(str2)
t=12345,'good',54321
print(t[0],'after',t[1],t[2])
u= t,(1,2,3,4,5)
print(len(u))

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
num=0
for i in basket:
    # for num in range(10):
      print(num,i)
a = set('abracadabra')
print(a)

b = set('alacazam')
print(a-b)
print(a|b)
print(a&b)
print(a^b)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
tel={ 'jack':4098 }
tel['years'] =1980
tel['sape'] =4139
print('look----------------------')
print(tel)
del tel['sape']
print(tel)
print('years' in tel)
print({x:x**2 for x in  (2,4,6) })

dict_test=dict(sape=4139, guido=4127, jack=4098)
print(dict_test)

for i ,v in enumerate(['whgloveu','www','ddd','eedsf','dsdf',]):
    print(i,v)

from math import pi
print([str(round(pi,i)) for i in range(1,6)])

matrix=[[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12]]

b=[ [ row[i] for row in matrix ] for i in range(4)]
print(b)
print(list(zip(*b)))
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[len(a)-1]
a.pop(1)
del(a[:])
print(a)
# tuple 是元组
t = 12345, 54321, 'hello!'
print(t)
print(t[0])
u = t, (1, 2, 3, 4, 5)
print(u)

v = ([1, 2, 3], [3, 2, 1])
empty = ()
singleton = 'hello',
print(len(empty))
print(len(singleton))
print(len(*singleton))
t = 12345, 54321, 'hello!'
x, y, z = t
print(x)
print(y)
print(z)
# 5.4. Sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
j='apple' in basket
print(j)
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a-b)
print(b-a)
print(b|a)
print(b&a)
print(a^b)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
questions=['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
    print('what is your {0} ? it is {1} '.format(q,a))

    for i in reversed(range(1,10,2)):
        print(i)
        basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

print(sorted(set(basket)))
a=3
b=5
c=5
print(a < b == c)
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)
