import time
import intro


def accuse(looseCount=0):
    q5 = input("""You've chosen to accuse someone and thus you should have a clear scenario of what happened.
To accuse someone you first type who you want to accuse and the motive that person had. Example queen power / Viable 
motives are power, belief, revenge, defense and envy. """)
    accuseInput = q5.split()
    print(accuseInput[0])
    print(accuseInput[1])
    if not (not (accuseInput[0] == "chef") or not (accuseInput[1] == "revenge")):
        print("Suddenly the answer struck you")
        time.sleep(5)
        print("""With a loud cough you gather everyones attention and present your solution.
         The chef, also known as the mistress, is jailed and you receive a juicy reward.""")
        time.sleep(5)
        print("VICTORY")
    else:
        print("Unfortunately your story doesn't hold up by lacking evidence and the " + accuseInput[0] + """ means that
you should be jailed for falsely accusation and the motion goes through""")
        time.sleep(5)
        print("DEFEAT")
        if looseCount > 0:
            print("You've guessed wrong " + looseCount + "time(s)")
        looseCount += 1
        time.sleep(5)
        tryAgain = input("Want to guess again?")
        if tryAgain == "yes":
            intro.gameplayStart()
        elif tryAgain == "no":
            print("")
