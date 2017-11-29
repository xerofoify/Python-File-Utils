import os
## This takes a passed path and
## returns a relative path from it
## as it relates to working directory
def getRelPath(path):
	path = os.path.relpath(path);
	return path;
