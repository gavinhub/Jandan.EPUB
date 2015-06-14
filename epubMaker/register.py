# -*- coding:utf-8 -*-
import os

class Register():

    def __init__(self, epubmaker):
        self.images = epubmaker.image_names
        self.articles = epubmaker.articles
        self.reg_root = epubmaker.root + os.sep.join([
            'epub',
            epubmaker.filename,
            'OEBPS']) + os.sep
        self.id_counter = 0

    def build_opf(self):
        filename =  self.reg_root + 'content.opf'
        with open(filename, 'w') as f:
            f.write(Register.OPF_HEADER + os.linesep)

            ##### manifest
            f.write("<manifest>" + os.linesep)
            f.write('<item id="ncx" href="toc.ncx" media-type="text/xml"/>' + os.linesep)

            ## images
            image_template = '<item id="%d" href="images/%s.jpg" media-type="image/jpg"/>'
            for image in self.images:
                self.id_counter += 1
                f.write(image_template % (self.id_counter, image) + os.linesep)

            ## htmls
            html_template = '<item id="%d" href="html/%s.html" media-type="application/xhtml+xml"/>'
            
            # index, info
            self.id_counter += 1
            self.index_id = self.id_counter
            f.write(html_template % (self.id_counter, 'index') + os.linesep)
            self.id_counter += 1
            self.info_id = self.id_counter
            f.write(html_template % (self.id_counter, 'infoPage') + os.linesep)

            # articles
            self.article_start = self.id_counter
            
            for article in self.articles:
                self.id_counter += 1
                f.write(html_template % (self.id_counter, article[1].encode('utf-8')) + os.linesep)
            self.article_end = self.id_counter
            f.write("</manifest>" + os.linesep)      

            # spine
            spine_template = '<itemref idref="%d" linear="yes"/>'
            f.write('<spine toc="ncx">' + os.linesep)
            f.write(spine_template % self.index_id+ os.linesep)
            f.write(spine_template % self.info_id+ os.linesep)
            for i in range(self.article_start+1, self.article_end+1):
                f.write(spine_template % i + os.linesep)
            f.write('</spine>' + os.linesep)

            # guide
            f.write(Register.OPF_FOOTER + os.linesep)

    def build_ncx(self):
        filename =  self.reg_root + 'toc.ncx'
        with open(filename, 'w') as f:
            f.write(Register.NCX_HEADER + os.linesep)

            # index, infoPage
            order = 1
            f.write(Register.NAV_TEMPLATE % (self.info_id, order, 'Index', 'index') + os.linesep)
            order += 1
            f.write(Register.NAV_TEMPLATE % (self.info_id, order, 'Info Page', 'infoPage') + os.linesep)
            order += 1
            
            # articles
            for i in range(self.article_start, self.article_end):
                article = self.articles[i-self.article_start]
                f.write(Register.NAV_TEMPLATE % (i, order, article[0].encode('utf-8'), article[1].encode('utf-8')) + os.linesep)
                order += 1

            # footer
            f.write("</navMap></ncx>" + os.linesep)

    OPF_HEADER = \
"""<?xml version='1.0' encoding='utf-8'?>
<package xmlns="http://www.idpf.org/2007/opf" 
xmlns:dc="http://purl.org/dc/elements/1.1/" 
unique-identifier="27149527" version="2.0">
<metadata>
<dc:title>content.opf</dc:title>
<dc:identifier id='27149527'>27149527</dc:identifier>
<dc:language>zh-cn</dc:language>
<dc:creator>MyHands</dc:creator>
<dc:description>呃。。。就是我写的</dc:description>
<dc:rights>CC</dc:rights>
<dc:publisher>我，没错就是我</dc:publisher>
</metadata>"""

    OPF_FOOTER = \
"""<guide>
    <reference href="./html/index.html" type="toc" title="index.html"/>
</guide>        
</package>"""

    NCX_HEADER = \
"""<?xml version='1.0' encoding='utf-8'?>
        <!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" 
          "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
        <ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
        
        <head>
          <meta name="dtb:uid" content="27149527"/>
          <meta name="dtb:depth" content="-1"/>
          <meta name="dtb:totalPageCount" content="0"/>
          <meta name="dtb:maxPageNumber" content="0"/>
        </head>
        <docTitle>
           <text>toc.ncx</text>
        </docTitle>
        <navMap>"""

    NAV_TEMPLATE = \
"""       <navPoint id="%d" playOrder="%d">
          <navLabel>
             <text>%s</text>
          </navLabel>
          <content src="html/%s.html"/>
        </navPoint>"""
