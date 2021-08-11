from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/ThisPC/Downloads/chromedriver')
driver.get("https://www.americanmuscle.com/sr-performance-mustang-muffler-delete-axle-back-exhaust-with-polished-tips-407862.html")

print(driver)






# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

