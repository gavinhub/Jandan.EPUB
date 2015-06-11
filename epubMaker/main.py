import os, errno, shutil, json

class EpubMaker:
    ''' Make the epub file according to `article.json`'''
    # @param filename string: The name of the product - xxxx.epub
    # @param rootpath string: Absolut path of first PaJandan.
    def __init__(self, filename, rootpath):
        self.filename = filename
        self.root = rootpath.rstrip(os.sep) + os.sep # with ending '/'
        self.image_names = set()
        self.articles_en = set()


    def run(self):
        self.extract_info()
        self.archtecture()

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

    # Extract important infomations e.g. article names, image names...
    # @param No
    # @return No
    def extract_info(self):
        with open(self.root + 'articles.json', 'r') as json_file:
            for art in json_file:
                art_dict = json.loads(art) # art_dict = {"images_url":[u'', u'']}
                # save image names
                for imname in art_dict['image_urls']:
                    self.image_names.add(imname)
                # save article English name
                self.articles_en.add(art_dict['en_title'])


    def display_test(self):
        print self.image_names

    def make_HTMLs(self):
        pass

