import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    cel = (sys.argv[1])
    ferh = (cel * 9/5) + 32
    print(f"{cel} Celsius is {ferh} Fahrenheit")