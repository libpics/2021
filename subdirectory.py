import os

src = '/Users/mceruti/Desktop/toplevelsourcefolder' # input
dst = '/Users/mceruti/Desktop/desinationfolder' # desired     location

def move():
    for (dirpath, dirs, files) in os.walk(src):
        if files.endswith('.tif'): #change this to the specific filetype that you want to be pulled
            shutil.move(os.path.join(src,files),dst)
            print ('Moving ', + files, + ' to ', + dst)
        else:
            print('No Such File Exists')
