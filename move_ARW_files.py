import glob
import os
import shutil

# creates the folders for the new pictures to be moved to
# note that when you give the windows path name with backslashes, you need to use "r" for raw string.
# That way it won't red the "\" as escape characters.

newest_pictures_directory = r""
RAW_directory = r"\RAW"
JPG_directory = r"\JPG"
os.mkdir(newest_pictures_directory)
os.mkdir(RAW_directory)
os.mkdir(JPG_directory)

raf_files = glob.iglob(os.path.join(r"T:\DCIM\101_FUJI", "*.RAF"))
jpg_files = glob.iglob(os.path.join(r"T:\DCIM\101_FUJI", "*.JPG"))

for file in raf_files:
    if os.path.isfile(file):
        shutil.move(file, r"\RAW")

for jpg in jpg_files:
    if os.path.isfile(jpg):
        shutil.move(jpg, r"\JPG")

print("All files successfully moved from Memory Card")
input("Press Enter to continue")
