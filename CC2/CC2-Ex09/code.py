hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    h = float(hours)
    r = float(rate)
    if h > 40:
        ot = h - 40
        otr = r * 1.5
        otpay = 40 * r + float(ot) * float(otr)
        print ("Pay:", float(otpay))
    else:
        pay = float(hours) * float(rate)
        print ("Pay:", float(pay))
except:
    print("Error, please enter numeric input")
    quit()