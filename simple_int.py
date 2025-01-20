#Write a Python program that calculates simple interest. Prompt for principal, rate and time, then compute the interest.

ppl=float(input("Enter Principal "))
roi=float(input("Enter Rate of Interest in %"))
time=float(input("Enter Time in years"))

sint=ppl*roi*time/100
print("Simple Interest is ",sint)