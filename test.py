import os
import shutil

source_location = r"G:\My Drive"
target_location = r"C:\Users\jay25\Desktop\test"

file_names = os.listdir(source_location)

print(source_location, target_location)
shutil.copytree(source_location, target_location)

# for file_name in file_names:
#     # shutil.move(os.path.join(source_location, file_name), target_location)
#     shutil.copytree(source_location, target_location)
#     print(os.path.join(source_location, file_name))
print("finish")
os.system("pause")