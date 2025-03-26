import os
import utils.folder_op as fop

folder_path = ""
base_folder = "E:\\迅雷下载\\base\\"


if __name__ == "__main__":
    new_folder_path = fop.file_name_generate(base_folder)
    if not os.path.exists(new_folder_path):
        fop.makedir(new_folder_path)
    fop.traverse_dir(new_folder_path, new_folder_path)
