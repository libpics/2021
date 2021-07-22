#grabbed from https://stackoverflow.com/questions/34960343/how-to-change-multiple-filenames-in-a-directory-using-python and then edited to match our needs

import os
import sys

path = '/Volumes/digitalmedialib/TIFF cropped/1000-148/box003/box003folder002/raymonda' #change this path to the location of the files

for filename in os.listdir(path):
    filename_splitext = os.path.splitext(filename)
    if filename_splitext[1] in ['.tif']: #change the extenstion here to match the ones of the files that you are looking to change
        os.rename(os.path.join(path, filename), 
                os.path.join(path, filename_splitext[0] + 'cpd' + '.tif'))#modify this to meet the needs of your rename change
