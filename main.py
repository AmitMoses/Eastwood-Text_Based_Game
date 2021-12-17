import asyncio
import multiprocessing
import threading
from multiprocessing import Process, shared_memory
from multiprocessing.managers import BaseManager

import Signs
import Sentences as sn
import TestCheck as tc
import Areas
from DoTheInput import init_reader
from StoryStructure import get_start_zone


async def intro():
    sn.narrator('Hey Roni')
    sn.narrator('You woke up alone in middle of unfamiliar road...')
    sn.narrator('The sky are cloudy and everything look grey...')
    sn.narrator('You notice that not far from you there is an old sign...')
    print()
    sn.player('What is this place?')

    Signs.openSign()
    answer = await tc.input_commend(['yes', 'no'], "Do you wish to continue? [yes/no]", show_options=False, getback=False)
    return answer


async def main(qu):

    reader = tc.MosesReader(qu)
    writer = sn.Writer()

    await get_start_zone(reader, writer).do_story()

    return
    # Definitions:


class Moses_q(BaseManager):
    pass

Moses_q.register("Qu", asyncio.Queue)

async def ionit_moses(q):
    return await asyncio.create_task(init_reader(q))

async def init_main(qu):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return await loop.run_until_complete(main(qu))

async def method_name():

    m = Moses_q()
    m.start()

    s = m.Qu()
    #
    # s=""
    pool = multiprocessing.Pool(2)
    pool.apply_async(func=init_main, args=(s,))
    pool.apply_async(func=init_reader, args=(s,))

    # Process(target=ionit_moses, args=(s,)).start()
    # Process(target=main, args=(s,)).start()


if __name__ == '__main__':
    asyncio.run(method_name())
    # asyncio.run(main())
    # asyncio.run(init_reader())
