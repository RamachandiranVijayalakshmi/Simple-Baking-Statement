a=input('Enter The Your Name:')
b=input('Enter The Account Number:')
if b=='155401608667':
    print('Accesse Done')
    print('Welcome')
    print('Your Name:',a)
    print('Account Number:',b)
    a=45000
    print('Current Balance:',a) 
    print('Enter Ther Credit Or Debit:')
    b=input()
    if b=='credit':
        print('Enter Your Credit Amount:')
        c=int(input())
        print('Current Amount:',a+c)
    else:
        print('Enter Your Debit Amount:')
        d=int(input())
        print('Current Amount:',a-d)
else:
    print('Wrong Password')


