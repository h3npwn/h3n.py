import sys
from string import punctuation
if len(sys.argv) > 2:
    print("AssertionError: argc  > 2 !!! ")
    exit(0)
elif len(sys.argv) == 2:
    mes = sys.argv[1]
else:
    print("ur text count ??????????")
    mes = sys.stdin.readline() #!!!
spaces = [' ', '\n', '\t']
print(f"The resulta lmohim !!  {len(mes)} characters:")
print(f"{sum(1 for c in mes if c.isupper())} upper letters")
print(f"{sum(1 for c in mes if c.islower())} lower letters")
print(f"{sum(1 for c in mes if c in punctuation)} punctuation marks")
print(f"{sum(1 for c in mes if c in spaces)} spaces")
print(f"{sum(1 for c in mes if c.isdigit())} digits")