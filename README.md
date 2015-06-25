# Jandan.EPUB - 煎蛋电子书
煎蛋爬虫，使用Scrapy，快完成了！
已经能生成电子书了，看起来还不错～
Spider for Jandan.net; Using Scrapy; Almost done!
It can generate the epub already, looks nice :]

## Features
+ 使用Scrapy框架 | Using Scrapy
+ 收集文章内容 | Collect articles on jandan.net
+ 生成电子书(equb) | Generate epub files

## TODO 
- [x] 抓取网页 | Capture webpages
- [x] 下载图片 | Download images
- [x] 整理内容，重新排版 | re-organize
- [x] 生成电子书 | make epub
- [ ] 美化样式 | beautify
- [x] 压缩图片 (No need) | Compress images
- [x] 优化爬取速度 (Should be futher imporved) | Speed up
- [ ] 优化交互 | UI
- [ ] 适配Windows | For Windows
- [ ] 妹子图Bonus :) | ooxx

## Usage

#自动模式 - auto mode

`./run.sh [-d <days>] [-f <from date> -t <to date>] [-n filename]`

#手动模式 - manual mode
    scrapy crawl jandan-article [-L INFO|ERROR|...] 
        [-a dates=(DAYS|RANGE)] [-a length=<days>] [-a from=<from date> -a to=<to date>]`
    ./mkepub.py [-n filename]

###Examples
下载三天内文章，生成名为“FirstBlood”的电子书

`./run.sh -d 3 -n FirstBlood`

或

`scrapy crawl jandan-article -L ERROR -a dates=DAYS -a length=3`

`./mkepub.py -n FirstBlood`

