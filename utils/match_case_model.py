"""
    来源：https://github.com/edgedb/edgedb/blob/master/edb/common/value_dispatch.py
    按参数值进行分派    适用于 python < 3.10
    python >=3.10 请直接使用 match case 语句
"""
import functools


def value_dispatch(func):
    """
    适用于同步函数
    """
    registry = {}

    @functools.wraps(func)
    def wrapper(arg0, *args, **kwargs):
        """
           arg0: 即是调用函数时，传递的那个 选择分支的参数
        """
        try:
            delegate = registry[arg0]
        except KeyError:
            pass
        else:
            # 这里传入arg0参数，需要在定义分支函数时，接收该参数，尽管有时并不会使用该参数
            return delegate(arg0, *args, **kwargs)

        return func(arg0, *args, **kwargs)

    __register_tools(wrapper, registry)
    return wrapper


def value_dispatch_async(func):
    """
        适用于异步函数
    """
    registry = {}

    @functools.wraps(func)
    async def wrapper(arg0, *args, **kwargs):
        """
           arg0: 即是调用函数时，传递的那个 选择分支的参数
        """
        try:
            delegate = registry[arg0]
        except KeyError:
            pass
        else:
            # 这里传入arg0参数，需要在定义分支函数时，接收该参数，尽管有时并不会使用该参数
            return await delegate(arg0, *args, **kwargs)

        return await func(arg0, *args, **kwargs)

    __register_tools(wrapper, registry)
    return wrapper


def value_dispatch_class(func):
    """
        适用于同步的实例方法
    """
    registry = {}

    @functools.wraps(func)
    def wrapper(self, arg0, *args, **kwargs):
        """
           arg0: 即是调用函数时，传递的那个 选择分支的参数
        """
        try:
            delegate = registry[arg0]
        except KeyError:
            pass
        else:
            # 这里传入arg0参数，需要在定义分支函数时，接收该参数，尽管有时并不会使用该参数
            return delegate(self, arg0, *args, **kwargs)

        return func(self, arg0, *args, **kwargs)

    __register_tools(wrapper, registry)
    return wrapper


def value_dispatch_class_async(func):
    """
        适用于异步的实例方法
    """
    registry = {}

    @functools.wraps(func)
    async def wrapper(self, arg0, *args, **kwargs):
        """
           arg0: 即是调用函数时，传递的那个 选择分支的参数
        """
        try:
            delegate = registry[arg0]
        except KeyError:
            pass
        else:
            # 这里传入arg0参数，需要在定义分支函数时，接收该参数，尽管有时并不会使用该参数
            return await delegate(self, arg0, *args, **kwargs)

        return await func(self, arg0, *args, **kwargs)

    __register_tools(wrapper, registry)

    return wrapper


def __register_tools(wrapper, registry):
    def register(value):
        def wrap(func):
            if value in registry:
                raise ValueError(
                    f'@value_dispatch: there is already a handler '
                    f'registered for {value!r}'
                )
            registry[value] = func
            return func

        return wrap

    def register_for_all(values):
        def wrap(func):
            for value in values:
                if value in registry:
                    raise ValueError(
                        f'@value_dispatch: there is already a handler '
                        f'registered for {value!r}'
                    )
                registry[value] = func
            return func

        return wrap

    wrapper.register = register
    wrapper.register_for_all = register_for_all


if __name__ == '__main__':
    import asyncio
    from match_case_model import value_dispatch, value_dispatch_async, value_dispatch_class_async, value_dispatch_class
    # 四个装饰器分别对应 value_dispatch: 同步函数， value_dispatch_async: 异步函数，
    # value_dispatch_class_async: 异步实例方法， value_dispatch_class: 同步实例方法

    class Demo:
        @value_dispatch_class_async
        async def eat(self, fruit, *args, **kwargs):
            """
                主函数，需要选择4个装饰器之一来装饰，这是类中的异步实例方法，所以使用该装饰器
            :param fruit: 分支选择参数
            :param args, kwargs: 选择分支失败后用来接收原本传给分支的额外参数
            """
            return f"I don't want a {fruit}..."

        @eat.register('apple')  # 注册 fruit == 'apple' 时的函数
        async def _eat_apple(self, fruit, feel):
            """
                分支函数（被@主函数.register("XXX")装饰的函数）
            :param fruit: 调用主函数时传入的分支选择参数，该函数体内可能用不上这个参数，但是必须要接收该参数
            :param feel: 分支函数需要的额外参数，只要有一个分支函数接收该参数，那么所有分支函数都要接收该参数
            """
            return f"I love {fruit},{feel}"

        # @eat.register('eggplant')   # 一个函数可以接受多个注册，但推荐使用下面那个方式
        # @eat.register('squash')
        # async def _eat_what(self, fruit, feel):
        #     return f"I didn't know {fruit} is a fruit!"

        @eat.register_for_all(('eggplant', 'squash'))  # 一个函数接受多个注册的方式
        async def _eat_what(self, fruit, feel):  # 这个分支无需使用feel参数，但还是需要接收
            return f"I didn't know {fruit} is a fruit!"


    a = Demo()
    print(asyncio.run(a.eat("apple", 'happy')))
    print(asyncio.run(a.eat("eggplant", 'happy')))
    print(asyncio.run(a.eat("origin", 'happy')))
