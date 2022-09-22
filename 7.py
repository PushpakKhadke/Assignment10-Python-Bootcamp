# 7. Write a python script to print first N even natural numbers in reverse order

Number=int(input("Enter the Number: "))
for i in range (Number*2,1,-2):
    print(i,end=" ")
print()