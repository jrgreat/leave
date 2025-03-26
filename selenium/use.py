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


url = "https://https--bbs2.b1201369.cc/pw/thread.php?fid=110"
KEY_WORD1 = "【驗證全碼】"
KEY_WORD2 = "【验证全码】" 

if __name__=="__main__":

    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(3)
                                    
    item_list = browser.find_elements(By.XPATH,'//td/h3/a')
    ignore = 0
    csv_data = list()
    for item in item_list:
        ignore += 1
        if ignore <= 18:
            continue
        item.click()
        browser.implicitly_wait(10)
        time.sleep(2)
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
        #url = item.get_attribute('href')     
        elem = browser.find_element(By.XPATH,'//*[@id="read_tpc"]')
        info_text = elem.text

        if KEY_WORD1 or KEY_WORD2 in info_text:
            hash_code = get_hash_code(info_text)
            video_name = get_video_name(info_text)
            if hash_code == 0:
                continue
            csv_data.append((video_name, hash_code))
            print(video_name, hash_code)
        else:
            continue
        browser.switch_to.window(browser.window_handles[0])
    browser.close()
    csv_file_name = "report.csv"
    write_to_csv(csv_file_name,csv_data)



