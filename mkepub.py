#!/usr/bin/python
from epubMaker.main import EpubMaker
import os

working = os.getcwdu()

ebook_name = 'Jandan-June'

mker = EpubMaker(ebook_name, working)
mker.run()

os.chdir("epub" + os.sep + ebook_name)
os.system("zip -rq " + ebook_name + ".epub *")
os.chdir('..')

