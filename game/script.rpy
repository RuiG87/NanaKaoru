# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

jump variables

# The game starts here.

label start:
    jump new_game

    label rename_done:
        

        show eileen happy

        jump prologue_dream

        "test return"

        return
