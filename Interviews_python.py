''' find out the polindram or not  '''

'''string = input('enter name ')
if string == string [::-1]:
    print('its polindram')
else:                                  # finding the  polindram or not using string 
    print('its not polindram')


def fun_name(string):
     reversed=string[::-1]
     if string==reversed:
         print('its polindram')        #    find polindram by using functions
     else:
         print('not polindram')
fun_name('nanan')
'''

'''#check if list contains integer x in or not
list=[1,2,3,4,5,6,7,8,9,10]
print(5 in list)                      #check if list contains integer x in or not
print(12 in list)
'''

'''#owel (or) 'a,e,i,o,u' in list or not find out:::
names=['malli','ajai','ali','erope','das','pallavi']
x=[name for name in names if name[0] in 'a,e,i,o,u']      #oweal (or) 'a,e,i,o,u' in list or not find out::
print(list(x))
'''
'''
names=['malli','ajai','ali','erope','das','pallavi']
y=filter(lambda x:x[0] in 'a,e,i,o,u',names)              #oweal (or) 'a,e,i,o,u' in list or not find out::  
print(tuple(y))
'''

# find the lenght of the charecter and postion of charecter
'''names=['malli','ajali','ali','erope','das','pallavi']
z=list(filter(lambda x:len(x)>4 and x[4]=='i' ,names))     # find the lenght of the charecter and postion of charecter
print(z)

names=['malli','ajali','ali','erope','das','mallavi']
x=[name for name in names if len(name)>4 and name[0]=='m']   # find the lenght of the charecter and postion of charecter
print(list(x))
'''


'''#zip function using
list1=[10,12,14]
list2=['a','b','c']             #zip function using
list3=zip(list1,list2)
print(list(list3))
'''

'''#separete the string and intiger in list:::
numbers=[]
names=[]
list=['vijay','manas',12,5454,33,'raja',434,'das']
for e in list:
    if type(e)==str:
        numbers.append(e)
    if type(e)==int:                                #separete the string and intiger in list:::
        names.append(e)
print('numbers',numbers)
print('names',names)
'''

#how to swap of 2 numbers:::
'''x=20
y=12
temp=x
x=y
y=temp
                                                           #how to swap of 2 numbers:::
print('the x value is {}'.format(x))
print('the y value is {}'.format(y))

# byusing input method in swap 2 values:::
x=input('enter any number')
y=input('enter any number')

x,y=y,x                                        # byusing input method in swap 2 values:::
print('x--->',x)
print('y--->',y)
'''

'''#Check if 2 string are Anagram:
def is_anagram(s1,s2):
    return set(s1)==set(s2)                        #Check if 2 string are Anagram:
s=is_anagram('twist','wtsti')
print(s)
'''

'''#Remove the all duplicate from the list :::
s=list(range(10))+list(range(10))
nd=list(set(s))                                        #Remove the all duplicate from the list :::
print(nd)
'''

'''#Compute the first  n Fibonacci numbers: 
a,b=0,1
n=10
for i in range(n):                                     #Compute the first  n Fibonacci numbers:
    print(b)
    a,b=b,a+b
'''


numbers=[1,2,3,4,5,6]
first,second,third,*other = numbers
print(first)
print(other)









