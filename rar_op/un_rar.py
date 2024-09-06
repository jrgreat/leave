import os
import sys
import utils.rar_op as decomp_tool
import utils.folder_op as file_op
import datetime

src_folder_path = "E:\\迅雷下载\\base\\"
base_folder = "E:\\迅雷下载\\base"

SIZE_LIMITATION = 1024 * 1024 # 1 MB   

if __name__=="__main__":
    new_folder_path = file_op.file_name_generate(base_folder)
    if not os.path.exists(new_folder_path):
        file_op.makedir(new_folder_path)
    files = os.listdir(src_folder_path)
    for item in files:
        (basename, extname)= os.path.splitext(os.path.basename(item))
        full_path = os.path.join(src_folder_path, item)
        print(full_path)
        dst_file_path = os.path.join(new_folder_path, item)
        if not os.path.isdir(full_path):
            size = os.path.getsize(full_path)
            if int(size) > int(SIZE_LIMITATION): 
                if extname in ['.7z','.zip','.rar']:
                    file_op.move_file(full_path, dst_file_path)
            else:
                continue
        (basename, extname)= os.path.splitext(os.path.basename(item))
        decomper = decomp_tool.rar_op(dst_file_path, new_folder_path)
        if ".7z" == extname:
            decomper.z7_extract_file()
            file_op.remove_file(dst_file_path) 
        if ".rar" == extname:
            decomper.extract_file()
            file_op.remove_file(dst_file_path) 
        if ".zip" == extname:
            decomper.zip_extract_file()
            file_op.remove_file(dst_file_path)  

                
    print("done")

