# req: 1. host info is stored in a yaml file

import paramiko
import logging
import yaml

LOGGER = logging.getLogger(__name__)
#logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',level=logging.DEBUG)

def get_host_info(yaml_file="host.yaml"):
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    data = yaml.safe_load(file_data)
    print(data)
    for key,value in data.items():
        yield value[0]


def connnect_to_host(host_ip, username,password,cmd='ls -l'):
    #LOGGER.info("start to connect host!")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host_ip,port=22,username=username,password=password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    result = stdout.read()
    print(result)
    #LOGGER.info("ended the session.")


if __name__=="__main__":
    #connnect_to_host()
    hostG = get_host_info()
    no_1 = next(hostG)
    host_name = no_1['name']
    host_ip = no_1['ip']
    host_password = no_1['password']
    user = no_1['user']
    connnect_to_host(host_ip,user,host_password)
    pass