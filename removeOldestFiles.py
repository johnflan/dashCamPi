#!/usr/bin/python
import os
import time

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
    while True:
        folderSizeBytes = getFolderSize("/home/johnflan/workspace/dashCamPi")
        print str(folderSizeBytes)
        
        #8GB 8589934592
        if (folderSizeBytes >= 34592):
            fileToBeRemoved = oldest_file_in_tree("/home/johnflan/workspace/dashCamPi")
            print "DELETE " + fileToBeRemoved
            os.remove(fileToBeRemoved)
        else:
            time.sleep(60 * 10)

if __name__ == '__main__':
    main()
