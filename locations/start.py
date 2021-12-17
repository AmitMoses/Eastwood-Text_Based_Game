import Signs
from locations.location import Location


class Start_location(Location):

    async def do_story(self):
        self.writer.narrator('Hey Roni')
        self.writer.narrator('You woke up alone in middle of an unfamiliar road...')
        self.writer.narrator('The sky are cloudy and everything look grey...')
        self.writer.narrator('You notice that not far from you there is an old sign...')
        print() #yes
        self.writer.player('What is this place?')

        Signs.openSign()
        answer = await self.reader.input_commend(['yes', 'no'], "Do you wish to continue? [yes/no]", show_options=False,
                                        getback=False)

        Locations = ['Tavern', 'Church', 'Gallows', 'Quarter A', 'Quarter B', 'Apothecary', 'Unknown road']

        # intro
        if answer.lower().strip() == "yes":
            self.writer.narrator('(EVERY THING LOOKS DIM)')
            self.writer.narrator('As you begin to walk towards Eastwood, you can barely fill the thin air around you...')
            self.writer.narrator('The path looks abandoned, like nobody take it for a while..')
            self.writer.narrator('You arrived to the middle of small town... Eastwood as the old sign described..')
            self.move_to_location("Areas")
        elif answer.lower().strip() == "no":
            self.writer.player('Maybe another day..')

