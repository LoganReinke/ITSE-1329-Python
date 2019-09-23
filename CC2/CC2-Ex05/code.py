try:
    hours = input("Enter hours: ")
    rate = input("Enter rate: ") 
    pay = int(hours) * float(rate)
    print ("Pay: ", float(pay))
except:
    print("Error, please enter numeric input")