score = input("Enter Score: ")
try:
    s = float(score)
    if s >= float(10.0):
        print("Bad Score")
    elif s >= float(0.9):
        print ("A")
    elif s >= float(0.8):
        print ("B")
    elif s >= float(0.7):
        print ("C")
    elif s >= float(0.6):
        print ("D")
    elif s < float(0.6):
        print ("F")
except:
    print("Please enter numaric input")
    quit()