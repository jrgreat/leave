
import base64
import requests

import logging
import time
import re
import json
import sys
import getopt
import smtplib
import xlwt
import subprocess
import threading
from jenkinsapi.jenkins import Jenkins


LOGGER = logging.getLogger(__name__)


JENKINS_FOLDER_URL = "http://192.168.121.131:3001/"
def create_jenkins_server_obj(jenkins_foloer_url = JENKINS_FOLDER_URL):
    jenkins_server_obj = Jenkins(jenkins_foloer_url,
                                 username='admin',
                                 password='11a9b0e7d28c75a67adc348123b73e1f6f',
                                 lazy=True,
                                 ssl_verify=False)
    return jenkins_server_obj

def start_jenkins_job(jenkins_server_obj, job_name, data):
    try:
        jenkins_server_obj.build_job(job_name, params=data)
    except ValueError as e:
        LOGGER.info("caught an acceptable exception [{}]".format(e))
    except Exception as e:
        LOGGER.info("jenkins start job error is : [{}]".format(e.message))
        return
    job_instance = jenkins_server_obj.get_job(job_name)
    LOGGER.info("sleep 30s for Jenkins SYNC")
    time.sleep(30)
    last_build_number = job_instance.get_last_buildnumber()
    LOGGER.info("last build number is: [{}]".format(last_build_number))
    build_dict = job_instance.get_build_dict()
    build_url = build_dict[last_build_number]
    LOGGER.info("last launched build_url is: [{}]".format(last_build_number))
    LOGGER.info("job [{}] started".format(build_url))
    return last_build_number
def run_a_job():
    jenkins_obj = create_jenkins_server_obj()
    start_jenkins_job(jenkins_obj, "first_job", None)



username = 'admin'
api_token = '110c5a0c065b536fb6e250d0d35a06682b'
passwd = '11111'
auth =(username, api_token)
#auth = base64.b64encode(f'{username}:{api_token}'.encode()).decode()

#response = requests.get(jenkins_url, headers=headers)
url = "http://192.168.121.131:3001/job/hello/build"
JENKINS_CRUMB_URL = "http://192.168.121.131:3001/crumbIssuer/api/json"

def request_work(url):
    header={'Authorization':f'Basic{auth}', 
        'Jenkins-Crumb':'8956907924167809ec0f61f50f32a593afc0d9af599fa93baec28177e6034a08',
        'Cookie':'JSESSIONID.efe34042=node0oop3cv508bkd1llivp06uan1d1.node0'}
    response = requests.post(url)
    response=requests.post(url, auth=auth, headers=header, verify=False)
    if response.status_code != 201:
        raise Exception("can't connect to jenkins server!")


def session_work(url):
    #session = requests.Session()
    #session.auth = (username, api_token)
    #crumb_json = (session.get("http://192.168.121.131:3001/crumbIssuer/api/json", verify=False))
    #jenkins = session.post(url, headers = {'Jenkins-Crumb':'8956907924167809ec0f61f50f32a593afc0d9af599fa93baec28177e6034a08'}, verify=False)
    
    with requests.Session() as s:
        s.auth = auth
        crumb = s.get(JENKINS_CRUMB_URL).json()['crumb']
        s.headers.update({"token": api_token,"Jenkins-Crumb":crumb})
        resp = s.post(url)
        if resp.status_code != 201:
            raise Exception("can't connect to jenkins server!")        


class test_tick:
    tick = 0
    def __init__(self):
        test_tick.tick += 1
    

if __name__=="__main__":
    #request_work(url)
    session_work(url)



