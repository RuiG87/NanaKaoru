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
    define pStr = 1
    define pSta = 0
    define pKnow = 1
    define pCon = 0
    define pSad = 3
    define Dom = 2
    #Event specific
    define inevent = False

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
