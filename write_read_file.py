# Script to write a data to a file and to read from it. 

def name(n):
	f = open("<file_path>/123.txt", 'wr+')
	f.write("Hello %s" % n)
	f = open("<file_path>/123.txt", 'r') 
	return f.readline()


if __name__=="__main__":
	n = raw_input("Enter the name:")
	print name(n)
