# from aiogram import Bot, Dispatcher, types, executor 
# from logging import basicConfig, INFO 
# from bs4 import BeautifulSoup
# import requests
# from config import token 

# bot = Bot(token=token)
# dp = Dispatcher(bot)
# basicConfig(level=INFO)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer("Hello")


# @dp.message_handler(commands='parsing')
# async def start(message:types.Message):
#     await message.answer("Start parsing")
    
#     url = "https://barmak.store/category/Acer/"
#     response = requests.get(url=url)
#     soup = BeautifulSoup (response.text, 'lxml')
#     titles = soup.find_all('div', class_ = 'tp-product-tag-2')
#     prices = soup.find_all('span', class_ = 'tp-product-price-2 new-price')

#     # print (titles) 
#     for title,price in zip(titles,prices):
#             true_price = "".join(price.text.split())
#             print (title.text,price.text)
#             await message.answer(f"{title.text} - {true_price} \n")

# def parsing_vizitka():
#      url = 'https://new.vizitka.kg/blog'
#      respons = requests.get(url=url)
#      sopo = BeautifulSoup (respons.text, 'lxml')
#      news = sopo.find('div', class_ = "content mt-20 mt-lg-0" )
#      data = sopo.find_all('span', class_ = "me-40")

# for news, data in zip('news','data'):
#      true_data = "".join(data.text.split())
    
# executor.start_polling(dp)