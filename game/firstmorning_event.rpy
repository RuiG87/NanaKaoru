label first_morning:
    default dressed = False
    scene bg-kaoru_room_day

    "I feel a dull pain on the back of my head and find myself staring at a very familiar ceiling."

    "I glance over to the sliding doors the lead out to the balcony, the morning daylight seeps into my room signaling the start of a brand new day."

    k "That was one heck of a wet dream."

    "I sit up and feel a slight discomfort in my underwear."

    k "Great, looks like I discharged a load...man this is embarassing."

    k "I am going to have to give these a wash without Mom noticing."

    "Now that I think about it I haven't introduced myself have I?"

    k "(My name is [s] [k], an 18 year old that has gone without a girlfriend for has long as he lived)"

    "My looks clearly don't help, people have likened me to a frog and they aren't wrong. {w}Sadly I am pretty self aware of this fact."

    "And then there is my hobby. I am a S&M aficionado, most of my spending money goes towards porn and these toys."

    "I notice that on top of my bed there is a familiar piece of leather clothing."

    k "(That is...)"

    "I reach out and pick up the costume. {w}The feeling of the leather against my hands feels great, it was a great purchase."

    k "(It's a shame that I have no one to use it for me)"

    k "(If she was willing to put it on I am certain it would look amazing)"

    "I bring the leather close to face and rub my cheeks on it, while all giddy imagining it"

    k "(Can't be helped)"

    "Mom" "[p]!! What are you doing with that creepy look on your face?"

    k "M-MOM!!!"

    "I turn back and see my Mother standing behind me with this disturbed look on her face."

    k "(Holly shit, she scared the crap out of me)"

    k "Don't just enter my room like this! D-d-d-on't you even respect your own son's pricacy?"

    "Mom" "Did you buy another weird toy?"

    k "Shut up!!! Don't look!!!"

    k "It's Sunday, at least cut me some slack today!!"

    "Mom" "Don't you have school today?"

    k "...eh?"

    "Mom" "Well, it's that Nana you know..."

    "My mother glances behind her and a girl peeks through the open door."

    show eileen happy

    "She stands straight with a hand resting on her hip. {w}And looking as beautiful as always."

    "This is Chigusa Nana. Same age as me, she is my next door neighbour and my childhood friend."

    "Since we both have single mothers, we have always close since we were little kids."

    "And as one might have guessed already, she is my first love."

    "Of course I have never told her this and I do my best to not let her notice."

    "I mean just look at us, we are worlds apart."

    n "[k]! You have supplementary classes!!"

    "The surprise of seeing here still hasn't subdued, especially not after last nights dream"

    "I can't help but stare at her while in a trance."

    "She looks looks at me with a puzzled look"

    n "What? Do I have something on my face?"

    "Her remark snaps me out of it, I shake my head in order to clear my thoughts"

    k "(Damn it control yourself)"

    "That's right, supplementary classes. My grades have fallen quite a bit so now I have to dedicate my weekends to make sure I don't repeat a year."

    k "I completely forgot about those classes."

    "Nana narrows her eyes and glares as me, then she sighs"

    n "Come on, get ready. I will wait for you downstairs."

    "Nana turns around and walks away from my room"

    hide eileen happy

    "Mom" "Hurry up, don't leave her waiting too long. I will pack a Sandwich for you to eat on your way."

    "Mom leaves the room and closes the door behind her"

    k "Let's get ready then"

    label .notDressed_loop:
        menu:
            "Change clothes":
                if dressed == False:
                    "I picked up my uniform and changed into it"
                    $ dressed = True
                    jump .notDressed_loop
                else:
                    "I alredy changed into my uniform"
                    jump .notDressed_loop
            "Leave Room":
                if dressed == False:
                    "I still haven't changed into my uniform"
                    jump .notDressed_loop
                else:
                    k "(I better not keep Nana waiting for much longer)"

    "As I am about to leave I remember that it might be better for me to tuck away the bondage suit"

    "I pick it off of the bed and put it away in a drawer"

    scene black

    "On my way out Mom handed me a sandwich and some lunch money"

    "I stuff the sandwich into my mouth as I go down the stairs, since me and Nana live on the top floor of a 8 storie building."

    call lockmap
    $ school = True
    $ inevent = True
    call worldmap
    call unlockmap
    $ inevent = False

    scene bg-road

    "I am walking alongside Nana while she is nagging me"

    n "I give up, did you really forget that you had lessons today?"

    k "..."

    n "You do know that if you fail these you will be held back a year right?"

    k "I don't see how it has anything to do with you. Rather why are you even tagging along?"

    n "Us from Class A have things to do as well"

    "Nana glances over at me with an inquisitive look"

    n "Why are you slouching?"

    k "I didn't get enough sleep"

    "I already hunch forward as it is but whenever I look at her it reminds of my dread and I feel my cock starting to harden"

    n "You end up looking shorter that way"

    "Nana wraps her arm around me and pulls me towards her"

    k "!!!"

    "I feel her massive tits pull up against me and the images from my dream become even more vivid"

    n "You have to stand up straight or else it will be bad for your back."

    k "(Her tits are so soft)"

    "My cock jumps to attention istantly. I pull away from Nana and slouch forward while using my bag to cover my crotch"

    n "Eh? What's wrong?"

    n "Why are you slouching forward more than before?"

    k "No reason! Just stay away and touch get too touchy-feely with me."

    k "(It's your fucking fault! If I could I would shove my cock down your throat damn it!)"

    n "Why do y..."

    "Nana is about to say something when she is cut short"

    "???" "Nana"

    n "Ah! Yukari...and Kikuko as well"

    "It's the girls from A class"

    "The short haired brunette that called out to Nana is Mutsuki Yukari, the student council secretary"

    "They have been friends since Nana's first year and are constantly seen together on campus"

    "If you ask me she takes Nana's friendship for granted, constanly Nana to help with her student council work despite the fact that Nana isn't a member"

    "And on top of that she doesn't seem to like me very much despite the fact that we haven't really interacted before"

    y "..."

    k "(Hmm? Why is she glaring at me? The bitch needs to lighten up and get a fat cock stuck up her ass)"

    "On the other hand Yagami Kikuko, the long haired one is the student council president"

    "She has this prideful and cunning air surrounding her, she is known to be able to get others to do what she wants"

    ki "Good morning [s]"

    k "..."

    "That smile of hers gives me cold sweat and I don't know how to deal with her since it seems like she can see through you"

    "If we were to follow clichés she would normally be the type to enjoy being degraded once she submits to you"

    n "[k] stop bring rude, you can at least answer back"

    k "tch"

    n "Stop being so distant and come and walk next to us"

    k "Just go on and stay away from me. I wouldn't want to be seen hanging around you stuck up bastards from A-Class"

    n "If you are going to be like that then see if I care when people call you a creep, you idiot!!"

    "I increase my pace and walk from Nana and the other two..."

    "Fuck! Why am I always like this?"
