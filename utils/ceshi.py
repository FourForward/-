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


if __name__ == '__main__':
    a = Demo()
    print(asyncio.run(a.eat("apple", 'happy')))
    print(asyncio.run(a.eat("eggplant", 'happy')))
    print(asyncio.run(a.eat("origin", 'happy')))
