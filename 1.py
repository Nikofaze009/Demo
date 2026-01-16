import sys

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 1.py <celsius_temperature>")
        print("Using default value: 25°C")
        c = 25.0
    else:
        c = float(sys.argv[1])
    print("Fahrenheit:", celsius_to_fahrenheit(c))
