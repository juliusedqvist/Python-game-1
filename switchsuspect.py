import Suspect


def switchSuspect():

    q4 = input("""All the others are still there, you can talk to: Queen, noble, priest, chef, blacksmith""")
    if q4 == "queen":
        Suspect.queen.startup(0)
    elif q4 == "noble":
        Suspect.noble.startup(0)
    elif q4 == "priest":
        Suspect.priest.startup(0)
    elif q4 == "chef":
        Suspect.chef.startup(0)
    elif q4 == "blacksmith":
        Suspect.blacksmith.startup(0)
    else:
        print("unvalid action")
        switchSuspect()
