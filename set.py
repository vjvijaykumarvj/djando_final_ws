
'''l1={'monday','tuesday','friday','saturday','sunday'}
l2={'wednesday','saturday','sunday'}

print(l1 and l2)

l1.remove('saturday')
print(l1)


l2.add('monday')
print(l2)

l1.discard('monday')
print(l1)

l1.pop()
print(l1)

l1.clear()
print(l1)

len(l2)
print('length--->',l2)
print('len--->',len(l2))

s={10,23,21,24,5}
t={10,23,21,24,1,2,3}
#print(s.issuperset(t))
#print(s.symmetric_difference(t))
s.update(t)
print(s)


s={10,20,30,40}
s.remove(20)
print(s)
s.add(50)
print(s)
'''
'''
#zip function
numbers=[1,2,3,4]
letters=['a','b','c','d']
x=zip(numbers,letters)
print(list(x))

#polindram
string=input('enter the name')
if (string == string[::-1]):
    print('its polindram')
else:
    print('its not polindram')
'''


