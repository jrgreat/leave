import os
import shutil
import datetime

SIZE_LIMITATION = 4 * 1024 * 1024 # 1 MB 

def remove_file(file_path):
    os.remove(file_path)

def makedir(file_path):
    os.makedirs(file_path)

def move_file(src_file_path, dst_file_path):
    try:
        shutil.move(src_file_path, dst_file_path)
    except Exception as e:
        pass

def file_name_generate(base_folder):
    now = datetime.datetime.now()
    new_folder_name = now.strftime('%Y-%m-%d %H:%M:%S')
    new_folder_name = new_folder_name.split(' ')[0]
    new_folder_path = os.path.join(base_folder , new_folder_name)
    return new_folder_path

def traverse_dir(path, dest):
    file_list = list()
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            print("folder:", file_path)
            traverse_dir(file_path, dest)
        else:
            print("file：", file_path)
            size = os.path.getsize(file_path)
            if int(size) > int(SIZE_LIMITATION):
                file_list.append(file_path)
    if len(file_list) > 1:
        print("now , moving [{}] to [{}]".format(path, dest))
        move_file(path, dest)
    else:
        for file in file_list:
            #path = os.path.join(,file)
            print("now , moving [{}] to [{}]".format(file, dest))
            move_file(file, dest) 

def get_level1_sub_folder_names(path):
    folder_name_list = list()
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            print("folder:", file_path)
            folder_name_list.append(file_path)
    return folder_name_list

