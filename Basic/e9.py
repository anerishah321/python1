## write a programme to multiplication table of given number

# number = int(input("input your number: "))
# i = 1
# # for i  in range(1,11):
# #     print(str(number)+"*"+str(i)+"="+str(number*i))
# while i < 11:
#    print(str(number)+"*"+str(i)+"="+str(number*i))
#    i += 1
 


##Write a programme too greet the persion whose name start with a 

# l1=["aneri","aarchi","diksha","abhi"]
 
# for name in l1:
#     if name.startswith("a"):
#         print("hello",name)


##write a programme to find a number is even or odd
# for  i in range(0,50):
#     if i%2 == 0:
#         print("its odd",i)
#     else:
#         print("it's even",i)

##find factorial of given number 
##what is factorial
##5!= 1*2*3*4*5 

# num = int (input("Enter your number: "))
# factorial= 1
# for i in range (1,num+1):
#    factorial = factorial*i
# print(f"The factorial is {factorial}")

## make pattern as follow

rows = int (input("rows you want: "))

for i in range (1, rows+1):
    for j in range (1, i+1):
        print("*",end=" ")
    print("\r")    


   