from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = "8068312783:AAFaX6Lz1Tw3bqXL32HTenGgpyR1d6UYmro"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text=['Calories'])
async def set_age(message):
    await message.answer('Напишите свой возраст.')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Напишите свой рост.')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Напишите свой вес.')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def set_send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    normal_clrs_w = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) - 161
    normal_clrs_m = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Норма калорий для женщины - {normal_clrs_w}.\n'
                         f'Норма калорий для мужчины - {normal_clrs_m}.')
    await state.finish()

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите слово "Calories", чтобы рассчитать дневную норму каллорий.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)