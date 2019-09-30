count = 0
total = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        count = count + 1
        total = total + num
    except:
        print("Invalid input")
print(total,count,total/count)