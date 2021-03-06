import Signs
import Sentences as sn
import TestCheck as tc
import Areas
import player as pl


def intro():
    sn.narrator('Hey Roni')
    sn.narrator('You woke up alone in middle of familiar road...')
    sn.narrator('The sky are cloudy and everything look grey...')
    sn.narrator('You notice that not far from you there is an old sign...')
    print()
    sn.player('What is this place?')

    Signs.openSign()
    answer = tc.input_commend(['yes', 'no', 'always'], "Do you wish to continue? [yes/no]",
                              show_options=False, getback=False)
    return answer


def main():
    # Definitions:
    Locations = ['Tavern', 'Church', 'Gallows', 'Quarter A', 'Quarter B', 'Apothecary', 'Unknown road']

    # intro
    answer = intro()
    if answer.lower().strip() == "yes":
        sn.narrator('(EVERY THING LOOKS DIM)')
        sn.narrator('As you begin to walk towards Eastwood, you can barely fill the thin air around you...')
        sn.narrator('The path looks abandoned, like nobody take it for a while..')
        sn.narrator('You arrived to the middle of small town... Eastwood as the old sign described..')
        Areas.intro_town_square()

    elif answer.lower().strip() == "no":
        sn.player('Maybe another day..')

    elif answer.lower().strip() == "always":
        sn.narrator("...")
        sn.narrator("...")
        sn.narrator("...")
        sn.narrator("You encounter the hooded man from yesterday - your informer.")
        sn.NPC("Your informer", "Good morning Roni.")
        sn.narrator("He takes off his hood")
        sn.narrator("He had a very familiar face...")
        sn.NPC("Amit", "Yes, It was me all along.")
        sn.NPC("Amit", "I just want to tell you one thing - I love you Roni, more then anything else...")
        sn.NPC("Amit", "and...   I have one final surprise for you :)")
        sn.narrator("...")
        sn.NPC("Amit", "Check Moka :)")
        sn.narrator("...")
        Signs.end_pic()
        while True:
            pass


if __name__ == '__main__':
    main()
