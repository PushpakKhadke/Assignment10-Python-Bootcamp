# 5. Write a python script to print first N odd natural numbers in reverse order

Number=int(input("Enter the Number: "))
for i in range (Number*2,0,-2):
    print(i-1,end=" ")
print()
