'''
this is table method
'''
'''
table=4
value=10
for value in range(1,1+value):
    print(table,'*',value,'=',table*value)
'''
'''table=int(input('enter table'))
value=int(input('enter value'))
for value in range(1,1+value):
    print('{}*{}={}'.format(table,value,table*value))
'''

# x = 10
# def fun1():
#     global x
#     x = 20
#     print('This is fun1 ::', x)
# def fun2():
#     x = 400
#     print('This is fun2 ::',x)
# def fun3():
#     print('This is fun3 ::',x)
#
# print('THIS IS OUT SIDE FINCTION ::',x)
# fun1()
# fun2()
# fun3()





# def ical():
#     for i in range(0,11):
#         yield i
# x = ical()
# for j in x:
#     print(j)

# Python program to check if two
# to get unique values from list
# using traversal

# function to get unique values

# def unique(list1):
#     # initialize a null list
#     unique_list = []
#     # traverse for all elements
#     for x in list1:
#         # check if exists in unique_list or not
#         if x not in unique_list:
#             unique_list.append(x)
#     # print list
#     for x in unique_list:
#         print(x),
# # driver code
# list1 = [10, 20, 10, 30, 40, 40]
# print("the unique values from 1st list is")
# unique(list1)
#
# list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]
# print("\nthe unique values from 2nd list is")
# unique(list2)


# from random import shuffle
# x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
# shuffle(x)
# print(x)


# print(dir())
# #The dir()function used to return the methods and propertites with specific objects, without return the values
# print(help())




# def fun_obj(r):
#     for i in range(r):
#         print(' '*(r - i - 1) + '*' * (2 * i + 1))
# x = fun_obj(9)


#         *
#        ***
#       *****
#      *******
#     *********
#    ***********
#   *************
#  ***************
# *****************
#


# name = input('enter value')
# def poly(name):
#     reversed = name[::-1]
#     if name == reversed:
#         print('polindrum')
#     else:
#         print('no polindrum')
# x = poly(name)

# x= input('enter name ')
# y = x[::-1]
# if x == y:
#     print('polu')
# else:
#     print('no')


# def poly(name):
#     reversed = name[::-1]
#     if name ==reversed:
#         print('polyndrum')
#     else:
#         print('not ploindrum')
# x = poly('das')


# number = int(input('enter number'))
# if number > 1:
#     for i in range(2,number):
#         if number % i == 0:
#             print(number,'not prime')
#             break
#     else:
#         print(number,'prime number')






# names = []
# numbers = []
# tuples = ['pallavi',12,345,'das','manas',8898,'balaji']
# for i in tuples:
#     if type(i) == str:
#         names.append(i)
#     if type(i) == int:
#         numbers.append(i)
# print(names)
# print(numbers)

# def swap(x,y):
#     x,y = y,x
#     print('x--------->',x)
#     print('y--------->',y)
# swap(x = 10,y = 20)

# list1 =  [1,2,3,4,5]
# list2 = ['bala','sundar','das']
#
# list3 = zip(list1,list2)
# print(dict(list3))

# names = ['vijay','owl','pallavi','elephent','bananana','iam','uare','balakumar']
# print(list(filter(lambda name : name[0] in 'a,e,i,o,u',names)))
# x = [i for i in names if i[0] in 'a,e,i,o,u']
# print(list(x))

# names = ['vijay','owl','palavi','elephent','ebananana','iam','uare','valakumar']
# print(list(filter(lambda x : len(x) > 5 ,names)))
# x = [i for i in names if len(i)>4 and i[0]=='v']
# print(list(x))

# def is_anagram(s1,s2):
#     return set(s1) == set(s2)
# s = is_anagram('evils','svile')
# print(s)


# set1 = eval(input('enter value'))
# set2 = eval(input('enter value'))
#
# if set(set1) == set(set2):
#     print('anagram')
# else:
#     print('not anagram')


# l = list(range(10)) + list(range(10))
# print(list(set(l)))

# a,b = 0,1
# n = 10
# for i in range(n):
#     print(b)
#     a,b = b,a+b

#ATM Management system

# username = 'vijay'
# password = 12345
#
# c_username = str(input('enter username'))
# c_password = int(input('enter password'))
#
# if c_username == username and c_password == password:
#     print(
#         '''
#         1.deposite
#         2.withdraw
#         3.ministatement
#         4.exit
#         '''
#     )
#     amount = 50000
#     options = int(input('enter any number'))
#     if options == 1:
#         deposite = int(input('enter amount'))
#         amount +=deposite
#         print('available balance',amount)
#     elif options == 2:
#         withdraw = int(input('enter amount'))
#         amount -=withdraw
#         print('availble balance',amount)
#     elif options == 3:
#         print('########################')
#         print('**********Welcome to SBI ATM***********')
#         print('Availble amount',amount)
#         print('username',username)
#         print('Thanking you')
#     else:
#        if options == 4:
#            print('Exists')


# list = ["1", "4", "0", "6", "9"]
# x = [int(i) for i in list]
# x.sort()
# print(x)




# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1 = range(10)
# A2 = sorted([i for i in A1 if i in A0])
# A3 = sorted([A0[s] for s in A0])
# A4 = [i for i in A1 if i in A3]
# A5 = {i:i*i for i in A1}
# A6 = [[i,i*i] for i in A1]
# A7 = [(i,i*i) for i in A1]
# print('A--------->',A0)
# print('A1---------->',A1)
# print('A2---------->',A2)
# print('A3----------->',A3)
# print('A4---------->',A4)
# print('A5----------->',A5)
# print('A6------------->',A6)
# print('A7------------->',A7)



#polymorphism:
# Impementing diffrent ways
#method overloading
# Single class,same method ,different parementers
#
# class Overriding:
#     def __init__(self,name,age,salary):
#         self.a = name
#         self.b = age
#         self.c = salary
#     def display(self,a,b,c):
#         print('a--------->',self.a)
#         print('b--------->',self.a)
#         print('c--------->',self.a)
# class child(Overriding):
#     def display(self,a,b,c):
#         print('a--------->', self.a)
#         print('b--------->', self.a)
#         print('c--------->', self.a)
#         # print('d--------->', self.d)
# obj = child(1,2,3)
# obj.display(1,2,3)

# from abc import ABC,abstractmethod
#
# class vehical():
#     @abstractmethod
#     def wheels(self):
#         pass
# class Bus(vehical):
#     def wheels(self):
#         print('bus has the 8 wheels')
#     def driver(self):
#         print('bus has 2 drovers')
# class Lorry(vehical):
#     def driver(self):
#         print('Lorry has 1 driver 1 cleaner')
#
# obj = Bus()
# obj.wheels()
# obj.driver()
# obj1 = Lorry()
# obj1.driver()


#####################################################################################################################
'''s = 'vijaykumar'
def findout(s):
    for i in s:
        print(i,'-------->',s.index(i))
findout(s)'''
#####################################################################################################################
