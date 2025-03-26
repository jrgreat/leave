from utils.utils import *
from selenium.webdriver import ActionChains
import time

EDIT_URL = "https://letcode.in/edit"
BUTTON_URL = "http://sahitest.com/demo/clicks.htm"
RAIDO_CHECKBOX_URL = "https://letcode.in/radio"
SELECT_URL = "https://letcode.in/dropdowns"
TABLE_URL = "https://letcode.in/table"
FRAME_URL = "https://letcode.in/frame"


def button_practise(url):
    browser = get_browser(url)
    time.sleep(2)
    xpath = '/html/body/form/input[2]'
    item = dict()
    item['xpath'] = xpath
    item['name'] = None
    item['type'] = "button"
    elem = get_elem(browser, **item)
    if elem.is_enabled():
        elem.click()
    else:
        print("not enabled button!")
    actions = ActionChains(browser)
    actions.double_click(elem).perform()
    time.sleep(30)

def radio_checkbox_practises(url):
    browser = get_browser(url)
    time.sleep(2) 
    radio_xpath = '/html/body/app-root/app-radio-check/section[1]/div/div/div[1]/div/div/div[1]/div/label[1]'
    item = {'xpath':radio_xpath, 'type': None, 'name':None}
    radio = get_elem(browser, **item)
    radio.click()
    check_box_xpath = '/html/body/app-root/app-radio-check/section[1]/div/div/div[1]/div/div/div[6]/label[2]/input'
    item = {'xpath':check_box_xpath, 'type': "checkbox", 'name':None}
    check_box = get_elem(browser, **item)
    if not check_box.is_selected():
        print("had been checked, no operations!")
    else:
        check_box.click()

    time.sleep(30)

def select_practises(url):
    browser = get_browser(url)
    time.sleep(2) 
    select_xpath = '//*[@id="fruits"]'  
    item = {'xpath':select_xpath, 'type': None, 'name':None}  
    select = get_elem(browser, **item)
    select.select_by_index(1)
    select.select_by_index(2)
    #select.deselect_by_index(1)
    #select.deselect_all()
    select.select_by_value('0')
    #select.deselect_all()
    all = select.options
    for each in all:
        print(each.text)
    select.select_by_visible_text('Apple')

def table_practise(url):
    browser = get_browser(url)
    time.sleep(2) 
    #td_path = '//*[@id="shopping"]/tfoot/td[2]/b'  
    table_path = '//*[@id="shopping"]'
    item = {'xpath':table_path, 'type': None, 'name':None}  
    table = browser.find_element(By.ID, 'shopping')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        row_data = [col.text for col in cols]
        print(row_data)    

def frame_practise(url):
    browser = get_browser(url)
    time.sleep(2) 
    #elem = browser.find_element(By.XPATH, '//*[@id="firstFr"]')
    #browser.switch_to.frame(elem)
    #input_elem = browser.find_element(By.XPATH, '/html/body/app-root/app-frame-content/div/div/form/div[1]/div/input')
    #input_elem.send_keys("hello,world!")
    #browser.switch_to.default_content()
    elem2 = browser.find_element(By.XPATH, '//*[@id="aswift_8"]') 
    browser.switch_to.frame(elem2)
    button = browser.find_element(By.XPATH, '//*[@id="aw0"]')
    button.click()
    time.sleep(30)

DRAG_URL = "https://letcode.in/draggable"
def drag_practise(url): 
    browser = get_browser(url)
    time.sleep(2)
    actions = ActionChains(browser)
    elem = browser.find_element(By.XPATH, '//*[@id="sample-box"]')
    #for i in range(10):  
    actions.drag_and_drop_by_offset(elem, 198,257).drag_and_drop_by_offset(elem, 261,452).drag_and_drop_by_offset(elem, 74,254).perform()
    time.sleep(30)

SLIDER_URL = "https://letcode.in/slider"
def slider_practise(url):
    browser = get_browser(url)
    time.sleep(2)    
    slider_xpath = '//*[@id="generate"]'
    elem = browser.find_element(By.XPATH, slider_xpath)
    actions = ActionChains(browser)
    for i in range(10):
        actions.click_and_hold(elem).move_by_offset(5, 0).release().perform()
        time.sleep(1)

    time.sleep(30)

SORT_URL = "https://letcode.in/sortable"
def sort_practise(url):
    browser = get_browser(url)
    time.sleep(2)   
    item_xpath = '//*[@id="sample-box1"]'
    actions = ActionChains(browser)
    elem = browser.find_element(By.XPATH, item_xpath)  
    actions.click_and_hold(elem).move_by_offset(100, 0).release().perform()
    time.sleep(5)
 


if __name__=="__main__":
    
    
    """
    xpath = '//*[@id="fullName"]'
    elem = find_input_box(browser, xpath)
    elem.send_keys("hello,world")
    elem.send_keys(Keys.TAB)
    print(elem.is_enabled())
    elem2 = find_input_box(browser, '//*[@id="noEdit"]')
    print(elem2.is_enabled())
    time.sleep(300)
    """
    #button_practise(BUTTON_URL)
    #radio_checkbox_practises(RAIDO_CHECKBOX_URL)
    #select_practises(SELECT_URL)
    #table_practise(TABLE_URL)
    #drag_practise(DRAG_URL)
    #slider_practise(SLIDER_URL)
    sort_practise(SORT_URL)




