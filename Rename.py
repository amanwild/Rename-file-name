import os
from pathlib import Path
# my_file = 'my_file.txt'
# base = os.path.splitext(my_file)[0]
# print(base)
# os.rename(my_file, base + '.bin')

# Get the list of all files and directories
path = "C://vdo from tube//"
dir_list = os.listdir(path)
# dir_list = path+str(dir_list)
# dir_list = dir_list.sort(key=os.path.getctime)
lists = (enumerate(dir_list))

# files = []
# for i in dir_list:
#     paths = path+str(i)
#     files.append(paths)
#     print(paths)

# sorting by Created time
paths = sorted(Path(path).iterdir(), key=os.path.getmtime) 
pathss = (enumerate(paths))
for count, filename in pathss:
    src =f"{filename}"  # pathname/filename, if .py file is outside path
    
    # pathname/filename, if .py file is outside path
    dst =f"{os.path.dirname(filename )}\{count+1} {Path(filename).name}"  
    print(src)
    print(dst)
    
    # rename() function will
    # rename all the files
    os.rename(src, dst)