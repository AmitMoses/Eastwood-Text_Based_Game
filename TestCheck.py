import threading

import Sentences
from ActionState import action_state

class MosesReader():
    def __init__(self, message_q):
        self.message_q = message_q


    async def input(self, text=None):
        if text is not None:
            print(text)
        print("trying")
        ans = await self.message_q.get()
        print("got message from q")
        return ans

    async def input_check(self, user_input, valid_vec, text, text_check=True):
        # print(valid_vec)
        # print(user_input)
        if text_check:  # string to string input
            valid_vec = [str(item).lower() for item in valid_vec]
            user_input = user_input.lower()
            while user_input not in valid_vec:
                Sentences.instruction('please enter valid input')
                user_input = await self.input(text).lower()
        else:  # string to int input
            while user_input not in [str(x) for x in range(1, len(valid_vec) + 1)]:
                Sentences.instruction('please enter valid input')
                user_input = await self.input(text)
            user_input = int(user_input)
        return user_input

    # keydown tners input to cmd - please no

    async def input_commend(self, valid_vec, text, show_options=True, text_check=True, getback=True):
        text = text + "\n>"
        if getback:
            valid_vec.append('Return to the town square')
        if show_options:
            self.options_list(valid_vec)
        answer = input(text)
        answer = self.input_check(answer, valid_vec, text, text_check)
        return answer

    def options_list(names):
        for i in range(0, len(names)):
            print("{}.  {}".format(i + 1, names[i]))


if __name__ == "__main__":
    print("s")
