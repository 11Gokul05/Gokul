num=int(input("Enter thr number:"))
Count = 0
while(num > 0):
    num=num//10
    Count=Count+1
print("\n Number of Digit= %d" %Count)
