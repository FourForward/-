优化 `Playwright API`文档跳转效果, 以及显示效果

以下步骤在 pycharm 的`CTRL + R 查找替换模式下进行`

### 1.将`<XXX>`的前面加上反斜杠

​		以优化 typora 的显示

```
将
<[NoneType](https://docs.python.org/3/library/constants.html#None)>
修改为
\<[NoneType](https://docs.python.org/3/library/constants.html#None)>
```

`<(.*?)>`

`\\<$1>`

### 2.修改自定义锚点 

​		以供 typora 下锚

```
将
[#](https://playwright.dev/python/docs/api/class-playwright#playwright-stop-return)
修改为
<a name="playwright-stop-return">#</a>
```

`\[#?\]\(https://playwright.dev/python/docs/api/([^\)]*?)#(.*?)\)`

`<a name="$2">#</a>`

### 3.修改指向锚点的超链接(带#)

​		以供 typora 跳转到自定义锚点

```
将
[browser.new_context(**kwargs)](https://playwright.dev/python/docs/api/class-browser#browser-new-context)
修改为
[browser.new_context(**kwargs)](#browser-new-context)
```

`\[([^\]]*?)\]\(https://playwright.dev/python/docs/api/([^\)]*?)#(.*?)\)`

`\[$1\]\(#$3\)`

### 4.1.修改指向锚点的超链接(不带#)

​		以供 typora 跳转到 **一级标题**

```
将
[APIRequestContext](https://playwright.dev/python/docs/api/class-apirequestcontext)
修改为
[APIRequestContext](#apirequestcontext)    # 一级标题锚是单词首字母大写,这里是全小写,实测typora的跳转是忽略大小写的,所以无需再修改大小写
```

`\[([^\]]*?)\]\(https://playwright.dev/python/docs/api/(.*?)\)`

`\[$1\]\(#$2\)`

### 4.2.修改指向锚点超链接的大小写(略: 实测typora的跳转是忽略大小写的)

