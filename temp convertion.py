temp = input("Please enter the temperature in Fahrenheit... (eg 45f,29F etc)\n\t")
Tf = int(temp[:-1])
result = int(round((Tf - 32)* 5/9))
print("\nTemperature in celsius is", result, "degree\n")