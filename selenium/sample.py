from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


driver.get("http://www.baidu.com")
input = driver.find_element(By.XPATH,'//*[@id="kw"]')
input.send_keys("hello,world")


driver.find_element(By.XPATH, '//*[@id="su"]').click()

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="2"]/div/h3/a').click()

time.sleep(30)
