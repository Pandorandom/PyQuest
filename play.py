from sys import exit


#this is the end room, player will end the game after this room.
def rescued_kingdom():
    print "Thanks for rescuing the chalice and returning our kingdom's glory! Please take as much gold as you wish."

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("That is not a treasure we can part with.")

    if how_much < 5000:
        print "Thank you for being such a modest hero. Please return any time you wish."
        exit(0)
    else:
        dead("I'm sorry, but we cannot part with that much gold, you will now be executed!")

# A test to see if the user can successfully kill the dragon to take the chalice.
def dragon_lair():
    print "This is the lair of a dragon!"
    print "You must be very careful and quiet, any sudden noises will surely awake the beast."
    print "You see the dragon sleeping."
    print "The dragon has a bunch of gold and treasure surrounding it."
    print "At the dragon's feet lies the Chalice of the King. How will you move the dragon?"
    dragon_moved = False

    # tells program what to do after user has input something. If the player guesses right,
    # they will receive a message of congratulations and a prompt to move forward in the game.
    while True:
        next = raw_input("> ")

        if next == "take gold":
            dead("You are not very intelligent. Dragons love their gold!")
        elif next == "stab dragon" and not dragon_moved:
            print "You killed the dragon with a decisive strike to the heart, the dragon is no longer a threat."
            dragon_moved = True
        elif next == "stab dragon" and dragon_moved:
            dead("The dragon was actually playing dead, and you now are the dead one.")
        elif next == "take chalice" and dragon_moved:
            rescued_kingdom()
        else:
            print "I'm sorry, I don't understand that command."

#gives the player 3 choices, 2 resulting in death, 1 being the right choice.
def tunnel_challenge():
    print "Before you lies a very long tunnel."
    print "It break off in three directions."
    print "do you take the left, right, or middle tunnel?"
    middle_tunnel = False


    # tells program what to do after user has input something. If the player guesses right,
    # they will receive a message of congratulations and a prompt to move forward in the game.
    while True:
        next = raw_input("> ")

        if next == "left":
            dead("You took the tunnel that lead to a cliff and fell down a hole to your untimely death.")
        if next == "middle":
            dead("You went down this tunnel and were immediately killed by a lurking goblin.")
        elif next == "right" and not middle_tunnel:
            print "The right tunnel seems to be safe, you can head down the rest of the way."
            middle_tunnel = True
        elif next == "right" and middle_tunnel:
            print "You went much too far down the tunnel and were lost forever."
        elif next == "into tunnel" and middle_tunnel:
            dragon_lair()
        else:
            print "You'll have to be more specific, or face certain death!"


# the player has to solve a riddle, no death at this point as nothing dangerous.
def logic_puzzle():
    print "You come upon the Cave of Aranea."
    print "Sitting on a perch you see a rather unusual crow."
    print "This crow has one large eye where it should have two."
    print "The crow looks at you and begins speaking."
    print "'Welcome traveler. I know why you are here.'"
    print "'You may enter this cave if you pass my test.'"
    print "'A sundial is a timepiece that has the fewest number of moving parts. Which timepiece has the most moving parts?'"
    crow_test = False


    # tells program what to do after user has input something. If the player guesses right,
    # they will receive a message of congratulations and a prompt to move forward in the game.
    while True:
        next = raw_input("> ")

        if next == "hourglass" and not crow_test:
            print "'You have solved my riddle and proved your superior logic. You may continue.'"
            crow_test = True
        elif next == "hourglass" and crow_test:
            print "'You already said that, move along!'"
        elif next == "into cave" and crow_test:
            tunnel_challenge()
        else:
            print "'You are not a smart person, try again!'"


# town where if player makes specific choices will accept quest to reclaim the chalice.
# saving the boy in previous scenario will bring the player here.
def mountain_town():
    print "You arrive in the mountain town of Halfhill, eager to start your quest for glory."
    print "You find the king of the town, who reigns over the entire Hectoro Mountain Range, Brock Slate."
    print "The king informs you that you must venture to the Cave of Aranea and reclaim the Chalice of the King."
    print "The king also tells you to have caution, there are many tests and perils in that cave."
    print "Do you accept the king's quest in exchange for a gold reward from the kingdom?"
    quest_accepted = False


    # tells program what to do after user has input something. If the player guesses right,
    # they will receive a message of congratulations and a prompt to move forward in the game.
    while True:
        next = raw_input("> ")

        if next == "yes" and not quest_accepted:
            print "Fantastic! Time for a feast before we send you off on your adventure!"
            quest_accepted = True
            logic_puzzle()
        elif next == "yes" and quest_accepted:
            print "You've already accepted the quest and the feast will begin shortly."
        if next == "no":
            dead("You are an idiot, that quest would have been easy money!")
        else:
            print "You have to accept the quest or turn down your chance for glory, fame, and wealth."



"""
Here is where the adventure can become very unique. The player is presented with the challenge of saving one of three people.
There is an old man, who will teleport the player all the way to the dragon's lair, the final challenge room before the player
    chooses their gold reward.
Another option is a beautiful woman, who happens to be dressed in tattered clothes. She is a witch, and offers the player a portal
to the logic puzzle with the talking crow.
the third choice is a young boy in peasant's clothing. If the player decides to save this person, the boy will take the player
to the mountain town to actually hear the quest from the king.
"""
def forest_maze():
    print "You have found your way to Forest of Frost."
    print "You feel very cold, and must react quickly."
    print "The forest has presented you with a choice."
    print "You must choose to save one of three people."
    print "1. A beautiful woman, dressed in very tattered clothing."
    print "2. A young boy, dressed in peasant's clothing."
    print "3. An old man, dressed in extravagant clothing."
    test_passed = False

    # Begin While loop of input from player. Until player chooses a person to save by "1, 2, or 3"
    # if player enters invalid number or phrase, program will tell player to pick another number or option.
    while True:
        next = raw_input("> ")


        # Saving witch scenario. if the test_passed class is still marked as "FALSE," the player will advance to the saved
        # witch dialog. If the player has already saved the witch and does not "take portal" player will get a message they
        # they have already talked to this person.


        if next == "1" and not test_passed:
            print "The woman turns out to be a witch."
            print "The witch forsees a grand adventure in your future."
            print "She tells you that you will go on a quest from a king, and travel through the Cave of Aranea, and rescue the chalice."
            print "She offers you a portal, telling you that this will take you to the Cave of Aranae to save you time."
            test_passed = True
        elif next == "1" and test_passed:
            print "You've already spoken with the witch"
        elif next == "take portal" and test_passed:
            logic_puzzle()
        # peasant boy scenario, will take player to mountain_town if this option selected.
        if next == "2" and not test_passed:
            print "The boy is gracious for you rescuing him."
            print "The boy tells you he comes from Halfhill, and offers to bring you home for a feast fit for heroes for saving him."
            print "'Please come with me.' the boy says."
            test_passed = True
        elif next == "2" and test_passed:
            print "You already saved the boy."
        elif next == "go with boy" and test_passed:
            mountain_town()
        # old man scenario. old man will teleport the player to the final challenge room.
        if next == "3":
            print "The old man thanks you profusely, and tells you that you are bound to go on a grand adventure."
            print "He explains that he is a great wizard, and he will teleport you to the final challenge you will face."
            print "The wizard says, 'You are going to accept a quest from Brock Slate, and will go to the Cave of Aranea.'"
            print "'In the Cave of Aranea, you will face a dragon who protects the chalice with which you are tasked to return.'"
            print "'Please, take hold of my arm and I will provide you passage to the dragon's lair.'"
            test_passed = True
        elif next == "3" and not test_passed:
            print "You already saved the old man."
        elif next == "take arm" and test_passed:
            dragon_lair()
        else: print "You cannot pick a simple number, can you?"

# quest board room giving player 3 options of quests, will force player to take option 3.
def quest_board():
    print "You walk up to the quest board in the center of your town and look at the available quests."
    print "You get the feeling that today there will be a quest of legendary proportions."
    print "On the board, you see three quests available."
    print "1. A farmer's dog has gone missing and is offering 10 gold for the safe return of the dog."
    print "2. There is a bandit camp forming outside of the town, and the mayor has offered 50 gold for the clearance of this camp."
    print "3. A king from the mountains requires a noble knight to go on a quest, safety is not guaranteed."
    print "Which do you take?"
    beginning_quest = False

    while True:
        next = raw_input("> ")

        # players will end the game if they choose the incorrect quest, assuming their character has gone to this task.
        if next == "1":
            dead("You set out with the intentions of taking a grand quest, not a mundane task!")
        if next == "2":
            dead("Hey! We are trying to find a GRAND adventure, not a quest for a measley 50 gold!")
        if next == "3" and not beginning_quest:
            print "This sounds very dangerous but very promising."
            print "Let's set off! It says I must get to a town in the mountains and I must go to the Forest of Frost."
            beginning_quest = True
        elif next == "3" and beginning_quest:
            print "Come on, you need to Go to the Forest!"
        elif next == "go to forest" and beginning_quest:
            "Let's go!"
            forest_maze()
        else:
            dead("You need to pick more carefully!")

# after wake up test, asks player to leave home to go to quest board.
def bedroom():
    print "You awake in your mundane bedroom."
    print "Today, you wake up and feel like today you need to find something that will set you among the gods."
    print "You need to set off for the town quest board and see if something calls your name as needing extra heroic effort."
    leave_home = False

    while True:
        next = raw_input("> ")

        if next == "leave" and not leave_home:
            print "Alright, off to see what grand adventures lie ahead!"
            leave_home = True
        elif next == "leave" and leave_home:
            print "You made the decision already, let's go to the quest board!"
        elif next == "go" and leave_home:
            "We're off!"
            quest_board()
# defines the function "dead", shows why(this is typed at each if statement's dead("") as well as "Good Job!" and then exits.
def dead(why):
    print why, "Good job!"
    exit(0)

# start of text adventure, reality check like lucid dreaming, must "wake up" to advance game.
def start():
    print "You realize you are sleeping."
    print "It is time to wake up."
    print "What is your reality check for dreaming?"

    next = raw_input("> ")

    if next == "wake up":
        bedroom()
    elif next == "dream":
        dead("You can't dream a reality check in a dream, you'll never wake up!")
    else:
        dead("Seriously, you need to Wake up!")

start()
