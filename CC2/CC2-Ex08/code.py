number = input("What is your height in inches? ")
try:
    height = int(number)
    if height >= 48:
        print("Welcome aboard, enjoy the ride!")
    else:
        print("Sorry, you are not tall enough for this ride")
except:
    print("That is not a valid number")