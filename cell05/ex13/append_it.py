import sys

params = sys.argv[1:]

if params:
    for word in params:
        if word.endswith("ism"):
            print(word)
        else:
            print(word + "ism")
else:
    print("none")
