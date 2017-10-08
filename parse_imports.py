import sys
from os import path
import os
from pprint import pprint


def parse_imports(file):
	l = []
	f = open(file)
	for s in f:
		s = s.strip()
		if s.find("Ordinal") == 0:
			ordinal = int(s.partition(' ')[2].strip())
			l.append(ordinal)

	f.close()
	#pprint(l)
	#print (len(l))
	return l

if __name__ == "__main__":
	filename = sys.argv[1]
	print("Ready to parse file " + path.abspath(filename))