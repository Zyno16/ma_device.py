a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
if b > a:
    min =a
else:
    min = b

for i in range(1,(min+1)):
    if a % i ==0 and b %i == 0:
            max_devise = i
print("the max device is",max_devise)
