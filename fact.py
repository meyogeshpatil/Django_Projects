def fact(n):
    return 1 if n==0 else n*fact(n-1)
n=int(input('Please enter the number: '))
print( 'factorial of {} is:{}'.format(n,fact(n)))