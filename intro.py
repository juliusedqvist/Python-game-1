import time
import Suspect


def intro():
    print("A game of guesses")
    introText()


def introText():
    Suspect.set_difficulty()
    skipIntro = input("Want to skip intro?")
    if skipIntro == "yes":
        gameplayStart()
    else:
        time.sleep(3)
        print("You are a detective in the 10th century.\n")
        time.sleep(5)
        print("In the middle of the dinner a page stumbles through your door.\n")
        time.sleep(5)
        print("""There's been a murder! The king is dead!
Can you help us find the one guilty of this horrible deed?\n""")
        time.sleep(5)
        print("""You follow the page through the city and up to the castle and into a secluded room. In the room there
are five others. The Queen, A noble, the local priest, a chef and a blacksmith.
The page says that these are the suspects and only one of them is guilty but the others could be involved in several
ways and you have to find out what happened and who's guilty of the deed by questioning them.\n""")
        time.sleep(10)
        print("""First you pick who to question, then you can ask the suspect about other suspects including the one
you're talking to. You can also ask them about their relationship with the king by simply typing king. \n""")
        time.sleep(10)
        gameplayStart()


def gameplayStart():
    q6 = input("Who'd you like to start question? 'queen', 'noble', 'priest', 'chef', 'blacksmith'")
    if q6 == "queen":
        Suspect.queen.startup(0)
    elif q6 == "noble":
        Suspect.noble.startup(0)
    elif q6 == "priest":
        Suspect.priest.startup(0)
    elif q6 == "chef":
        Suspect.chef.startup(0)
    elif q6 == "blacksmith":
        Suspect.blacksmith.startup(0)
    else:
        print("Unvalid action")
        gameplayStart()