import Sentences as sn
import TestCheck as tc
import player as pl


class TheBartender:
    def __init__(self):
        self.drinks = ['beer', 'wine']
        self.codewords = ['vampire kiss', 'black jin', 'red n black liqueur', 'mudbeer', 'honey whisky']
        self.name = "The Bartender"

    def speak(self, sentence):
        sn.NPC(self.name, sentence)

    def order(self):
        while True:
            order_ = input("Your order >> ")
            order_ = order_.lower()

            # Drink
            if order_ in self.drinks:
                self.speak("Here you go.")
                sn.player("Thank you.")

            # Nothing
            elif order_ not in self.codewords:
                self.speak("We do not serve it here")

            # vampire kiss
            elif order_ == self.codewords[0]:
                sn.narrator("The bartender looked behind you to varify nobody listen.")
                self.speak("I see...")
                self.speak("You ask to do a dangerous thing... ")
                sn.narrator("The bartender say it while pouring you a redish drink.")
                self.speak("Rumors says that the vampire hideout locate in Quarter B.")
                self.speak("SECTION:    [-sqrt(3)/2].")
                self.speak("AREA:       [8*PI].")
                sn.player("I cant just walk there without protection. I need to check the Book of Shadows")
                sn.player("Thanks for the drink.")

            # black jin
            elif order_ == self.codewords[1]:
                sn.narrator("The bartender looked behind you to varify nobody listen.")
                self.speak("I was in the black market... like every merchant.")
                self.speak("To get in you need to know the password: MATRIMIM.")
                sn.narrator("The bartender say it while pouring you a chaser of dark jin.")
                sn.player("Thanks for the drink.")

            # red & black liqueur
            elif order_ == self.codewords[2]:
                sn.narrator("The bartender looked behind you to varify nobody listen.")
                self.speak("So they sent you... Makes sense...")
                self.speak("Listen closely because wat Im about to say ain't a rumor.")
                self.speak("The executor at the gallows its human. He is a very powerful demon.")
                self.speak("Go to the gallows to figure out.")
                pl.Roni.addItem("GC")
                sn.player("I will investigate it.")

            # mudbeer
            elif order_ == self.codewords[3]:
                sn.narrator("The bartender looked behind you to varify nobody listen.")
                self.speak("You again... I can work with that...")
                self.speak("Have you ever been in The Swamps?")
                sn.player("No... Why?")
                self.speak("Today is your day... But not in the good way.")
                self.speak("There a rumors about demos that came to hunt the young woman and man of Eastwood")
                self.speak("Little I know about their powers, but their origin is in The Swamps")
                sn.player("Ok. Anything I should know about The Swamps?")
                self.speak("It is not shape like The Dark Forest, there is no map the will help you.")
                self.speak("There is a fisherman that live in there, you should investigate him")
                pl.Roni.addItem("URP")
                sn.player("Got it, thanks for the information")

            # honey whisky
            elif order_ == self.codewords[4]:
                sn.narrator("Suddenly, the bartender filled with joy. He look you directly in the eye")
                self.speak("Ha Ha! My favorite. It would be my honor to pour you this special one")
                sn.narrator("The bartender put a littel glass in front of you")
                sn.narrator("and filling it with the honey whisky")
                self.speak("You know... I should thank you... No. Whole Eastwood should!")
                self.speak("Maybe there is something I can help you with... Especially because tomorrow")
                sn.player("What happening tomorrow?")
                self.speak("You don't know already? really?.... So I will not spoil you")
                sn.player("Spoil what?")
                self.speak("Nevermind, listen, you should check your book, search the \"Charm of Love\"")
                self.speak("Take this, maybe it can help you find all the ingredient.")
                pl.Roni.addItem("URP")
                self.speak("Trust me, its all I can give you")
                sn.player("Got it, thank you, I will")

            self.speak("Something else?")
            answer = tc.input_commend(['y', 'n'], '[y/n]', show_options=False, getback=False)
            if answer == 'y':
                pass
            if answer == 'n':
                break

    def confront(self):
        self.speak("Greeting, What would you like to order?")
        # answer = input()
        self.order()


Bartender = TheBartender()

def main():
    Ned = TheBartender()
    Ned.confront()
    # Ned.order('11232')
    # Ned.order('aaa')
    # Ned.order('bbb')




if __name__ == '__main__':
    main()
