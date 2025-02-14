from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

url='http://www.google.com'

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

driver.get(url)

search=driver.find_element(By.NAME,'q')
search.send_keys("python")
search.send_keys(Keys.RETURN)

driver.find_element(By.XPATH,'//*[@id="Xod3Ie"]/div/div/div[1]/div/div/span/a').click()