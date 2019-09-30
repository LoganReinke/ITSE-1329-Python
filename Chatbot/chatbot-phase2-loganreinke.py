#Logan Reinke
greetings = 0
while True:
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    time = input("What time of day is it (Morning, Afternoon, Evening): ")
    if time == "morning":
        print("Have a good breakfast " + first_name + " " + last_name[0])
    elif time == "afternoon":
        print("Have a good lunch " + first_name + " " + last_name[0])
    elif time == "evening":
        print("Have a good dinner " + first_name + " " + last_name[0])
    else:
        print("Have a good one " + first_name + " " + last_name[0])
    greetings = greetings + 1
    new = input ("Would you like another greeting? ")
    if new == "no":
        break
print("You received " + str(greetings) + " greetings")