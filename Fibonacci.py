#Print the first n numbers of the Fibonacci sequence using a for loop.

num=int(input("Enter a no of terms in fibonacci series"))
a=0
b=1
for i in range (1,num+1):
    fibo=a+b
    a=b
    b=fibo
    print(fibo)