'''
this is ATM MANAGEMENT SYSTEM
'''
user_name='vijay'
password=12345

c_name=str(input('enter user_name'))
c_password=int(input('enter_password'))

if c_name==user_name and password==c_password:
    print('''
    1.deposite
    2.withdraw
    3.ministatement
    4.exit
    ''')
    amount=12000
    option=int(input('enter any option'))
    if option==1:
        deposite=int(input('enter amount'))
        amount += deposite
        print('total amount:',amount)
    elif option==2:
        withdraw=int(input('enter amount'))
        amount -= withdraw
        print('total amount:',amount)
    elif option==3:
        print('<-----ATM----->')
        print('user_name:',user_name)
        print('total amount:',amount)
        print('THANKYOU')
    elif option==4:
        exit()
    else:
        print('enter correct details')