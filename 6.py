# 6. Write a python script to print first N even natural numbers.

Number=int(input("Enter the Number: "))
for i in range (1,Number*2,2):
    print(i+1,end=" ")
print()
