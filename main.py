import Signs
import Sentences as sn
import TestCheck as tc
import Areas


def intro():
    sn.narrator('Hey Roni')
    sn.narrator('You woke up alone in middle of unfamiliar road...')
    sn.narrator('The sky are cloudy and everything look grey...')
    sn.narrator('You notice that not far from you there is an old sign...')
    print()
    sn.player('What is this place?')

    Signs.openSign()
    answer = tc.input_commend(['yes', 'no'], "Do you wish to continue? [yes/no]", show_options=False, getback=False)
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


if __name__ == '__main__':
    main()
