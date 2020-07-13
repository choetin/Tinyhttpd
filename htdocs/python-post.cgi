#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# CGI处理模块
import cgi, cgitb
import json

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
site_name = form.getvalue('name')
site_url  = form.getvalue('url')

res = {'站点名称': site_name, '站点网址': site_url}
print('')
print(json.dumps(res))
