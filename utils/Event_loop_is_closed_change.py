"""
【解决 asyncio.run()有时会报错 RuntimeError:Event loop is closed 情况】

当asyncio.run()被修改为:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    确实不会报错

大佬总结, 总而言之是asyncio.run()会自动关闭循环,并且调用_ProactorBasePipeTransport.__del__报错, 而asyncio.run_until_complete()不会.

大佬提供了解决方案, 就是重写方法以保证run()的运行.

【导入此包即可解决问题，如若还不能请使用上面的方式】
"""
from functools import wraps
from asyncio.proactor_events import _ProactorBasePipeTransport


def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise

    return wrapper


_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)
