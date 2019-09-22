import os


for folder_name, sub_folders, file_names in os.walk('C:\\Users\\ZBhur\\Downloads\\food'):
    print('The folder is ' + folder_name)
    print('The sub folders in ' + folder_name + ' are ' + str(sub_folders))
    print('The file names in ' + folder_name + ' are ' + str(file_names))
    print()

    for sub_folder in sub_folders:
        if 'healthy' in sub_folder:
            os.rmdir(sub_folder)

    for file_name in file_names:
        if file_name.endswith('.py'):
            os.unlink(file_name)