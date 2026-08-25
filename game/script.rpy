#Transitions defined 
define fade = Fade(0.5, 3, 0.5) #Transition to prologue

# CHARACTERS DEFINED
define cat1 = Character("Carmen Strahd")
define cat2 = Character("Mason Strahd")

define lion = Character("Raegan Williams")
define hyena = Character("Elizabeth Williams")

define crow = Character("Officer")
define salamander = Character("Barron Rogers")
define pigeon = Character("I FORGOR HIS NAME")
define ostrich = Character("Ethel Crosswire")
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
return #Game ends
