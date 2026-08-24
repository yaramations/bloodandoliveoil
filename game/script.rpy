# CHARACTERS DEFINED
define cat1 = Character("Carmen Strahd")
define cat2 = Character("Mason Strahd")

define lion = Character("Raegan Williams")
define hyena = Character("Elizabeth Williams")

define crow = Character("Officer")
define salamander = Character("Barron Rogers")
define pigeon = Character("I FORGOR HIS NAME")
define ostrich = Character("Ethel Foster")

define n = Character("") #narrarator



label start: # The game starts here.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


#STORY STARTS

# Prologue
    show cat1 sample.png #Strahd in his room
    n "A knock can be heard at the door"
    cat1 "Come in!"

    show lion sample.png #Raegan walks in

    cat1 "By golly, it's you!"
    cat1 "So tell me, how have you been, old friend? Was the train kind to you? Can I have Ethel get you anything?"
    
    lion "Ah, well I suppose it went as well as any journey could go. My wife Elizabeth found the journey rather uneventful, but you know how she can get. "
    cat1"I still remember my first train ride up the East Coast. My back, how it ached, on and on for nine hours! Thank God the train had plenty of liquor or I fate may not have been so kind to me!"
    lion "I’d reckon so, not a journey for the lightweight to say the least."
    lion "Besides the point, why did you ask to meet up with me so soon?"
    cat1 "I need to … make arrangements with you before the retirement party tomorrow."
    lion "In what way?"

    n "A second knock can be heard at the door"

    cat1 "Your service is most appreciated, place them here Ethel."

    #CG OF ETHEL AND THE TEACUP GOES HERE

    ostrich"Of course, Mister Strahd"
    cat1 "As I was saying, there are still many preparations that need to be made, including my inheritance."

    n "The conversation has seemed to attrack the attention of a nearby listner"
    cat1 "Hold on, I think we have an eavesdropper"

    show cat2 sample.png #Mason walks in

    cat1 "You’re not supposed to be drinking that, Mason!" #Sound effect for hiss

    cat2 "I knoooow dad, but just this once..."
    cat1 "Absolutely not, put that down young man!"
    cat2 "You just don’t understand..."

    hide cat2
    hide cat1
    hide lion
    hide ostrich

    return #Game ends
