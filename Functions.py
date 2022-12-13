'''
def fun_name(name):
    print('hello welcome')
    print('hello welcome {}'.format(name))
    print('hello welcome')
fun_name('vijay')
'''
'''
def Student(name,age,salary):
   print('my name is {}'.format(name))
   print('my age is {}'.format(age))
   print('my salary {}'.format(salary))

Student('vijay',20,35000)
'''

'''def isum(num1,num2):
    add=num1 + num2
    sub=num1 - num2
    mul=num1 * num2
    div=num1 / num2
    return add,sub,mul,div

x,y,z,a=isum(10,20)
print('x----',x)
print('y----',y)
print('z----',z)
print('a----',a)
'''
'''def fun_name(a,b):
    isub=a-b
    return isub
x=fun_name(a=10,b=20)
print(x)
'''
'''
def ical(x , y):
    isum = x + y
    isub = x - y
    imul = x * y
    idiv = x / y
    return isum,isub,imul,idiv
isum,isub,imul,idiv=ical(50,30)
print('isum--->',isum)
print('isub--->',isub)
print('imul--->',imul)
print('idiv--->',idiv)
'''

'''def fun_name(age,name='guest'):
    print('hello welcome',name,age)
fun_name(20)
'''

'''
#swap method in functions:
def fun_name():
    a=int(input('enter a value'))
    b=int(input('enter b value'))
    a,b=b,a
    print(a,b)

fun_name()
'''
# nonlocal functions
'''def parent_f():
    name='vijaykumar'
    def fun1():
        nonlocal name
        name='vijay'
        print('this is fun1!!!,name',name)
    def fun2():
        name='kumar'
        print('this is fun2!!! name',name)
    fun1()
    fun2()
    print('this is parent_f !!!!! name',name)
parent_f()
'''

'''def fun(x):
    return x * x
print(fun(10))

y=lambda x: x * x
print(y(2))
'''
'''
#postional arguments:
def student(name,age,address):
#    print('my name is {},{},{}'.format(name,age,address))
     print('my name is {}'.format(name))
     print('my age is {}'.format(age))
     print('my address is {}'.format(address))

student('vijay','vgr',20) #its correct postions and numbers are must be matches
student('vijay',35000,25) # its wrong postions are changes 
'''

'''#keywords arguments:
def employee(name,age,address):
    print('employee name',name)
    print('employee age',age)
    print('employee address',address)
employee(age=24,name='vijay',address='Bangalore')#this is true postions are not matched but keys are matched
employee(name='vijay',age=25,address='Bangalore')#this is true postions are not matched but keys are matched
'''
'''def fun_name(child1,child2,child3):
    print('the youngest child is {} '.format(child2))
fun_name(child1='vijay',child2='vamsi',child3='sai')
'''
'''
#default argumants:
#we can't pass the arguments or parameters inside of the parantisis is called default arguments :
#postion are must be equal its not equal its leades to error
def student(name,age=24,address='BTM'):  # this condition is true:::
    print('my name is ',name)
    print('my age is ',age)
    print('my address is ',address)
student('vijay')

#SyntaxError: non-default argument follows default argument
def student(age=24,name,address='BTM'): 

    print('my name is ',name)
    print('my age is ',age)
    print('my address is ',address)
student('vijay')
'''

# Arbitary or variable length arguments:::
'''def fun_name(*x):
    print('x--->',x)
fun_name(23,323,2232,3232,32,32,3,232,32,676)
'''
'''def fun(*x,y):
    print('x---->',x)
    print('y---->',y)

fun(10,23,34,232,32,32,4,y='vijay')
'''
'''def fun(y,*x):
    print('x---->',x)
    print('y---->',y)

fun(10,23,34,232,32,32,4)
'''
'''def add(*num):
    sum=0
    for e in num:
        sum=sum+e
    print('sum is ',sum)
add(12,13)
add(12,13,12)
add(12,12,12,12)
'''
'''def greet(*names):
    for e in names:
        print('welcome',e)
greet('vijay','anitha','subramanyam','eswaramma')

def fun_name(*kids):
    print('the youngest child is ',kids[2])
fun_name('sai','ram','das','vijay')

def fun_name(*kids):
    print('the youngest child is ',kids[2]) # by using index numbers
fun_name('sai','ram','das','vijay')
'''

'''
#variable length keywords arguments or arbitary keywords arguments:::
def fun_name(**kwargs):
    print('type(kwargs):::',type(kwargs))
    print('kwargs--->',kwargs)
fun_name(name='vijay',age=25,address='venkatagiri',salary=35000)
'''
'''def fun_name(y,**kwargs):
    print('type(kwqrgs)--->',type(kwargs))
    print('type(y)--->',type(y))
    print(y)
    print(kwargs)
fun_name(y='malli',a=10,b=12,c=14)
'''

'''def fun_name(y,**kwargs):
    print('type(kwqrgs)--->',type(kwargs))
    print('type(y)--->',type(y))
    print(y)
    print(kwargs)
fun_name(a=10,b=12,c=14,y='malli')
'''
'''def fun_name(**kwargs):
    print('the child name is',kwargs['name1'])
fun_name(name1='vijay',name2='sai',name3='ram',name4='raja')
'''

'''
#findout even and odd numbers: by using functions
def number(x):
    x=int(input('enter any number'))
    if x % 2 == 0:
        print('even')
    else:
        print('odd')
number('enter the value')
number('enter the value')
'''
'''num_list=[1,2,3,4,5,6,7,8,9,10]
number=map(lambda x : x * 2 ,num_list)
print(list(number))
'''
'''numlist=[1,2,3,4,5,6,7,8,9,10]
y=filter(lambda x: x%3==0 and x%2 !=0 ,numlist)
print(tuple(y))
'''
'''numlist=[1,2,3,4,5,6,7,8,9,10]
x=filter(lambda x : x % 2 ==0 ,numlist)
print(list(x))
'''

'''name_list=['java','python','casendra','pycharm','pypy','django','pyramid']z=filter(lambda name : len(name)>2 and name[1]=='a' ,name_list )
print(list(z))
'''

'''name_list=['jarva','python','casendra','pycharm','pypy','django','pyramid']
x=[name for name in name_list if len(name)>2 and name[2]=='r']
print(tuple(x))
'''

'''num_list=[1,2,3,4,5,6,7,8,9,10]
final_result=[]
for num in num_list:
    final_result.append(num*3)
print(final_result)

z=filter(lambda num:num*3,num_list)
print(list(z))

names=['vikram','vijay''vinay','vasu','vinay','vamsi','venky']
j=map(lambda x: len(x)>2 and x[1]=='i',names)
print(tuple(j))
'''
# tuenary operator:
'''x=12
y=10
if x>y:
    print('True')
else:
    print('False')
'''

'''names=['mansa','uncle','auntie','iterable','bala','sudan','owel']
z=list(filter(lambda x:x[0].lower() in 'aeiou',names))
print(z)

courses=['java','python','casendra','c++','c','scalal','sasi','ravi']
l=list(filter(lambda course:len(course)>2 and course[2]=='v',courses))
print(l)
'''
'''
names=['malli','ajai','ali','erope','das','pallavi']
x=(name for name in names if name[0] in 'a,e,i,o,u')
print(tuple(x))
'''


