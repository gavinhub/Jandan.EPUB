from epubMaker.main import EpubMaker
import os

mker = EpubMaker('jdt', os.getcwdu())
mker.run()
