import os
import shutil

from_dir= 'C:Users/aarus/Downloads/'
to_dir='C:Users/aarus/OneDrive/Desktop/proj102'

list_of_files= os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name,ext= os.path.splitext(file)

    if os.path.exists(path2):
        print("Moving " + file + "......")
        shutil.move(path1,path3)

    if ext=='':
        continue
    elif ext in ['.txt', '.docs', '.docx', '.pdf' ]:
        path1= from_dir+'/'+file
        path2= to_dir+'/files'
        path3= path2+'/'+file

        if os.path.exists(path2):
            shutil.move(path1, path3)
            
        else:
            os.mkdir(path2)
            shutil.move(path1, path3)