import Sentences as sc
import Signs
import TestCheck as tc
import numpy as np
import player as pl


class SquareQuarter:
    def __init__(self, max_x, max_y):
        self.addresses = np.random.randint(1, 4, size=(max_x, max_y), dtype=int)
        self.addresses[5, 8] = 0

    def get_location(self, x_pos, y_pos):
        return self.addresses[x_pos, y_pos]

    def print_quarter(self):
        print(self.addresses)

    def goto(self, x_pos, y_pos):
        location_index = self.addresses[x_pos, y_pos]
        if location_index == 0:
            sc.narrator('This is the place')
        elif location_index == 1:
            sc.narrator('You knock the door, but there is no answer')
        elif location_index == 2:
            sc.narrator('You enter into random house...')
            sc.narrator('...while the dwelling eating supper')
            sc.NPC('Scared kid', 'Mommy I am afraid! who is the strange woman?')
            sc.player('I\'m sorry, wrong house')
        elif location_index == 3:
            sc.narrator('As you approach the house someone shout from the window')
            sc.NPC('dweller', 'GET OUT YOU FILTHY WITCH!')


class CircularQuarter:
    def __init__(self, radios_num, angle_num):
        self.addresses = np.random.randint(1, 4, size=(radios_num, angle_num), dtype=int)
        self.dAngle = int(360/angle_num)
        self.addresses[9, 5] = 0

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
            sc.narrator('This is the place')
        elif location_index == 1:
            sc.narrator('You knock the door, but there is no answer')
        elif location_index == 2:
            sc.narrator('Someone open you the door')
            sc.NPC('Random man', 'You are not my pizza')
        elif location_index == 3:
            sc.narrator('As you approach the house someone shout from the window')
            sc.NPC('dweller', 'phh... another woman, another witch...')


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
        self.goal_man = 7
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
        elif self.maze[self.y][self.x] == self.goal_man:
            print('man')
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
                sc.narrator("You blocked by a tree")
            else:
                self.y = self.y - 1

        elif direction == 's':
            if self.blockCheck(self.x, self.y+1):
                sc.narrator("You blocked by a tree")
            else:
                self.y = self.y + 1

        elif direction == 'd':
            if self.blockCheck(self.x+1, self.y):
                sc.narrator("You blocked by a tree")
            else:
                self.x = self.x + 1

        elif direction == 'a':
            if self.blockCheck(self.x-1, self.y):
                sc.narrator("You blocked by a tree")
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
            sc.narrator('There are in the swamps a lot of trees, stones, deep mud and places with heavy fog')
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
    sc.narrator("You can see around you:")
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
    sc.narrator('From the outside it looks uninviting, dark and dire.')
    sc.narrator('Large and small stones and intricate stone carvings make up most of the building\'s outer structure.')
    sc.narrator('It\'s near impossible to see through the dusty windows, but the coldness from within can be felt '
                'outside.')
    sc.narrator('As you enter the tavern through the dirty, metal door,')
    sc.narrator('you\'re welcomed by thick air and a feeling of discomfort.')
    sc.narrator('The bartender is coughing into a dirty napkin and makes no effort to acknowledge your pressence.')
    sc.narrator('It\'s as dire inside as it is on the outside.')
    sc.narrator('Hardwooden beams support the upper floor and the huge, dusty lamps attached to them.')
    sc.narrator('The walls are loaded with pictures, though the dust and cobwebs stops you from taking a closer look.')
    sc.narrator('The tavern itself is almost completely abandoned. The few people inside could be locals, could be '
                'lost souls,')
    sc.narrator('but whoever they are, it\'s about the clearest sign you can get, telling you you don\'t belong.')
    sc.narrator('...')
    sc.narrator('After few second you notice a strange looking man near the fireplace... He does not seems local...')
    print()
    while True:
        options = ["Order from the bartender", "Approach the people", "Talk to the stranger"]
        answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False)
        if answer == 1:     # Order from the bartender
            print('Order from the bartender')
            pass
        elif answer == 2:     # Approach the people
            print('Approach the people')
            pl.Roni.addItem(pl.Roni.KeyItems[0])
            pass
        elif answer == 3:     # Talk to the stranger
            print('Talk to the stranger')
            pass
        elif answer == 4:     # Return to the town square
            sc.player('I should go back..')
            intro_town_square()


def Church():
    Signs.church()
    sc.narrator('Surrounded by poor looking peasants, there was the church...')
    sc.narrator('Thick walls made of light white stone.')
    sc.narrator('Tall middle tower with ancient cross on top of it.')
    sc.narrator('A great gate with enormous wooden doors between two statues.')
    sc.narrator('Well kept gardens with fragrant flowers, gorgeous trees and many bushes decorate the outside...')
    sc.narrator('As you enter to the Main Hall, The pastor finish the pray and leave the Alter to enter the Sacristy')
    sc.narrator('Bunch of prayer are still in the Main Hall')
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
                    print('Holy water')
                    pass
                # Nothing
                elif answer_1 == 2:
                    print('Nothing')
                    pass
                # Go somewhere else
                elif answer_1 == 3:
                    break
                # Return to the town square
                elif answer_1 == 4:
                    sc.player('I should go back..')
                    intro_town_square()

        # Sacristy
        elif answer == 2:
            print('Sacristy')
            sc.narrator('At the moment you try to enter the Sacristy, the poster stop you and say:')
            sc.NPC('Poster', "Greeting my child.. You have the eyes of a nun")
            sc.NPC('Poster', "However, you don\'t look like one..")
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
                    pass
                # Talk to the prayers
                elif answer_3 == 2:
                    print('Talk to the prayers')
                    pass
                # Go somewhere else
                elif answer_3 == 3:
                    break
                # Return to the town square
                elif answer_3 == 4:
                    sc.player('I should go back..')
                    intro_town_square()

        # Return to the town square
        elif answer == 4:
            sc.player('I should go back..')
            intro_town_square()


def Gallows():
    Signs.gallows()
    sc.narrator('You\'re pulled to the sound of an excited crowd surrounding a raised wooden structure, from which an '
                'empty noose hangs.')
    sc.narrator('A young woman is led across the creaky platform by a heavyset man clad in black towards the rope '
                'swinging in the breeze.')
    while True:
        options = ["Blend in the crowd", "Approach the stage"]
        answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False)
        # Blend in the crowd
        if answer == 1:
            print('Blend in the crowd')
            pass
        # Approach the stage
        elif answer == 2:
            print('Approach the stage')
            pass
        elif answer == 3:     # Return to the town square
            sc.player('I should go back..')
            intro_town_square()


def Quarter_A():
    Square = SquareQuarter(10, 10)
    while True:
        options = ['Visit a house']
        answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False)
        if answer == 1:
            # SquareQuarter = np.zeros((10, 10))
            print('Quarter A')
            print('choose house address:')
            x_pos = list(range(1, 11))      # 10 options,from 1 to 10
            y_pos = list(range(1, 11))      # 10 options,from 1 to 10
            x_loc = int(tc.input_commend(x_pos, 'enter X coordinate:', show_options=False, text_check=True))
            y_loc = int(tc.input_commend(y_pos, 'enter Y coordinate:', show_options=False, text_check=True))
            print(x_loc, y_loc)
            Square.goto(x_loc, y_loc)
            Square.print_quarter()
        elif answer == 2:
            sc.player('I should go back..')
            intro_town_square()


def Quarter_B():
    phi_pos = list(range(0, 360, 45))  # 10 options,from 1 to 10
    rho_pos = list(range(1, 10))  # 10 options,from 1 to 10
    Circular = CircularQuarter(len(rho_pos), len(phi_pos))
    print('Quarter B')
    while True:
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
            sc.player('I should go back..')
            intro_town_square()


def Apothecary():
    Signs.apothecary()
    sc.narrator('As you get close, you notice a wooden store and little garden')
    sc.narrator('From the outside this store looks nice and traditional with apothecary sign on it.')
    sc.narrator('It has been built with white pine wood and has walnut wood decorations.')
    sc.narrator('Small, half rounded windows brighten up the house and have been added to the house in a very '
                'asymmetric way.')
    sc.narrator('You can see long shelf full of potion behind the windows.')
    sc.narrator('the garden looks well-kept full of variety of flora')
    while True:
        options = ["Go inside the store", "Walk to the garden"]
        answer = tc.input_commend(options, "Would you like enter the store?[Enter number]", text_check=False)
        # Go inside the store
        if answer == 1:
            print('enter the store')
            pass
        # Walk to the garden
        elif answer == 2:
            print('Walk to the garden')
            pass
        # Return to the town square
        elif answer == 3:
            sc.player('I should go back..')
            intro_town_square()


def Unknown_road(method='from town'):
    if method == 'from town':
        sc.narrator('After five minutes walk you encounter a sign:')
        Signs.danger()
        req_item = pl.Roni.KeyItems[0]
        if pl.Roni.checkBag(req_item):
            sc.narrator('You have {}'.format(req_item))
            sc.player('I can pass this now')
        else:
            sc.player('I can\'t take this risk rigt now, I should go back...')
            intro_town_square()
        sc.narrator('After ten more minutes you encounter a crossroad')
    elif method == 'back from':
        sc.narrator('You walk all the way back to the crossroad')
    while True:
        options = ["The Dark Forest", "The Swamps"]
        answer = tc.input_commend(options, "Where do you like to go?[Enter number]", text_check=False)
        if answer == 1:     # The Dark Forest
            TheDarkForest()
        elif answer == 2:   # The Swamps
            print('The Swamps')
            TheSwamp()
        elif answer == 3:   # return
            sc.player('I should go back..')
            intro_town_square()


def TheDarkForest(method='walk'):
    if method == 'walk':
        sc.narrator('You walk slowly into the tall trees in the beginning of the forest')
        sc.narrator('As you enter you notice a large bolder with engraving:')
        sc.narrator('To Return: \" Revertere hic \" ')
    elif method == 'return spell':
        sc.narrator('Everything around you start to spin very fast')
        sc.narrator('and then, vanished and replaced by familiar place - The forest entrance')
    sc.narrator('What do you want to do?')
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
                    print('cave')
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
                elif Maze.maze[Maze.y][Maze.x] == Maze.goal_man:
                    print('man')
                    options = ["Talk to the lost man", "Ignore the lost man"]
                    answer = tc.input_commend(options, "What would you like to do?[Enter number]", text_check=False,
                                              getback=False)
                    # Talk to the lost man
                    if answer == 1:
                        print('Talk to the lost man')
                    # Ignore the lost man
                    elif answer == 2:
                        print('Stay in the forest')
                        pass

        elif answer == 2:  # return
            sc.player('I should go back..')
            Unknown_road(method='back from')


def Cave():
    sc.narrator('You enter the cave')
    sc.narrator('You see an old witch-like lady and glooming mushrooms')
    while True:
        options = ["Talk with the witch", "Examine the mushrooms", "Go back to the Forest"]
        answer = tc.input_commend(options, "Would you like to do?[Enter number]", text_check=False, getback=False)
        # Talk with the witch
        if answer == 1:
            print('Talk with the witch')
            pass
        # Examine the mushrooms
        elif answer == 2:
            print('Examine the mushrooms')
            pass
        # Go back to the Forest
        elif answer == 3:
            sc.player('Revertere hic...')
            TheDarkForest(method='return spell')


def oldMansion():
    sc.narrator('You enter an old mansion')
    while True:
        options = ["Explore the outside", "Enter the mansion", "Go back to the Forest"]
        answer = tc.input_commend(options, "Would you like to do?[Enter number]", text_check=False, getback=False)
        # Explore the outside
        if answer == 1:
            print('Explore the outside')
            sc.narrator('You see an old witch, a god and sleeping dragon')
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
                    sc.player('enough with the exploration')
                    break
            pass
        # Enter the mansion
        elif answer == 2:
            print('Enter the mansion')
            sc.narrator('you see a picture, armor and old rune')
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
                    sc.player('enough with the exploration')
                    break
            pass
        # Go back to the Forest
        elif answer == 3:
            sc.player('Revertere hic...')
            TheDarkForest(method='return spell')


def TheSwamp(method='walk'):
    if method == 'walk':
        sc.narrator('Go to the swamp...')
    elif method == 'spell':
        sc.narrator('teleport to the swamp')
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
            sc.narrator('Inside the hut living a fisherman and his wife')
            while True:
                options = ["Talk to the fisherman", "Talk to the fisherman's wife", "Live th hut"]
                answer = tc.input_commend(options, "Would you like to do?[Enter number]", text_check=False, getback=False)
                # Talk to the fisherman
                if answer == 1:
                    sc.NPC('Fisherman', 'Im am a fisherman')
                elif answer == 2:
                    sc.NPC('Fisherman\'s wife', 'Im am a wife')
                elif answer == 3:
                    sc.narrator('You live the hut')
                    break
            pass
        # Return to the town square
        elif answer == 3:
            sc.player('I should go back..')
            Unknown_road(method='back from')
