import crypt
import time

def testpass(uname,cPass,dname):
	salt = cPass[0:2]
	dfile = open(dname,"r")
	for word in dfile.readlines():
		word = word.strip("\n")
		cword = crypt.crypt(word,salt)
		if (cword == cPass):
			print "Password for " +uname +" is " +word +"\n"
			time.sleep(2)
	print "No password found for " +uname +"\n"
	return

def Main():
	hashFile = raw_input("Enter the name of the hash file to be used: ")
	passFile = open(hashFile,"r")
	dname = raw_input("Enter the name of the dictionary file to be used: ")
	for line in passFile.readlines():
		if ":" in line:
			uname = line.split(":")[0]
			cPass = line.split(":")[1].strip(" ")
			print "Cracking password for: " +uname
			testpass(uname,cPass,dname)




if __name__ == "__main__":
	Main()