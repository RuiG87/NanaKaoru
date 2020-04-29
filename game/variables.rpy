label variables:
    define daytime = True
    #Characters
    define narrator = Character(what_italic=True)
    define n = Character("Nana", color="#ff3333")
    define k = Character("[name]")
    define s = Character("[surname]")
    define y = Character("Yukari")
    define ki = Character("Kikuko")
    #Kaoru Stats
    define kStr = 1
    define kSta = 1
    define kKnow = 5
    define kCon = 0
    define kSad = 3
    define kDom = 2
    define kInt = 2
    #Event specific
    define inevent = False

    define audio.breathermusic = "music/dream_sequence_song.mp3"

    return

label unlockmap:
    #Map locations are open
    define school = True
    define shop = True
    define home = True
    define work = True
    define park = True

    return

label lockmap:
    #Map locations are locked
    define school = False
    define shop = False
    define home = False
    define work = False
    define park = False

    return
