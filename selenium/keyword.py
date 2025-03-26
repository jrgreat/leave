from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
import csv

"""
        try:
            element = WebDriverWait(browser , .5).until(lambda x: x.find_element(By.XPATH, '//*[@id="read_tpc"]/a[3]'))
        except Exception as e:
            raise e
"""

def get_hash_code(text_info):
    pattern = re.compile(r'[a-zA-Z0-9]{40}')
    match_grp = re.search(pattern, text_info)
    if match_grp:
        return match_grp.group()
    else:
        return 0
def get_video_name(text_info):
    pattern = re.compile(r'^([^\n]*)')
    match_grp = re.search(pattern, text_info)
    if match_grp:
        return match_grp.group()
    else:
        return 0 

def write_to_csv(csv_filename, data):
    with open(csv_filename, 'a', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file)
        for row in data:
            writer.writerow(row)


URL_PREFIX = "https://t66y.com/thread0806.php?fid=15&search=&page="
URL_PAGE_START = 1
URL_PAGE_END = 150
KEY_WORD1 = "神級女優經典"
KEY_WORD2 = "【验证全码】" 

if __name__=="__main__":

    browser = webdriver.Chrome()
    for page in range(URL_PAGE_START, URL_PAGE_END):
        url = URL_PREFIX + str(page)
        browser.get(url)
        #time.sleep(3)
        try:
            element = WebDriverWait(browser , .5).until(lambda x: x.find_element(By.XPATH, '//td/h3/a'))
        except Exception as e:
            #print(e)
            print("page {} end".format(page))
            break       
                                        
        item_list = browser.find_elements(By.XPATH,'//td/h3/a')
        ignore = 0
        csv_data = list()
        for item in item_list:
            #ignore += 1
            #if ignore <= 18:
            #    continue
            if KEY_WORD1 in item.text:
                #print("FOUND!")
                print(item.get_attribute('href'))
                print(item.text)
    print("Done")

    



