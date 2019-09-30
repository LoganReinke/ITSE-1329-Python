maximum = 0
minimum = 100
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    except:
        print("That is not a number")
print(minimum,maximum)