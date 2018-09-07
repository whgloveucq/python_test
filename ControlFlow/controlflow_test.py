# x = int(input("Please enter an integer: "))
x=0
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))
#     # if len(w) > 6:
#     #     words.insert(0, w)
for i in range(5):
    print(i)
for i in range(5,10):
    print(i)
for i in range(0,10,3):
    print(i)
for i in range(-10,-100,-30):
    print(i)
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i,a[i])
print(range(10))
print(list(range(10)))
for i in list(range(10)):
    print(i)
# region Description
for n in range(2,10):
    for x in range(2,n):
        if n%x ==0 :
            print(n,'equals',x,'*',n//x)
            break
        else:
            print(n,'is a prime number')
    # endregion
# region Description
for num in range(2,10):
    if num%2 ==0 :
        print("found an even num ",num)
        continue
    print("found a number",num)
# endregion
# region Description
# # Busy-wait for keyboard interrupt (Ctrl+C)
# while True:
#     print('ok')
#     pass
    # endregion

def fib(n):
    a,b=0,1
    result2=[]
    while a<n:
        print (a,end=' ')
        result2.append(a)
        a,b=b,a+b
    # print(result2)
    return result2
fib(200)
print('\n')
f=fib(20)
f
def ask_ok(prompt,retries=4,complaint='Yes or no,please!'):
    while True:
        ok=input(prompt)
        if ok in ('y','ye','yes','YES'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries=retries - 1
        if retries<0:
            raise OSError('uncooperative user')
        print(complaint)


# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
print('\n')
i = 5
def f(arg=i):
    print(arg,end='\n')
i=6
f()
f(i)
print('do you see ',f())
print(f())

def f1(a,L=[]):
    L.append(a)
    return L
print(f1(1))
print(f1(2))
# print(f(1))
def f2(a,L=None):
    if L is None:
        L= []
    L.append(a)
    return  L
print(f2(2))
print(f2(3))



