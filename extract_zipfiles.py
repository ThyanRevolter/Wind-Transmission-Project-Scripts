import gzip
import os
import shutil

inputfolder = r'C:\Users\thyan\Documents\Wind Transmission Project - Local\4th Sep'
for file in os.listdir(inputfolder):
    print(file)
    folderpath = inputfolder + '\\' + file
    for zipfile in os.listdir(folderpath):
        print(zipfile)
        if zipfile.endswith('.gz'):
            zipfilepath = folderpath + '\\' + zipfile
            print(zipfilepath.removesuffix('.gz'))
            with gzip.open(zipfilepath, 'rb') as f_in:
                with open(zipfilepath.removesuffix('.gz'), 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)


