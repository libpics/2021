import os

src = '/Users/mceruti/Desktop/ALL ORDERS copy' # input
dst = '/Users/mceruti/Desktop/test' # desired     location

def move():
    for (dirpath, dirs, files) in os.walk(src):
        if files.endswith('.tif'):
            shutil.move(os.path.join(src,files),dst)
            print ('Moving ', + files, + ' to ', + dst)
        else:
            print('No Such File Exists')