'''local non local'''
'''
def fun():
    name='vijay'
    def fun1():
        nonlocal name
        name='kumar'
        print('my fun1 name is :::',name)
    def fun2():
        print('my fun2 name is :::',name)
    def fun3():
        print('my fun3 name is :::',name)
    fun1()
    fun2()
    fun3()
    print('my fun name is :::', name)
fun()
'''

'''def fun(name,age,address):
    print('my name is ',name)
    print('my age is ',age)
    print('my address is ',address)
fun('vijay',20,'vgr')
'''


