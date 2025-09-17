import sys

if len(sys.argv) == 2:
    text = sys.argv[1]
    result = ""
    for char in text:
        if char == 'z':
            result += "z!"
    print(result if result else "none")
else:
    print("none")