import os, errno, shutil, json
from html_builder import HtmlBuilder as HB
from register import Register as RG

class EpubMaker:
    ''' Make the epub file according to `article.json`'''
    # @param filename string: The name of the product - xxxx.epub
    # @param rootpath string: Absolut path of first PaJandan.
    def __init__(self, filename, rootpath):
        self.filename = filename
        self.root = rootpath.rstrip(os.sep) + os.sep # with ending '/'
        self.image_names = set() # no '.jpg'
        self.articles = [] # (title, en_title, tag, date)


    def run(self):
        self.archtecture()
        self.process_json()
        self.build_indexpage()
        self.build_infopage()
        self.register()
        self.copyimgs()

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

    # Extract images, titles and build articles
    # @param No
    # @return No
    def process_json(self):
        with open(self.root + 'articles.json', 'r') as json_file:
            for art in json_file:
                art_dict = json.loads(art)
                '''
                    keys in art_dict:
                    [u'origin',
                     u'author',
                     u'title',
                     u'image_urls',
                     u'content',
                     u'date',
                     u'tag',
                     u'en_title',
                     u'images']
                '''
                # save image names
                if 'image_urls' in art_dict:
                    for imname in art_dict['image_urls']:
                        self.image_names.add(imname)

                # save article name
                for t in ('title', 'en_title', 'tag', 'date'):
                    if not t in art_dict:
                        art_dict[t] = ""
                self.articles.append((art_dict[u'title'], 
                    art_dict[u'en_title'], 
                    art_dict[u'tag'],
                    art_dict[u'date']))

                # build article html
                article_file_name = self.root + os.sep.join([
                    'epub', 
                    self.filename, 
                    'OEBPS', 
                    'html', 
                    art_dict[u'en_title']+'.html'
                    ])
                HB.build_file(article_file_name, HB.ARTICLE_TEMPLATE, 
                    art_dict[u'title'],
                    art_dict[u'title'],
                    art_dict[u'author'],
                    art_dict[u'date'],
                    art_dict[u'tag'],
                    art_dict[u'content'])
    
    # build /OEBPS/html/index.html
    def build_indexpage(self):
        Li_Templete = "<li><a href='%s'>%s</a>"
        menu = []
        for art in self.articles:
            li = Li_Templete % (art[1]+'.html', art[0])
            menu.append(li)
        index_name = self.root + os.sep.join([
                    'epub', 
                    self.filename, 
                    'OEBPS', 
                    'html', 
                    'index.html'
                    ])
        HB.build_file(index_name, HB.INDEX_TEMPLATE, ''.join(menu))

    # build /OEBPS/html/info.html
    def build_infopage(self):
        info_name = self.root + os.sep.join([
                    'epub', 
                    self.filename, 
                    'OEBPS', 
                    'html', 
                    'infoPage.html'
                    ])
        HB.build_file(info_name, HB.INFOPAGE_TEMPLATE)

    def register(self):
        rg = RG(self)
        rg.build_opf()
        rg.build_ncx()

    # copy images from 'images/' to 'OEBPS/images/'
    def copyimgs(self):
        for imgname in self.image_names:
            shutil.copy(self.root+os.sep.join(['images', 'full', imgname+'.jpg']), 
                self.root+os.sep.join(['epub', self.filename, 'OEBPS', 'images', imgname+'.jpg']))

    def display_test(self):
        pass

