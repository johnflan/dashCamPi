#!/usr/bin/python
import os
import time

log = open('/home/pi/dashCamPi/dashcam-delete.log','a')

def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size

def oldest_file_in_tree(rootfolder, extension=".avi"):
    return min(
        (os.path.join(dirname, filename)
        for dirname, dirnames, filenames in os.walk(rootfolder)
        for filename in filenames
        if filename.endswith(extension)),
        key=lambda fn: os.stat(fn).st_mtime)

def main():
    print "Starting..."
    while True:
        folderSizeBytes = getFolderSize("/home/pi/dashCamPi")
	print "Folder size:\t" + str(folderSizeBytes)
        print "Threshold size:\t" + str(524288000)
	#8GB 8589934592
	#500mb 524288000
        if (folderSizeBytes >= 524288000):
            fileToBeRemoved = oldest_file_in_tree("/home/pi/dashCamPi")
	    print "Deleting " + fileToBeRemoved
            log.write("DELETE " + fileToBeRemoved + "\n")
            os.remove(fileToBeRemoved)
        else:
	    log.write("No files to be deleted, folder size "+ str(folderSizeBytes) +"\n")
	    print "Sleeping"
            time.sleep(60 * 10)

if __name__ == '__main__':
    main()
