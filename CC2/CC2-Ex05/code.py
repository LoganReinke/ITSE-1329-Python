hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
if hours > 40:
    ot = hours - 40
    otr = rate * 1.5
    otpay = 40 * rate + float(ot) * float(otr)
    print ("Pay: ", float(otpay))
else:
    pay = float(hours) * float(rate)
    print ("Pay: ", float(pay))
