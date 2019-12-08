import glob
import os
import shutil

# creates the folders for the new pictures to be moved to
# note that the drive cannot be part of the path

newest_pictures_directory = '/test_folder/newest_pictures'
RAW_directory = '/test_folder/newest_pictures/RAW'
JPG_directory = '/test_folder/newest_pictures/JPG'
os.mkdir(newest_pictures_directory)
os.mkdir(RAW_directory)
os.mkdir(JPG_directory)

arw_files = glob.iglob(os.path.join('/Users/marc/Downloads', "*.pdf"))
jpg_files = glob.iglob(os.path.join('/Users/marc/Downloads', "*.jpg"))

for file in arw_files:
    if os.path.isfile(file):
        shutil.move(file, '/test_folder/newest_pictures/RAW')

for jpg in jpg_files:
    if os.path.isfile(jpg):
        shutil.move(jpg, '/test_folder/newest_pictures/JPG')

print("All files successfully moved from Memory Card")
input("Press Enter to continue")
