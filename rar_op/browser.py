
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def find_specific_name(browser, name:str):
    counter = 0
    element_list = browser.find_elements(By.XPATH, "//td/h3/a")
    for element in element_list:
        if name in element.text:
            #element.click()
            print(element.get_attribute('href')) 
 
    


if __name__ == "__main__":
    # 新版本写法
    browser = webdriver.Chrome(service=
        Service(r'E:\D\Tools\chromedriver-win64\chromedriver.exe'))
    # 旧版写法
    # browser = webdriver.Chrome(r'D:\software\PyCharmLib\chromedriver.exe')
    
    for i in range(1,20):
        page_part = "page" + str(i)
        url = "https://yj2306s.monster/pw/thread6.php?fid=22&" + page_part
        browser.get(url)

    browser.implicitly_wait(5)
    find_specific_name(browser, 'DVDMS')

    
    # 关闭浏览器
    browser.close()

