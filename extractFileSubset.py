
import os
import shutil
import random
import glob
import sys
import re

# Write input variables
input_folder = str(input("Input folder: ")).replace("\"", "")
output_folder = str(input("Output folder: ")).replace("\"", "")
percentage = str(input("Percentage (integer): "))
extension = str(input("File extension: "))

# Clean input variables to extract relevant information
# Replace anything but numbers and . with empty strings
percentage = int(float(re.sub(r"[^\d\.]", "", percentage)))
# Replace any non-word character with empty strings
extension = re.sub(r"[\W]", "", extension)
ext = "/*." + extension

# List all files in directory with matching extension
file_list = glob.glob(input_folder + ext)

# Calculate number of files to extract based on input percentage
num = int((len(file_list) / 100) * percentage)

# Sample files
files = random.sample(file_list, num)
file_names = [os.path.split(file)[1].split(".")[0] for file in files]

# Check if directory exists and if it is empty
if os.path.exists(output_folder):
    if not os.listdir(output_folder):
        print("Copying files")
    else:
        dir_empty = str(input(f"{output_folder} contains {len(os.listdir(output_folder))} "\
                   f"files. Do you wish to proceed (y/n)?")).replace("\"", "")
        if dir_empty.lower() == "y" or "yes":
            print("Copying files")
        else:
            sys.exit()
else:
    dir_create = str(input(f"{os.path.split(output_folder)[-1]} does not exist in "\
                        f"directory {os.path.split(output_folder)[0]}. Do you "\
                        f"wish to create this directory (y/n)?")).replace("\"", "")
    if dir_create.lower() == "y" or "yes":
        os.mkdir(output_folder)
        print(f"Directory {os.path.split(output_folder)[-1]} created\n")
    else:
        sys.exit()

print(f"Number of matching files found: {len(file_list)}")
print(f"Number of files to be copied: {len(files)}")

# Copy files to output folder
for index, file in enumerate(files):
    shutil.copy(file, output_folder)
    # Print progress
    if index % 10 == 0:
        print(f"{(index / len(files)) * 100:.2f}%")
    
# Write .csv containing file names in file subset
with open(output_folder + "/_ExtractedFiles.csv", "w") as f:
    f.write("\n".join(file_names))
    
print("Complete!")


