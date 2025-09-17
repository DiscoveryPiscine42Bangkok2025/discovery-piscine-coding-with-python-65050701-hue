import sys

params = sys.argv[1:]

if params:
    print("parameters:")
    for param in params:
        print(f"{param}: {len(param)}")
else:
    print("none")