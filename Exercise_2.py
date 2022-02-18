Sum = 0
quantity = 0
avg = 0

while True:
    num = input("Enter a number: ")
    if num.isnumeric():
        Sum += int(num)
        quantity += 1
    elif num.lower() == "done":
        break
    else:
        print("Invalid Input!!!")
        continue

avg = Sum / quantity

print("The Sum is: " + str(Sum))
print("Quantity is: " + str(quantity))
print("The Average is: " + str(avg))
