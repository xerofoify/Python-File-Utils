import os
import hashlib
## This takes a passed path and
## returns a relative path from it
## as it relates to working directory
def getRelPath(path):
	path = os.path.relpath(path)
	return path
## This takes a passed path,
## retrieves the absolute path
## as it relates to the working
## directory and returns the file
## size in bytes
def getFileSize(path):
	path = abspath(path)
    fileSize = os.path.getsize(path)
    return fileSize
## Return a md5 checksum object after
## usinf getRelPath to convert the path
## into a relative path as related to
## the current working directory
def getMd5(path):
	path = getRelPath(path)
	checksum = md5.new(path)
	return path;
## Same as the above function but
## for SHA1 hashes instead
def getSHA1(path):
	path = getRelPath(path)
	checksum = sha1.new(path);
	return checksum
