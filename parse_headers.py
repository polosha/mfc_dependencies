import sys
from os import path
import os
from pprint import pprint

import parse_imports

def getValue(s):
	val = s.partition(':')[2]
	val =val.strip()
	return val



filename = sys.argv[1]
print("Ready to parse file " + path.abspath(filename))

fread = open(filename)
i = 0
ordinals = {}
for s in fread:
	# if i > 20:
		# break
	
	s = s.strip()
	if s.find("Version") == 0:
		
		# Start parsing a block
		name = ""
		ordinal = 0
		for subline in fread:
			subline = subline.strip()
			if len(subline):
				# Parse subline
				if subline.find("Symbol name") == 0:
					name = getValue(subline)
				elif subline.find("Ordinal") == 0:
					ordinal = int(getValue(subline))
			else:
				break
		ordinals[ordinal] = name
	i += 1 	
	
	
	# split = s.split(":")
	# if (len(split) != 
	# s = s.strip(os.linesep)
	# print(str(i) + " : " + s)
print (i)
print (len(ordinals))
#pprint (ordinals)
fread.close()

l = parse_imports.parse_imports("jobInspectorImport.txt")
#pprint(l)
print("names = \n")
for i in l:
	print(ordinals[i])