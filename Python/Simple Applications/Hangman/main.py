import csv
import random


def draw_hangman(phase):
   display_man = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    """]
   if phase > len(display_man):
       return "Game Over"
   return display_man[phase-1]

def main():
    shows = {}
    shows_list = []
    shows_description = []
    with open("shows.csv", mode='r') as file:
        fileRead = csv.reader(file,delimiter=";")
        for i in fileRead:
            shows_a = {i[0]:i[1]}
            shows.update(shows_a)
            shows_list.append(i[0])
            shows_description.append(i[1])

    random_description = random.choice(shows_description)

    value = [i for i in shows if shows[i.strip()]==random_description]

    show_len = len(value[0])
    tv_show = value[0]

    print(tv_show)

    print("Enter one letter at the time.\nHint: "+random_description )
    character = "_" * show_len

    
    score = 0
    while True:
        user_input = input("Enter a letter:")
        found = False
        for i in range(show_len):
            if tv_show[i] == user_input:
                found = True
                
                print("You guessed correctly!")
                character = character[:i] + user_input + character[i+1:]
                print(character)

        if tv_show == character:
            print("Congratulations! You Guessed Correctly!!!")
            break

        if not found:
            score += 1
            print(draw_hangman(score))
            print("Incorrect")
            print(character)

        if draw_hangman(score) == "Game Over":
            print("Game Over")
            break
if __name__ == "__main__":
    main()

        

