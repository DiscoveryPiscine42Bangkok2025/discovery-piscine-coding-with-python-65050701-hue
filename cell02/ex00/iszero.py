
while True:
    num = input("?> ")

    try:
        num = float(num)
        if num == 0:
            print("This number is equal to zero.")
        else:
            print("This number is different from zero.")
        break 
    except ValueError:
        print("Invalid input. Please enter a number.")


