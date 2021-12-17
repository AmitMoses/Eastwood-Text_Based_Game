
class Location:
    def __init__(self, reader, writer, move_function, history_state):
        self.reader = reader
        self.writer = writer
        self.move_function = move_function
        self.history_state = history_state

    def move_to_location(self, location_name):
        next_lo = self.move_function(location_name)(self.reader, self.writer, self.move_function, self.history_state)
        next_lo.do_story()

    def do_story(self):
        print("no")
