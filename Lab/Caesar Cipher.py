alphabet = "abcdefghijklmnopqrstuvwxyz"

while True:
    while True:
        choice = int(input("Choose The Option (Enter 1 or 2)\n1. Encode\n2. Decode\n>>> "))
        if choice == 1 or choice == 2:
            break
        else:
            print("\nYour Option is out of Range: ")
            continue
    while True:
        key = input("\nEnter the key of Cipher (it can be also negative)\n>>> ")
        if key.replace('-', '').isnumeric():
            key = int(key)
            break
        else:
            print("Your key must be an integer !!!\n")
    while not 1 <= key <= 25:
        if key < 0:
            key += 26
            continue
        elif key > 0:
            key -= 26
        else:
            print("Ձե՞ռ եք առնում, չեմ ջոգում...")
            exit()
    text = input("\nEnter Your Text:\n>>> ").lower()

    if choice == 1:
        encoded = ''
        for letter in text:
            if letter in alphabet:
                if alphabet.find(letter) + key > 25:
                    encoded_letter = alphabet[alphabet.find(letter) - (26 - key)]
                else:
                    encoded_letter = alphabet[alphabet.find(letter) + key]
                encoded += encoded_letter
            else:
                encoded += letter
        print("\nThe Encoded Text: " + encoded + '\n')

    else:
        decoded = ''
        for letter in text:
            if letter in alphabet:
                if alphabet.find(letter) - key < 0:
                    decoded_letter = alphabet[alphabet.find(letter) + (26 - key)]
                else:
                    decoded_letter = alphabet[alphabet.find(letter) - key]
                decoded += decoded_letter
            else:
                decoded += letter
        print("\nThe Decoded Text: " + decoded + "\n")

    print("Wanna Try Again ?\nType 'y' if YES, 'n' for NO")
    while True:
        again = input('>>> ').lower()
        if again == 'n':
            exit()
        elif again == 'y':
            print()
            break
        else:
            print("\nType 'y' or 'n'")
