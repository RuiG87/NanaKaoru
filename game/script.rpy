# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

jump variables

# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #label prologue_dream:

    jump new_game

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    label rename_done:

        scene bg-kaoru_room_night
        
        show eileen happy

        jump prologue_dream

        "test return"

        return
