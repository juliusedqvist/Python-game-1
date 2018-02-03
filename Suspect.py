import switchsuspect

import accuse


class suspect():

    def __init__(self, king, queen, noble, priest, chef, blacksmith, dialog1, dialog2, suspect):
        self.king = king
        self.queen = queen
        self.noble = noble
        self.priest = priest
        self.chef = chef
        self.blacksmith = blacksmith
        self.dialog1 = dialog1
        self.dialog2 = dialog2
        self.suspect = suspect

    def startup(self, qval):

        if qval == 0:
            q = input(self.dialog1)
        else:
            q = input(self.dialog2 + " (type thanks to switch suspect)")
        qa = q.split()
        qa[-1] = qa[-1].lower()
        if qa[-1] == "king":
            print(self.king)
            self.startup(1)

        elif qa[-1] == "queen":
            print(self.queen)
            self.startup(1)
        elif qa[-1] == "noble":
            print(self.noble)
            self.startup(1)
        elif qa[-1] == "priest":
            print(self.priest)
            self.startup(1)
        elif qa[-1] == "chef":
            print(self.chef)
            self.startup(1)
        elif qa[-1] == "blacksmith":
            print(self.blacksmith)
            self.startup(1)
        elif q == "thanks":
            self.stepback()
        else:
            print("unvalid action")
            self.startup(1)

    def stepback(self):

        print("You step back from the ", self.suspect, " and process the information")
        q3 = input("Would you like to talk with someone else or accuse someone? 'talk', 'accuse'")
        if q3 == "talk":
            switchsuspect.switchSuspect()
        elif q3 == "accuse":
            accuse.accuse()
        else:
            print("unvalid action")
            self.stepback()


def set_difficulty():
    difficulty = input("Choose your difficulty")
    if difficulty == "easy":
        pass
    print("You choose " + difficulty)

queen = suspect(
            "He's a strange man, for two weeks I've almost not seen him at all. But yesterday he seemed like a different man who wanted me",
            "sometimes I take long night walks in the city",
            "Alberto once planned a heist against the crown to get more power, you should question him",
            "I've always disliked the priest. Though he's one of my husbands best friends",
            "She often personally serve us appetizers in our private chambers. I really like her",
            "Before all this I dated him but had to break up because my family wanted me to marry the king",
            "I will miss him, the king that is", "now what?", "queen")
noble = suspect(
            "In a way I'm glad the king died. This land will be better without him",
            "The queen used to look happier before... like some sort of glow has disappeared", "I like ducks",
            "The priest once came to me at night, asking for help with some 'cleaning' of course I declined.",
            "Oh the chef, she's pretty good looking", "I used to order my silver from him", "yes?",
            "How may I assist you now", "noble")
priest = suspect(
            "As any good friend should, I recently discussed an urgent dilemma with him. That could've been his fall",
            "I think someone was about to take her role. You should look it up",
            "Yesterday was probably the first time he showed up to church, I think the only reason he came were to talk with the blacksmith",
            "You get to here the strangest things when listening to confessions",
            "One of my most active confessors",
            "He's in the same chorus as me, I overheard his conversation with alberto. they were supposed to find him a lover",
            "ask me anything my child", "I wonder why god did this", "priest")
chef = suspect(
            "Such a tradgedy!? Why would god do this??",
            "It was probably she who did it... Her family wants to control the kingdom, everybody knows that",
            "Excuse me but I don't get involved in politics",
            "A true man of god, I believe he's here to save us all",
            "My fiance left me two weeks ago. Apparently I focus to much on my work",
            "I once bought one of his jewelry, astounding work", "Please",
            "God will cleanse this world from sinners", "chef")
blacksmith = suspect(
            "The last time I saw him was at church talking to his old friend about. I overheard something about the queen before I had to leave",
            "Apparently I'm not good enough for her... but she's the best I ever had maybe she'll go back to me now",
            "We went drinking yesterday. I had to carry him home afterwards",
            "A good singer and a man of his word",
            "I used to know her before. She's not even that good of a cook", "Making tools is fun",
            "Waddya want?", "You could use a good hammer", "blacksmith")
butler = suspect(1, 2, 3, 4, 5, 6, "Yes?", "now what?", "butler")


