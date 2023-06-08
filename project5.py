def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius=kelvin - 273.15
    return celsius

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
    return fahrenheit

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
    return kelvin

print("Enter the tempr convert:")
print("1. Celsius to Fahrenheit")
print("2.fahrenheit to Celsius")
print("3.Celsius to Kelvin")
print("3.Kelvin to Celsius")
print("4.Kelvin to Celsius")
print("5.Kelvin to fahrenheit")
print("6.Fahrenheit to kelvin")
print("7.Exit")


choice=int(input("Enter a operation to perform:"))
if choice==1:
    celsius=float(input("Enter the temprature:"))
    fahrenheit=celsius_to_fahrenheit(celsius)
    print("The fahrenheit temprature is:",fahrenheit)

elif choice==2:
    fahrenheit=float(input("Enter the temprature:"))
    celsius=fahrenheit_to_celsius(fahrenheit)
    print("Celsius:",celsius)

elif choice==3:
    celsius=float(input("Enter a tempr:"))
    kelvin=celsius_to_kelvin(celsius)
    print("The kelvin temprature is :",kelvin)

elif choice==4:
    kelvin=float(input("Enter the tempr:"))
    celsius=celsius_to_kelvin(kelvin)
    print("The tempr is :",celsius)

elif choice==5:
    kelvin=float(input("Enter a tempr:"))
    fahrenheit = kelvin_to_fahrenheit(kelvin)
    print("The tempr is :",fahrenheit)

elif choice==6:
    fahrenheit=float(input("Enter the tempr:"))
    kelvin=fahrenheit_to_kelvin(fahrenheit)
    print("The tempr is:",kelvin)

elif choice==7:
    print("Have a great day!!!")

else:
    print("Sorry Wrong Entry!!!!")



