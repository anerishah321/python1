num = int (input("how many nubers?? "))
toatal_sum = 0

for n in range(num):
    numbers = float(input("enter number: "))
    toatal_sum += numbers

avg = toatal_sum/num
print("avrage is : ",avg)