# Hangman

print("Willkommen zu Hangman")
word = input("Hier ihr Wunschwort eingeben: ")
print(f"Das Wort hat {len(word)} Stellen.")
space = "_" * len(word)
word = word.lower()
guessed_letters =  []

trys = 11

while trys > 0:
    print(space)
    print(f"Du hast noch {trys} Versuche.")
    guess = input("Errate einen der Bustaben: ").lower()
    before = space
    for i in range(len(word)):
        
        if word[i] == guess:
            guessed_letters.append(guess)
            
            print(f"Die Stelle des Bustaben ist {i+1}")
            space = space[:i] + guess + space[i+1:]
    if before == space:
        print("Ist nicht im Wort.")
        trys = trys -1
    if space == word:
        print("Du hast das richtige Wort erraten")
        break

input("Das Spiel ist vorbei")
            