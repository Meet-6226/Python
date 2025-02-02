#Print a diamond-shaped pattern of stars with a width given by the user 

width=int(input("Enter the width in odd number"))
if width%2==0:
    print("Pls enter a width in odd number")
else:
    for i in range(1, width + 1, 2):
        space=(width-i)//2
        print(" "*space+"*"*i)
    for i in range(width-2,0,-2):
        space=(width-i)//2
        print(" "*space+"*"*i)
    