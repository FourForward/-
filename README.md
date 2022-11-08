# Python笔记汇总

[**Python的新变化 — 更新到Python 3.10.0** ](https://docs.python.org/zh-cn/3.10/whatsnew/index.html)

```shell
# pip3 永久换源：
	不建议永久换源
# pip3 提示更新
pip3 install --upgrade pip

# 单次换源示例：
sudo pip3 install uwsgi==2.0.18 -i https://pypi.tuna.tsinghua.edu.cn/simple/
```



## ①  语法

### [python基础语法](./python/python3.6基础语法.md)

### [面向对象](./python/面向对象.md)

### [python高级语法](./python/Python高级语法.md)

### [常用函数](./python/Python常用函数.md)

### [python黑魔法](./python/python黑魔法.md)

### [python标准库官方文档](https://docs.python.org/3/library/functions.html)




## ②  数据处理——数据库

### [文件处理](./python/文件处理.md)



### [正则表达式](./python/正则表达式.md)



### Mysql

#### [MySQL-基础](./python/MySQL.md)

#### [SQL_To_Everything](./python/SQL_To_Everything.md)



### Redis

#### [Redis 基础教程](./python/redis基础教程.md)

#### [Redis 原理讲解 - 数据结构](./python/Redis原理讲解 - 数据结构.md)

#### [Redis 原理讲解 - 配置策略](./python/Redis 配置-策略.md)

#### [Redis 原理讲解 - 特殊场景及技巧](./python/Redis 特殊场景及技巧.md)



## ③  并发编程

###  [socket,TCP,udp,线程,进程,IO多路复用](./python/网络并发编程.md)

###  [IO多路复用,同步,异步,阻塞和非阻塞 区别(转)](./python/IO同步异步的区别.md)

###  [协程——asyncio](./python/协程——async.md)




## ④  http框架

### django

#### [django2.2---教程](./python/Djnago2.2.md)

#### [django_channels,django中使用websocket的方式](./python/django_channels.md)

####  [djagno日志的参数传递](./python/djagno日志的参数传递.md)

####  [Django 官网中文文档 ](https://docs.djangoproject.com/zh-hans/3.2/)



### aiohttp

####  [aiohttp stable 官网](https://docs.aiohttp.org/en/stable/)

####  [aiohttp部分中文文档(客户端部分)](./python/aiohttp部分中文文档.md)




## ⑥  爬虫相关

###  [Spider  教学文档-达内](./python/spider.md)

### [Python3WebSpider - 崔庆才](./python/Python3WebSpider/0-目录.md)

### [在网页的JS中注入Hook的方式](./python/在网页的JS中注入Hook.md)

### [各种 web-js-hook](./python/js-hook.md)

### [playwright-docs-api-中文文档.pdf](./python/playwright-docs-api-中文文档.pdf)

[playwright-中文文档.md(建议使用上面的PDF查看,md会卡)](./python/playwright-docs-api-中文文档.md)      [web自动化工具 playwright-docs-api 英文文档](./python/playwright-docs-api.md)

### 骑行数据相关整合

1. [Garmin-fit 解析方案](./python/Garmin-fit-parse方案.md)
1. [捷安特骑行app爬虫](./python/捷安特骑行app爬虫.md)
1. [捷安特骑行app逆向](./python/捷安特骑行app逆向.md)
1. [RPC-JS  Sekiro 使用详情  行者web爬虫](./python/行者web爬虫.md)

### 猿人学系列

[猿人学01](./python/猿人学01.md)

[猿人学02_ob混淆](./python/猿人学02_ob混淆.md)

[猿人学03_headers顺序](./python/猿人学03.md)

[猿人学04_css干扰](./python/猿人学04_css干扰.md)

[猿人学05_hook任意cookie被设置的瞬间](./python/猿人学第5题.md)




## ⑦  数据结构——算法相关

###  [数据结构 and 算法  教学文档](./python/数据结构.md)

###  [推荐算法](./python/部分算法文档/推荐算法——向量空间__陈煜文.pptx)




## ⑧  数据分析相关

###  [数据分析  教学文档](./python/数据分析.md)

###  [jieba 中文文档](./python/jieba.md)




## ⑨ 机器学习相关

### [机器学习  教学文档](./python/机器学习.md)




## ⑩  深度学习相关

###  深度学习	教学文档因格式原因，请进入文件夹自行查看

###  [OpenCV](./python/OpenCV.md)



## python 相关杂项

[Pyinstaller 打包 Pyzbar 运行闪退解决方案](./python/Pyinstaller打包Pyzbar解决方案.md)




# 前端相关

##  [基础网页标签元素](./前端/基础网页标签元素.md)

## CSS

### [css 基础](./前端/css.md)

### [flex布局详解](./前端/flex布局详解.md)

##  [js基础](./前端/js基础.md)

## [jQuery](./前端/jQuery.md)



# Linux相关

## ① Docker

### [Docker基础](./python/Docker手册.md)

### [一次对dockerfile所生成镜像的大小优化](./python/一次对dockerfile所生成镜像的大小优化.md)


## ②Linux

### [Linux基础](./python/Linux基础.md)

### [Linux常用命令](./python/linux常用命令.md)


## ③git

### [git基本操作](./python/git基础.md)






# IDE相关

## ① pycharm

### [pycharm完全使用指南](./python/pycharm完全使用指南.md)

### [pycharm非常规操作](./python/pycharm非常规操作.md)

 

# 网工相关

[在局域网中共享打印机的几种方式](./网工/局域网内共享打印机.md)

# 杂项

- [在ppt中展示百度 echars 图表](./杂项/PPT中展示Echarts图表.md)
- [esp32-cam 面部识别门禁系统](./杂项/esp32cam人脸识别门禁系统.md)
- [华为鸿蒙深度解析——兴业证券](./杂项/information/华为鸿蒙深度解析.pdf)
- [关于奖金压缩的一种算法](./杂项/关于奖金压缩的一种算法.md)

