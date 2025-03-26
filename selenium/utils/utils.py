from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select

import time
import re


def get_browser(url):
    browser = webdriver.Chrome()
    browser.get(url)
    return browser

def find_input_box(browser, xpath):
    elem = browser.find_element(By.XPATH,xpath)
    if elem.tag_name != "input":
        raise Exception("didn't find correct type !")
    return elem

def get_elem(browser, **kwargs):
    """sumary_line
    
    Keyword arguments:
    kwargs: 
        - xpath
        - type
        - name
    Return: elem
    """
    if not kwargs['xpath']:
        raise Exception("must contain xpath")
    elem = browser.find_element(By.XPATH, kwargs['xpath'])
    if kwargs['type']:
        if elem.get_attribute('type') != kwargs['type']:
            raise Exception("didn't find correct type!")
    if kwargs['name']:
        if kwargs['name'] and elem.text != kwargs['name']:
            raise Exception("didn't find correct type!")  
    #return Select(elem)
    return elem


    