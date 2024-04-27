# from aiogram import Bot, Dispatcher, types, executor
# from config import token 
# import logging

# bot = Bot(token)
# dp = Dispatcher(bot)
# logging.basicConfig(level=logging.INFO)

# start_buttons = [
#     types.KeyboardButton('О нас'),
#     types.KeyboardButton('Курсы'),
#     types.KeyboardButton('Контакты'),
#     types.KeyboardButton('Адрес'),
#     types.KeyboardButton('Записаться'),
# ]
# start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer(f"Привет {message.from_user.first_name}!", reply_markup=start_keyboard)
#     # await message.answer(f"{message}")

# @dp.message_handler(text="О нас")
# async def about(message:types.Message):
#     await message.reply("Geeks - это айти курсы в Бишкеке, Ташкенте и Оше! Основана в 2019")

# @dp.message_handler(text="Контакты")
# async def contacts(message:types.Message):
#     await message.answer_contact("0777121212", "Nurbolot", "Erkinbaev")
#     await message.answer_contact("0555141516", "Ulan", "Ashirov")
#     await message.answer_contact("+996 225 082021", "Geeks", "Admin")

# @dp.message_handler(text="Адрес")
# async def send_address(message:types.Message):
#     await message.answer("Отправляю местоположение...")
#     await message.answer_location(40.52, 72.8030)

# courses_buttons = [
#     types.KeyboardButton("Backend"),
#     types.KeyboardButton("Frontend"),
#     types.KeyboardButton("Android"),
#     types.KeyboardButton("iOS"),
#     types.KeyboardButton("UX/UI"),
#     types.KeyboardButton("Назад")
# ]
# courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_buttons)

# @dp.message_handler(text="Backend")
# async def back(message:types.Message):
#     await message.answer(" Backend — это внутренняя часть продукта, которая находится на сервере и скрыта от пользователей. Для ее разработки могут использоваться самые разные языки, например, Python, PHP, Go, JavaScript, Java, С#")

# @dp.message_handler(text="Frontend")
# async def front(message:types.Message):
#     await message.answer("Frontend — презентационная часть web приложений, информационной или программной системы, её пользовательский интерфейс и связанные с ним компоненты; применяется в соотношении с базисной частью системы, её внутренней реализацией, называемой в этом случае бэкендом")

# @dp.message_handler(text="Android")
# async def andr(message:types.Message):
#     await message.answer("Специалист занимается созданием приложений для мобильных устройств, которые используют операционную систему Android. А также решением сопутствующих задач – например, взаимодействием в команде, размещение ПО на Google Play, разработкой обновлений и новых версий программы.")

# @dp.message_handler(text="iOS")
# async def ios(message:types.Message):
#     await message.answer("iOS-разработчик, или iOS developer, — это программист, который пишет сервисы и программы для айфонов. Из-за особенностей устройств Apple и их операционной системы для них нужно писать специальный код. Основной язык, на котором пишут код iOS-разработчики, — Swift.")

# @dp.message_handler(text="UX/UI")
# async def uxui(message:types.Message):
#     await message.answer("UX/UI дизайнер — специалист, который проектирует и рисует интерфейсы цифровых продуктов: мобильных и веб-приложений, сайтов. Такой дизайнер может участвовать как в создании новых продуктов, так и помогать дорабатывать те, что уже запущены.")


# @dp.message_handler(text="Курсы")
# async def all_couses(message:types.Message):
#     await message.answer("Вот все наши курсы:", reply_markup=courses_keyboard)

# @dp.message_handler(text="Назад")
# async def backk(message:types.Message):
#     await message.answer("Хорошо",reply_markup=start_keyboard) 
    


# @dp.message_handler()
# async def not_found(message:types.Message):
#     await message.reply("Я вас не понял, введите /start")

# @dp.message_handler(text="Записаться")
# async def goha(message:types.Message):
#     await message.answer("Введите ФИО")

# executor.start_polling(dp)

