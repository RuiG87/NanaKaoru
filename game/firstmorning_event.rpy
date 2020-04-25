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

    "Mom" "Hurry up, don't leave her waiting too long. I will pack a Sandwich for you to eat on your way."

    "Mom leaves the room and closes the door behind her"

    k "Let's get ready then"

    label notDressed_loop:
        menu:
            "Change clothes":
                if dressed = False:
                    "I picked up my uniform and changed into it"
                    $ dressed = True
                    jump notDressed_loop
                else:
                    "I alredy changed into my uniform"
                    jump notDressed_loop
            "Leave Room":
                if dressed = False:
                    "I still haven't changed into my uniform"
                    jump notDressed_loop
                else:
                    k "(I better not keep Nana waiting for much longer)"

    "As I am about to leave I remember that it might be better for me to tuck away the bondage suit"

    "I pick it up off of the bed and put it away in a drawer"

    "On my way out Mom handed me a sandwich and some lunch money"

    "I stuff the sandwich into my mouth as I go down the stairs, since me and Nana live on the top floor of a 8 storie building."
