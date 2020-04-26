label worldmap:
    if daytime == True:
        scene bg-citymap_day
    else:
        scene bg-citymap_night

    menu:
        "Home":
            if home == False:
                "I can't go here right now"#change to var
                jump worldmap
            else:
                if inevent == False:
                    jump room_navigation
                else:
                    return
        "School":
            if school == False:
                "I can't go here right now"#change to var
                jump worldmap
            else:
                if inevent == False:
                    "to be implemented later"
                    jump worldmap
                else:
                    return
        "Tachibana Bondage":
            if shop == False:
                "I can't go here right now"#change to var
                jump worldmap
            else:
                if inevent == False:
                    "to be implemented later"
                    jump worldmap
                else:
                    return
        "Work":
            if work == False:
                "I can't go here right now"#change to var
                jump worldmap
            else:
                if inevent == False:
                    "to be implemented later"
                    jump worldmap
                else:
                    return
        "Park":
            if park == False:
                "I can't go here right now"#change to var
                jump worldmap
            else:
                if inevent == False:
                    "to be implemented later"
                    jump worldmap
                else:
                    return
