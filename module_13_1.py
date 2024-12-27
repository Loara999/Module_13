import time
import asyncio

async def start_strongman(name, power):
    for n in range(1, 6):
        print(f'Силач {name} поднял шар под номером {n}.')
        await asyncio.sleep(1 / power)
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    strongmen = [('Дима',2), ('Вася',3), ('Вова', 5)]
    tasks = [asyncio.create_task(start_strongman(n, p)) for n, p in strongmen]
    for t in tasks:
        await t
