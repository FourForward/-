之前写过一篇佳明的`fit`文件使用`gpsbabel`转换成`GPX`的文章,

但是后来发现转换后的GPX文件丢失了很多聚合信息,比如各项平均数,最大值.而且运动类型也无法查看,很是不满意,于是在网上重新查找佳明fit文件的解析方法

以下示例测试环境为:

python 3.8
		fitparse 1.2

## fitparse

## 安装

```shell
pip3 install fitparse
```

## 使用方式

```python
import fitparse
from datetime import timedelta

def get_message(file_name):
    file = fitparse.FitFile(file_name)
    # message = file.get_messages()	 # 返回一个生成器  其中每一项都可以看作是一行数据
    message = file.messages  # 等同于 list(file.get_messages())
    for item in message:
        # 获取每一行数据的名称,其中有几个名称非常关键:
        # item.name == 'file_id' (唯一) 一般位于第一行,里面包含该fit文件的编号ID
        # item.name == 'session' (唯一) 一般位于倒数第几行,里面包含该fit文件的所有聚合信息,各种平均数,极值,功率区间,起止时间,运动类型,等等
        # item.name == 'record' (非常多) 每一个record就代表一个GPS点的信息
        print(item.name)
        
        # 获取每一行的所有信息
        print(item.as_dict())
        
        # 获取特定行的所有信息,比如 file_id 这行
        # 注:实际使用时,建议 将 'file_id','session' 都打印出来放在一个py文件里,随时查看使用 'record'也可以随意打印一个
        if item.name == 'file_id':
            print(item.as_dict())
        
        # 获取行中某个特定的值 比如 获取该fit文件的运动类型 和起止时间
        # 注: 运动类型包含在 名称为 'session' 的行里面,键名为 'sport'
        if item.name == 'session':
            print(item.get_value('sport'))	# 运动类型 >>> 'cycling'
            # 转成国内时间需要加8小时
            # 如果你直接获取时间戳 item.get_raw_value('start_time'),请注意,佳明的时间戳是从1989.12.31 00:00:00 开始的
            start_time = item.get_value('start_time') + timedelta(hours=8)
        	end_time = item.get_value('timestamp') + timedelta(hours=8)
        
        """
        	获取所有点的GPS数据
        	佳明在fit文件中使用的是 semicircles(圆度值) 来记录GPS,比通用的wgs84要更加精准,转换关系如下
        	degrees = semicircles * ( 180 / 2^31 )
			semicircles = degrees * ( 2^31 / 180 )
        """
        try:
            print(item.get_value('position_lat') * (180 / 2 ** 31), item.get_value('position_long') * (180 / 2 ** 31))
            print(item.as_dict())
        except TypeError:
            continue
```

## 附件

### file_id 行内(部分)信息展示

该信息只作为参考,实际使用时,请自己打印该行信息:

```python
import datetime

file_id = {'name': 'file_id', 'fields': [
    # serial_number 文件编号 类型:int 
    {'name': 'serial_number', 'def_num': 3, 'base_type': 'uint32z', 'type': 'uint32z', 'units': None, 'value': 3950...83, 'raw_value': 3950...83},
    {'name': 'time_created', 'def_num': 4, 'base_type': 'uint32', 'type': 'date_time', 'units': None, 'value': datetime.datetime(2018, 1, 24, 4, 52, 23), 'raw_value': 885703943},
    {'name': 'manufacturer', 'def_num': 1, 'base_type': 'uint16', 'type': 'manufacturer', 'units': None, 'value': 'garmin', 'raw_value': 1},
    {'name': 'garmin_product', 'def_num': 2, 'base_type': 'uint16', 'type':'garmin_product', 'units': None, 'value': 2533, 'raw_value': 2533},]}
```

### session 行内(部分)信息展示

session  内都是当前fit文件的聚集信息

该信息只作为参考,实际使用时,请自己打印该行信息:

```python

session = {'name': 'session', 'fields': [
    # 结束时间
    {'name': 'timestamp', 'def_num': 253, 'base_type': 'uint32', 'type': 'date_time', 'units': None, 'value': datetime.datetime(2018, 3, 25, 10, 26, 57), 'raw_value': 890908017},
    # 开始时间
    {'name': 'start_time', 'def_num': 2, 'base_type': 'uint32', 'type': 'date_time', 'units': None, 'value': datetime.datetime(2018, 3, 25, 0, 17, 20), 'raw_value': 890871440},
	.
    .
    .
    # 运动时间
    {'name': 'total_timer_time', 'def_num': 8, 'base_type': 'uint32', 'type': 'uint32', 'units': 's','value': 25048.871, 'raw_value': 25048871},
    # 总里程
    {'name': 'total_distance', 'def_num': 9, 'base_type': 'uint32', 'type': 'uint32', 'units': 'm', 'value': 88924.04,'raw_value': 8892404},
    .
    .
    .
    {'name': 'time_in_hr_zone', 'def_num': 65, 'base_type': 'uint32', 'type': 'uint32', 'units': 's',
     'value': (778.726, 5631.959, 7464.129, 4913.151, 4478.913, 1204.132, 0.0),
     'raw_value': (778726, 5631959, 7464129, 4913151, 4478913, 1204132, 0)},
    # 功率区间
    {'name': 'time_in_power_zone', 'def_num': 68, 'base_type': 'uint32', 'type': 'uint32', 'units': 's',
     'value': (13527.302, 1585.171, 1841.759, 990.07, 935.986, 813.014, 1078.521, 1631.342, 0.0, 0.0),
     'raw_value': (13527302, 1585171, 1841759, 990070, 935986, 813014, 1078521, 1631342, 0, 0)},
    .
    .
    .
    # 消耗卡路里
    {'name': 'total_calories', 'def_num': 11, 'base_type': 'uint16', 'type': 'uint16', 'units': 'kcal', 'value': 1979,'raw_value': 1979},
    # 速度
    {'name': 'avg_speed', 'def_num': 14, 'base_type': 'uint16', 'type': 'uint16', 'units': 'm/s', 'value': 3.55,'raw_value': 3550},
    {'name': 'max_speed', 'def_num': 15, 'base_type': 'uint16', 'type': 'uint16', 'units': 'm/s', 'value': 15.76,'raw_value': 15760},
    # 功率
    {'name': 'avg_power', 'def_num': 20, 'base_type': 'uint16', 'type': 'uint16', 'units': 'watts', 'value': 83,'raw_value': 83},
    {'name': 'max_power', 'def_num': 21, 'base_type': 'uint16', 'type': 'uint16', 'units': 'watts', 'value': 1591,'raw_value': 1591},
    # 总爬升 与下降
    {'name': 'total_ascent', 'def_num': 22, 'base_type': 'uint16', 'type': 'uint16', 'units': 'm', 'value': 626,'raw_value': 626},
    {'name': 'total_descent', 'def_num': 23, 'base_type': 'uint16', 'type': 'uint16', 'units': 'm', 'value': 647,'raw_value': 647},
    # 得分?
    {'name': 'training_stress_score', 'def_num': 35, 'base_type': 'uint16', 'type': 'uint16', 'units': 'tss','value': 770.3, 'raw_value': 7703},
    {'name': 'intensity_factor', 'def_num': 36, 'base_type': 'uint16', 'type': 'uint16', 'units': 'if', 'value': 1.113,'raw_value': 1113},
    # 运动类型
    {'name': 'sport', 'def_num': 5, 'base_type': 'enum', 'type': 'sport', 'units': None, 'value': 'cycling','raw_value': 2},
    # 子类型?
    {'name': 'sub_sport', 'def_num': 6, 'base_type': 'enum', 'type': 'sub_sport', 'units': None, 'value': 'generic','raw_value': 0},
    # 心率
    {'name': 'avg_heart_rate', 'def_num': 16, 'base_type': 'uint8', 'type': 'uint8', 'units': 'bpm', 'value': 128,'raw_value': 128},
    {'name': 'max_heart_rate', 'def_num': 17, 'base_type': 'uint8', 'type': 'uint8', 'units': 'bpm', 'value': 179,'raw_value': 179},
    # 踏频
    {'name': 'avg_cadence', 'def_num': 18, 'base_type': 'uint8', 'type': 'uint8', 'units': 'rpm', 'value': 68,'raw_value': 68},
    {'name': 'max_cadence', 'def_num': 19, 'base_type': 'uint8', 'type': 'uint8', 'units': 'rpm', 'value': 172,'raw_value': 172},]}
    .
    .
    .
```

### record 行内(部分)信息展示

每个record都是一个GPS点, 里面都是当前GPS点的瞬时信息

该信息只作为参考,实际使用时,请自己打印该行信息:

```python
record = {'name': 'record', 'fields': [
    # 时间戳 和 经纬度
    {'name': 'timestamp', 'def_num': 253, 'base_type': 'uint32', 'type': 'date_time', 'units': None,'value': datetime.datetime(2018, 3, 25, 10, 19, 11), 'raw_value': 890907551},
    {'name': 'position_lat', 'def_num': 0, 'base_type': 'sint32', 'type': 'sint32', 'units': 'semicircles','value': 365908323, 'raw_value': 365908323},
    {'name': 'position_long', 'def_num': 1, 'base_type': 'sint32', 'type': 'sint32', 'units': 'semicircles','value': 1241201927, 'raw_value': 1241201927},
    # 当前里程
    {'name': 'distance', 'def_num': 5, 'base_type': 'uint32', 'type': 'uint32', 'units': 'm', 'value': 86430.14,'raw_value': 8643014},
    {'name': 'accumulated_power', 'def_num': 29, 'base_type': 'uint32', 'type': 'uint32', 'units': 'watts','value': 1801134, 'raw_value': 1801134},
    # 海拔
    {'name': 'enhanced_altitude', 'def_num': 78, 'base_type': 'uint32', 'type': 'uint32', 'units': 'm','value': 452.79999999999995, 'raw_value': 452.79999999999995},
    {'name': 'altitude', 'def_num': 2, 'base_type': 'uint16', 'type': 'uint16', 'units': 'm','value': 452.79999999999995, 'raw_value': 4764},
    # 速度
    {'name': 'enhanced_speed', 'def_num': 73, 'base_type': 'uint32', 'type': 'uint32', 'units': 'm/s', 'value': 8.659,'raw_value': 8.659},
    {'name': 'speed', 'def_num': 6, 'base_type': 'uint16', 'type': 'uint16', 'units': 'm/s', 'value': 8.659,'raw_value': 8659},
    # 功率
    {'name': 'power', 'def_num': 7, 'base_type': 'uint16', 'type': 'uint16', 'units': 'watts', 'value': 191,'raw_value': 191},
    # 心率
    {'name': 'heart_rate', 'def_num': 3, 'base_type': 'uint8', 'type': 'uint8', 'units': 'bpm', 'value': 151,
     'raw_value': 151},
    # 踏频
    {'name': 'cadence', 'def_num': 4, 'base_type': 'uint8', 'type': 'uint8', 'units': 'rpm', 'value': 95,'raw_value': 95},
    # 温度
    {'name': 'temperature', 'def_num': 13, 'base_type': 'sint8', 'type': 'sint8', 'units': 'C', 'value': 20,'raw_value': 20},]}
```

