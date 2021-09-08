#This code puts only the filenames and extensions in a txt file  from a given directory. T
# This does not include any heirarchy-- just the filenames. I will include XML files that are not visible in finder
# https://www.psychwire.co.uk/2010/03/python-script-get-the-filenames-from-a-directory/ 
import os
f = open('names2.txt', 'w') #change the filename to whatever you want, but you need to already be in the directory that you want it to live when you run the code.

srcDir='/Volumes/visualresources/Digital Projects' #change this to the directory that you want the filenames to be copied from. This will even grab from subdirectories.

for root, dirs, files in os.walk(srcDir):
	for newname in files:
		filename = os.path.join(newname)
		newstring = filename + '\n'
		f.write(newstring)