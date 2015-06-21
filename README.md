# Jandan.EPUB - 煎蛋电子书
煎蛋爬虫，使用Scrapy，快完成了！
已经能生成电子书了，看起来还不错～

## Features
+ 使用Scrapy框架
+ 收集文章内容
+ 生成电子书(equb)

## TODO
- [x] 抓取网页
- [x] 下载图片
- [x] 整理内容，重新排版
- [x] 生成电子书
- [ ] 美化样式
- [ ] 优化爬取速度
- [ ] 优化交互
- [ ] 适配Windows
- [ ] 妹子图Bonus :)

## Usage
进入Jandan.EPUB目录后：

`scrapy crawl jandan-article`

等待爬取，结束后：

`python mkepub.py`