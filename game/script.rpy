#Transitions defined 
define fade = Fade(0.5, 3, 0.5) #Transition to prologue

# CHARACTERS DEFINED
define cat1 = Character("Carmen Strahd")
define cat2 = Character("Mason Strahd")

define lion = Character("Raegan Williams")
define hyena = Character("Elizabeth Williams")

define crow = Character("Officer")
define salamander = Character("Barron Rogers")
define pigeon = Character("Eren Barnes")
define ostrich = Character("Ethel Crosswire")
define olive = Character("The Olive Man")

define n = Character("") #narrarator
define a = Character("All")


label start: # The game starts here.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
#STORY STARTS

# Raegan's Letter
    play music "/audio/bgost/249_Steampunk_Station.mp3"
# CG of train
    lion "Dear Carmen Strahd,"
    lion "I wish you my warm regards from the new transcontinential railroad."
    lion "Despite not seeing you for years, I appreciate your invitation and look forward to our reunion."
    lion "These past few months have made me bitter, and the sting of the cold brings an omen of uncertianty."
    lion "In the dawn of this new American frontier, I'm afraid I will become outshone by far more suitable business partners."
    lion "You, on the other hand, were always the more suitable businessman."
    lion "I wish I was quicker to discover the profitability of oil in this economy, and I'm grateful you still think of me as your longtime companion."
    lion "You were always considered the savant between the two of us. Utilizing oil made out of olives to power the Industrial Revolution? Genius!"
    lion "This shrewdness of yours has never truly surprised me though, just as one could have easily predicted your early retirement."
    lion "Not many can pass on the business at only 42 years old."
    lion "But alas, we have much more to speak about in person. I will await our next meeting to disclose my latest expidentures."
    lion "In the meantime, I bid you well."
    lion "Sincerely, Raegan Williams"

    play music "/audio/bgost/267_Court_of_the_Count.mp3"
    with fade #transitions to prologue


# Prologue
    # show cat1 sample.png #Strahd in his room
    play sound "/audio/soundeffects/soundscrate-wood-door-knock-outside-twice-01.mp3"
    n "A knock can be heard at the door"
    cat1 "Come in!"

    # show lion sample.png #Raegan walks in

    cat1 "By golly, it's you!"
    cat1 "So tell me, how have you been, old friend? Was the train kind to you? Can I have Ethel get you anything?"
    
    lion "Ah, well I suppose it went as well as any journey could go. My wife Elizabeth found the journey rather uneventful, but you know how she can get. "
    cat1"I still remember my first train ride up the East Coast. My back, how it ached, on and on for nine hours! Thank God the train had plenty of liquor or fate may not have been so kind to me!"
    lion "I’d reckon so, not a journey for the lightweight to say the least."
    lion "Besides the point, why did you ask to meet up with me so soon?"
    cat1 "I need to…make arrangements with you before the retirement party tomorrow."
    lion "In what way?"

    play sound "/audio/soundeffects/soundscrate-wood-door-knock-outside-twice-01.mp3"
    n "A second knock can be heard at the door"

    cat1 "Your service is most appreciated, place them here Ethel."

    #CG OF ETHEL AND THE TEACUP GOES HERE

    ostrich"Of course, Mister Strahd"
    cat1 "As I was saying, there are still many preparations that need to be made, including my inheritance."

    n "The conversation has seemed to attrack the attention of a nearby listner"
    cat1 "Hold on, I think we have an eavesdropper"

    # show cat2 sample.png #Mason walks in
    play sound "/audio/character/cat/mixkit-angry-cartoon-kitty-meow-94.wav"
    cat1 "You’re not supposed to be drinking that, Mason!" #Sound effect for hiss

    cat2 "I knoooow dad, but just this once..."
    cat1 "Absolutely not, put that down young man!"
    cat2 "You simply cannot understand..."

    #hide cat2
    #hide cat1
    #hide lion
    #hide ostrich


## CHAPTER 1
    play sound "/audio/soundeffects/mixkit-rioting-crowd-376.wav" loop
    with fade

    cat1 "Welcome welcome welcome dear guests!"
    crow "(Dammit, I can't see anything with this crowd!)"

    cat1 "My name is Carmen Strahd, successful millionaire, olive oil tycoon, and most well groomed feline of the year for five years straight, but you already know that!"
    cat1 "That is why you're here after all. All my family, acquaintances, and business associates all gathered here to honor my life and legacy."
    cat1  "I'm so excited to finally go on retirement!"
    cat1 "However, before the celebrations can begin, I need to make some preparations."
    cat1 "..."
    cat1 "Particularly those concerning...my inheritance"

    stop sound
    n "A hush falls over the once lively crowd"

    cat1 "Well well it won't be long, and I'll make sure everybody gets a piece of the pie!"
    n "Carmen steps awat"

    play sound "/audio/soundeffects/soundscrate-wood-door-pounding-outside-5-times-01.mp3"
    cat1 "Ouch...my leg"

    pigeon "Officer! You finally made it!"
    crow "and...?"
    pigeon "Why aren't you more excited? We're meeting THE REAL CARMEN STRAHD!"
    pigeon "Do you think he'll sign my copy of his autobiography?"
    crow "I don't care to become reaquainted. I'm just here for the business."
    pigeon "wait...you KNEW HIM!?"
    pigeon "OHGOODNESSPLEASETELLMEEVERYTHINGIMUSTKNOW"
    crow "Just calm down...you know more about him than I do."
    crow "and if you haven't forgotten: we're on A MISSION."
    pigeon "Yes sir! I will be very serious, sir! I will not dissapoint you!"
    crow "Good. We have an investigation to conduct."

    pigeon "So tell me boss, WHO are we investigating?"
    menu:
        "The femme fatale seducing the gentlemen.":
            pigeon "Wait.....why her?"
            crow "Why not? Women like her tend to lure out the secrets of those they can charm."
            pigeon "She's frightening!"
            play sound "/audio/soundeffects/mixkit-footsteps-on-heels-on-the-pavement-542.wav"
            n "You and Eren begin walking up to the seductive hyena."
            play sound "/audio/character/hyena/Coyote Call-SoundBible.com-1347099109.mp3"
            hyena "I have been looking for someone to sweep my chimney, and I like the look of your brush."
            n "The flock of guys surrounding her found that *very charming*."
            crow "Madam, may I borrow you for a minute?"
            n "She turns her attention towards you."
            hyena "OOOOOOOOh, an officer..."
            hyena "Are you gonna arrest me for my crimes against fashion?"
            crow "We just have some questions we'd like to ask."
            pigeon "We're doing SERIOUS BUSNIESS THINGS, so you better cooperate."
            hyena "Oh.."
            crow "Is something the matter?"
            hyena "Sorry sirs"
            hyena "I can't hang out with serious people..."
            hyena "...I don't want their energy to rub off me."
            pigeon "(How dare she! I am PLENTY OF FUN!...when I'm not on business of course.)"
            crow "(Note to self: Have Eren handle her next time...)"

        "The man in (what appears to be) an olive costume":
            pigeon "Why do you want to talk to that weirdo?"
            crow "I don't know, but he looks pretty interesting."
            olive "Do you guys happen to be friends of Strahd..?"
            crow "We've been aquainted"
            olive "Well, I think you should DITCH HIM!"
            pigeon "Why?"
            olive "Back in 1867, Strahd commited a most heinous sin against me"
            crow "Well, what did he do?"
            olive "He BUMPED me on a stairwell!"
            olive "Do you believe the AUDACITY of some people!?"
            crow "Sounds good sir, goodbye"
            pigeon "Why did you end the conversation so quickly?"
            crow "I think he had too much liquor..."

        "The dapper salamander counting the money in his wallet.":
            pigeon "Him? Can we really trust a guy who only cares about money?"
            crow "People like him will pay all the money in the world for information to outwit their competitors."
            salamander "So, what can I do for you fine gentleman?"
            crow "Let's make a deal."
            salamander "OOOOOH straight to the chase! Those are my four favorite words, officer. Let me hear your offer!"
            crow "Tell me what you know about Strahd, and I won't release your crimes to the public."
            salamander "Woah woah woah hold your horses..."
            salamander "I already got hitmen that do that for me."
            salamander "Poke around any longer, and you'll be next on their list."
            crow "(I have a feeling antagonizing him won't bode very well for us...)"
            pigeon "(Geez, so harsh)"

        "We're investigating a place, not a person.":
            pigeon "Oh yes, sorry sir!"
            n "You and Eren take note of the building's interesting features."
            n "Strahd's manor, which is a 'humble' 500 acres in size, only recenly finished construction two years prior to his retirement party (1887)."
            n "The architecture can be described as gaudy and flamboyant, which are common characteristics of Gilded Age homes."
            n "Greek statues can be seen just around the gardens of the estate, and the manor boats 15 separate pavillions around the periphery of the home."
            n "Furthermore, it sits just off the coast of Newport, Rhode Island, and the magnificent Atlantic Ocean can be seen from its entrance."
            n "While these extravagant manors are traditionally used as 'summer cottages' for the extremely wealthy, Strahd intends to make the estate his year-round retirement home."
            crow "Wow, that was..."
            crow "pretty useless actually."

    pigeon "OFFICER, LOOK!"
    pigeon "Strahd is about to start"
    # renpy.movie_cutscene("On_Your_Mark.webm")
    play sound "/audio/soundeffects/mixkit-trailer-screaming-people-annihilation-351.wav"
    a "AAAAAAAAAAAAAAAAH!"

return #Game ends
