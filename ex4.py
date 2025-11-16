# celsius to fahrenheit
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(str(celsius )+ " degree Celsius is equal to " + str(fahrenheit )+ " degree Fahrenheit.")

# fahrenhiet to celsius
fahrenheit = float(input("Enter temperature in fahrenhiet: "))
celsius = (fahrenheit-32)/1.8
print('%.2f Fahrenheit is equivalent to: %.2f Celsius'% (fahrenheit ,celsius))