label new_game:
    "Welcome to Nana & Kaoru: SM Training."

    "This version of the game is a prototype hence all art and assets are placeholder."

    "The purpose of this iteration is the show off what I wish to achieve in the final version. If you see potential in this game please consider supporting the project."

    "Hope you have fun."

    menu:
        "Do you wish to set a custom name for the Protagonist?"

        "No (Default: Kaoru)":
            jump .rename_no
        "Yes":
            jump .rename_yes

            label .rename_no:
                $ p = "Kaoru"

                "Default Protagonist name is [p]"

                return

            label .rename_yes:
                python:
                    name = renpy.input("Enter new name for the Protagonist")

                    name = name.strip() or "Kaoru"

                    "Your name is [p]"

                return
