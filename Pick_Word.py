from random import randint
from sys import exit

def draw_hangman(incorrect_counter):
    if incorrect_counter == 0:
        print("  +---+")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    if incorrect_counter == 1:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    if incorrect_counter == 2:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |")
        print("=========")
    if incorrect_counter == 3:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("      |")
        print("=========")
    if incorrect_counter == 4:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print("      |")
        print("      |")
        print("=========")
    if incorrect_counter == 5:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print(" /    |")
        print("      |")
        print("=========")
    if incorrect_counter == 6:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print(" / \  |")
        print("      |")
        print("=========")


def open_file():
    with open('dictionary.txt', 'r') as f:
        line = f.readline()
        list_1 = []
        while line:
            list_1.append(line.strip())
            line = f.readline()
        return list_1

def guess(guess_list, list_2, list_3, incorrect_counter):
    guess = input("Guess a letter: ")
    guess = guess.upper()
    pos_counter = 0
    if guess in guess_list:
        print(f"{guess} was already selected!")
        return incorrect_counter
    elif guess in list_2:
        for item in list_2:
            if guess == list_2[pos_counter]:
                list_3[pos_counter] = guess
            pos_counter += 1
        guessed_list.append(guess)
        guessed_list.sort()
        return incorrect_counter
    else:
        guessed_list.append(guess)
        guessed_list.sort()
        incorrect_counter += 1
        return incorrect_counter
        
def win_game(list_3,replay_flag):
    while True:

        if '-' in list_3:
            return replay_flag
        else:
            replay = input("Would you like to play again? y/n ")
            if replay == 'n':
                exit()
            if replay == 'y':
                replay_flag = False
                return replay_flag
            else:
                print("Invalid input.")

def lose_game(list_3):
    pos_counter = 0
    for item in list_3:
        list_3[pos_counter] = '0'
        pos_counter += 1
    return list_3



while True:
    counter = 0
    list_1 = open_file()
    list_1 = list_1[randint(0,len(list_1))]
    list_2 = []
    list_3 = []
    letters = len(list_1)
    guessed_list = []
    incorrect_counter = 0
    replay_flag = True

    for item in range(0,letters):
        list_3.append("-")

    for item in list_1:
        list_2.append(item)
    print("Welcome to Hangman!!!!")
    draw_hangman(incorrect_counter)
    while replay_flag:
    
        print(list_3)
        incorrect_counter = guess(guessed_list, list_2, list_3, incorrect_counter)
        print (f"Current guesses: {guessed_list}.")
        print(f"{incorrect_counter} incorrect guesses!")
        draw_hangman(incorrect_counter)
        if incorrect_counter == 6:
            print(f"The word was {list_2}.")
            list_3 = lose_game(list_3)

        replay_flag = win_game(list_3,replay_flag)