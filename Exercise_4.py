digits1 = ("1", "3", "5", "7")
digits2 = ("2", "4", "6", "8")
letters1 = ("a", "c", "e", "g")
letters2 = ("b", "d", "f", "h")

while True:
    letter = input("Input the letter-coordinate of board: ")
    if not letter.isalpha():
        print("Enter LETTER !!!")
        continue
    elif len(letter) > 1:
        print("Input SINGLE letter !!!")
        continue
    elif letter.lower() > "h":
        print("ENTER THE LETTER OF THE BOARD !!! \n (it is FROM 'A' TO 'H')")
        continue
    break

while True:
    digit = input("Input the digit-coordinate of board: ")
    if not digit.isnumeric():
        print("Enter DIGIT !!!")
        continue
    elif len(digit) > 1:
        print("Input SINGLE digit !!!")
        continue
    elif not 1 <= int(digit) <= 8:
        print("ENTER THE DIGIT OF THE BOARD !!! \n (it is FROM '1' TO '8')")
        continue
    break

print()
if letter.lower() in letters1:
    if digit in digits1:
        print("BLACK !!!")
    else:
        print("WHITE ¡¡¡")

if letter.lower() in letters2:
    if digit in digits2:
        print("BLACK !!!")
    else:
        print("WHITE ¡¡¡")
