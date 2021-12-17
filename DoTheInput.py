import asyncio
from multiprocessing import Manager
import threading

from ActionState import action_state



async def input_reader(qu):
    while True:
        user_input = input()
        print(user_input)
        # if action_state["isNarrating"]:
        #     action_state["isSkipping"] = True
        #     return
        qu.put_nowait(user_input)
        print("message in")
        print(user_input)



async def init_reader(qu):
    # asyncio.create_task(read_input())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return await loop.run_until_complete(input_reader(qu))
    # asyncio.set_event_loop(k)
    # asyncio.run(input_reader(qu))
    # threading.Thread(target=init_reader).start()
