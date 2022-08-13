[TOC]

# 列表

查找

```python
L.index(v, begin, end)  # 返回对应元素的索引下标, begin为开始索引，end为结束索引,当 value 不存在时触发ValueError错误 
L.count(x)		# 用于统计某个元素在列表中出现的次数 
L.pop(index)	# 删除索引对应的元素，如果不加索引，默认删除最后元素，同时返回删除元素的引用关系
L.insert(index, obj)	# 将某个元素插放到列表中指定的位置 
L.extend(lst)	# 向列表追加另一个列表
L.remove(x)		# 从列表中删除第一次出现在列表中的值 
L.clear()		# 清空列表,等同于 L[:] = [] 
L.sort(reverse=False)	# 将列表中的元素进行排序，默认顺序按值的小到大的顺序排列 
L.reverse()		# 列表的反转，用来改变原列表的先后顺序 
```

拷贝

```python
L.copy()		# 复制此列表（只复制一层，不会复制深层对象) 
```

# 字典

## 查找



locals()将当前局部变量全部存入字典

[**get(key, default=None)**](http://www.runoob.com/python3/python3-att-dictionary-get.html)
		返回指定键的值，如果值不在字典中返回default值（默认值）

 

[**setdefault(key, default=None)**](http://www.runoob.com/python3/python3-att-dictionary-setdefault.html)

<font color='red'>如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，</font>
		default 默认值为 None。		解决了很多时候需要先判断键是否存在的问题

```python
In [1]: s = {'key1':20}                                                                                                                                                                 In [2]: s.get('key1')                                                                       Out[2]: 20                                                                                                                                                                               In [3]: s.setdefault('key1',30)                                                             Out[3]: 20                                                                                                                                                                               In [4]: s                                                                                   Out[4]: {'key1': 20}

```

[**popitem()**](http://www.runoob.com/python3/python3-att-dictionary-popitem.html)
		随机返回并删除字典中的一对键和值(一般删除末尾对)。

 

[**items()**](http://www.runoob.com/python3/python3-att-dictionary-items.html)
		以列表返回可遍历的(键, 值) 元组数组

 

[**keys()**](http://www.runoob.com/python3/python3-att-dictionary-keys.html)
		返回一个迭代器，可以使用 list() 来转换为列表

 

[**values()**](http://www.runoob.com/python3/python3-att-dictionary-values.html)
		返回一个迭代器，可以使用 list() 来转换为列表

## 修改

[**update(dict2)**](http://www.runoob.com/python3/python3-att-dictionary-update.html)**
** 字典记录累加，该方法没有任何返回值。

 

[**clear()**](http://www.runoob.com/python3/python3-att-dictionary-clear.html)**
** 删除字典内所有元素

# 集合

[update()](http://www.runoob.com/python3/ref-set-update.html) 
		给集合添加新的元素或者集合

[clear()](http://www.runoob.com/python3/ref-set-clear.html) 移除集合中的所有元素

[pop()](http://www.runoob.com/python3/ref-set-pop.html) 随机移除元素 

# 字符串

## 判断

**[isspace()](http://www.runoob.com/python3/python3-string-isspace.html)**

如果字符串中只包含空白，则返回 True，否则返回 False.

[**startswith(substr, beg=0,end=len(string))**](http://www.runoob.com/python3/python3-string-startswith.html)

检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。

[**endswith(suffix, beg=0, end=len(string))**](http://www.runoob.com/python3/python3-string-endswith.html)

检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

## 查找

L.[**find(str, beg=0 end=len(string))**](http://www.runoob.com/python3/python3-string-find.html)

检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1,如果str = “” 则必然返回0

L.[**rfind(str, beg=0,end=len(string))**](http://www.runoob.com/python3/python3-string-rfind.html)

类似于 find()函数，不过是从右边开始查找.

L.[**count(str, beg= 0,end=len(string))**](http://www.runoob.com/python3/python3-string-count.html)

返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

## 修改

split       str.split('str')

```python
>>> msg='hello    world'
>>> msg.split(' ')
['hello', '', '', '', 'world']
```

拆分字符串,如果不填参数，则是按所有空字符串拆分，并且连续的空字符串会被视为一个空字符串

```python
>>> msg='hello \t \r\n world'
>>> msg.split()
['hello', 'world']
```

[**replace(old, new [, max\])**](http://www.runoob.com/python3/python3-string-replace.html)

把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。

[**lstrip()**](http://www.runoob.com/python3/python3-string-lstrip.html)

截掉字符串左边的空格或指定字符。

[**rstrip()**](http://www.runoob.com/python3/python3-string-rstrip.html)

删除字符串字符串末尾的空格.

[**strip([chars\])**](http://www.runoob.com/python3/python3-string-strip.html)

在字符串上执行 lstrip()和 rstrip()

[**lower()**](http://www.runoob.com/python3/python3-string-lower.html)

转换字符串中所有大写字符为小写.

[**upper()**](http://www.runoob.com/python3/python3-string-upper.html)

转换字符串中的小写字母为大写

[**swapcase()**](http://www.runoob.com/python3/python3-string-swapcase.html)

将字符串中大写转换为小写，小写转换为大写

## 对齐

[**center(width, fillchar)**](http://www.runoob.com/python3/python3-string-center.html)

返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。

[**zfill (width)**](http://www.runoob.com/python3/python3-string-zfill.html)

返回长度为 width 的字符串，原字符串右对齐，前面填充0

[**ljust(width\[, fillchar\])**](http://www.runoob.com/python3/python3-string-ljust.html)

返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。

# 时间

python中部分时间日期的格式化符号

| 格式 | 解释                                      |
| ---- | ----------------------------------------- |
| %y   | 两位数的年份表示（00-99）                 |
| %Y   | 四位数的年份表示（000-9999）              |
| %m   | 月份（01-12）                             |
| %d   | 月内中的一天（0-31）                      |
| %H   | 24小时制小时数（0-23）                    |
| %I   | 12小时制小时数（01-12）                   |
| %M   | 分钟数（00-59）                           |
| %S   | 秒数（00-59）                             |
| %a   | 本地简化星期名称                          |
| %A   | 本地完整星期名称                          |
| %b   | 本地简化的月份名称                        |
| %B   | 本地完整的月份名称                        |
| %c   | 本地相应的日期表示和时间表示              |
| %j   | 年内的一天（001-366）                     |
| %p   | 本地A.M.或P.M.的等价符                    |
| %U   | 一年中的星期数（00-53）星期天为星期的开始 |
| %w   | 星期（0-6），星期天为星期的开始           |
| %W   | 一年中的星期数（00-53）星期一为星期的开始 |
| %x   | 本地相应的日期表示                        |
| %X   | 本地相应的时间表示                        |
| %Z   | 当前时区的名称                            |
| %%   | %号本身                                   |



## time

**import** time

 时间戳（从1970年1月1日 *0:0:0 UTC* 到现在经过的秒数）

```python
time.time() 
# 1584156103.0306678
```

时间元组（年、月、日、时、分、秒、星期、这一年的第几天、夏令时）
获取当前本地时间元组

```python
time_tuple = time.localtime()

print(time_tuple)
print(time_tuple.tm_year) *# print(time_tuple[0])
print(time_tuple.tm_wday) *# print(time_tuple[-3]) # print(time_tuple[6])
```

### 时间戳 --> 时间元组

```python
time.localtime(1584156103.0306678)
```

### 时间元组 --> 时间戳

```python
time.mktime(time_tuple)		# 1584157476.0
```

### 时间元组 --> 字符串

```python
# 大写 Y 和小写 y 的区别
time.strftime("%y/%m/%d %H:%M:%S", time_tuple)	# 20/03/14 11:58:26
time.strftime("%Y/%m/%d %H:%M:%S", time_tuple)	# 2020/03/14 11:58:26
```

### 字符串 --> 时间元组

```python
time.strptime("2020/03/14 11:58:26", "%Y/%m/%d %H:%M:%S")
time.strptime("2020 26", "%Y %S")
```

## datetime

datatime模块重新封装了time模块，提供更多接口，提供的类有：date,time,datetime,timedelta,tzinfo。

主要用作日期时间之间的相互运算

### **1、date类**

datetime.date(year, month, day)

静态方法和字段

```python
date.max、date.min：date对象所能表示的最大、最小日期；
date.resolution：date对象表示日期的最小单位。这里是天。
date.today()：返回一个表示当前本地日期的date对象；
date.fromtimestamp(timestamp)：根据给定的时间戮，返回一个date对象；
```

```python
from datetime import *
import time

print('date.max:', date.max)
print('date.min:', date.min)
print('date.today():', date.today())
print('date.fromtimestamp():', date.fromtimestamp(time.time()))

#Output======================
# date.max: 9999-12-31
# date.min: 0001-01-01
# date.today(): 2016-10-26
# date.fromtimestamp(): 2016-10-26

```

```python
# 方法和属性

d1 = date(2011,6,3)	# date对象
d1.year		# 年
date.month	# 月
date.day	# 日
d1.replace(year, month, day)	# 生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）
d1.timetuple()		# 返回日期对应的time.struct_time对象；
>>> time.struct_time(tm_year=2011, tm_mon=6, tm_mday=3, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=154, tm_isdst=-1)

d1.weekday()		# 返回weekday，如果是星期一，返回0；如果是星期2，返回1，以此类推；

d1.isoweekday()		# 返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推；

d1.isocalendar()	# 返回格式如(year，month，day)的元组；
>>> (2011, 22, 5)
d1.isoformat()		# 返回格式如'YYYY-MM-DD’的字符串；
>>> '2011-06-03'
d1.strftime(fmt)	# 和time模块format相同。
```

### **2、time类**

datetime.time(hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ) 

静态方法和字段

```
time.min、time.max：time类所能表示的最小、最大时间。其中，time.min = time(0, 0, 0, 0)， time.max = time(23, 59, 59, 999999)；
time.resolution：时间的最小单位，这里是1微秒；
```

```python
# 方法和属性

t1 = datetime.time(10,23,15)	# time对象
t1.hour			# 时
t1.minute		# 分
t1.second		# 秒
t1.microsecond	# 微秒
t1.tzinfo		#时区信息
t1.replace([ hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )	# 创建一个新的时间对象，用参数指定的时、分、秒、微秒代替原有对象中的属性（原有对象仍保持不变）；
t1.isoformat()：返回型如"HH:MM:SS"格式的字符串表示；
t1.strftime(fmt)：同time模块中的format；
```

### **3、datetime类**

datetime相当于date和time结合起来，年月日是必须参数
datetime.datetime (year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )

#### 静态方法和字段

```python
datetime.today()	# 返回一个表示当前本地时间的datetime对象；
>>> datetime.datetime(2021, 10, 6, 0, 29, 21, 840636)
datetime.now([tz])	# 返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间；
>>> datetime.datetime(2021, 10, 6, 0, 29, 30, 47878)
datetime.utcnow()	# 返回一个当前utc时间的datetime对象；#格林威治时间

datetime.fromtimestamp(timestamp[, tz])	# 根据时间戳创建一个datetime对象，参数tz指定时区信息；
datetime.utcfromtimestamp(timestamp)	# 时间戳创建一个datetime对象；

# date和time，创建一个datetime对象；
datetime.combine(date, time)

# 式字符串转换为datetime对象；datetime.strptime('2020-01-01 15:30:59', '%Y-%m-%d %H:%M:%S') 超出取值范围或者分隔符号错误都会报错
datetime.strptime(date_string, format)
```

#### 实例方法和属性

```python
dt=datetime.now()  # datetime对象
# 基础属性
dt.year、month、day、hour、minute、second、microsecond、tzinfo
```

```python
dt.date()：获取date对象；
dt.time()：获取time对象；

dt.replace ([ year[ , month[ , day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] ] ] ])
```

```python

dt.timetuple ()	# time.struct_time(tm_year=2016 ... tm_hour=16,...)获取当前一个包含当前时间的结构体
dt.utctimetuple ()
dt.timestamp()	# 1463473711.057878  获取当前的时间戳
dt.toordinal ()
dt.weekday ()
dt.isocalendar ()
dt.isoformat ([ sep] )
dt.ctime ()	# 返回一个日期时间的C格式字符串，等效于time.ctime(time.mktime(dt.timetuple()))；
```

````python
dt.strftime (format)	# 格式化时间
# 使用方式
dt.strftime("%Y-%m-%d %H:%M:%S")	# '2021-12-23 14:46:41'
dt.strftime("%Y/%m/%d-%H:%M:%S")	# '2021/12/23-14:47:09'
dt.strftime("abc/def/%Y-%m-%d")	# 'abc/def/2021-12-23'	传入的普通字符串会原样返回,django用此方式来实现用户上传文件的储存目录随日期变化的需求 from django/db/models/fields/files.py import generate_filename

````



datetime 类相互之间的运算

```python
d1 = datetime.now()
d2 = datetime.now()

d3 = d2-d1
print(d3)
>>> datetime.timedelta(seconds=13, microseconds=344243)
print(d3.seconds)
>>> 13
```

### **4.timedelta类，时间加减**

使用timedelta可以很方便的在日期上做天days，小时hour，分钟，秒，毫秒，微妙的时间计算，如果要计算月份则需要另外的办法。

```python
from  datetime import *

dt = datetime.now()
#日期减一天
dt1 = dt + timedelta(days=-1)	# 昨天
dt2 = dt - timedelta(days=1)	# 昨天
# 日期加一天
dt3 = dt + timedelta(days=1)	# 明天
delta_obj = dt3-dt

print type(delta_obj),delta_obj	# <type 'datetime.timedelta'> 1 day, 0:00:00
print delta_obj.days ,delta_obj.total_seconds()	# 1 86400.0
```

