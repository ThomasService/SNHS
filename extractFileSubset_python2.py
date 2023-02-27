
import os
import shutil
import random
import glob
import sys 
import re

# Write input variables
input_folder = str(raw_input("Input folder: ")).replace("\"", "")
output_folder = str(raw_input("Output folder: ")).replace("\"", "")
percentage = str(raw_input("Percentage (integer): "))
extension = str(raw_input("File extension: "))

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
        print("\nCopying files\n")
    else:
        dir_empty = str(raw_input(output_folder + " contains " + str(len(os.listdir(output_folder))) + " files. \
Do you wish to proceed (y/n)?")).replace("\"", "")
        if dir_empty.lower().startswith("y"):
            print("\nCopying files\n")
        else:
            sys.exit(0)
            
else:
    dir_create = str(raw_input(os.path.split(output_folder)[-1] + " does not exist \
in " + os.path.split(output_folder)[0] + ". Do you wish to create this directory (y/n)?")).replace("\"", "")
    if dir_create.lower().startswith("y"):
        os.mkdir(output_folder)
        print("Directory created\n")
        print("Copying files\n")
    else:
        sys.exit(0)

print("Number of matching files found: " + str(len(file_list)))
print("Number of files to be copied: " + str(len(files)))

# Copy files to output folder
for index, file in enumerate(files):
    shutil.copy(file, output_folder)
    if index % 10 == 0:
        completion = round(100 * float(index) / len(files), 2)
        print(str(completion) + "%")

# Write .csv containing file names in file subset
with open(output_folder + "/_ExtractedFiles.csv", "w") as f:
    f.write("\n".join(file_names))

print("Complete!")
input("\nClose to exit")

        


