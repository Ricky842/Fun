import random
correct_number = random.randint(1, 100)

def welcome():
    """To welcome the player"""
    print("Welcome to the game")

welcome()

def exit():
    print("Thanks for Playing")


def game_check(guessed_num):
    while guessed_num.isnumeric() is True:
        guessed_number = int(guessed_num)
    
        if guessed_number > 100 or guessed_number < 1:
             print("Your number must be between 1 and 100")
             guessed_num = input("Please input your number again: ")
        else:
            return guessed_number
    print("Your have an invalid integer")
    new_guessed_num = input("Please input a valid integer: ")
    while new_guessed_num.isnumeric() is False:
        new_guessed_num = input("Please input a Valid integer as specified: ")
    game_check(new_guessed_num)
    new_guessed_num = int(new_guessed_num)
    return new_guessed_num
    

def game():
    guessed_number_str = input("Please enter your number here: ")
    guessed_num = game_check(guessed_number_str)
    guessed_num = int(guessed_num)
    count = 1
    while guessed_num != correct_number:
        print("Sorry, this was the wrong number")
        if count == 5:
            break
        elif guessed_num < correct_number:
            print("Your number was less")
        else:
            print("Your number was greater")
        guessed_number = input("Please enter your number again: ")
        game_check(guessed_number)
        guessed_number = int(guessed_number)
        count += 1
    return guessed_num

def win_check(guessed_number):
    if guessed_number == correct_number:
        print("Congratulations, you won")
    else:
        print("Sorry, you lost")
        print("The winning number was ", correct_number)

last_guess = game()
win_check(last_guess)
exit()
