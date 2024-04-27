# from aiogram import Bot, Dispatcher, types,executor
# from config import token 

# bot = Bot(token = token)
# dp = Dispatcher(bot)

# @dp.message_handler(commands='start')
# async def start (message:types.message):
#     await message.answer("Привет!!!")
    
# @dp.message_handler(commands='help')
# async def help(message:types.message):
#     await message.answer("Чем могу помочь?")

# @dp.message_handler(text='Привет')
# async def hello(message:types.message):
#     await message.answer("Привет,как дела?")
        
# @dp.message_handler(text='привет')
# async def hello(message:types.message):
#     await message.reply("Привет,как дела?")
# @dp.message_handler(commands='test')
# async def test(message:types.message):
#     await message.answer_location(0, 0)
#     await message.answer_photo("https://media.architecturaldigest.com/photos/63079fc7b4858efb76814bd2/16:9/w_4000,h_2250,c_limit/9.%20DeLorean-Alpha-5%20%5BDeLorean%5D.jpg")
# @dp.message_handler(commands='kino')
# async def kino(message:types.message):
#     await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMGvsz9Rn-Sa7TwluiikBHTjq9zsr7SgMOKQKHrUFWIw&s")

# executor.start_polling(dp)


