from utils.utils import *
from selenium.webdriver import ActionChains
import time

LOGIN_URL = "http://127.0.0.1:5000/auth/login"
ITEM_TEMPLATE = {'xpath':None, 'type':None, 'name':None}

def test_login(url):
     browser = get_browser(url)
     time.sleep(2)
     mail_box_xpath = '//*[@id="exampleInputEmail1"]'
     password_xpath = '//*[@id="exampleInputPassword1"]'
     item_template = ITEM_TEMPLATE
     item_template['xpath'] = mail_box_xpath
     mail_box = get_elem(browser, **item_template)
     mail_box.send_keys("great2000_1@163.com")
     item_template['xpath'] = password_xpath
     password = get_elem(browser, **item_template)
     password.send_keys("111111")
     login_button_xpath = '/html/body/div/div/div/div[2]/form/div[3]/button'
     item_template['xpath'] =  login_button_xpath
     login_button = get_elem(browser, **item_template) 
     login_button.click()
     item_template['xpath'] = '/html/body/div/div/div[2]/ul/li[1]/div[2]/div[1]/a'
     elem = get_elem(browser, **item_template)
     elem.click()
     time.sleep(300)

if __name__=="__main__":
    test_login(LOGIN_URL)