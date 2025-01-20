#Write a Python program to calculate compound interest given principal, rate, and time in years.
ppl=float(input("Enter Principal "))
roi=float(input("Enter Rate of Interest in %"))
time=float(input("Enter Time in years"))
num=int(input("Enter no of times interest is compounded per year"))

roi=roi/100
amt=ppl*(1+roi/num)**(num*time)
cint=amt-ppl
print("Compound Interest is ",cint)