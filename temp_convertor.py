#Write a Python program to convert a temperature from Celsius to Fahrenheit and vice versa.

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice=int(input("Choose 1 or 2"))
if choice==1:
    cel=float(input("Enter temperature in °C"))
    fahr=(cel* 9/5) + 32
    print(f"{cel:.2f}°C in fahrenheit is {fahr:.2f}°F")
elif choice==2:
    fahr=float(input("Enter temperature in °F"))
    cel=(fahr- 32) * 5/9
    print(f"{fahr:.2f}°F in Celsius is {cel:.2f}°C")
