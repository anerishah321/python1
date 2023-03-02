# find a factorial number of n
#n! = n * (n-1) * (n -2) * (n-3) .....1

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print (fact(7))   