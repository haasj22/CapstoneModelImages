import os
import subprocess

class_file = open("classes.txt", 'r')
lines = class_file.readlines()

for index in range(int(len(lines)/2)):
    class_id = lines[2 * index][:-1]
    class_name = lines[2 * index + 1]
    class_name_list = class_name.split(", ")

    #print(class_id)
    folder_name = None
    if len(class_name_list) == 1:
        #print(class_name[:-1])
        folder_name = class_name[:-1]
    else:
        #print(class_name_list[0])
        folder_name = class_name_list[0]
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    print(folder_name)
    for filename in os.listdir('/mnt/storage2/METRO_recycling/train_images/val'):
        if not filename.startswith("ILS"):
            continue
        classname = filename.split("_")[-1][:-5]
        if class_id == classname:
            temp = subprocess.Popen(['mv', filename, folder_name])
            temp.wait()

