import os
import hashlib
## This takes a passed path and
## returns a relative path from it
## as it relates to working directory
def getRelPath(path):
	path = os.path.relpath(path)
	return path
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
## This takes a passed path and
## returns a file size in bytes
def getSize(path):
	path = os.stat(path)
	return path.st_size
