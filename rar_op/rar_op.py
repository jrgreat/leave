from unrar import rarfile
import py7zr
import zipfile

class rar_op:
    def __init__(self,folder_path,extract_path):
        self.folder_path = folder_path
        self.extract_path = extract_path

    def extract_file(self):
        zf = rarfile.RarFile(self.folder_path)  # rarfile 读取压缩文件对象
        zf.extractall(self.extract_path)     # 压缩文件内全部文件解压到输入的文件夹中
        

    def z7_extract_file(self):
        archive = py7zr.SevenZipFile(self.folder_path , mode = 'r')
        archive.extractall(path=self.extract_path)
        archive.close()
    
    def zip_extract_file(self):
        zipFile = zipfile.ZipFile(self.folder_path)
        for file in zipFile.namelist():
            zipFile.extract(file , self.extract_path)
        zipFile.close()

            
    