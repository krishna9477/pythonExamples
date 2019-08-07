import os,zipfile
zip_file_path =r"C:\Users\Ismail\Downloads\bootstrap files"
file_list = os.listdir(zip_file_path)
abs_path = []
for a in file_list:
    x = zip_file_path+'\\'+a
    abs_path.append(x)
for f in abs_path:
    if f.endswith('.zip'):
        zip=zipfile.ZipFile(f)
        zip.extractall(r"C:\Users\Ismail\Downloads\bootstrap files\output2")
