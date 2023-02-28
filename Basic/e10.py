## write a programme using function to find greatest of three numbers\

# a = int (input("enter first number: "))
# b = int (input("enter second number: "))
# c = int (input("enter third number: "))

# def maximum(a,b,c):
#     list = [a,b,c]
#     return max(list)

# print(maximum(a,b,c))

## write a programme sor sum of first natural numbers

n= int (input("enter the number: "))

def Sum(n):
    if n <= 1:
       return n
    else:
       return n + Sum(n-1)
print ("sum is: ",Sum(n))    
    
