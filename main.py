VOWELS = ["a", "e", "i", "o", "u"]

print("Vowel Counter!\n")

counting = True

while counting:
    word_or_sentence = list(input("What word/sentence would you like counted?: ").lower())
    total = 0
    for letter in word_or_sentence:
        if letter in VOWELS:
            total += 1
    print(total)
    check_to_continue = True
    while check_to_continue:
        continue_counter = input("Do you have more word/sentences to be counted?: y or n\n").lower()
        if continue_counter == "y" or continue_counter == "n":
            check_to_continue = False
            if continue_counter == "y":
                counting = True
            elif continue_counter == "n":
                counting = False
        else:
            print("please input a valid letter")
            check_to_continue = True
