import sys
if len(sys.argv) < 2:
    exit(0)
if len(sys.argv) > 2:
    print("Assertion Error: more than one argument are provided")
    exit(0)
try:
    n = int(sys.argv[1])
    if n % 2 == 0:print("I'm Even.")
    else:print ("I'm Odd.")
except ValueError:
    print("Assertion Error: argument is not an integer")
    exit(0)