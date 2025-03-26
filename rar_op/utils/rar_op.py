from unrar import rarfile
import py7zr
import zipfile
import os

class rar_op:
    def __init__(self,folder_path,extract_path):
        self.folder_path = folder_path
        self.extract_path = extract_path

    def extract_file(self):
        try:
            zf = rarfile.RarFile(self.folder_path)  # rarfile 读取压缩文件对象
            zf.extractall(self.extract_path) # 压缩文件内全部文件解压到输入的文件夹中
        except Exception as e:
            zf = rarfile.RarFile(self.folder_path, pwd = '1024')
            print(e)
            zf.extractall(self.extract_path, pwd = '1024')   
        
        

    def z7_extract_file(self):
        archive = py7zr.SevenZipFile(self.folder_path , mode = 'r')
        archive.extractall(path=self.extract_path)
        archive.close()
    
    def zip_extract_file(self):
        def checkEncodeError(string):
            try:
                string.encode('gb2312')
            except UnicodeEncodeError:
                return True
            return False
        zipFile = zipfile.ZipFile(self.folder_path)
        for file in zipFile.namelist():
            zipFile.extract(file , self.extract_path)
            if (checkEncodeError(file)):
                full_path = os.path.join(self.extract_path, file)
                try:
                    new_name = file.encode('cp437').decode('gbk')
                    new_name_path = os.path.join(self.extract_path, new_name)
                    os.rename(full_path, new_name_path)
                except Exception as e:
                    continue
                #os.remove(full_path)
        zipFile.close()

            
    