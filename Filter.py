'''find out even numbers by using filter functions::::
'''
'''
numbers=[12,13,14,17,18]
s=list(filter(lambda x : x % 2 == 0, numbers))
print('s---->',s)
y=tuple(filter(lambda x : x % 2 !=0, numbers))
print('y--->',y)
'''

from functools import reduce
'''numbers=[1,2,3,4,5,6,7,8,9,10]
z=list[reduce(lambda x,y:x+y ,numbers)]
print(z)
'''


'''numbers=[True,12.4,False,None,12,14,'',[],738,{},()]
x=list(filter(None,numbers))
print(x)
'''
'''numbers=[True,12.4,False,None,12,14,'',[],738,{},(),1]
z=reduce(lambda x,y:x+y,list(map(lambda x:x*2,list(filter(None,numbers)))))
print(z)
'''






