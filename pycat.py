#!/usr/bin/python -tt

"""
cat.py - cat implemented in python
"""

import sys
a = 123

def cat(filename):
	print filename, '======='
	f = open(filename, 'r')
	for line in f:
		print line,
	f.close()

def main():
	args = sys.argv[1:]
	for filename in args:
		if filename == 'voldemort' or filename == 'vader':
			print 'VERY WORRYING FILE'
			cat(filename)
		else:
			cat(filename)
	print 'all done'

if __name__ == '__main__':
	main()
