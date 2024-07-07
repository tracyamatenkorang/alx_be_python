# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # Prompt user for input
    temperature = input("Enter the temperature to convert: ")
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    try:
        # Convert input to float
        temperature = float(temperature)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    if unit.upper() == "C":
        # Convert Celsius to Fahrenheit
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result}°F")
    elif unit.upper() == "F":
        # Convert Fahrenheit to Celsius
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result}°C")
    else:
        raise ValueError("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

if __name__ == "__main__":
    main()