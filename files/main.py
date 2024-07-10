import os
import shutil

print(os.path.exists('c:\\windows\\system32\\calc.exe'))

total_size = 0
for file_name in os.listdir("c:\\msys64\\mingw64\\bin\\"):
    if not os.path.isfile(os.path.join("c:\\msys64\\mingw64\\bin\\", file_name)):
        continue
    else:
        total_size += os.path.getsize(os.path.join("c:\\msys64\\mingw64\\bin\\", file_name))

print(total_size)

hello_file = open("files/test.txt")
contents = hello_file.read()

write_mode = open("files/test.txt", 'a')
write_mode.write("Testing")

new_file = open("files/new.txt", 'w')
new_file.write("Hello")

new_file.close()
write_mode.close()
hello_file.close()

#shutil.copytree('files/', 'files/backup') Would copy the entire folder into a new folder within `files` named `backup`

# To delete a file
if(os.path.exists("files/test.txt")):
    os.unlink("files/test.txt")

# os.rmdir() deletes an entire folder if it's empty
# shutil.rmtree() will delete a folder and all of its contents

# Sample code for function to walk a directory and delete all `.py` files
#for folder_name, sub_folders, file_names in os.walk("files/"):
#    for file in file_names:
#        if file.endswith('.py'):
#            os.unlink(file)