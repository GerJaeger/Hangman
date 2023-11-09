# Hangman

import Hangman_zeichnung as hz

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
        match trys:
            case 11:
                hz.first()
            case 10:
                hz.second()
            case 9:
                hz.third()
            case 8:
                hz.fourth()
            case 7:
                hz.fifth()
            case 6:
                hz.sixth()
            case 5:
                hz.seventh()
            case 4:
                hz.eigth()
            case 3:
                hz.nineth()
            case 2:
                hz.tenth()
            case 1:
                hz.last()
                print(f"Das richtige Wort war {word}")
        trys = trys -1
            
    if space == word:
        print("Du hast das richtige Wort erraten")
        break

input("Das Spiel ist vorbei")
quit()