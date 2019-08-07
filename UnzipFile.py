from zipfile import ZipFile

# Create a ZipFile Object and load sample.zip in it
with ZipFile(r'C:\Users\Ismail\Downloads\EmailSending-master.zip', 'r') as zipObj:
    # Extract all the contents of zip file in current directory
    zipObj.extractall(r'C:\Users\Ismail\Downloads\output')
    print("okay")