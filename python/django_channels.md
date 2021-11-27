django_channels简易教程

官方文档:[Django Channels — Channels 3.0.4 documentation](https://channels.readthedocs.io/en/stable/)

## 什么是Channels

Django本身不支持WebSocket，但可以通过集成Channels框架来实现WebSocket

## Django中使用Channel

### 安装channels

```shell
sudo pip3 install channels
sudo pip3 install channels-redis
```

### 安装daphne

```shell
sudo pip3 install daphne
```

daphne是一个http、http2和websocket协议服务器，用于 [ASGI](https://github.com/django/asgiref/blob/master/specs/asgi.rst)和 [ASGI-HTTP](https://github.com/django/asgiref/blob/master/specs/www.rst)， 为Django频道开发。

它支持协议的自动协商；不需要URL 前缀以确定WebSooT端点与HTTP端点。

*注意：*daphne 2与channels 1.x应用程序不兼容，仅与 频道2.x和其他asgi应用程序。安装1.x版本的Daphne 对于通道1.x支持

### 运行

只需将daphne指向您的asgi应用程序，并且可以选择 设置绑定地址和端口（默认为localhost，端口8000）：

```shell
# 进入 django 项目目录内
daphne 项目名称.asgi:application -b 0.0.0.0 -p 8001 
```

### 修改setting.py文件

```python
# 添加进 INSTALLED_APPS
INSTALLED_APPS = [
    'channels',		# 添加该行
    'django.contrib.admin',
    'django.contrib.auth',
    .
    .
    .
]

WSGI_APPLICATION = 'qixing_app.wsgi.application'
# 添加 ASGI_APPLICATION
ASGI_APPLICATION = 'qixing_app.asgi.application'	# 添加该行


# 添加 channels_redis 的配置
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)]
        }
    }
}
```

### 改写 `asgi.py` 文件

```python
# asgi.py
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack   # django 自带用户身份认证
from middleware.my_middleware import WsTokenVerify  # 自己写的用户身份认证
from 【应用名称】.urls import websocket_urlpatterns		# 导入url配置

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qixing_app.settings')

django_application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # 这里没有使用自带的身份认证AuthMiddlewareStack，改用自编的文件WsTokenVerify
    "websocket": WsTokenVerify(URLRouter(websocket_urlpatterns))
})
```

### 编写权限验证中间件（可省略）

项目目录下，新建一个 middleware 目录，内部创建一个 my_middleware.py 文件

```python
# middleware/my_middleware.py
# 这是一个无需在settings中注册的中间件
# 使用该中间件，需要前端在连接 WS 时，将 token放入headers中
import jwt


class WsTokenVerify:
    """
        websocket 使用的 token解析中间件
    """

    def __init__(self, app):
        # Store the ASGI application we were passed
        self.app = app

    async def __call__(self, scope, receive, send):
        headers = scope['headers']
        # headers 里面是一个个的元组类似于[(b'User-Agent',b'XXXX'),(b'token',b'XXXXX'),……]
        # 从headers中取出token
        for k, v in headers:
            if k.decode() == 'token':
                token = v.decode()
                break
        # 解析 token
        try:
            jwt_dict = jwt.decode(token, key=settings.TOKEN_KEY)
        except Exception as e:
            # 解析失败，则不做任何处理，直接交给视图函数，视图函数会尝试从scope中取出关键信息，失败则会断开websocket连接
            return await self.app(scope, receive, send)
        # 将客户端的唯一身份标识（关键信息）加入scope
        scope['uid'] = jwt_dict['uid']
        scope['nickname'] = jwt_dict['nickname']
        scope['group_name'] = jwt_dict['group_name']
        return await self.app(scope, receive, send)
```

### 编写url文件

```python
# 【应用名称】.urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 这是给http协议用的路由
]

websocket_urlpatterns = [
    # 这是给websocket协议用的路由， views.Connect.as_asgi() 指定了该应用下 views.py里面一个名为 Connect的类来处理Ws请求
    path(r'gps/connect', views.Connect.as_asgi()),
]
```

### 选择视图函数的类型

大致有两种类型，`WebsocketConsumer` 是**`同步`**类型，使用方式和django处理http请求的语法一致

`AsyncWebsocketConsumer`是**`异步`**类型，一旦选择异步类型，那么其中的所有代码，都应该选用异步代码，不可与同步代码混用

```python
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

class Connect(AsyncWebsocketConsumer 或者 WebsocketConsumer):
    pass
```

### 编写视图类

```python
# views.py
from channels.generic.websocket import AsyncWebsocketConsumer	# 这里选用了异步类型
class Connect(AsyncWebsocketConsumer):
    async def connect(self):
        # 请求连接的函数
        try:
            self.uid = self.scope['uid']
            self.nickname = self.scope['nickname']
            self.room_group_name = f"channel_{self.scope['group_name']}"
        except Exception as e:
            # 拒绝连接
            await self.close()
        else:
            # Join room group
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            # 建立连接
            await self.accept()

    async def disconnect(self, close_code):
        # 断开连接的函数
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        # 连接关闭
        await self.close(close_code)

    # Receive message from WebSocket
    async def receive(self, text_data=None, byte_text_data=None):
        """
			接收消息的函数
        """
        try:
            text_data_json = json.loads(text_data)
        except Exception as e:
            print('数据无法被json格式化', e)
            await self.disconnect(400)
        else:
            # 回传相同的信息的示例
            await self.send(text_data=json.dumps(text_data_json))
			
            # 向小组内所有成员推送信息的示例
            message = text_data_json['message']
            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name, {'type': 'chat_message', 'message': message})

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({'message': message}))

```

## 非常规使用方式

### [channels向小组中的某个特定成员推送消息](./django-channels如何向组内特定成员推送信息的解决方案.md)