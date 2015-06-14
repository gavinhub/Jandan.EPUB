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

            # manifest
            f.write("<manifest>" + os.linesep)
            f.write('<item id="ncx" href="toc.ncx" media-type="text/xml"/>' + os.linesep)

            image_template = '<item id="%d" href="images/%s.jpg" media-type="image/jpg"/>'
            for image in self.images:
                self.id_counter += 1
                f.write(image_template % (self.id_counter, image) + os.linesep)

            self.article_start = self.id_counter
            html_template = '<item id="%d" href="html/%s.html" media-type="application/xhtml+xml"/>'
            for article in self.articles:
                self.id_counter += 1
                f.write(html_template % (self.id_counter, article[1].encode('utf-8')) + os.linesep)

            f.write("</manifest>" + os.linesep)      

            # spine
            f.write('<spine toc="ncx">' + os.linesep)
            for i in range(self.article_start+1, self.id_counter+1):
                f.write('<itemref idref="%d" linear="yes"/>' % i + os.linesep)
            f.write('</spine>' + os.linesep)

            # guide
            f.write(Register.OPF_FOOTER + os.linesep)


    OPF_HEADER = \
"""<?xml version='1.0' encoding='utf-8'?>
<package xmlns="http://www.idpf.org/2007/opf" 
xmlns:dc="http://purl.org/dc/elements/1.1/" 
unique-identifier="27149527" version="2.0">
<metadata>
<dc:title>测试Epub-content.opf-dc:title</dc:title>
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
