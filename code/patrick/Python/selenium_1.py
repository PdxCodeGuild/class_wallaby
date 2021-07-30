from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os 
import wget #has not been updated since 2015.

driver = webdriver.Chrome() #path to chrominium, inside (), is not needed if included in the same folder.
driver.get("https://instagram.com")
try: 
    # https://stackoverflow.com/questions/65921911/unable-to-locate-element-username-while-logging-in-instagram-with-selenium-hos
    #https://github.com/MariyaSha/WebscrapingInstagram/blob/main/WebscrapingInstagram_completeNotebook.ipynb
    # https://selenium-python.readthedocs.io/navigating.html#filling-in-forms
    #targeting the username first and then passing through keys and repeated for password.
    username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@name='username']"))) 
    username.send_keys("9713306619")
    password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@name='password']"))) 
    password.send_keys("Cascade!@3")
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    not_now= WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    not_now_1= WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    # Below is the roundabout way of using the search function, below that is the shortcut way using the url.
    # searchbox = WebDriverWait(driver, 6).until(EC.element_to_be_clickable(By.XPATH, "//input[@placeholder='Search']"))
    # searchbox = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    # keyword = "news"
    # searchbox.send_keys(keyword)
   
    # searchbox.send_keys(Keys.ENTER)
    # # time.sleep(1)
    # # searchbox.send_keys(Keys.ENTER)
    # # time.sleep(45)
    # # searchbox.send_keys(Keys.ENTER)
    
    keyword = "news" #what you want to search for
    driver.get("https://www.instagram.com/explore/tags/" + keyword + "/")
    time.sleep(5)

finally:
    n_scrolls = 10
    for i in range(1, n_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
    images = driver.find_elements_by_tag_name('img')
    images = [image.get_attribute('src') for image in images]
    images = images[:-2]
    print('Number of scraped images: ', len(images))
   
    path = os.getcwd()
    path = os.path.join(path, keyword[1:] + "s")
    os.mkdir(path)
    print(path)

    counter = 0    
    for image in images:
        save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
        wget.download(image, save_as)
        counter += 1


# try:
    
# finally:
#         pass
#     # finally: #if file already exists then this will save images with a different name protocol and not try to make a folder with the same name. WAS PLAYING AROUND WITH THIS WHEN NOT USING THE URL SEACH SHORTCUT. MULTIPLE ENTERS WERE REQUIRED.
#     #     for image in images:
#     #         save_as = os.path.join("C:\\Users\\patjo\\pdx_code\\class_wallaby\\code\\patrick\\Python\\ewss", str(counter) + '.jpg')
#     #         wget.download(image, save_as)
#     #         counter += 1

