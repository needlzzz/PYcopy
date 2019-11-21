#move the files filetype JPG#
import glob, os, shutil

files = glob.iglob(os.path.join('SRCpath', "*.jpg"))
for file in files:
    if os.path.isfile(file):
        shutil.move(file, 'DESTpath')
print("all done")

