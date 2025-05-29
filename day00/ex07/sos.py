import sys
lang = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}
if len(sys.argv) > 2:
    print("AssertionError: more than two argument are provided") , exit(2)
elif len(sys.argv) < 2:
    print("AssertionError: less than two argument are provided"), exit(2)
for letter in sys.argv[1]:
    if letter.upper() not in lang:
        print("AssertionError: the arguments are bad"), exit(2)
print(' '.join([lang[letter.upper()] for letter in sys.argv[1]]))