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
        self.addresses[6, 8] = 0
        self.addresses[1, 4] = 10

    def get_location(self, x_pos, y_pos):
        return self.addresses[x_pos, y_pos]

    def print_quarter(self):
        print(self.addresses)

    def goto(self, x_pos, y_pos):
        location_index = self.addresses[x_pos, y_pos]
        # hunted house
        if location_index == 0:
            sn.narrator('This is the place')
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
        self.addresses[8, 5] = 0
        self.addresses[2, 4] = 10

    def angle_index(self, angle):
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
            print('out of maze')
            return True
        elif self.maze[self.y][self.x] == self.goal_cave:
            print('cave')
            return True
        elif self.maze[self.y][self.x] == self.goal_naked_tree:
            print('naked_tree')
            return True
        else:
            return False

    def blockCheck(self, x, y):
        isBlock = False
        print('blockCheck, x = {}, y = {}'.format(x,y))
        if x < 0 or x > self.width or y < 0 or y > self.height:
            print('out of maze')
            isBlock = True
        elif self.maze[y][x] == self.wall:
            print('wall')
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

        self.get_location()
        self.printMaze()
        self.ifTarget()


class Swamp:
    def __init__(self):
        self.correct_path = ['stone',  'tree', 'mud']
        self.options = ['Stone', 'Tree', 'Fog', 'Mud', 'Locum Tutum']
        self.path = []

    def move(self):
        while True:
            sn.narrator('There are in the swamps a lot of trees, stones, deep mud and places with heavy fog')
            answer = tc.input_commend(self.options, "Which way is for you to go?[Enter number]", getback=False)
            if answer == 'locum tutum':
                TheSwamp(method='spell')
            else:
                self.path.append(answer)
                print(self.path)
                if len(self.path) >= len(self.correct_path):
                    if self.path[-len(self.correct_path)::] == self.correct_path:
                        print('Found it!')


def intro_town_square():
    Locations = ['Tavern', 'Church', 'Gallows', 'Quarter A', 'Quarter B', 'Apothecary', 'Unknown road']
    Signs.townSquare()
    sn.narrator("You can see around you:")
    # Signs.options(Locations)
    # answer = input("Where to you want to go?")
    # answer = tc.input_check(answer, Locations, "Where to you want to go?")
    answer = tc.input_commend(Locations, "Where to you want to go?", getback=False)
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
    sn.narrator('...')
    sn.narrator('After few second you notice a strange looking man near the fireplace... He does not seems local...')
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
            sn.narrator("You decided to sit down, while the drunk people tell tales...")
            sn.NPC("Drunk 1", "I tell you... you can buy rare and illegal stuff in there.")
            sn.NPC("Drunk 2", "You did not been there, you dont have the guts.")
            sn.NPC("Drunk 1", "So how do I now that it is locate on Quarter A, at: x=X(1), y=X(2).")
            sn.NPC("Drunk 2", "You are full of bullshit.")
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
    sn.narrator('As you enter to the Main Hall, The pastor finish the pray and leave the Alter to enter the Sacristy')
    sn.narrator('Bunch of prayer are still in the Main Hall')
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
            sn.narrator('At the moment you try to enter the Sacristy, the poster stop you and say:')
            sn.NPC('Poster', "Greeting my child.. You have the eyes of a nun")
            sn.NPC('Poster', "However, you don\'t look like one..")
            pass

        # Stay in the Main Hall
        elif answer == 3:
            print('Stay in the Main Hall')
            while True:
                options_3 = ["Investigate the church", "Talk to the prayers", "Go somewhere else"]
                answer_3 = tc.input_commend(options_3, "What would you wish to do?[Enter number]", text_check=False)
                # Investigate the church
                if answer_3 == 1:
                    print('Investigate the church')
                    sn.narrator("As Investigate the church, you notice a pile of Wooden Stake")
                    sn.player("This could be useful.")
                    pl.Roni.addItem("V2")
                    pass
                # Talk to the prayers
                elif answer_3 == 2:
                    print('Talk to the prayers')
                    sn.narrator("You approach the prayers")
                    sn.player("May the lord guide us in our ways.")
                    sn.NPC("Prayer 1", "He is. Always.")
                    sn.NPC("Prayer 2", "You can take a Wooden Stake before you go out.. Good for lord's protection")
                    sn.player("Thank you, I will")
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
            print('Approach the stage')
            pass
        elif answer == 3:     # Return to the town square
            sn.player('I should go back..')
            intro_town_square()


def Quarter_A():
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
            Square.print_quarter()
        elif answer == 2:
            sn.player('I should go back..')
            intro_town_square()


def Quarter_B():
    phi_pos = list(range(0, 360, 45))  # 10 options,from 1 to 10
    rho_pos = list(range(1, 10))  # 10 options,from 1 to 10
    Circular = CircularQuarter(len(rho_pos), len(phi_pos))
    print('Quarter B')
    while True:
        print()
        options = ['Visit a house']
        answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False)
        if answer == 1:
            print('choose house address:')
            rho_loc = int(tc.input_commend(rho_pos, 'enter rho coordinate:', show_options=True, text_check=True))
            phi_loc = int(tc.input_commend(phi_pos, 'enter phi coordinate:', show_options=True, text_check=True))
            print(Circular.get_location(rho_loc, phi_loc))
            Circular.goto(rho_loc, phi_loc)
            Circular.print_quarter()
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
            print('enter the store')
            sn.narrator("Hey this is the apothecary store")
            while True:
                options_2 = ["Purchase ingredients", "Look inside my bag", "Mix potion", "Exit the store"]
                answer_2 = tc.input_commend(options_2, "Would you like enter the store?[Enter number]",
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
                if answer_2 == 3:
                    print('Mix potion')
                    sn.narrator("You need to choose the potion you would like to mix.")
                    sn.narrator("The potion recipe is documented in the Book of Shadows")
                    choose_potion = input("What is the title of the page in th Book of Shadows? >>").lower()
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
            sn.narrator(f'You have {IT.itemdict[req_item]}')
            sn.player('I can pass this now')
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
        sn.narrator('You walk slowly into the tall trees in the beginning of the forest')
        sn.narrator('As you enter you notice a large bolder with engraving:')
        sn.narrator('To Return: \" Revertere hic \" ')
    elif method == 'return spell':
        sn.narrator('Everything around you start to spin very fast')
        sn.narrator('and then, vanished and replaced by familiar place - The forest entrance')
    sn.narrator('What do you want to do?')
    while True:
        options = ["Enter into th forest", "Return"]
        answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False, getback=False)
        if answer == 1:  # The Dark Forest
            print('Enter The Dark Forest')
            Maze = ForestMaze()
            while True:
                options = ['w', 's', 'd', 'a', 'Revertere hic']
                answer = tc.input_commend(options, "Which direction?", text_check=True, getback=False)
                Maze.move(answer)
                # Old Mansion
                if Maze.maze[Maze.y][Maze.x] == Maze.goal_mansion:
                    print('out of maze')
                    options = ["Go out form the forest", "Stay in the forest"]
                    answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False,
                                              getback=False)
                    # Go out form the forest
                    if answer == 1:
                        print('Go out form the forest')
                        oldMansion()
                    # Stay in the forest
                    elif answer == 2:
                        print('Stay in the forest')
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
                        print('Go inside the Cave')
                        Cave()
                    # Stay in the forest
                    elif answer == 2:
                        print('Stay in the forest')
                        pass
                # Lost Man
                elif Maze.maze[Maze.y][Maze.x] == Maze.goal_naked_tree:
                    sn.narrator('As you walk through th woods, a unique looking tree appear in front of you.')
                    sn.narrator('A abnormal tree, that look naked in fist sight')
                    sn.narrator(
                        'Despite it almost without leaves, it manege to prosper more then all the other trees in the forest')
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
                    sn.narrator("tiny blue mushroom with thin body and umbrella-like top")
                    answer2 = tc.input_commend(['y', 'n'], "Take this mushroom? (Can only take one at once) [y/n]"
                                               , text_check=True, getback=False)
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
    while True:
        options = ["Explore the outside", "Enter the mansion", "Go back to the Forest"]
        answer = tc.input_commend(options, "Would you like to do?[Enter number]", text_check=False, getback=False)
        # Explore the outside
        if answer == 1:
            print('Explore the outside')
            sn.narrator('You see an old witch, a god and sleeping dragon')
            while True:
                options = ["Talk with the old witch", "Pet the dog", "Examine the sleeping dragon", "Go back"]
                answer = tc.input_commend(options, "Would you like to do?[Enter number]", text_check=False,
                                          getback=False)
                # Talk with the old witch
                if answer == 1:
                    print('Talk with the old witch')
                    pass
                # Pet the dog
                elif answer == 2:
                    print('Pet the dog')
                    pass
                # Examine the sleeping dragon
                elif answer == 3:
                    print('Examine the sleeping dragon')
                    pass
                # Go back
                elif answer == 4:
                    sn.player('enough with the exploration')
                    break
            pass
        # Enter the mansion
        elif answer == 2:
            print('Enter the mansion')
            sn.narrator('you see a picture, armor and old rune')
            while True:
                options = ["Picture", "Armor", "Old rune", "Nothing (go back)"]
                answer = tc.input_commend(options, "What would you like to examine?[Enter number]", text_check=False,
                                          getback=False)
                # Picture
                if answer == 1:
                    print('Picture')
                    pass
                # Armor
                elif answer == 2:
                    print('Armor')
                    pass
                # Old rune
                elif answer == 3:
                    print('Old rune')
                    pass
                # Nothing (go back)
                elif answer == 4:
                    sn.player('enough with the exploration')
                    break
            pass
        # Go back to the Forest
        elif answer == 3:
            sn.player('Revertere hic...')
            TheDarkForest(method='return spell')


def TheSwamp(method='walk'):
    if method == 'walk':
        sn.narrator('Go to the swamp...')
    elif method == 'spell':
        sn.narrator('teleport to the swamp')
    while True:
        options = ["Go deep into the swamp", "Go to the old hut"]
        answer = tc.input_commend(options, "Would you like to do?[Enter number]", text_check=False)
        # Go deep into the swamp
        if answer == 1:
            print('Go deep into the swamp')
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
