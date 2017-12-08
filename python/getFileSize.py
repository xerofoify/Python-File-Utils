import os

## The following function returns the size of a file, in bytes
## To use, call the function as follows print getFileSize("path/to/file")
def getFileSize(path):
	
	if(os.path.isabs(path)):
        	return os.path.getsize(path)
	else:
        	fn = os.path.join(os.path.dirname(__file__), path)
		return os.path.getsize(fn)
