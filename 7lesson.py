# from aiogram import Bot, Dispatcher, types, executor
# from config import token 
# import requests, logging, aioschedule, asyncio

# bot = Bot(token=token)
# dp = Dispatcher(bot)
# logging.basicConfig(level=logging.INFO)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer(f"Привет {message.from_user.full_name}")

# async def hello_world():
#     print("Hello World")

# async def scheduler():
#     aioschedule.every().seconds.do(hello_world)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)

# async def on_startup(_):
#     asyncio.create_task(scheduler())

# executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
# 7