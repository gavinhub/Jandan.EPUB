#!/usr/bin/python
from epubMaker.main import EpubMaker
import os
import getopt, sys

working = os.getcwdu()

ebook_name = 'Jandan'

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:")
    if opts and opts[0][0] == '-n':
    	ebook_name = opts[0][1]
except getopt.GetoptError:
	raise
mker = EpubMaker(ebook_name, working)
mker.run()

os.chdir("epub" + os.sep + ebook_name)
os.system("zip -rq " + ebook_name + ".epub *")
os.chdir('..')

