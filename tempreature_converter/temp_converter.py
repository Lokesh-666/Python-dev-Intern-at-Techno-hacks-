def CelsiusToFahrenheit(amount):
    # Convert Celsius to Fahrenheit
    convertedAmount = amount * 9 / 5 + 32
    return convertedAmount

def FahrenheitToCelsius(amount):
    # Convert Fahrenheit to Celsius
    convertedAmount = (amount - 32) * 5 / 9
    return convertedAmount       

def main():
    # Welcome message
    print("Welcome to Temperature Converter")
    
    # Get the temperature value to convert
    amount = float(input("Value of temperature that you wish to convert: "))
    
    # Get the unit of the temperature
    unit = str(input("What is the unit of the temperature (C/F)? "))
    
    # Convert and display the result based on the input unit
    if unit.upper() == 'C':
        convertedAmount = CelsiusToFahrenheit(amount)
        print(amount, "℃ converted to ℉ is", convertedAmount)

    elif unit.upper() == 'F':
        convertedAmount = FahrenheitToCelsius(amount)
        print(amount, "℉ converted to ℃ is", convertedAmount)
    else:
        # Handle invalid input
        print("Invalid Input! Please choose C/c or F/f")

# Run the main function
if __name__ == "__main__":
    main()
