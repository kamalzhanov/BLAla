from aiogram import Bot,Dispatcher,types,executor 
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from config import token 
import logging, time, sqlite3

bot = Bot(token = token)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect('loogis.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER,
               first_name VARCHAR (100),
               last_name VARCHAR (100),
               phone VARCHAR (100),
               region VARCHAR (30),
               created VARCHAR (30)

);
''')

start_buttons =[
    types.KeyboardButton("Регистрация"),
    types.KeyboardButton("Шаблон регистрации"),
    types.KeyboardButton("О нас")
] 

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет, я чат-бот карго компании Geeks",
    reply_markup=start_keyboard)

@dp.message_handler(text="Шаблон регистрации")
async def reeg(message:types.Message):
    await message.answer('''Для того чтобы зарегистрироваться вам нужно:
1. Введите имя:
2. Введите фамилию:
3. Введите номер:                         
4. Введите регион:                         
Вот эти данные нужны вам для регистрации       
                         ''')

class UserRegisterState(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
    region = State()

@dp.message_handler(text="Регистрация")
async def start_register(message:types.Message):
    await message.answer("Для регистрации в нашем карго нам нужно от вас:")
    await message.answer("Имя, Фамилия, Номер, Регион")
    await message.answer("Введите свое имя: ")
    await UserRegisterState.first_name.set()
    
@dp.message_handler(state=UserRegisterState.first_name)
async def get_first_name(message:types.Message,state:FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer("Введите фамилию: ")
    await UserRegisterState.last_name.set()

@dp.message_handler(state=UserRegisterState.last_name)
async def get_phone(message:types.Message,state:FSMContext):
    await state.update_data(last_name=message.text)
    await message.answer("Введите номер")
    await UserRegisterState.phone.set() 
       
@dp.message_handler(state=UserRegisterState.phone)
async def get_region(message:types.Message,state:FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Введите регион: ")
    await UserRegisterState.region.set()

@dp.message_handler(state=UserRegisterState.region)
async def get_user_date(message:types.Message,state=FSMContext):
    await state.update_data(region=message.text)
    result = await storage.get_data(user=message.from_user.id)
    await message.answer(f"{result}")
@dp.message_handler(text="О нас")
async def about(message:types.Message):
    await message.answer("Geeks - это лучшие курсы программирования!")
    await message.answer("Подробнее можете узнать на этом сайте https://geeks.kg/")
executor.start_polling(dp,skip_updates=True)   