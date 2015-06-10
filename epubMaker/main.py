import os, errno, shutil

class EpubMaker:
    ''' Make the epub file according to `article.json`'''
    # @param filename string: The name of the product - xxxx.epub
    # @param rootpath string: Absolut path of first PaJandan.
    def __init__(self, filename, rootpath):
        self.filename = filename
        self.root = rootpath.rstrip(os.sep) + os.sep

    # Get file system ready.
    # @param No
    # @return No
    def archtecture(self):
        # make directorys
        dirlist = [
            os.sep.join(['epub',self.filename,'META-INF']),
            os.sep.join(['epub',self.filename,'OEBPS','html']),
            os.sep.join(['epub',self.filename,'OEBPS','images'])
            ]
        for dire in dirlist:
            try:
                os.makedirs(self.root + dire)
            except OSError, e:
                if e.errno != errno.EEXIST:
                    raise

        # copy necessary files
        shutil.copy(self.root+os.sep.join(['epubMaker', 'resource', 'mimetype']), 
            self.root+os.sep.join(['epub', self.filename, 'mimetype']))
        shutil.copy(self.root+os.sep.join(['epubMaker', 'resource', 'container.xml']), 
            self.root+os.sep.join(['epub', self.filename, 'META-INF', 'container.xml']))


    def input_info(self):
        pass

    def make_HTMLs(self):
        pass

