import Sentences as sn
import Signs
import TestCheck as tc
import numpy as np
import player as pl
import Items as IT
import trading_house as market
import NPC


class SquareQuarter:
    def __init__(self, max_x, max_y):
        self.addresses = np.random.randint(1, 4, size=(max_x, max_y), dtype=int)
        self.addresses[6, 8] = 0  # hunted house
        self.addresses[1, 4] = 10 # black market


    def get_location(self, x_pos, y_pos):
        return self.addresses[x_pos, y_pos]

    def print_quarter(self):
        print(self.addresses)

    def goto(self, x_pos, y_pos):
        location_index = self.addresses[x_pos, y_pos]
        # hunted house
        if location_index == 0:
            sn.narrator('This is the place')
            HuntedHouse()
        # Random houses
        elif location_index == 1:
            sn.narrator('You knock the door, but there is no answer')
        elif location_index == 2:
            sn.narrator('You enter into random house...')
            sn.narrator('...while the dwelling eating supper')
            sn.NPC('Scared kid', 'Mommy I am afraid! who is the strange woman?')
            sn.player('I\'m sorry, wrong house')
        elif location_index == 3:
            sn.narrator('As you approach the house someone shout from the window')
            sn.NPC('dweller', 'GET OUT YOU FILTHY WITCH!')
        # Black Market

        elif location_index == 10:
            sn.narrator('You knock the door...')
            sn.narrator('Someone ask you from inside')
            sn.NPC('???', 'Who is this?')
            password = input("Do you have the password? >> ").lower()
            if password == "matrimim":
                sn.NPC('???', 'Ok, you can enter The Black Market')
                pl.Roni = market.BlackMarket.enter(pl.Roni)
            else:
                sn.NPC('???', 'Get the hell out of here!')


class CircularQuarter:
    def __init__(self, radios_num=7, angle_num=6):
        self.addresses = np.random.randint(1, 4, size=(radios_num, angle_num), dtype=int)
        self.dAngle = int(180/angle_num)
        self.addresses[3, 4] = 10   # Vampire's dan

    def angle_index(self, angle):
        angle = angle-30
        angle_idx = int(angle / self.dAngle)
        return angle_idx

    def get_location(self, rho, phi):
        angle_idx = self.angle_index(phi)
        radios_idx = rho-1
        return self.addresses[radios_idx, angle_idx]

    def print_quarter(self):
        print(self.addresses)

    def goto(self, rho, phi):
        phi_index = self.angle_index(phi)
        radios_idx = rho - 1
        location_index = self.addresses[radios_idx, phi_index]
        if location_index == 0:
            sn.narrator('This is the place')
        elif location_index == 1:
            sn.narrator('You knock the door, but there is no answer')
        elif location_index == 2:
            sn.narrator('Someone open you the door')
            sn.NPC('Random man', 'You are not my pizza')
        elif location_index == 3:
            sn.narrator('As you approach the house someone shout from the window')
            sn.NPC('dweller', 'phh... another woman, another witch...')
        elif location_index == 10:
            VampireDen()


class ForestMaze:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 10
        self.height = 9
        self.wall = 0
        self.clear = 1
        self.goal_mansion = 9
        self.goal_cave = 8
        self.goal_naked_tree = 7
        self.maze = np.array([
            [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
            [7, 0, 0, 0, 0, 1, 0, 8, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 9],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        ])

    def get_location(self):
        print('x: {}, y: {}'.format(self.x, self.y))

    def printMaze(self):
        print(self.maze)

    def ifTarget(self):
        if self.maze[self.y][self.x] == self.goal_mansion:
            # print('out of maze')
            return True
        elif self.maze[self.y][self.x] == self.goal_cave:
            # print('cave')
            return True
        elif self.maze[self.y][self.x] == self.goal_naked_tree:
            # print('naked_tree')
            return True
        else:
            return False

    def blockCheck(self, x, y):
        isBlock = False
        # print('blockCheck, x = {}, y = {}'.format(x,y))
        if x < 0 or x > self.width or y < 0 or y > self.height:
            # print('out of maze')
            isBlock = True
        elif self.maze[y][x] == self.wall:
            # print('wall')
            isBlock = True

        return isBlock

    def move(self, direction):
        if direction == 'w':
            if self.blockCheck(self.x, self.y-1):
                sn.narrator("You blocked by a tree")
            else:
                self.y = self.y - 1

        elif direction == 's':
            if self.blockCheck(self.x, self.y+1):
                sn.narrator("You blocked by a tree")
            else:
                self.y = self.y + 1

        elif direction == 'd':
            if self.blockCheck(self.x+1, self.y):
                sn.narrator("You blocked by a tree")
            else:
                self.x = self.x + 1

        elif direction == 'a':
            if self.blockCheck(self.x-1, self.y):
                sn.narrator("You blocked by a tree")
            else:
                self.x = self.x - 1

        elif direction.lower() == 'revertere hic':
            TheDarkForest(method='return spell')

        # self.get_location()
        # self.printMaze()
        # self.ifTarget()


class Swamp:
    def __init__(self):
        self.correct_path = ['stone',  'tree', 'stone', 'stone', 'mist']
        self.options = ['Stone', 'Tree', 'Mist', 'Mud', 'Locum Tutum']
        self.path = []

    def move(self):
        while True:
            sn.narrator('There are in the swamps a lot of trees, stones, deep mud and places with heavy mist')
            answer = tc.input_commend(self.options, "Which way is for you to go?[Tree/Stone/Mud/Mist]",
                                      getback=False, show_options=False)
            if answer == 'locum tutum':
                TheSwamp(method='spell')
            else:
                self.path.append(answer)
                # print(self.path)
                if len(self.path) >= len(self.correct_path):
                    if self.path[-len(self.correct_path)::] == self.correct_path:
                        # print('Found it!')
                        sn.narrator("The fog start to disappear... you notice two figures in ahead of you")
                        winJavna = pl.Roni.checkBag("S1")
                        winSuccubus = pl.Roni.checkBag("S2")

                        # lose both
                        if (not winJavna) or (not winSuccubus):
                            sn.player("Javna and Succubus, together, there is no duet now")
                            sn.player("In order to deal with this situation, I must banish them both.")
                            sn.player("Unfortunately, I did not came prepared.. I must run for now")
                            TheSwamp(method='spell')
                            pass

                        elif winJavna and winSuccubus:
                            sn.narrator("You walk as quietly as you can through the swamp,")
                            sn.narrator("until an eerie sight greets your eyes. Not swamp gas,")
                            sn.narrator("but actually a few lit lanterns of different colours surrounding a cage "
                                        "holding two figures.")
                            sn.narrator("You see a young couple being withdrawn from the rusty cage by a winged "
                                        "monster")
                            sn.narrator("and a beautiful lady with a snake’s tongue - your queries.")
                            sn.narrator("The two monsters begin to dance with the charmed humans,")
                            sn.narrator(" the succubus grazing the male with her tongue and teeth,")
                            sn.narrator("and the Javna nibbling on the maiden before her.")
                            sn.narrator("You pour your backup bottle of holy water to the ground as a quick means to "
                                        "consecrate it")
                            sn.narrator("and draw a penis on the swamp ground with broken twigs.")
                            sn.narrator("You light a few candles around it and kneel upon it.")
                            sn.narrator("As soon as the candles are lit, the succubus approaches you hungrily,")
                            sn.narrator("not realizing you’ve began chanting her doom")
                            sn.player("By the forces of heaven and hell. Draw to us this woman fell. ")
                            sn.player("Rend from her foul desire. That she may perish as a moth to fire.")
                            sn.narrator("And the succubus steps unto the twig-penis she bursts into flames,")
                            sn.narrator("screaming and flailing away from you into the swamp that does nothing against "
                                        "the arcane flames.")
                            sn.narrator("The Javna takes flight, rushing you down as you fumble for the "
                                        "Hand of Fatima.")
                            sn.narrator("Just before you’re struck down you rush to the succubus,")
                            sn.narrator("giving her a soft hug as she burns in arcane flames that do nothing to you,")
                            sn.narrator("but a lot to dissuade the approaching Javna.")
                            sn.narrator("You take this precious moment to grab the Hand of Fatima and chant loudly")
                            sn.player("Evil eyes, look unto thee. May they soon extinguished be,")
                            sn.player("Bend thy will to the power of three,Eye of earth, evil and accursed.")
                            sn.narrator("And as the Succubus stops her flailing the Javna is sucked through the "
                                        "Hand to hell.")
                            sn.narrator("...")
                            Signs.quest_end()
                            sn.narrator(
                                "https://www.timeanddate.com/countdown/to?iso=20220321T15&p0=676&msg=1&font=cursive&csz=1")
                            pass


def intro_town_square():
    Locations = ['Tavern', 'Church', 'Gallows', 'Quarter A', 'Quarter B', 'Apothecary', 'Unknown road']
    Signs.townSquare()

    if pl.Roni.checkBag("P3"):
        sn.narrator("As you walk in the town square,  a pleasant breeze began to form")
        sn.narrator("The the sky doesn't looks so grey anymore...")
        sn.narrator("It's the sun. You can fill the warm of it on your skin.")
        sn.narrator("Eastwood is safe now, Thanks to you")

        Signs.end()

        sn.narrator("...")
        sn.narrator("...")
        sn.narrator("...")
        sn.NPC("You Informer", "Roni! before it is ending, there is one more thing... "
                               "Check your mailbox one more time.")
        sn.narrator("...")
        pass
    else:
        sn.narrator("You can see around you the different parts of the town.")
        # Signs.options(Locations)
        # answer = input("Where to you want to go?")
        # answer = tc.input_check(answer, Locations, "Where to you want to go?")
        answer = tc.input_commend(Locations, "Where to you want to go?", getback=False, show_options=False)
        if answer == 'tavern':
            Tavern()
        elif answer == 'church':
            Church()
        elif answer == 'gallows':
            Gallows()
        elif answer == 'quarter a':
            Quarter_A()
        elif answer == 'quarter b':
            Quarter_B()
        elif answer == 'apothecary':
            Apothecary()
        elif answer == 'unknown road':
            Unknown_road()


def Tavern():
    Signs.tavern()
    sn.narrator('From the outside it looks uninviting, dark and dire.')
    sn.narrator('Large and small stones and intricate stone carvings make up most of the building\'s outer structure.')
    sn.narrator('It\'s near impossible to see through the dusty windows, but the coldness from within can be felt '
                'outside.')
    sn.narrator('As you enter the tavern through the dirty, metal door,')
    sn.narrator('you\'re welcomed by thick air and a feeling of discomfort.')
    sn.narrator('The bartender is coughing into a dirty napkin and makes no effort to acknowledge your pressence.')
    sn.narrator('It\'s as dire inside as it is on the outside.')
    sn.narrator('Hardwooden beams support the upper floor and the huge, dusty lamps attached to them.')
    sn.narrator('The walls are loaded with pictures, though the dust and cobwebs stops you from taking a closer look.')
    sn.narrator('The tavern itself is almost completely abandoned. The few people inside could be locals, could be '
                'lost souls,')
    sn.narrator('but whoever they are, it\'s about the clearest sign you can get, telling you you don\'t belong.')
    sn.narrator("You take yourself a drink and seat down for few minutes.")
    sn.narrator("...")
    print()
    while True:
        options = ["Order from the bartender", "Seat and eavesdrop", "Talk to the stranger"]
        answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False)
        # Order from the bartender
        if answer == 1:
            NPC.Bartender.confront()
            pass
        # Seat and eavesdrop
        elif answer == 2:
            print('Seat and eavesdrop')
            sn.narrator("You decided to sit down, while the drunk people trade information...")
            sn.NPC("Drunk 1", "I tell you... you can buy rare and illegal stuff in there.")
            sn.NPC("Drunk 2", "I can't go there, it is too dangerous. However, I have to buy it. ")
            sn.NPC("Drunk 1", "Listen, you payed me already for the information, so I will give you the password "
                              "and you decide whatever you want.")
            sn.NPC("Drunk 2", "Ok, what is the password?")
            sn.NPC("Drunk 1", "MATRIMIM.")
            sn.player("I heard enough.")
            pass
        # Talk to the stranger
        elif answer == 3:
            print('Talk to the stranger')
            pass
        # Return to the town square
        elif answer == 4:
            sn.player('I should go back..')
            intro_town_square()


def Church():
    Signs.church()
    sn.narrator('Surrounded by poor looking peasants, there was the church...')
    sn.narrator('Thick walls made of light white stone.')
    sn.narrator('Tall middle tower with ancient cross on top of it.')
    sn.narrator('A great gate with enormous wooden doors between two statues.')
    sn.narrator('Well kept gardens with fragrant flowers, gorgeous trees and many bushes decorate the outside...')
    sn.narrator('As you enter to the Main Hall, The pastor finish the pray and leave the Alter to enter the Sacristy.')
    sn.narrator('Bunch of prayer are still in the Main Hall.')
    print()
    while True:
        options = ["Alter", "Sacristy", "Stay in the Main Hall"]
        answer = tc.input_commend(options, "Where do you like to go?[Enter number]", text_check=False)
        # Alter
        if answer == 1:
            print('Alter')
            while True:
                options_1 = ["Holy water", "Nothing", "Go somewhere else"]
                answer_1 = tc.input_commend(options_1, "What would you wish to do?[Enter number]", text_check=False)
                # Holy water
                if answer_1 == 1:
                    sn.narrator("You approach the Holy Water and take some in your bottle")
                    pl.Roni.addItem("V1")
                    pass
                # Nothing
                elif answer_1 == 2:
                    sn.narrator("...Nothing happen...")
                    pass
                # Go somewhere else
                elif answer_1 == 3:
                    break
                # Return to the town square
                elif answer_1 == 4:
                    sn.player('I should go back..')
                    intro_town_square()

        # Sacristy
        elif answer == 2:
            print('Sacristy')
            if pl.Roni.checkBag("P2"):
                sn.narrator("You arrive late at the church, walking against the bickering crowd of the evening sermon.")
                sn.player("I find my soul burdened priest, will you hear my confession?")
                sn.NPC("Priest", "Of course my lovely child, come after me")
                sn.narrator("You follow the priest to the confession booth,")
                sn.narrator("entering from the right as he enters from the left and opens a grated window between the "
                            "two of you.")
                sn.NPC("Priest", "What is it you wish to confess, child? What sins do you bear?")
                sn.narrator("The glass globe feels warm in your hand as you begin to chant as softly as possible:")
                sn.player("Sower of discord you work must cease")
                sn.narrator("The priest leans greedily towards the window.")
                sn.NPC("Priest", "Speak up child, do not let fear control your tongue - tell me all, embrace what you "
                                 "are")
                sn.narrator("And through the grated open window you splash the potion onto the demon, who recoils "
                            "in disgust.")
                sn.player("I vanquish thee now with these words of peace")
                sn.narrator("Sitting still now with your palms pressed together and your eyes gently shut,")
                sn.narrator("your mind finds momentary peace, silence,")
                sn.narrator("the machinations of the spell take effect calmly through your mind,")
                sn.narrator("like gentle hands easing the priest onto true peace, calming,")
                sn.narrator("and quieting him as they gently caress his head.")
                sn.narrator("You let go of the breath you were holding and approach the priest’s side of the booth.")
                sn.narrator("On the floor you find the Demon of Anarchy in what might have seemed like a gentle sleep "
                            "if his windpipe wasn't completely crushed.")
                sn.narrator("...")
                Signs.quest_end()
                sn.narrator("https://www.timeanddate.com/countdown/to?iso=20220319T12&p0=676&msg=3&font=cursive&csz=1")
                pass

            else:
                sn.narrator('At the moment you try to enter the Sacristy, the priest stop you and say:')
                sn.NPC('Priest', "Greeting my child.. You have the eyes of a nun.")
                sn.NPC('Priest', "However, you don\'t look like one..")
                pass

        # Stay in the Main Hall
        elif answer == 3:
            # print('Stay in the Main Hall')
            sn.player("L will stay in the main hall.")
            while True:
                options_3 = ["Investigate the church", "Talk to the prayers", "Go somewhere else"]
                answer_3 = tc.input_commend(options_3, "What would you wish to do?[Enter number]", text_check=False)
                # Investigate the church
                if answer_3 == 1:
                    sn.narrator("while Investigating the church, you notice a pile of Wooden Stake.")
                    sn.player("This could be useful.")
                    pl.Roni.addItem("V2")
                    pass
                # Talk to the prayers
                elif answer_3 == 2:
                    # print('Talk to the prayers')
                    sn.narrator("You approach the prayers.")
                    sn.player("May the lord guide us in our ways.")
                    sn.NPC("Prayer 1", "He is. Always.")
                    sn.NPC("Prayer 2", "You can take a Wooden Stake before you go out.. Good for lord's protection.")
                    sn.player("Thank you, I will.")
                    pass
                # Go somewhere else
                elif answer_3 == 3:
                    break
                # Return to the town square
                elif answer_3 == 4:
                    sn.player('I should go back..')
                    intro_town_square()

        # Return to the town square
        elif answer == 4:
            sn.player('I should go back..')
            intro_town_square()


def Gallows():
    Signs.gallows()
    sn.narrator('You\'re pulled to the sound of an excited crowd surrounding a raised wooden structure, from which an '
                'empty noose hangs.')
    sn.narrator('A young woman is led across the creaky platform by a heavyset man clad in black towards the rope '
                'swinging in the breeze.')
    while True:
        options = ["Blend in the crowd", "Approach the stage"]
        answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False)

        # Blend in the crowd
        if answer == 1:
            print('Blend in the crowd')
            if pl.Roni.checkBag("GC"):
                sn.NPC("Peasant 1", "I heard rumors the the executor isn't what you think.")
                sn.NPC("Peasant 1", "You can find the true in the Old Mansion, at the end of The Dark forest.")
                pl.Roni.addItem("URP")
            else:
                sn.NPC("Peasant 1", "Poor woman...")
                sn.NPC("Peasant 2", "Do not feel sorry for her, she is a witch!")
            pass

        # Approach the stage
        elif answer == 2:
            if pl.Roni.checkBag("B1"):
                sn.narrator("You’ve seen enough.")
                sn.narrator("You cut in front of the woman being led to the stage and grab the knot of the empty noose "
                            "as you begin to chant:")
                sn.player("MAGIC FORCES, BLACK AND WHITE, REACHING OUT THROUGH, SPACE AND LIGHT, BE HE FAR OR, "
                          "BE HE NEAR, BRING US THE DEMON ,BELTHAZOR HERE")
                sn.narrator("The executioner jumps off the ground as his head is pulled through the noose,")
                sn.narrator("which you tighten with a quick satisfying tug.")
                sn.narrator("What first seems like the rosy cheeks of asphyxiation, turns out to be the bloody head of "
                            "a demon.")
                sn.narrator("Belthazor’s red features come into the crowd’s view,")
                sn.narrator("everyone begins to flee under the terrifying gaze of his blood-shot eyes.")
                sn.narrator("Your ears pop as the demon opens his mouth to taunt you:")
                sn.NPC("BELTHAZOR", "Great parlor tricks witch, did you think I require breath?")
                sn.NPC("BELTHAZOR", "Or maybe that I’m just going to wrench my own neck with this rotten piece of "
                                    "string?")
                sn.narrator("Your senses scream at you to flee with the crowd, never to be seen again, away from this "
                            "monstrosity.")
                sn.narrator("A hand twitches at the noose, a hand that feels almost incorporeal,")
                sn.narrator("what should be your hand but completely numb -")
                sn.narrator("sets spittle flying out of the demon’s mouth in a grotesque yet comical expression,")
                sn.narrator("as your sense of self returns you break the potion at Belthazor’s feet, chanting:")
                sn.player("SPIRITS OF AIR, FOREST AND SEA; SET US OF THIS DEMON FREE; BEASTS OF HOOF AND BEASTS OF "
                          "SHELL, DRIVE THIS EVIL BACK TO HELL!")
                sn.narrator("Belathzor’s eyes bulge as a portal to hell opens at his feet,")
                sn.narrator("pulling at him in complete disregard of the disagreeing noose.")
                sn.narrator("Just as the demon’s neck begins bending, the noose snaps and Belathzor plunges back to "
                            "hell.")
                sn.narrator("...")
                Signs.quest_end()
                sn.narrator("https://www.timeanddate.com/countdown/to?iso=20220320T14&p0=676&msg=2&font=cursive&csz=1")
                pass
            else:
                sn.narrator("The executor stop you from getting closer")
                pass

        elif answer == 3:     # Return to the town square
            sn.player('I should go back..')
            intro_town_square()


def Quarter_A():
    Signs.quarter_a()
    sn.narrator("The smell hits you like a fist.")
    sn.narrator("But what could you expect with so many houses cloistered shoulder to shoulder, ")
    sn.narrator("as if their neighbors are the only thing keeping them upright in this boxed quarter.")
    sn.narrator("You’d like to slow your pace and make sure you don’t step in any weirdly coloured puddles of what is surely water,")
    sn.narrator("but you’d rather not draw attention to yourself.")
    sn.narrator("With your head held relatively high, you take your first steps through the puddles of what is definitely NOT water.")


    Square = SquareQuarter(10, 10)
    while True:
        print()
        options = ['Visit a house']
        answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False)
        if answer == 1:
            # SquareQuarter = np.zeros((10, 10))
            print('Quarter A')
            print('choose house address:')
            x_pos = list(range(1, 11))      # 10 options,from 1 to 10
            y_pos = list(range(1, 11))      # 10 options,from 1 to 10
            x_loc = int(tc.input_commend(x_pos, 'enter x coordinate:', show_options=False, text_check=True))
            y_loc = int(tc.input_commend(y_pos, 'enter y coordinate:', show_options=False, text_check=True))
            print(x_loc, y_loc)
            Square.goto(x_loc, y_loc)
            # Square.print_quarter()
        elif answer == 2:
            sn.player('I should go back..')
            intro_town_square()


def Quarter_B():
    Signs.quarter_b()
    sn.narrator("Round as the coins flowing through it, this neighborhood is home to merchants, "
                "craftsmen and many other respected citizens.")
    sn.narrator("This is a place of commerce, with paths wide enough to accommodate two wagons and imposing houses "
                "surrounded by lush gardens.")
    sn.narrator("You find yourself gawking at a nearby mansion and quickly lower your eyes to avoid looking "
                "like a bumpkin.")
    sn.narrator("As you get further away from the main square you see more typical normal-sized houses,"
                " but all of them are well taken care of.")
    phi_pos = list(range(30, 181, 30))  # 6 options,from 0 to 180
    rho_pos = list(range(1, 8))  # 7 options,from 1 to 7
    Circular = CircularQuarter(len(rho_pos), len(phi_pos))
    while True:
        print()
        options = ['Visit a house']
        answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False)
        if answer == 1:
            print('choose house address:')
            rho_loc = int(tc.input_commend(rho_pos, 'enter r coordinate:', show_options=False, text_check=True))
            phi_loc = int(tc.input_commend(phi_pos, 'enter phi coordinate [degree]:', show_options=False, text_check=True))
            # print(Circular.get_location(rho_loc, phi_loc))
            Circular.goto(rho_loc, phi_loc)
            # Circular.print_quarter()
        elif answer == 2:
            sn.player('I should go back..')
            intro_town_square()


def Apothecary():
    Signs.apothecary()
    sn.narrator('As you get close, you notice a wooden store and little garden')
    sn.narrator('From the outside this store looks nice and traditional with apothecary sign on it.')
    sn.narrator('It has been built with white pine wood and has walnut wood decorations.')
    sn.narrator('Small, half rounded windows brighten up the house and have been added to the house in a very '
                'asymmetric way.')
    sn.narrator('You can see long shelf full of potion behind the windows.')
    sn.narrator('the garden looks well-kept full of variety of flora')
    while True:
        options = ["Go inside the store", "Walk to the garden"]
        answer = tc.input_commend(options, "Would you like enter the store?[Enter number]", text_check=False)
        # Go inside the store
        if answer == 1:
            sn.narrator("You decided to enter the store.")
            sn.narrator("Inside, you see only one woman - The apothecary of Eastwood")
            while True:
                options_2 = ["Purchase ingredients", "Look inside my bag", "Mix potion", "Exit the store"]
                answer_2 = tc.input_commend(options_2, "Greeting traveler. How can I help you?[Enter number]",
                                            text_check=False, getback=False)
                # Purchase ingredients
                if answer_2 == 1:
                    # market.ApothecaryStore.showGoods()
                    # pl.Roni = market.ApothecaryStore.buy(pl.Roni)
                    pl.Roni = market.ApothecaryStore.enter(pl.Roni)
                    sn.narrator('Anything else you wish to do?')
                    pass
                # Look inside my bag
                if answer_2 == 2:
                    sn.narrator('You check the items in your bag')
                    pl.Roni.lookBag()
                    pass
                # Mix potion
                if answer_2 == 3:
                    sn.narrator("You need to choose the potion you would like to mix.")
                    sn.narrator("The potion recipe is documented in the Book of Shadows")
                    choose_potion = input("What is the title of the page in th Book of Shadows? \n>>").lower()
                    pl.Roni.makePotion(choose_potion)
                    pass
                # Exit the store
                if answer_2 == 4:
                    sn.narrator('You exit the store')
                    break
        # Walk to the garden
        elif answer == 2:
            print('Walk to the garden')
            # market.ApothecaryGarden.showGoods()
            # pl.Roni = market.ApothecaryStore.buy(pl.Roni)
            pl.Roni = market.ApothecaryGarden.enter(pl.Roni)
            pass
        # Return to the town square
        elif answer == 3:
            sn.player('I should go back..')
            intro_town_square()


def Unknown_road(method='from town'):
    if method == 'from town':
        sn.narrator('After five minutes walk you encounter a sign:')
        Signs.danger()
        req_item = 'URP'
        if pl.Roni.checkBag(req_item):
            # sn.narrator(f'You have {IT.itemdict[req_item]}')
            sn.player('I can pass this now.')
        else:
            sn.player('I can\'t take this risk rigt now, I should go back...')
            intro_town_square()
        sn.narrator('After ten more minutes you encounter a crossroad')
    elif method == 'back from':
        sn.narrator('You walk all the way back to the crossroad')
    while True:
        options = ["The Dark Forest", "The Swamps"]
        answer = tc.input_commend(options, "Where do you like to go?[Enter number]", text_check=False)
        if answer == 1:     # The Dark Forest
            TheDarkForest()
        elif answer == 2:   # The Swamps
            print('The Swamps')
            TheSwamp()
        elif answer == 3:   # return
            sn.player('I should go back..')
            intro_town_square()


def TheDarkForest(method='walk'):
    if method == 'walk':
        sn.narrator("Massive ancient trees watch as you enter the dark forest.")
        sn.narrator("The thick trees blot out the sun and the smell of dead plants is thick in the air.")
        sn.narrator("The wind picks up, rustling the leaves and putting your hairs on ends.")
        sn.narrator("You’ve braved forests before, but did the wind really just pick up?")

        sn.narrator('You walk slowly into the tall trees in the beginning of the forest')
        sn.narrator('As you enter you notice a large bolder with engraving:')
        sn.narrator('To Return: \" Revertere hic \" ')
    elif method == 'return spell':
        sn.narrator('Everything around you start to spin very fast')
        sn.narrator('and then, vanished and replaced by familiar place - The forest entrance')
    sn.narrator('What do you want to do?')
    while True:
        options = ["Enter into the forest", "Return"]
        answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False, getback=False)
        if answer == 1:  # The Dark Forest
            sn.narrator("You enter into the forest")
            Maze = ForestMaze()
            while True:
                options = ['w', 's', 'd', 'a', 'Revertere hic']
                answer = tc.input_commend(options, "Which direction? [w/d/s/a]",
                                          text_check=True, getback=False, show_options=False)
                Maze.move(answer)
                # Old Mansion
                if Maze.maze[Maze.y][Maze.x] == Maze.goal_mansion:
                    sn.narrator("You find a way out of The Dark Forest")
                    options = ["Go out form the forest", "Stay in the forest"]
                    answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False,
                                              getback=False)
                    # Go out form the forest
                    if answer == 1:
                        sn.narrator("You decided to exit the forest.")
                        oldMansion()
                    # Stay in the forest
                    elif answer == 2:
                        sn.narrator("You decided to stay in the forest.")
                        pass
                # Cave
                elif Maze.maze[Maze.y][Maze.x] == Maze.goal_cave:
                    sn.narrator("In the middle of the forest, between two massive tree, a cave revealed to your eyes")
                    sn.narrator("The cave entrance is around ten feet tall, so you can go inside easly.")
                    options = ["Go inside the Cave", "Stay in the forest"]
                    answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False,
                                              getback=False)
                    # Go inside the Cave
                    if answer == 1:
                        sn.narrator("You decided to go inside the cave.")
                        Cave()
                    # Stay in the forest
                    elif answer == 2:
                        sn.narrator("You decided to stay in the forest.")
                        pass
                # Lost Man
                elif Maze.maze[Maze.y][Maze.x] == Maze.goal_naked_tree:
                    sn.narrator('As you walk through the woods, a unique looking tree appear in front of you.')
                    sn.narrator('A abnormal tree, that look naked in fist sight')
                    sn.narrator(
                        'Despite it almost without leaves, it manage to prosper better then any other '
                        'trees in the forest')
                    sn.player('Found it, The Naked Tree.. I can always trust the book of shadows')
                    pl.Roni.addItem('A5')

        elif answer == 2:  # return
            sn.player('I should go back..')
            Unknown_road(method='back from')


def Cave():
    sn.narrator('You enter the cave')
    sn.narrator('an old witch-like lady catches your eye, and after a few more moments you notice the variety '
                'of mushrooms deeper in the cave')
    while True:
        options = ["Talk with the witch", "Examine the mushrooms", "Go back to the Forest"]
        answer = tc.input_commend(options, "Would you like to do?[Enter number]", text_check=False, getback=False)
        # Talk with the witch
        if answer == 1:
            sn.narrator("The moment you turn yourself through the witch, she disappears.")
            sn.player("Where did she go?")
            sn.NPC("Old witch", "Hello there you wondering child")
            sn.narrator("Suddenly the witch reappears close to you.")
            sn.NPC("Old witch", "Watch out. You can see the mushrooms, but not take them!")
            sn.NPC("Old witch", "If you try to do something stupid I will curse you!")
            sn.NPC("Old witch", "Ha Ha Ha!!!")

        # Examine the mushrooms
        elif answer == 2:
            sn.player("I need to go deeper into the cave to examine the mushrooms")
            sn.narrator("As you get closer, you notice five different kinds of mushrooms")
            while True:
                # 1.Coral Widow | 2.Trompeta Gray Saddle | 3.Death Earthball | V 4.Hairy Grisette | 5.Cloudy Brittlegill
                mushrooms = ["Mushroom type-A", "Mushroom type-B", "Mushroom type-C", "Mushroom type-D",
                             "Mushroom type-E", "No"]
                mushrooms_choose = tc.input_commend(mushrooms,
                                                    "Do you wish to further examine on of the mushrooms?[Enter number]"
                                                    , text_check=False, getback=False)
                if mushrooms_choose == 1:   # Coral Widow
                    sn.narrator("A tiny blue mushroom with thin body and umbrella-like top")
                    answer2 = tc.input_commend(['y', 'n'], "Take this mushroom? (Can only take one at once) [y/n]"
                                               , text_check=True, getback=False, show_options=False)
                    if answer2 == 1:
                        pl.Roni.addItem("M1")
                        sn.NPC("Old witch", "You wicked witch!!! I told you not to do it!")
                        sn.player("Dont worry old hug, Im just about to go")
                        sn.player("Revertere hic!")
                        TheDarkForest(method='return spell')
                        break
                    elif answer2 == 2:
                        sn.player("I don't think that this is the right one")
                        pass

                if mushrooms_choose == 2:   # Trompeta Gray Saddle
                    sn.narrator("Hairy brown-gray hat shape like an umbrella. Medium size.")
                    answer2 = tc.input_commend(['y', 'n'], "Take this mushroom? (Can only take one at once) [y/n]"
                                               , text_check=True, getback=False)
                    if answer2 == 'y':
                        pl.Roni.addItem("M2")
                        sn.NPC("Old witch", "You wicked witch!!! I told you not to do it!")
                        sn.player("Dont worry old hug, Im just about to go")
                        sn.player("Revertere hic!")
                        TheDarkForest(method='return spell')
                        break
                    elif answer2 == 'n':
                        sn.player("I don't think that this is the right one")
                        pass

                if mushrooms_choose == 3:   # Death Earthball
                    sn.narrator("Round red top with white spots. Medium size.")
                    answer2 = tc.input_commend(['y', 'n'], "Take this mushroom? (Can only take one at once) [y/n]"
                                               , text_check=True, getback=False)
                    if answer2 == 'y':
                        pl.Roni.addItem("M3")
                        sn.NPC("Old witch", "You wicked witch!!! I told you not to do it!")
                        sn.player("Dont worry old hug, Im just about to go")
                        sn.player("Revertere hic!")
                        TheDarkForest(method='return spell')
                        break
                    elif answer2 == 'n':
                        sn.player("I don't think that this is the right one")
                        pass
                if mushrooms_choose == 4:   # Hairy Grisette
                    sn.narrator("Hairy white-gray rounded top. Medium size.")
                    answer2 = tc.input_commend(['y', 'n'], "Take this mushroom? (Can only take one at once) [y/n]"
                                               , text_check=True, getback=False)
                    if answer2 == 'y':
                        pl.Roni.addItem("M4")
                        sn.NPC("Old witch", "You wicked witch!!! I told you not to do it!")
                        sn.player("Dont worry old hug, Im just about to go")
                        sn.player("Revertere hic!")
                        TheDarkForest(method='return spell')
                        break
                    elif answer2 == 'n':
                        sn.player("I don't think that this is the right one")
                        pass

                if mushrooms_choose == 5:   # Cloudy Brittlegill
                    sn.narrator("Big mushroom with large unconventional brown-gray hat")
                    answer2 = tc.input_commend(['y', 'n'], "Take this mushroom? (Can only take one the once) [y/n]"
                                               , text_check=True, getback=False)
                    if answer2 == 'y':
                        pl.Roni.addItem("M5")
                        sn.NPC("Old witch", "You wicked witch!!! I told you not to do it!")
                        sn.player("Dont worry old hug, Im just about to go")
                        sn.player("Revertere hic!")
                        TheDarkForest(method='return spell')
                        break
                    elif answer2 == 'n':
                        sn.player("I don't think that this is the right one")
                        pass

                if mushrooms_choose == 6:
                    break

            pass
        # Go back to the Forest
        elif answer == 3:
            sn.player('Revertere hic...')
            TheDarkForest(method='return spell')


def oldMansion():
    sn.narrator('You enter an old mansion')
    sn.narrator("A focal point of local legends, what seems to be a deserted old mansion looms ahead.")
    sn.narrator("The mansion is definitely in a state of disrepair - the rusty iron gate hangs by a single hinge,")
    sn.narrator("tall weeds over what must have been a garden,")
    sn.narrator(" plants growing over the brick walls and covering the windows, even unwashed… scorch marks?")
    sn.narrator("You could swear you caught a glimpse of something in one of the windows…")


    while True:
        options = ["Explore the outside", "Enter the mansion", "Go back to the Forest"]
        answer = tc.input_commend(options, "Would you like to do?[Enter number]", text_check=False, getback=False)
        # Explore the outside
        if answer == 1:
            sn.narrator("I will stay here.")
            sn.narrator('You see an old witch, a dog and sleeping dragon')
            while True:
                options = ["Talk with the old witch", "Pet the dog", "Examine the sleeping dragon", "Go back"]
                answer = tc.input_commend(options, "Would you like to do?[Enter number]", text_check=False,
                                          getback=False)
                # Talk with the old witch
                if answer == 1:
                    if pl.Roni.checkBag("M4") and pl.Roni.checkBag("GC"):
                        sn.narrator(f"You approach the old witch with Hairy Grisette in your hand.")
                        sn.NPC("Old Witch", "Ho! How did you? Who are you?!")
                        sn.NPC("Old Witch", "Now. Now I can finish th potion.... wait a few minutes please")
                        sn.narrator("The old witch go inside the mansion...")
                        sn.narrator("...")
                        sn.narrator("After 30 minutes she got out, she give you the potion.")
                        sn.NPC("Old Witch", "This is yours, do your best.")
                        pl.Roni.addItem("B1")
                        sn.player("I will.")
                    elif pl.Roni.checkBag("GC"):
                        sn.narrator("You approach to the old witch, you can tell she notice you but try to ignore.")
                        sn.player("Hey, can you help me? I had got some questions.")
                        sn.NPC("Old witch", "...")
                        sn.player("Please, it to help another young witch today, and possibly more in the future.")
                        sn.NPC("Old witch", "What? What do you want?")
                        sn.player("I came from Eastwood, I want the gallows today, and something smells bad over there")
                        sn.player("Additionally, I got a tip that I can find answer here.")
                        sn.NPC("Old witch", "... The gallows... The executor... It was all my fault... "
                                            "and I cand do nothing")
                        sn.player("Tell me what happened.")
                        sn.NPC("Old witch", "I was young and stupid, this was a mistake."
                                            " I summon him, to destroyed my enemies")
                        sn.NPC("Old witch", "The demonic soldier of Fortune... Belthazor")
                        sn.player("I thing he is mention in the Book of Shadows")
                        sn.narrator("I tries to vanquished him, but I lack of one ingredient")
                        sn.player("Why cant you get it?")
                        sn.NPC("Old witch", "He made a deal with the blind witch, my former enemies "
                                            "I tried to destroyed")
                        sn.NPC("Old witch", "She guard the cave in The Dark Forest prevent me to enter "
                                            "and get the mushroom.")
                        sn.player("I can help you, tell me what mushroom you need and I will steal it from her.")
                        sn.NPC("Old witch", "You would do it? ... Ok. If you can bring me back 'Hairy Grisette' "
                                            "I can finish the potion")
                        sn.NPC("Old witch", "With that, you can vanquish Belthazor and make it stop")
                        sn.player("I will do it. Trust me")
                    else:
                        sn.NPC("old witch", "...")

                    pass
                # Pet the dog
                elif answer == 2:
                    sn.narrator("The dog run to you and start to lick your face.")
                    sn.player("Hello doggy!")
                    sn.NPC("Dog", "I like Red Peppers :) Every pepper I find I hide in my stash!")
                    pass
                # Examine the sleeping dragon
                elif answer == 3:
                    sn.narrator("You approach to the dragon, but nothing happen.")
                    pass
                # Go back
                elif answer == 4:
                    sn.player('Enough with the exploration')
                    break
            pass
        # Enter the mansion
        elif answer == 2:
            sn.narrator("I will check the inside")
            sn.narrator('you see a picture, armor and old rune')
            while True:
                options = ["Picture", "Armor", "Old rune", "Nothing (go back)"]
                answer = tc.input_commend(options, "What would you like to examine?[Enter number]", text_check=False,
                                          getback=False)
                # Picture
                if answer == 1:
                    sn.player("This is an ugly picture.")
                    pass
                # Armor
                elif answer == 2:
                    sn.player("There is a lot of res pepper in this armor.")
                    pl.Roni.addItem("L9")
                    pass
                # Old rune
                elif answer == 3:
                    sn.narrator("This is an old rune.")
                    sn.player("Very boring...")
                    pass
                # Nothing (go back)
                elif answer == 4:
                    sn.player('enough with the exploration.')
                    break
            pass
        # Go back to the Forest
        elif answer == 3:
            sn.player('Revertere hic...')
            TheDarkForest(method='return spell')


def TheSwamp(method='walk'):
    sn.narrator("The mud pulls at your feet as you approach the swamp, every step is taxing.")
    sn.narrator("As you push on you see rotten planks forming a small hut on stakes, above the murky waters.")
    sn.narrator("At the balcony sits an old man with a fishing pole,")
    sn.narrator("in the lamplight reflected from the swamp one could think he’s made from the same mildewed wood as "
                "the house and the rod.")
    sn.narrator("You shudder to think what he may catch in these waters, thankfully the basket next to him sits empty.")

    if method == 'walk':
        sn.narrator('Go to the swamp...')
    elif method == 'spell':
        sn.narrator('teleport to the swamp')
    while True:
        options = ["Go deep into the swamp", "Go to the old hut"]
        answer = tc.input_commend(options, "Would you like to do?[Enter number]", text_check=False)
        # Go deep into the swamp
        if answer == 1:
            sn.narrator("You start to goo deeper into the swamp.")
            sn.narrator("There is a runic curving in one of the stones you passed by.")
            sn.player("This is an Elder's sign, I know how to read it.... let's see")
            sn.player("If you want out, use the spell: Locum Tutum")
            TheSwamp = Swamp()
            TheSwamp.move()
            pass
        # Go to the old hut
        elif answer == 2:
            print('Go to the old hut')
            sn.narrator('Inside the hut living a fisherman and his wife')
            while True:
                options = ["Talk to the fisherman", "Talk to the fisherman's wife", "Live the hut"]
                answer = tc.input_commend(options, "Would you like to do?[Enter number]", text_check=False, getback=False)
                # Talk to the fisherman
                if answer == 1:
                    sn.NPC('Fisherman', 'Im am a fisherman')
                    sn.NPC('Fisherman', 'She always call me... the demon... I am so afraid...')
                    sn.NPC('Fisherman', "She seeks out powerful men who become helpless against her magic then feeds"
                                        " on their testosterone with her razor-sharp tongue")
                    sn.player("She is a witch renounces all human emotion and makes a pact with darkness to protect "
                              "herself from heartbreak")
                    sn.player("Succubus")
                    sn.NPC('Fisherman', "Can you destroy her?")
                    sn.player("Yes, but I need thing for the spell to work. I need to check the Book of Shadows")
                elif answer == 2:
                    sn.narrator("The women look very old, more like the Fisherman\'s mom the wife")
                    sn.NPC('Fisherman\'s wife', 'Im am young, but... but...')
                    sn.NPC("Fisherman's wife", "The Demon! HE stole my life force to regain his youth!")
                    sn.NPC("Fisherman's wife", "He was old, and after what he done to me... no more...")
                    sn.player("I read about him... Javna.")
                    sn.player("I need to check the Book of Shadows.")
                    sn.NPC('Fisherman\'s wife', 'Help me please.')
                    sn.player("Dont worry, I will do whatever I can.")
                elif answer == 3:
                    sn.narrator('You live the hut')
                    break
            pass
        # Return to the town square
        elif answer == 3:
            sn.player('I should go back..')
            Unknown_road(method='back from')


def VampireDen():
    sn.narrator("The abandoned house is indifferent to your arrival, a feeling you'd wish to share.")
    sn.narrator("The wooden planks lining the fence and blocking the windows seem bleached,")
    sn.narrator("so do the weeds that grow freely about the parched garden.")
    sn.narrator("Everything seems to thirst, except for a neat row of beautiful blood-red roses, "
                "growing in rusty-red soil.")
    sn.narrator("...")

    if pl.Roni.checkBag("V1"):
        sn.narrator("You rub a few drops of Holy Water on your palm and gingerly reach for the doorknob, "
                    "it opens with ease. ")
        sn.narrator("As you enter the abandoned house your mind is instantly jarred by the unexpected size,")
        sn.narrator("the floor is big and lavish and exquisite red roses decorate the long table at the "
                    "center.")
        sn.narrator("As you gape at the sheer size of it all your eyes finally focus on 6 pale bedraggled "
                    "figures seated at the table,")
        sn.narrator("recoiling slightly from your presence, and a regal looking woman lounging at their head.")
        sn.NPC("Vampire lady", "Go ahead")
        sn.narrator("she tells you in an amused manner")
        sn.NPC("Vampire lady", "Say it.")
        sn.player("It's smaller on the outside")
        sn.NPC("Vampire lady", "Ok, that's a first. Now - what brings you to Our castle, witch?")

        while True:
            options = ["I came for Blood meal", "Nothing, I should go back"]
            answer = tc.input_commend(options, "Choose your answer [Enter number]", text_check=False, getback=False)

            # I came for Blood meal
            if answer == 1:
                if pl.Roni.checkBag("V2"):
                    sn.player("Flowers")
                    sn.NPC("Vampire lady", "I will offer you a seat next to our queen to talk about flora.")
                    sn.narrator("She take you upstairs, to a large dining table with dozen vampires. Between them, "
                                "the vampire queen")
                    sn.narrator("As you reach the subject of fertiliser the queen grins,")
                    sn.NPC("Vampire Queen", "Surely we can come to an arrangement, a witch of your calibre must be able"
                                            " to guide a few lost souls here.")
                    sn.NPC("Vampire Queen", "Better be food to Us and our family than begging on the streets.")
                    sn.narrator("You casually place the bottle of holy water on the table, idly spinning it.")
                    sn.NPC("Vampire Queen", "So you’d dare threaten Us? In Our own castle? We could have been friends")
                    sn.player("I did not come to threaten your highness, I came to slay you.")
                    sn.NPC("Vampire Queen", "A splash of priest juice won’t do more than a slight burn to me")
                    sn.narrator("You toss the bottle of holy water up - ")
                    sn.narrator("the vampires’ eyes are glued to it as it hits the ceiling in a splash.")
                    sn.narrator(" But as the others leap away from the table the queen sits firmly,")
                    sn.narrator("determined to make a show of force here - holy water would not be enough.")
                    sn.narrator("Maybe even the wooden stake in your hands wouldn't be enough if she wasn't so caught "
                                "up on the spectacle.")
                    sn.narrator("You drive into her chest with one hand as the queen's hand belatedly tries to grab "
                                "the stake - ")
                    sn.narrator("so you let go of the stake and grab onto her shoulders,")
                    sn.narrator("slamming her into the dining table and driving the stake to her heart.")
                    sn.narrator("The easy regicide makes for a compelling argument to the rest of the vampires")
                    sn.narrator("to flee this city for good.")
                    sn.narrator("You return a few minutes later realizing you forgot the blood-meal in your spectacle.")
                    pl.Roni.addItem("G5")
                    break
                else:
                    sn.player("I came for the Blood meal")
                    sn.NPC("Vampire lady", "Ha Ha... child, you will have to take it directly from the vampire queen.")
                    sn.player("The vampire queen? I can not deal with her right now, holy water isn't enough")
                    break
            if answer == 2:
                sn.player("Nothing, I should go back")
                break
    else:
        sn.narrator("Steeling yourself for whatever lurks inside, you reach for the doorknob.")
        sn.narrator("At that moment dozens of phantoms assault you - until you let go of the door. ")
        sn.narrator("Nothing to do but turn back and come back better prepared. ")


def HuntedHouse():
    sn.narrator("The door is open, so you let yourself in...")

    if pl.Roni.checkBag("P1"):
        sn.narrator("You feel cold sweat cover your skin at the sound of silence, your ears stand ready for a sudden "
                    "shriek.")
        sn.narrator("The couple greets you warmly again, as you ask about your goal - the ghost’s bones.")
        sn.NPC("The Husband", "Never seen no bones round here, young lady")
        sn.NPC("The Wife", "But you are welcome to look, love. Maybe take a look at our gallery before the ghost will "
                           "disturb us again?")
        sn.narrator("You grudgingly accept.")
        sn.narrator("As you’re taken through the “gallery” and through the entire “creative process” - ")
        sn.narrator("that created EACH AND EVERY ONE of these things,")
        sn.narrator(" you notice something surprisingly white-ish in this sea of brown, black and green.")
        sn.NPC("The Wife", "Oh, this? A dog unearthed some driftwood in our yard and we put it to good use.")
        sn.NPC("The Husband", "The white colour beneath the dirt is nice, isn’t it?")
        sn.player("Driftwood here? Unearthed? ")
        sn.narrator("You rub the “driftwood” with a piece of discarded cloth and lo and behold - these are bones.")
        sn.narrator("A shriek builds in the heart of the house and the ghost begins to manifest,")
        sn.narrator("you quickly uncork the mixture and pour it onto the bones.")
        sn.narrator("As you pour the mixture onto the bones they hiss and slightly crack, ")
        sn.narrator("but the sculptures remain standing, and the ghost does not form.")
        sn.player("Thank you for your hospitality, make sure you get enough sleep")
        sn.player("and only make sculptures if you truly feel that’s right for you.")
        sn.narrator("The air feels warmer as you leave the joyous sculptures and refuse to have your likeness "
                    "sculpted.")
        sn.narrator("...")
        Signs.quest_end()
        sn.narrator("https://www.timeanddate.com/countdown/to?iso=20220318T16&p0=676&msg=4&font=cursive&csz=1")
        pass
    else:
        sn.narrator("If houses had a moral compass, this one would be evil.")
        sn.narrator("The windows seem to reflect the same starless sky regardless of the time")
        sn.narrator("and a heavy blanket of silence covers the grounds despite a buffeting wind.")
        sn.narrator("A high shriek pierces that blanket, stealing the air from your lungs -")
        sn.narrator("but for a moment so short, so free of evidence, it may have never happened.")
        sn.narrator("...")
        sn.narrator("Then it happens again, must be the haunted house then.")
        sn.narrator("An adult couple with a desperate need for sleep greets you as warmly as they can,")
        sn.narrator("offering tea before remembering all the cups were shattered.")
        sn.narrator("You look a bit around the house and see sculptures abound, big and small, depicting humanoid "
                    "figures or just strange symbols.")
        sn.NPC("The Husband", "Sleepin’ gets rough at times, so the missus and I build dem sculptures you see around ‘ere")
        sn.NPC("The Wife", "I think the ghost may like it. we tend to get a few hours of silence after building one, "
                           "but we’re running out of space and ideas")
        sn.NPC("The Husband", "Ghosts don’ appreciate repetition, young lady")
        sn.NPC("The Wife", "Will you help us and banish this ghost? We’d so like to have a full night for ourselves… To sleep.")
        sn.narrator("The ghost begins to screech and manifest in the living room, ")
        sn.narrator("so given you’ve seen enough art for one day, it feels like a good time to leave.")
        sn.player("I will get back here and help you. Goodbye for now. Stay safe.")
        pass
