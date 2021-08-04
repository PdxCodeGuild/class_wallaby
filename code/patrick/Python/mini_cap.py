from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


user_input = 'corporate actions'
driver = webdriver.Chrome() #path to chrominium, inside (), is not needed if included in the same folder.
driver.get("https://www.google.com/search?q=related:&rlz=1C1ONGR_enUS958US958&tbm=nws&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwjvx6y-vpbyAhVRo54KHc6OBxsQpwV6BAgHECE&biw=929&bih=888&dpr=1")
try:
    g_search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@title='Search']")))
    g_search.clear()
    g_search.send_keys(user_input)
    g_search.submit()
   
    
    lnks=driver.find_elements_by_tag_name("href" and "a")
# traverse list
    for lnk in lnks:
    # get_attribute() to get all href
        print(lnk.get_attribute('href'))
   
    
except:                                                         
    pass