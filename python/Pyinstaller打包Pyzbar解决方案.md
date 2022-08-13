# Pyinstaller 打包 Pyzbar 后,exe程序无法运行的解决方案

## 问题

Pyinstaller 是python 打包exe程序的第三方库, 大多数情况下 使用 `pyinstaller -F 脚本.py` 可以打包出一个能够运行的`exe`程序

但是当脚本中导入了某些第三方库时, pyinstaller 打包出的程序将无法运行(闪退),

其中一个原因是pyinstaller 在打包时没有将某些第三方库一并打包进去, 就会导致 `import` 语句失败报错, 程序闪退.

## 解决方法

解决方案是: `修改配置文件, 指定所缺失的文件, 然后通过配置文件打包`

## 以下为示例:

### 准备脚本文件

```python
# bar_code_recognition.py
"""
    条形码识别程序:
    输入:
        快捷键触发,捕获整个屏幕截图中的二维码.
    输出:
        输出数字到剪切板
"""

import cv2
import pyautogui
import numpy as np
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol
import pyperclip
import keyboard
# import pillow


def get_bar_code():
    img = pyautogui.screenshot()	# 全屏截图
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_BGR2GRAY)	 # 黑白
    barcodes = pyzbar.decode(img, symbols=[ZBarSymbol.EAN13])	# 条形码识别
    if not barcodes:
        print(0)
        pyperclip.copy('')
        return
    print(barcodes[0].data.decode())
    pyperclip.copy(barcodes[0].data.decode())	# 将识别的结果存入系统剪切板


if __name__ == '__main__':
    keyboard.add_hotkey('f8', get_bar_code)	 # 添加 F8 为热键
    keyboard.wait('f9')	 # 输入 F9 关闭程序

```

### 准备虚拟环境venv

通过pycharm 创建虚拟环境,并安装以下依赖库

> 使用windows的管理员身份打开Power Shell, 进入虚拟环境后安装, 否则部分库无法安装.
>
> 安装时无需注重版本, 全部是最新版也行, 以下的版本号为 2022.05.07 安装时的最新版本号

```
numpy                     1.22.3
opencv-python             4.5.5.64
pyautogui                 0.9.53
pyzbar                    0.1.9
pyperclip                 1.8.2
keyboard                  0.13.5
pillow                    9.1.0
pyinstaller               5.0.1
```

### 问题复现

在虚拟环境中执行` pyinstaller -D .\bar_code_recognition.py`(测试阶段全部使用`-D`,这样可以向输出的dist 目录中添加或删除文件,以便调试)

手动双击打开`...\dist\bar_code_recognition`目录中的 `bar_code_recognition.exe` 文件, 会发现程序闪退,无法运行

### 问题分析

此时使用powershell执行该文件,可以看到如下报错信息:

```shell
>>> PS C:\Users\Administrator\Desktop\job_project\utools\evens\dist\bar_code_recognition> .\bar_code_recognition.exe
# 截选部分报错信息
>>> pyimod04_ctypes.install.<locals>.PyInstallerImportError: Failed to load dynlib/dll 'C:\\Users\\Administrator\\Desktop\\job_project\\utools\\evens\\dist\\bar_code_recognition\\pyzbar\\libiconv.dll'. Most likely this dynlib/dll was not found when the application was frozen.
```

提示该路径下缺少一个`.dll`文件,我们顺着路径去看一看,发现,不止是这个dll 文件, 连它的上一级目录 `pyzbar` 都不存在,

这说明了pyinstaller 在打包时,根本就没有将 `pyzbar`库打包进去.

此时我们手动拷贝整个 `pyzbar`库到`...\dist\bar_code_recognition`目录下(该库位于虚拟环境中),

再次运行程序(命令行或者双击程序都行), 发现程序已经可以正常使用.

于是现在修改pyinstaller 的配置文件`.spec` 中 Analysis 中的 datas 参数:

格式为:

```python
datas=[
        (
            'dell 文件的绝对路径',
            '该文件需要被放置的相对路径'
        ),
	]
```

示例:

```python
a = Analysis(
    .
    .
    .
    datas=[
        (
            r'C:\Users\Administrator\Desktop\job_project\utools\evens\venv\Lib\site-packages\pyzbar\libzbar-64.dll',
            r'.\pyzbar'
        ),
        (
            r'C:\Users\Administrator\Desktop\job_project\utools\evens\venv\Lib\site-packages\pyzbar\libiconv.dll',
            r'.\pyzbar'
        )
    ],
    .
    .
    .
)
```

保存该配置文件后,使用该配置文件重新打包程序: `pyinstaller .\bar_code_recognition.spec`

然后运行生成的exe文件,正常运行.测试成功.

### 解决方式

在虚拟环境下先执行一遍: `pyinstaller -F .\bar_code_recognition.py` 以生成配置文件`.spec`

然后修改配置文件中的内容,指定导入缺失的dll文件.

最后使用修改后的配置文件重新生成`exe`文件: `pyinstaller .\bar_code_recognition.spec`

打完收工.





