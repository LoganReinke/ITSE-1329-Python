score = float(input("Enter Score: "))
if score >= float(10.0):
    print("Bad Score")
elif score >= float(0.9):
    print ("A")
elif score >= float(0.8):
    print ("B")
elif score >= float(0.7):
    print ("C")
elif score >= float(0.6):
    print ("D")
elif score < float(0.6):
    print ("F")