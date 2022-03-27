"""
    Chapter Three
    Test one

    * Number Guessing Game.
     *  Make a variable, like winning_game,
        and assign anything to it.
     *  ask user to guess a number.
     *  if user guessed correctly then print "you win"

     * if user did not guessed correcty then.
        * if user guessed lower than actual number then print too low
        * if usre guessed higher than actual number then print too high

"""

import random

winning_number = random.randint(1, 10)

guess_number = int(input('Guess any number to win the game : '))
attempt = 0
game_over = True
while game_over:
    if guess_number == winning_number:
        attempt += 1
        print(f'Congrats you win this game in {attempt} atempts')
        game_over = False
        break
    else:
        if guess_number < winning_number:
            print('too low')

        else:
            print('too high')
    guess_number = int(input('Try again... : '))
    attempt += 1
