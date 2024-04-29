from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import token 
import logging, time, sqlite3 #не забудьте sqlite3

bot = Bot(token=token)
dp = Dispatcher(bot)
memory = MemoryStorage()
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect("ojak_users.db")
cursor = connection.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
               id INTEGER, 
                username VARCHAR(300),
               first_name VARCHAR(300),
               last_name VARCHAR(300),
               created VARCHAR(300)

                
);
""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS ojak(
               last_name VARCHAR(200),
               first_name VARCHAR (200),
               created VARCHAR (200)    
);
""")

start_buttons =  [


        types.KeyboardButton("Меню"),
        types.KeyboardButton("О нас"),
        types.KeyboardButton("Адрес"),
        types.KeyboardButton("Заказать еду")        
        ]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)


@dp.message_handler(commands='start')
async def start(message:types.Message):
    cursor.execute(f"SELECT id FROM users WHERE id = {message.from_user.id};")
    result = cursor.fetchall()
    print(result)
    if result == []:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?);",
                    (message.from_user.id, message.from_user.username,
                        message.from_user.first_name, message.from_user.last_name,
                        time.ctime() ))
        cursor.connection.commit()
    await message.answer(f"{message.from_user.full_name} Здраствуйте", reply_markup=start_keyboard)

@dp.message_handler(text='Меню')
async def menu(message:types.Message):
    await message.answer("Шашлыки:  https://nambafood.kg/ojak-kebap", reply_markup=start_keyboard)

@dp.message_handler(text='О нас')
async def about(message:types.Message):
        await message.answer('''Кафе "Ожак Кебап" на протяжении 18 лет радует своих гостей с изысканными турецкими блюдами в особенности своим кебабом.

Наше кафе отличается от многих кафе своими доступными ценами и быстрым сервисом.

В 2016 году по голосованию на сайте "Horeca" были удостоены "Лучшее кафе на каждый день" и мы стараемся оправдать доверие наших гостей.

Мы не добавляем консерванты, усилители вкуса, красители, ароматизаторы, растительные и животные жиры, вредные добавки с маркировкой «Е». У нас строгий контроль качества: наши филиалы придерживаются норм Кырпотребнадзор и санэпидемстанции. Мы используем только сертифицированную мясную и рыбную продукцию от крупных поставщиков
''')
        
@dp.message_handler(text='Адрес')
async def address(message:types.Message):
     await message.answer("Наш адрес: 234، 246 Курманжан-Датка ул., Ош")
     
executor.start_polling(dp)