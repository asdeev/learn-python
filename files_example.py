import os


os.path.join('folder1', 'folder2', 'folder3', 'file.png')
separator = os.sep  # returns current os file path separator
os.getcwd()     # get current directory
os.chdir('.\\')      # change directory
os.path.abspath('file.png')     # will get absolute path based on current relative path
os.path.isabs('.\\')    # checks if path is absolute or not
os.path.relpath('c:\\folder1\\folder2\\file.png', 'c:\\folder1')    # gets relative path from some starting point
os.path.dirname()   # retrieves the directory name of path
os.path.basename()  # retrieves the file name of path
os.path.exists()    # checks to see if file path exists
os.path.getsize()   # returns size in bytes as integer of path
os.path.isfile()    # checks if path is file or folder
os.makedirs()   # creates all folders specified
os.listdir()    # returns list of files and folders of directory passed
