def c2f (c):
    f = c*(9/5)+32
    return f

def c2f_2 ():
    c = input('Enter a temp in Celcius:')
    c = float(c)
    f = c*(9/5)+32
    print('The temp in fehrenheit is ',f,'.')
    
def SI(P,R,N):
    return (P*R*N)/100

def SI_2 ():
    P = float(input('Enter amount invested:'))
    R = float(input('Enter interest rate:'))
    N = float(input('Enter number of years:'))
    print('The simple interest earned is',(P*R*N)/100)

def csa (A):
    return len(A), sum(A), sum(A)/len(A)

def csa_2(A):
    print('The number of elements in array are',len(A))
    print('The sum of elements of array are',sum(A))
    print('The average of elements of array are',sum(A)/len(A))
