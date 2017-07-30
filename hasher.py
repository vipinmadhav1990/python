import hashlib
import os

def gethash(file):
	hasher = hashlib.md5()
	with open(file, "rb") as f:
		buf = f.read()
		hasher.update(buf)
	return hasher.hexdigest()
	
hashmap= {}

for rootdir, dirs, files in os.walk("/root/"):
		for f in files:
			path = os.path.join(rootdir, f)
			print path

	
gethash("/etc/hosts")
