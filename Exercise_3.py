print("type 'done' to finish inputting")
vowels = ("a", "e", "u", "i", "o",)
while True:
    letter = input("Enter the letter: ")
    if letter.lower() == "done":
        break

    if not letter.isalpha():
        print("Write down only a letter !!!")
        continue
    elif len(letter) > 1:
        print("Write down only 1 letter !!!")
        continue

    if letter.lower() in vowels:
        print("The letter is a vowel")
    elif letter.lower() == "y":
        print("The letter is both vowel and consonant")
    else:
        print("The letter is consonant")
