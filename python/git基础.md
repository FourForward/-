综合项目及工具
==========================

| Tedu Python 教学部 |
| ------------------ |
| Author：吕泽       |

-----------

[TOC]

## 1. 软件项目开发

### 1.1 软件项目开发流程

```
需求分析 ----> 概要设计  ---> 项目计划 ----> 详细设计---> 编码测试 -----> 项目测试 ----> 调试修改 ---> 项目发布----> 后期维护
```

* 需求分析 ： 确定用户的真实需求 

>  1. 确定用户的真实需求，项目的基本功能
>  2. 确定项目的整体难度和可行性分析
>  3. 需求分析文档，用户确认

* 概要设计：对项目进行初步分析和整体设计

> 1. 确定整体架构
> 2. 进行技术可行性分析
> 3. 确定技术整体思路和使用框架模型
> 4. 形成概要文档指导开发流程

![](img/git基础/visio.jpg)

* 项目计划 ： 确定项目开发的时间轴和流程

> 1. 确定开发工作的先后顺序
> 2. 确定时间轴  ，事件里程碑
> 3. 人员分工 
> 4. 形成甘特图和思维导图等辅助内容

![](img/git基础/gt.jpg)

* 详细设计 ： 项目的具体实现

> 1.形成详细设计文档 ： 思路，逻辑流程，功能说明，技术点说明，数据结构说明，代码说明

* 编码测试 ： 按照预定计划实现代码编写，并且做基本检测

> 1. 代码编写
> 2. 写测试程序
> 3. 技术攻关

* 项目测试 ： 对项目按照功能进行测试

> 1. 跨平台测试 ，使用测试
> 2. 根据测试报告进行代码修改
> 3. 完成测试报告

* 项目发布

> 1.项目交付用户进行发布
> 2.编写项目说明文档

* 后期维护

> 1.维护项目正常运转
> 2.进行项目的迭代升级

### 1.2  开发注意事项

* 按时完成项目工作和项目时间不足之间的冲突
* 项目实施人员之间的冲突

### 1.3 项目管理工具

* 编写文档： word  ppt  excel  markdown   LaTex
* 项目流程图 ： Mindmanager  visio
* 项目管理 ： project
* 代码管理 ： svn   git



## 2. GIT和GitHub

### 2.1 GIT概述

* 什么是GIT

    GIT是一个开源的分布式版本控制系统，用于高效的管理各种大小项目和文件。

* 代码管理工具的用途

    * 防止代码丢失，做备份
    * 项目的版本管理和控制，可以通过设置节点进行跳转
    * 建立各自的开发环境分支，互不影响，方便合并
    * 在多终端开发时，方便代码的相互传输

* GIT的特点

    * git是开源的，多在*nix下使用，可以管理各种文件

    * git是分布式的项目管理工具(SVN是集中式的)

    * git数据管理更多样化，分享速度快，数据安全

    * git 拥有更好的分支支持，方便多人协调

        ![](img/git基础/分布.jpg)

        


> sudo apt  install  git



### GIT安装

#### linux下安装

```bash
sudo apt install git
```

#### windows下安装

首先抛一个Windows用户的下载链接：[Git for windows](https://git-scm.com/download/win)
	下载下来之后直接安装，除了下图选第一个，其他的不用改，直接next就行。
	选这个`use git from git bash only`

![img](img/git基础/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70.png)

安装完成后我的电脑上是显示了这么三个东西的。

![这里写图片描述](img/git基础/format,png.png)

Git CMD：
　　		Git CMD我并没用过，但是我查了一下它是什么。据别人说，Git中的Bash是基于CMD的，在CMD的基础上增添一些新的命令与功能。所以建议在使用的时候，用Bash更加方便（原网址）。
Git GUI：
　　		Git GUI，Git GUI是Git Bash的替代品，他为Windows用户提供了更简便易懂的图形界面。（但是相比GitHub Desktop这个桌面版客户端，_(:3 」∠)我觉得Git GUI也没什么用。）
Git Bash：
　　		Git Bash，Git Bash是命令行操作，官方介绍有一句就是“让*nix用户感到宾至如归。”（(;´༎ຶД༎ຶ`) 当然了，萌新用户使用了就肥肠憋屈。）



### 2.2 GIT使用

![git结构](img/git基础/git.jpeg)

* 基本概念
    * 工作区：项目所在操作目录，实际操作项目的区域
    * 暂存区: 用于记录工作区的工作（修改）内容
    * 仓库区: 用于备份工作区的内容
    * 远程仓库: 远程主机上的GIT仓库

> 注意： 在本地仓库中，git总是希望工作区的内容与仓库区保持一致，而且只有仓库区的内容才能和其他远程仓库交互。



#### 2.2.1 初始配置

**第一件事设置用户**。注意这个不是登录哦，是给你的电脑设置一个用户，等你上传的时候，告诉远程仓库是谁上传的而已。

* 配置命令： git config --global [选项]
* 配置文件位置:  ~/.gitconfig

1. 配置用户名

```bash
e.g. 将用户名设置为Tedu
sudo git config --global user.name Tedu
```

2. 配置用户邮箱

```bash
e.g. 将邮箱设置为lvze@tedu.cn
git config --global user.email lvze@tedu.cn
```

3. 查看配置信息

```bash
git config --list
# 注意： 该命令需要在某个git仓库下执行
```





#### 2.2.2 基本命令

* 初始化仓库

    ```bash
    git init 
    意义：将某个项目目录变为git操作目录，生成git本地仓库。即该项目目录可以使用git管理
    # 进入到你想建立本地仓库的文件夹，它可以是空的，也可以已经有代码，直接 init 就好。
    # 初始化成功之后，你的文件夹里就会多出.git的隐藏目录
    ```

* 查看本地仓库状态

    ```bash
    git  status
    说明: 初始化仓库后默认工作在master分支，当工作区与仓库区不一致时会有提示。
    ```

* 将工作内容记录到暂存区

    ```bash
    git add [files..]
    
    e.g. 将文件 a ，b 记录到暂存区
    git add  a b
    
    e.g. 将所有文件（不包含隐藏文件）记录到暂存区
    git add  *
    ```

    

* 设置忽略文件

在GIT项目中可以在项目根目录添加**.gitignore**文件的方式，规定相应的忽略规则，用来管理当前项目中的文件的忽略行为。.gitignore 文件是可以提交到公有仓库中，这就为该项目下的所有开发者都共享一套定义好的忽略规则。在.gitignore 文件中，遵循相应的语法，在每一行指定一个忽略规则。

```bash
# .gitignore忽略规则简单说明

file            # 表示忽略file文件
*.a             # 表示忽略所有 .a 结尾的文件
!lib.a          # 表示但lib.a除外
build/          # 表示忽略 build/目录下的所有文件，过滤整个build文件夹；

```

但是要注意，如果之前已经将这些需要忽略的文件提交了，那么之前所提交的这些应该被忽略的文件依然会被继续跟踪，因此，需要从存储库中将其删除，linux方式如下：

```shell
find . -name "*.pyc" -exec git rm -f "{}" \;
# 从git中删除作为跟踪文件的忽略文件后，将此更改提交到存储库即可

如果是要取消对某个目录的跟踪
# 先查看在git上将要要删除哪些文件，以免删错
git rm -r -n --cached user/migrations/
# 然后执行
git rm -r --cached u/migrations/
```



* 取消文件暂存记录

    ```bash
    git rm --cached [file] 
    ```

    

* 将文件同步到本地仓库

```bash
git commit [file] -m [message]
# -m 表示添加一些同步信息，表达同步内容,不加file表示同步所有暂存记录的文件

# 将暂存区所有记录同步到仓库区
git commit  -m 'add files'

# 怎么抢救一下commit的注释？
$ git commit --amend -m "修改的内容"
```



* 查看commit 日志记录

    ```bash
    git log
    git log --pretty=oneline
    ```

    

* 将暂存区或者某个commit点文件恢复到工作区

    ```bash
    git checkout [commit] -- [file]
    
    # 将a.jpg文件恢复,不写commit表示恢复最新保存的文件内容
    git checkout  --  a.jpg
    ```

    

* 移动或者删除文件

    ```bash
    git  mv  [file] [path]
    git  rm  [files]
    ```
    


### 2.3 版本控制

* 退回到上一个commit节点

    ```bash
    git reset --hard HEAD^
    # 一个 ^ 表示回退1个版本，依次类推。当版本回退之后工作区会自动和当前commit版本保持一致
    ```

    

* 退回到指定的commit_id节点

    ```bash
    git reset --hard [commit_id]
    ```

    

* 查看所有操作记录

    执行版本跳转之前一定要保证工作区是干净的

    ```bash
    git reflog
    # 注意:最上面的为最新记录，可以利用commit_id去往任何操作位置
    ```

    

* 创建标签

    * 标签: 在项目的重要commit位置添加快照，保存当时的工作状态，一般用于版本的迭代。

        ```bash
        git  tag  [tag_name] [commit_id] -m  [message]
        # 说明: commit_id可以不写则默认标签表示最新的commit_id位置，message也可以不写，但是最好添加。
        
        # 在最新的commit处添加标签v1.0
        git tag v1.0 -m '版本1'
        ```

        

* 查看标签

```
 git tag  查看标签列表
 git show [tag_name]  查看标签详细信息
```

* 去往某个标签节点

```
git reset --hard [tag]
```

* 删除标签

```
git tag -d  [tag]
```



###  2.4 保存工作区

* 保存工作区内容

    适用于工作中临时有事离开，但是代码还没有完成，不能上传，只能暂存。

    ```
    git stash save [message]
    说明: 将工作区未提交的修改封存，让工作区回到修改前的状态
    ```

* 查看工作区列表

    ```
    git stash  list
    说明:最新保存的工作区在最上面
    ```

* 应用某个工作区

    选择工作区之前，必须保证当前工作区是干净的

    ```
    git stash  apply  [stash@{n}]
    ```

* 删除工作区

    ```
    git stash drop [stash@{n}]  删除某一个工作区
    git stash clear  删除所有保存的工作区
    ```



### 2.5 分支管理

#### 2.5.1 基本概念

* 定义: 分支即每个人在原有代码（分支）的基础上建立自己的工作环境，完成单独开发，之后再向主分支统一合并工作内容。

* 好处

    * 各自开发互不干扰

    * 防止误操作对其他开发者的影响

        ![](img/git基础/fz.jpg)

#### 2.5.2 基本操作

* 查看现有分支

    ```
    git branch
    说明: 前面带 * 的分支表示当前工作分支
    ```

    

* 创建分支

    创建分支前，确保工作区是干净的

    ```
    git branch [branch_name]
    说明: 基于a分支创建b分支，此时b分支会拥有a分支全部内容。在创建b分支时最好保持a分支"干净"状态。
    ```

* 切换工作分支

    ```bash
    git checkout [branch]
    # 说明: 2,3可以同时操作，即创建并切换分支
    
    git checkout -b [branch_name]  # 可以同时完成创建分支和切换分支的工作
    ```

    

* 合并分支

    ```bash
    git merge [branch]
    # 现在，别人已经更新了远程主分支代码（没更新就极其方便了，也不必说了，快速更新）我想把分支合并到主分支。 我应该，先回到主分支，并更新。
    git  checkout master
    git pull [] master
    git merge [branch]
    git push []
    ```

    > 注意：分支的合并一般都是子分支向父分支中合并

* 删除分支

    ```
     git branch -d [branch]  删除分支
     git branch -D [branch]  删除没有被合并的分支
    ```

    ![分支合并](img/git基础/merge.png)

#### 2.5.3 分支冲突问题

* 定义： 当分支合并时，原来的父分支发生了变化，在合并过程中就会产生冲突问题，这是合并分支过程中最为棘手的问题。

* 冲突情形1—— 原来的分支增加了新文件或者原有文件发生了变化

    此时合并可能会出现:

    ![](img/git基础/merge1.png)

    此时只要先摁 **ctrl-o** 写入，然后回车，再摁**ctrl-x** 离开就可以了。

    也可能出现提示让直行commit合并，那么此时只需要直行commit操作就可以了。这种冲突比较好解决。

    

* 冲突情形2—— 子分支和父分支修改了相同的文件

    此时会出现：

    ![](img/git基础/merge2.png)

    这种冲突不太好解决需要自己进入文件进行修改后，再直行add ，commit操作提交

* 总结

    * 尽量在项目中降低耦合度不同给的分支只编写自己的模块。
    * 如果必须修改原来父级分支的文件内容，那么做好分工，不要让多个分支都修改同一个文件。

### 2.6 GitHub使用

* 远程仓库

    远程主机上的GIT仓库。实际上git是分布式结构，每台主机的git仓库结构类似，只是把别人主机上的git仓库称为远程仓库。GitHub可以帮助我们建立一个远程仓库。

* GitHub介绍

    GitHub是一个开源的项目社区网站，拥有全球最多的开源项目。开发者通过可以注册网站账户，在GitHub建立自己的项目仓库（我们可以视作一个远程仓库）,GitHub规定GIT为它的唯一代码管理工具。

    GitHub网址：[github.com](https://github.com/)



#### 2.6.1 获取项目

- 在左上角搜索栏搜索想要的获取的项目

![](img/git基础/1.png)

- 选择项目后复制项目git地址

![](img/git基础/2.png)

- 在本地使用git clone方法即可获取

```
git clone https://github.com/xxxxxxxxx
```

> 注意:
>
> 1. 获取到本地的项目会自动和GitHub远程仓库建立连接。且获取的项目本身也是个git项目。
> 2. GitHub提供两种地址链接方式，http方式和SSH方式。通常访问自己的项目可以使用SSH方式，clone别人的项目使用http方式。  



#### 2.6.2 创建自己的项目仓库

- 点击右上角加号下拉菜单，选择新的仓库

![](img/git基础/4.png)

- 填写相应的项目信息即可

    ![](img/git基础/0.png)

- github仓库相对本地主机就是一个远程仓库通过remote连接

    ![](img/git基础/7.png)

    

    

    与创建的仓库建立新链接

    - 使用https链接

        ```bash
        # 后续操作每次上传内容都需要输入密码，比较麻烦，一般用于临时计算机的连接使用
        # $ git remote add + 名字 + 连接地址
        git remote  add origin https://github.com/xxxxxxxxx
        # 后续无需输入密码，一般用于自己信任的计算机
        git remote add origin git@github.com:lvze0321/AID.git
        # 查看连接的远程仓库名称和地址
        git remote -v
        # 断开远程仓库连接
        git remote rm [origin]
        ```

    - 使用SSH连接

        ```
        # 先建立秘钥信任
        1. 将自己要连接github的计算机的ssh公钥内容复制
        2. github上选择头像下拉菜单，settings-》SSH and GPG keys-》new SSH key
        ```

    创建公钥：

    1.检查你电脑上是否有SSH Key

    ```bash
    ~/.ssh
    # 或者用
    ~/.ssh ls
    ```

    ​	上边这行命令的作用是看一哈你的电脑上有没有.ssh文件夹。

    ​	如果电脑上有，就会显示bash: /c/Users/…/.ssh: Is a directory
    ​	如果电脑上没有，那就显示bash: /c/Users/…/.ssh: No such file or directory

    2.创建SSH Key

    ​	**如果你电脑上有了，你就可以直接跳过这一步**

    ​	在Git Bash中输入以下内容，然后一路按回车

    ```bash
    $ ssh-keygen -t rsa -C "你的邮箱"
    # 这里的邮箱只是一个注释，可以随意写
    ```

    ```bash
    # 如果不是一路按回车，那么按照以下攻略：
    然后就会显示这两行：
    Generating public/private rsa key pair.
    Enter file in which to save the key (/c/Users/16627/.ssh/id_rsa):
    
    这是让你输入一个文件名，用于保存刚才生成的 SSH key 代码。为了避免麻烦，不用输入，直接回车，那么就会默认生成id_rsa和id_rsa.pub两个秘钥文件。
    这时候已经创建好.ssh这个文件夹了，会提示：
    Created directory ‘/c/Users/16627/.ssh’.
    紧接着又会问你：
    Enter passphrase (empty for no passphrase):
    就是让你输入密码，如果你设置了密码，那在你使用ssh传输文件的时候，你就要输入这个密码。为了避免麻烦，建议不用设置，直接回车。
    Enter same passphrase again:
    这就是让你再输入一次密码，就跟我们注册账号时候设置密码需要设置两次一样。上一步没设置密码，这里直接回车就可以了。到这里你的秘钥就设置好了，你会收到这段代码提示：
    Your identification has been saved in /c/Users/…/.ssh/id_rsa
    Your public key has been saved in /c/Users/…/.ssh/id_rsa.pub
    还会向你展示你的秘钥长啥样
    ```

    ![img](img/git基础/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70.png)

    

    当你看到上面这段代码，那就说明你的 SSH key 已经创建成功，你可以再使用`~/.ssh`看一下，现在文件是真的存在了。

    

    将公钥【id_rsa.pub】内容添加进去，并且起一个标题名字，点击添加

    ![](img/git基础/8.png)

    ![](img/git基础/9.png)

    

    

- 如果是自己的仓库需要删除，则选择自己的仓库选择settings，在最后可以选择删除仓库。

![](img/git基础/5.jpg)
![](img/git基础/6.jpg)



#### 2.6.3 远程仓库操作命令

* 将本地分支推送给远程仓库

    ```
    # 将master分支推送给origin主机远程仓库，第一次推送分支使用-u表示与远程对应分支	建立自动关联
    git push -u origin  master
    
    git push origin  [:branch]  # 删除向远程仓库推送的分支
    ```

* 推送代码到远程仓库

    ```
    # 如果本地的代码有修改项推送给远程仓库
    git push
    ```

* 推送标签

    ```
    git push origin [tag]  推送一个本地标签到远程
     
    git push origin --tags  推送所有本地所有标签到远程
    
    git push origin --delete tag  [tagname]  删除向远程仓库推送的标签
    ```

  

* 推送旧的版本

    ```
    # 用于本地版本比远程版本旧时强行推送本地版本
    git push --force origin  
    ```



* 从远程获取代码

    ```
    git pull
    ```

