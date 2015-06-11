# -*- coding:utf-8 -*-
class HtmlBuilder():
    @staticmethod
    def build_file(filename, template, *content):
        arglist = tuple(arg.encode('utf-8') for arg in content)
        with open(filename, 'w') as f:
            f.write(template % arglist)

    # @format <1 string>: list of '<li>'
    INDEX_TEMPLATE = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="provider" content="www.jandan.net"/>
    <meta name="builder" content="PaJandan"/>
    <meta name="right" content="本文档由PaJandan生成。PaJandan由Gavin
    Code提供，是整理煎蛋网文章的工具，文档和工具仅供交流和学习使用，不得用于任何商业用途。"/>
    <link rel="userDefine.css" type="text/css" href="../userDefine.css"/>
    <title>目录</title>
  </head>
  <body>
    <div>
      <h1>目录</h1>
    </div>
    <hr />
    <br />
    <ol>
      %s
    </ol>
  </body>
</html>
'''
    # @format <None>
    INFOPAGE_TEMPLATE = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="provider" content="www.jandan.net"/>
    <meta name="builder" content="PaJandan"/>
    <meta name="right" content="本文档由PaJandan生成。PaJandan由Gavin
    Code提供，是整理煎蛋网文章的工具，文档和工具仅供交流和学习使用，不得用于任何商业用途。"/>
    <link rel="userDefine.css" type="text/css" href="../userDefine.css"/>
    <title>声明</title>
  </head>
  <body>
    <h1>声明</h1>
    <p>我也不知道说点啥，你往后翻吧:)</p>
  </body>
</html>
'''
    # @format <6 strings>: (title, title, translator, date, tags, content)
    ARTICLE_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" type="text/css" href="../userDefine.css"/>
        <title>%s</title>
    </head>
    <body> 
    <div id='article'>
    <h1>%s</h1>
    <p>Ts: %s</p>
    <p>Date: %s</p>
    <p>Tag: %s</p>
    %s
    </div>
    <p></p>
    </body>
</html>
'''