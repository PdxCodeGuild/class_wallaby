from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import requests


user_input = 'corporate actions'
driver = webdriver.Chrome() #path to chrominium, inside (), is not needed if included in the same folder.
driver.get("https://www.google.com/search?q=related:&rlz=1C1ONGR_enUS958US958&tbm=nws&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwjvx6y-vpbyAhVRo54KHc6OBxsQpwV6BAgHECE&biw=929&bih=888&dpr=1")
try:
    g_search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@title='Search']")))
    g_search.clear()
    g_search.send_keys(user_input)
    g_search.submit()
   
    lst = [] 
    lnks=driver.find_elements_by_tag_name("href" and "a")
# traverse list
    for lnk in lnks:
    # get_attribute() to get all href
        lst.append(lnk.get_attribute('href'))
   
    
except:                                                         
    pass       
lst_1 = []

for url in lst:

    try:    
        if 'javascript:void' in url:
            pass
        elif 'google' not in url:
            lst_1.append(url)
    except:
        print("error")



for x in lst_1:
    r = requests.get(x)
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    #print(soup.prettify())    
    table = soup.find_all("div" and "p")
    print(table)

# for the in lst_1:
#     driver.get(the)
#     try:
#         stuff =WebDriverWait(driver, 20).until(driver.find_element_by_tag_name('p'))
#         print(stuff)
#     except:
#         print("error")