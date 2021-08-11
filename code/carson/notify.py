
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Users\cclot\pdx_code\class_wallaby\code\carson\chromedriver.exe')
response = driver.get("https://www.americanmuscle.com/sr-performance-mustang-muffler-delete-axle-back-exhaust-with-polished-tips-407862.html")
print(response)
# response = requests.get('https://www.americanmuscle.com/corsa-mustang-xtreme-cat-back-exhaust-black-tips-21040blk.html')
# #data = response.json()
# #print(response.text)
# soup = BeautifulSoup(response.content, "html.parser")
# results = soup.find(id="page")
# #print(results.prettify())
# elements = results.find_all("div",class_="status")
# #print(elements)
# for element in elements:
#     #print(element, end ="\n"*2)
#     status = element.find("span", class_="stock_status")
#     #print(f'Corsa{status}')


# response = requests.get('https://www.americanmuscle.com/sr-performance-mustang-muffler-delete-axle-back-exhaust-with-polished-tips-407862.html')


# soup = BeautifulSoup(response.content, "html.parser") 
# results = soup.find(id="page")
# time.sleep(4)

# elements = results.find_all("div",class_="status")
# #print(elements)
# name = results.find_all("h1", class_="headline product_name")
# #print(name)
# for element in elements:
#     #print(element, end ="\n"*2)
#     status = element.find("span", class_="stock_status")
#     delivery = element.find("p", class_="estimate_message")
 
#     #print(status)
#     print(delivery)

