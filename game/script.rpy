# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
call variables
call unlockmap

# The game starts here.
label start:

    #Load the "New Game" intro
    call new_game

    #Load the Dream Event
    call prologue_dream

    #Load First Morning Event
    call first_morning

    return
