"""
1. same folder
"""
import os
import re


#src_folder = "G:\\collections\\a4u_test\\a4u CD01"
src_folder = "G:\\collections\\ASIAN 4 YOU\\a4u CD10\\"
dst_folder = "G:\\collections\\a4u_test\\target\\"
import utils.folder_op as fop

star_name_list_with_path = fop.get_level1_sub_folder_names(dst_folder)


def create_star_name_list(star_name_list_with_path_par:list):
    star_name_list = list()
    if len(star_name_list_with_path_par) != 0:
        for star_name_with_path in star_name_list_with_path_par:
            star_name = star_name_with_path.split('\\')[-1]
            star_name_list.append(star_name)
    return star_name_list

def creat_gallery_name_list(folder_path):
    gallery_name_list = list()
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isdir(file_path):
            file_name = file.split(" ")[0]
            gallery_name_list.append(file_name)
    return gallery_name_list

def create_folder_name(exist_name_list:list):
    number_list = list()
    pattern = re.compile(r'\d+')
    for exist_name in exist_name_list:
        m = re.search(pattern, exist_name)
        if m:
            number_list.append(int(m.group()))
        else:
            print("error, can't match!")
    print(number_list)
    number_list.sort()
    print(number_list)
    last = int(number_list[-1]) + 1
    new_name = "gallery"+str(last)
    return new_name      

if __name__=="__main__":
    file_list = list()
    star_name_list = create_star_name_list(star_name_list_with_path) #target's star name
    
    for file in os.listdir(src_folder):
        file_path = os.path.join(src_folder, file) #stars in src folder
        if os.path.isdir(file_path):
            print("folder:", file_path)
            if file in star_name_list: # the star exist in target folder, need copy gallery folder one by one
                # go sub folder of the star to process each galleries
                for gallery in os.listdir(file_path):
                    dst_star_path = dst_folder + file
                    exist_gallery_list = creat_gallery_name_list(dst_star_path) #target/star/gallery
                    new_folder_name = create_folder_name(exist_gallery_list)
                    print(gallery)
                    src_path = os.path.join(file_path, gallery)
                    print(src_path)
                    dst_path = os.path.join(dst_star_path, new_folder_name)
                    print("now, copy [{}] to [{}]".format(src_path, dst_path))
                    fop.move_file(src_path, dst_path)
            else:
                dst_path = dst_folder + file
                fop.move_file(file_path, dst_path)  # the star does not exist in target folder, copy the whole folder ,easy!






