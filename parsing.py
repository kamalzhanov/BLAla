# from bs4 import BeautifulSoup
# import requests 

# def parsing_barmak():
#     url = "https://barmak.store/category/Acer/"
#     response = requests.get(url=url)
#     soup = BeautifulSoup (response.text, 'lxml')
#     titles = soup.find_all('div', class_ = 'tp-product-tag-2')
#     prices = soup.find_all('span', class_ = 'tp-product-price-2 new-price')
#     with open ('laptops.txt', 'w', enconding= 'utf-8') as file: 

#     # print (titles) 
#         for title,price in zip(titles,prices):
#             true_price = "".join(price.text.split())
#             print (title.text,price.text)
#             file.write(f"{title.text} - {true_price} \n")
# parsing_barmak()

    