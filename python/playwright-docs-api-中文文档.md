# Playwright-docs-api 中文文档

[Playwright | Playwright Python 官方文档--需要科学上网](https://playwright.dev/python/docs/api/class-playwright)

vesion: 1.20

language: Python

拷贝时间: 2022.03.31

拷贝完整度: > 99%

机翻: >90%

翻译: 有道词典, 小玉的玉

备注: 该文档针对 typora 的使用方式做了部分优化(超链接显示,锚点跳转[具体优化方式](./playwright文档优化方式.md))

# Playwright

Playwright 模块提供了一个方法来启动浏览器实例。下面是一个使用Playwright 驱动自动化的典型例子:

- Sync

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("http://example.com")
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.goto("http://example.com")
    # other actions...
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

- [playwright.stop()](#playwright-stop)
- [playwright.chromium](#playwright-chromium)
- [playwright.devices](#playwright-devices)
- [playwright.firefox](#playwright-firefox)
- [playwright.request](#playwright-request)
- [playwright.selectors](#playwright-selectors)
- [playwright.webkit](#playwright-webkit)

## playwright.stop()<a name="playwright-stop">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="playwright-stop-return">#</a>

终止这个剧作家实例，以防它是绕过Python上下文管理器创建的。这在REPL应用程序中非常有用。

```python
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()

browser = playwright.chromium.launch()
page = browser.new_page()
page.goto("http://whatsmyuseragent.org/")
page.screenshot(path="example.png")
browser.close()

playwright.stop()
```

## playwright.chromium<a name="playwright-chromium">#</a>

- type: \<[BrowserType](#browsertype)>

这个对象可以用来启动或连接到Chromium，返回[Browser](#browser)的实例。

## playwright.devices<a name="playwright-devices">#</a>

- type: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)>

返回与[browser.new_context(**kwargs)](#browser-new-context)或[browser.new_page(**kwargs)](#browser-new-page)一起使用的设备的字典。

- Sync

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    webkit = playwright.webkit
    iphone = playwright.devices["iPhone 6"]
    browser = webkit.launch()
    context = browser.new_context(**iphone)
    page = context.new_page()
    page.goto("http://example.com")
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    webkit = playwright.webkit
    iphone = playwright.devices["iPhone 6"]
    browser = await webkit.launch()
    context = await browser.new_context(**iphone)
    page = await context.new_page()
    await page.goto("http://example.com")
    # other actions...
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

## playwright.firefox<a name="playwright-firefox">#</a>

- type: \<[BrowserType](#browsertype)>

此对象可用于启动或连接到Firefox，返回[Browser](#browser)的实例。

## playwright.request<a name="playwright-request">#</a>

- type: \<[APIRequest](#apirequest)>

公开可用于Web API测试的API。

## playwright.selectors<a name="playwright-selectors">#</a>

- type: \<[Selectors](#selectors)>

选择器可用于安装自定义选择器引擎。有关更多信息，请参见[Working with selectors](https://playwright.dev/python/docs/selectors)。

## playwright.webkit<a name="playwright-webkit">#</a>

- type: \<[BrowserType](#browsertype)>

这个对象可以用来启动或连接到WebKit，返回[Browser](#browser)的实例。



# APIRequest

公开可用于Web API测试的API。每个剧作家浏览器上下文都有一个APIRequestContext实例，它与页面上下文共享cookie。也可以手动创建一个新的APIRequestContext实例。更多信息请参见[此处](#apirequestcontext)。

- [api_request.new_context(**kwargs)](#api-request-new-context)

## api_request.new_context(**kwargs)<a name="api-request-new-context">#</a>

- `base_url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>  [api_request_context.get(url, **kwargs)](#api-request-context-get) 之类的方法,通过使用 [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 构造函数来构建相应的url. 例子:<a name="api-request-new-context-option-base-url">#</a>
    - baseURL= `http://localhost:3000` 时发送请求至`/bar.html` 结果是 `http://localhost:3000/bar.html`
    - baseURL= `http://localhost:3000/foo/` 时发送请求至 `./bar.html` 结果是`http://localhost:3000/foo/bar.html`
    - baseURL= `http://localhost:3000/foo` 时发送请求至(末尾不加斜杠) `./bar.html`结果是`http://localhost:3000/bar.html`
- `extra_http_headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 一个包含附加HTTP头的对象，每个请求都要发送.<a name="api-request-new-context-option-extra-http-headers">#</a>
- `http_credentials` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)>  [HTTP认证凭据](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).<a name="api-request-new-context-option-http-credentials">#</a>
    - `username` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
    - `password` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
- `ignore_https_errors` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 发送网络请求时是否忽略HTTPS错误。默认值为 `false`.<a name="api-request-new-context-option-ignore-https-errors">#</a>
- `proxy` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 网络代理设置.<a name="api-request-new-context-option-proxy">#</a>
    - `server` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 所有请求使用的代理。支持HTTP代理和SOCKS代理，例如: `http://myproxy.com:3128` or `socks5://myproxy.com:3128`.缩写形式 `myproxy.com:3128` 被认为是一个HTTP代理.
    - `bypass` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 可选，用逗号分隔的域，绕过代理，例如 `".com, chromium.org, .domain.com"`.
    - `username` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>可选 username，当HTTP代理需要鉴权时使用.
    - `password` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 当HTTP代理需要鉴权时可选密码.
- `storage_state` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 用给定的存储状态填充上下文。这个选项可以用来用通过 [browser_context.storage_state(**kwargs)](#browser-context-storage-state) or [api_request_context.storage_state(**kwargs)](#api-request-context-storage-state). 获得的登录信息初始化上下文。可以是保存存储的文件路径，也可以是 [browser_context.storage_state(**kwargs)](#browser-context-storage-state) or [api_request_context.storage_state(**kwargs)](#api-request-context-storage-state) 方法返回的值.<a name="api-request-new-context-option-storage-state">#</a>
    - `cookies` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]>
        - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `domain` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `path` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `expires` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> Unix 时间，单位为秒.
        - `httpOnly` \<[bool](https://docs.python.org/3/library/stdtypes.html)>
        - `secure` \<[bool](https://docs.python.org/3/library/stdtypes.html)>
        - `sameSite` \<"Strict"|"Lax"|"None">
    - `origins` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]>
        - `origin` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `localStorage` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]>
            - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
            - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 等待响应的最大时间，单位为毫秒。默认为 `30000` (30 seconds). 传递`0` 以禁用超时.<a name="api-request-new-context-option-timeout">#</a>
- `user_agent` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 在此上下文中使用的特定用户代理.<a name="api-request-new-context-option-user-agent">#</a>
- returns: \<[APIRequestContext](#apirequestcontext)><a name="api-request-new-context-return">#</a>

创建 [APIRequestContext](#apirequestcontext) 新实例.



# APIRequestContext

此API用于Web API测试。您可以使用它来触发API端点、配置微服务、为您的端到端测试准备环境或服务。当在[Page](#page)或 [BrowserContext](#browsercontext)中使用时，这个API将自动使用相应的 [BrowserContext](#browsercontext)中的cookie。这意味着如果您使用这个API登录，您的e2e测试将被登录，反之亦然。

- Sync

```python
import os
from playwright.sync_api import sync_playwright

REPO = "test-repo-1"
USER = "github-username"
API_TOKEN = os.getenv("GITHUB_API_TOKEN")

with sync_playwright() as p:
    # This will launch a new browser, create a context and page. When making HTTP
    # requests with the internal APIRequestContext (e.g. `context.request` or `page.request`)
    # it will automatically set the cookies to the browser page and vise versa.
    browser = p.chromium.launch()
    context = browser.new_context(base_url="https://api.github.com")
    api_request_context = context.request
    page = context.new_page()

    # Alternatively you can create a APIRequestContext manually without having a browser context attached:
    # api_request_context = p.request.new_context(base_url="https://api.github.com")


    # Create a repository.
    response = api_request_context.post(
        "/user/repos",
        headers={
            "Accept": "application/vnd.github.v3+json",
            # Add GitHub personal access token.
            "Authorization": f"token {API_TOKEN}",
        },
        data={"name": REPO},
    )
    assert response.ok
    assert response.json()["name"] == REPO

    # Delete a repository.
    response = api_request_context.delete(
        f"/repos/{USER}/{REPO}",
        headers={
            "Accept": "application/vnd.github.v3+json",
            # Add GitHub personal access token.
            "Authorization": f"token {API_TOKEN}",
        },
    )
    assert response.ok
    assert await response.body() == '{"status": "ok"}'
```

- Async

```python
import os
import asyncio
from playwright.async_api import async_playwright, Playwright

REPO = "test-repo-1"
USER = "github-username"
API_TOKEN = os.getenv("GITHUB_API_TOKEN")

async def run(playwright: Playwright):
    # This will launch a new browser, create a context and page. When making HTTP
    # requests with the internal APIRequestContext (e.g. `context.request` or `page.request`)
    # it will automatically set the cookies to the browser page and vise versa.
    browser = await playwright.chromium.launch()
    context = await browser.new_context(base_url="https://api.github.com")
    api_request_context = context.request
    page = await context.new_page()

    # Alternatively you can create a APIRequestContext manually without having a browser context attached:
    # api_request_context = await playwright.request.new_context(base_url="https://api.github.com")

    # Create a repository.
    response = await api_request_context.post(
        "/user/repos",
        headers={
            "Accept": "application/vnd.github.v3+json",
            # Add GitHub personal access token.
            "Authorization": f"token {API_TOKEN}",
        },
        data={"name": REPO},
    )
    assert response.ok
    assert response.json()["name"] == REPO

    # Delete a repository.
    response = await api_request_context.delete(
        f"/repos/{USER}/{REPO}",
        headers={
            "Accept": "application/vnd.github.v3+json",
            # Add GitHub personal access token.
            "Authorization": f"token {API_TOKEN}",
        },
    )
    assert response.ok
    assert await response.body() == '{"status": "ok"}'

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
```

## api_request_context.delete(url, **kwargs)<a name="api-request-context-delete">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 目标URL.<a name="api-request-context-delete-option-url">#</a>
- `data` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)|[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)> 允许设置请求的post数据。如果data参数是一个对象，它将被序列化为json字符串，如果没有显式设置，`content-type`头将被设置为`application/json` . 否则，如果没有显式设置`content-type`头将被设置为 `application/octet-stream` .<a name="api-request-context-delete-option-data">#</a>
- `fail_on_status_code` \<[bool](https://docs.python.org/3/library/stdtypes.html)> •      是否对2xx和3xx以外的响应码抛出异常。默认情况下，返回所有状态码的响应对象.<a name="api-request-context-delete-option-fail-on-status-code">#</a>
- `form` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]> 提供一个对象，该对象将使用 `application/x-www-form-urlencoded` 编码序列化为html form, 并作为请求体发送。如果指定了这个参数，除非明确提供，否则 `content-type` 将被设置为 `application/x-www-form-urlencoded`.<a name="api-request-context-delete-option-form">#</a>
- `headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 允许设置HTTP头.<a name="api-request-context-delete-option-headers">#</a>
- `ignore_https_errors` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 发送网络请求时是否忽略HTTPS错误。默认值为 `false`.<a name="api-request-context-delete-option-ignore-https-errors">#</a>
- `multipart` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)|[ReadStream]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]> 提供一个对象，该对象将使用 `multipart/form-data` 编码序列化为html形式，并作为请求体发送。如果指定了该参数，除非明确提供，否则`content-type` 将被设置为 `multipart/form-data`. 文件值可以作为fs来传递, [`fs.ReadStream`](https://nodejs.org/api/fs.html#fs_class_fs_readstream) 或作为文件类对象，包含文件名、mime类型及其内容.<a name="api-request-context-delete-option-multipart">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件名
    - `mimeType` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件类型
    - `buffer` \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> 文件内容
- `params` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]> 查询参数.<a name="api-request-context-delete-option-params">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 请求超时时间，单位为毫秒。默认为 `30000` (30 seconds). 传递 `0` 以禁用超时.<a name="api-request-context-delete-option-timeout">#</a>
- returns: \<[APIResponse](#apiresponse)><a name="api-request-context-delete-return">#</a>

发送HTTP(S) [DELETE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE) 请求并返回响应。该方法将从上下文填充请求cookie，并从响应更新上下文cookie。该方法将自动遵循**重定向**。

## api_request_context.dispose()<a name="api-request-context-dispose">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="api-request-context-dispose-return">#</a>

 [api_request_context.get(url, **kwargs)](#api-request-context-get) 返回的所有响应和类似的方法都存储在内存中，这样你以后就可以调用 [api_response.body()](#api-response-body). 此方法丢弃所有存储的响应，并使 [api_response.body()](#api-response-body) 抛出“Response dispose”错误.

## api_request_context.fetch(url_or_request, **kwargs)<a name="api-request-context-fetch">#</a>

- `url_or_request` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Request](#request)> 获取所有参数的目标URL或请求.<a name="api-request-context-fetch-option-url-or-request">#</a>
- `data` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)|[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)> 允许设置请求的post数据。如果data参数是一个对象，它将被序列化为json字符串，如果没有显式设置，`content-type` 将被设置为 `application/json` ,否则，如果没有显式设置， `content-type` 将被设置为 `application/octet-stream` .<a name="api-request-context-fetch-option-data">#</a>
- `fail_on_status_code` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否对2xx和3xx以外的响应码排除。默认情况下，返回所有状态码的响应对象.<a name="api-request-context-fetch-option-fail-on-status-code">#</a>
- `form` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]> 提供一个对象，该对象将使用 `application/x-www-form-urlencoded` 编码序列化为html form，并作为请求体发送。如果指定了这个参数，除非明确提供，否则 `content-type` 将被设置为 `application/x-www-form-urlencoded`.<a name="api-request-context-fetch-option-form">#</a>
- `headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 允许设置HTTP头.<a name="api-request-context-fetch-option-headers">#</a>
- `ignore_https_errors` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 发送网络请求时是否忽略HTTPS错误。默认值为 `false`.<a name="api-request-context-fetch-option-ignore-https-errors">#</a>
- `method` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 改变了获取方法 (e.g. [PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) or [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)). 如果未指定，则使用GET方法.<a name="api-request-context-fetch-option-method">#</a>
- `multipart` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)|[ReadStream]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]> 提供一个对象，该对象将使用 `multipart/form-data` 编码序列化为html形式，并作为请求体发送。如果指定了该参数，除非明确提供，否则`content-type` 将被设置为 `multipart/form-data`. 文件值可以作为fs来传递, [`fs.ReadStream`](https://nodejs.org/api/fs.html#fs_class_fs_readstream) 或作为文件类对象，包含文件名、mime类型及其内容.<a name="api-request-context-fetch-option-multipart">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件名
    - `mimeType` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件类型
    - `buffer` \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> 文件内容
- `params` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]> 查询参数.<a name="api-request-context-fetch-option-params">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 请求超时时间，单位为毫秒。默认为 `30000` (30 seconds). 传递 `0` 以禁用超时.<a name="api-request-context-fetch-option-timeout">#</a>
- returns: \<[APIResponse](#apiresponse)><a name="api-request-context-fetch-return">#</a>

发送HTTP(S)请求并返回响应。该方法将从上下文填充请求cookie，并从响应更新上下文cookie。该方法将自动遵循重定向。

## api_request_context.get(url, **kwargs)<a name="api-request-context-get">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 目标 URL.<a name="api-request-context-get-option-url">#</a>
- `fail_on_status_code` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否对2xx和3xx以外的响应码排除。默认情况下，返回所有状态码的响应对象.<a name="api-request-context-get-option-fail-on-status-code">#</a>
- `headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 允许设置HTTP头.<a name="api-request-context-get-option-headers">#</a>
- `ignore_https_errors` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 发送网络请求时是否忽略HTTPS错误。默认值为 `false`.<a name="api-request-context-get-option-ignore-https-errors">#</a>
- `params` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]> 查询参数.<a name="api-request-context-get-option-params">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 请求超时时间，单位为毫秒。默认为 `30000` (30 seconds). 传递 `0` 以禁用超时.<a name="api-request-context-get-option-timeout">#</a>
- returns: \<[APIResponse](#apiresponse)><a name="api-request-context-get-return">#</a>

发送HTTP(S) GET请求并返回响应。该方法将从上下文填充请求cookie，并从响应更新上下文cookie。该方法将自动遵循重定向。

## api_request_context.head(url, **kwargs)<a name="api-request-context-head">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 目标  URL.<a name="api-request-context-head-option-url">#</a>
- `fail_on_status_code` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否对2xx和3xx以外的响应码排除。默认情况下，返回所有状态码的响应对象.<a name="api-request-context-head-option-fail-on-status-code">#</a>
- `headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 允许设置HTTP头.<a name="api-request-context-head-option-headers">#</a>
- `ignore_https_errors` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 发送网络请求时是否忽略HTTPS错误。默认值为 `false`.<a name="api-request-context-head-option-ignore-https-errors">#</a>
- `params` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]>查询参数.<a name="api-request-context-head-option-params">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 请求超时时间，单位为毫秒。默认为 `30000` (30 seconds). 传递 `0` 以禁用超时.<a name="api-request-context-head-option-timeout">#</a>
- returns: \<[APIResponse](#apiresponse)><a name="api-request-context-head-return">#</a>

发送HTTP(S) [HEAD](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD) 请求并返回其响应。该方法将从上下文填充请求cookie，并从响应更新上下文cookie。该方法将自动遵循重定向。

## api_request_context.patch(url, **kwargs)<a name="api-request-context-patch">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 目标 URL.<a name="api-request-context-patch-option-url">#</a>
- `data` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)|[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)> 允许设置请求的post数据。如果data参数是一个对象，它将被序列化为json字符串，如果没有显式设置，`content-type` 将被设置为 `application/json` ,否则，如果没有显式设置， `content-type` 将被设置为 `application/octet-stream` .<a name="api-request-context-patch-option-data">#</a>
- `fail_on_status_code` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否对2xx和3xx以外的响应码排除。默认情况下，返回所有状态码的响应对象.<a name="api-request-context-patch-option-fail-on-status-code">#</a>
- `form` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]> 提供一个对象，该对象将使用 `application/x-www-form-urlencoded` 编码序列化为html form，并作为请求体发送。如果指定了这个参数，除非明确提供，否则 `content-type` 将被设置为 `application/x-www-form-urlencoded`.<a name="api-request-context-patch-option-form">#</a>
- `headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 允许设置HTTP头.<a name="api-request-context-patch-option-headers">#</a>
- `ignore_https_errors` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 发送网络请求时是否忽略HTTPS错误。默认值为 `false`.<a name="api-request-context-patch-option-ignore-https-errors">#</a>
- `multipart` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)|[ReadStream]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]> 提供一个对象，该对象将使用 `multipart/form-data` 编码序列化为html形式，并作为请求体发送。如果指定了该参数，除非明确提供，否则`content-type` 将被设置为 `multipart/form-data`. 文件值可以作为fs来传递, [`fs.ReadStream`](https://nodejs.org/api/fs.html#fs_class_fs_readstream) 或作为文件类对象，包含文件名、mime类型及其内容.<a name="api-request-context-patch-option-multipart">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件名
    - `mimeType` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件类型
    - `buffer` \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> 文件内容
- `params` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]> 查询参数.<a name="api-request-context-patch-option-params">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 请求超时时间，单位为毫秒。默认为 `30000` (30 seconds). 传递 `0` 以禁用超时.<a name="api-request-context-patch-option-timeout">#</a>
- returns: \<[APIResponse](#apiresponse)><a name="api-request-context-patch-return">#</a>

发送HTTP(S) [PATCH](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH) 请求并返回响应。该方法将从上下文填充请求cookie，并从响应更新上下文cookie。该方法将自动遵循重定向。

## api_request_context.post(url, **kwargs)<a name="api-request-context-post">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>目标 URL.<a name="api-request-context-post-option-url">#</a>
- `data` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)|[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)> 允许设置请求的post数据。如果data参数是一个对象，它将被序列化为json字符串，如果没有显式设置，`content-type` 将被设置为 `application/json` ,否则，如果没有显式设置， `content-type` 将被设置为 `application/octet-stream` .<a name="api-request-context-post-option-data">#</a>
- `fail_on_status_code` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否对2xx和3xx以外的响应码排除。默认情况下，返回所有状态码的响应对象.<a name="api-request-context-post-option-fail-on-status-code">#</a>
- `form` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]> 提供一个对象，该对象将使用 `application/x-www-form-urlencoded` 编码序列化为html form，并作为请求体发送。如果指定了这个参数，除非明确提供，否则 `content-type` 将被设置为 `application/x-www-form-urlencoded`.<a name="api-request-context-post-option-form">#</a>
- `headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]>  允许设置HTTP头.<a name="api-request-context-post-option-headers">#</a>
- `ignore_https_errors` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 发送网络请求时是否忽略HTTPS错误。默认值为 `false`.<a name="api-request-context-post-option-ignore-https-errors">#</a>
- `multipart` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)|[ReadStream]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]> 提供一个对象，该对象将使用 `multipart/form-data` 编码序列化为html形式，并作为请求体发送。如果指定了该参数，除非明确提供，否则`content-type` 将被设置为 `multipart/form-data`. 文件值可以作为fs来传递, [`fs.ReadStream`](https://nodejs.org/api/fs.html#fs_class_fs_readstream) 或作为文件类对象，包含文件名、mime类型及其内容.<a name="api-request-context-post-option-multipart">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件名
    - `mimeType` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件类型
    - `buffer` \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> 文件内容
- `params` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]> 查询参数.<a name="api-request-context-post-option-params">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 请求超时时间，单位为毫秒。默认为 `30000` (30 seconds). 传递 `0` 以禁用超时.<a name="api-request-context-post-option-timeout">#</a>
- returns: \<[APIResponse](#apiresponse)><a name="api-request-context-post-return">#</a>

发送HTTP(S) [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) 请求并返回响应。该方法将从上下文填充请求cookie，并从响应更新上下文cookie。该方法将自动遵循重定向。

## api_request_context.put(url, **kwargs)<a name="api-request-context-put">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 目标 URL.<a name="api-request-context-put-option-url">#</a>
- `data` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)|[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)> 允许设置请求的post数据。如果data参数是一个对象，它将被序列化为json字符串，如果没有显式设置，`content-type` 将被设置为 `application/json` ,否则，如果没有显式设置， `content-type` 将被设置为 `application/octet-stream` .<a name="api-request-context-put-option-data">#</a>
- `fail_on_status_code` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否对2xx和3xx以外的响应码排除。默认情况下，返回所有状态码的响应对象.<a name="api-request-context-put-option-fail-on-status-code">#</a>
- `form` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]>提供一个对象，该对象将使用 `application/x-www-form-urlencoded` 编码序列化为html form，并作为请求体发送。如果指定了这个参数，除非明确提供，否则 `content-type` 将被设置为 `application/x-www-form-urlencoded`.<a name="api-request-context-put-option-form">#</a>
- `headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 允许设置HTTP头.<a name="api-request-context-put-option-headers">#</a>
- `ignore_https_errors` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 发送网络请求时是否忽略HTTPS错误。默认值为 `false`.<a name="api-request-context-put-option-ignore-https-errors">#</a>
- `multipart` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)|[ReadStream]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]> 提供一个对象，该对象将使用 `multipart/form-data` 编码序列化为html形式，并作为请求体发送。如果指定了该参数，除非明确提供，否则`content-type` 将被设置为 `multipart/form-data`. 文件值可以作为fs来传递, [`fs.ReadStream`](https://nodejs.org/api/fs.html#fs_class_fs_readstream) 或作为文件类对象，包含文件名、mime类型及其内容.<a name="api-request-context-put-option-multipart">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件名
    - `mimeType` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件类型
    - `buffer` \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> 文件内容
- `params` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]> 查询参数 <a name="api-request-context-put-option-params">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 请求超时时间，单位为毫秒。默认为 `30000` (30 seconds). 传递 `0` 以禁用超时.<a name="api-request-context-put-option-timeout">#</a>
- returns: \<[APIResponse](#apiresponse)><a name="api-request-context-put-return">#</a>

## api_request_context.storage_state(**kwargs)<a name="api-request-context-storage-state">#</a>

- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 存储状态保存到的文件路径. 如果 `path` 是一个相对路径，那么它是相对于当前工作目录解析的。如果没有提供路径，存储状态仍然返回，但不会保存到磁盘.<a name="api-request-context-storage-state-option-path">#</a>
- returns: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="api-request-context-storage-state-return">#</a>
    - `cookies` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]>
        - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `domain` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `path` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `expires` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> Unix 时间，单位为秒.
        - `httpOnly` \<[bool](https://docs.python.org/3/library/stdtypes.html)>
        - `secure` \<[bool](https://docs.python.org/3/library/stdtypes.html)>
        - `sameSite` \<"Strict"|"Lax"|"None">
    - `origins` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]>
        - `origin` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `localStorage` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]>
            - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
            - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>

返回此请求上下文的存储状态，如果它被传递给构造函数，则包含当前cookie和本地存储快照。



# APIResponse

[APIResponse](#apiresponse) 类表示 [api_request_context.get(url, **kwargs)](#api-request-context-get) 等类似的方法返回的响应

- Sync

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    context = playwright.request.new_context()
    response = context.get("https://example.com/user/repos")
    assert response.ok
    assert response.status == 200
    assert response.headers["content-type"] == "application/json; charset=utf-8"
    assert response.json()["name"] == "foobar"
    assert response.body() == '{"status": "ok"}'
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    context = await playwright.request.new_context()
    response = await context.get("https://example.com/user/repos")
    assert response.ok
    assert response.status == 200
    assert response.headers["content-type"] == "application/json; charset=utf-8"
    assert response.json()["name"] == "foobar"
    assert await response.body() == '{"status": "ok"}'


async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
```

## api_response.body()<a name="api-response-body">#</a>

- returns: \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)><a name="api-response-body-return">#</a>

返回带有响应体的缓冲区.

## api_response.dispose()<a name="api-response-dispose">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="api-response-dispose-return">#</a>

处理此响应的正文。如果没有调用，则主体将留在内存中，直到上下文关闭。

## api_response.headers<a name="api-response-headers">#</a>

- returns: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]><a name="api-response-headers-return">#</a>

具有与此响应关联的所有响应HTTP头的对象。

## api_response.headers_array<a name="api-response-headers-array">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]><a name="api-response-headers-array-return">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 头属性名称.
    - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 头属性值.

包含与此响应关联的所有请求HTTP头的数组。头属性名称不是小写的。具有多个条目的头属性，例如 `Set-Cookie`, 在数组中出现多次.

## api_response.json()<a name="api-response-json">#</a>

- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="api-response-json-return">#</a>

返回响应体的JSON表示。

如果响应体不能通过 `JSON.parse`进行解析，则该方法将排除.

## api_response.ok<a name="api-response-ok">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="api-response-ok-return">#</a>

包含一个布尔值，说明响应是否成功(状态在200-299之间)。

## api_response.status<a name="api-response-status">#</a>

- returns: \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)><a name="api-response-status-return">#</a>

包含响应的状态码(例如，200表示成功)。

## api_response.status_text<a name="api-response-status-text">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="api-response-status-text-return">#</a>

包含响应的状态文本(例如，通常一个“OK”表示成功)。

## api_response.text()<a name="api-response-text">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="api-response-text-return">#</a>

返回响应体的文本表示形式。

## api_response.url<a name="api-response-url">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="api-response-url-return">#</a>

包含响应的URL。



# Assertions

Playwright 为您提供了web优先的断言，提供了创建断言的方便方法，这些断言将等待并重试，直到满足预期的条件。

- Sync

```python
from playwright.sync_api import Page, expect

def test_status_becomes_submitted(page: Page) -> None:
    # ..
    page.click("#submit-button")
    expect(page.locator(".status")).to_have_text("Submitted")
```

- Async

```python
from playwright.async_api import Page, expect

async def test_status_becomes_submitted(page: Page) -> None:
    # ..
    await page.click("#submit-button")
    await expect(page.locator(".status")).to_have_text("Submitted")
```



Playwright 会用选择器 `.status` 重新测试节点，直到取回的节点有 `"Submitted"` 文本。它将重新获取节点并一遍又一遍地检查它，直到满足条件或到达超时。您可以将此超时作为一个选项传递。

默认情况下，断言的超时被设置为5秒。

## expect(locator).not_to_be_checked(**kwargs)<a name="locator-assertions-not-to-be-checked">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-be-checked-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-be-checked-return">#</a>

与 [expect(locator).to_be_checked(**kwargs)](#locator-assertions-to-be-checked) 相反.

## expect(locator).not_to_be_disabled(**kwargs)<a name="locator-assertions-not-to-be-disabled">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-be-disabled-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-be-disabled-return">#</a>

与 [expect(locator).to_be_disabled(**kwargs)](#locator-assertions-to-be-disabled) 相反.

## expect(locator).not_to_be_editable(**kwargs)<a name="locator-assertions-not-to-be-editable">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-be-editable-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-be-editable-return">#</a>

与 [expect(locator).to_be_editable(**kwargs)](#locator-assertions-to-be-editable) 相反.

## expect(locator).not_to_be_empty(**kwargs)<a name="locator-assertions-not-to-be-empty">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-be-empty-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-be-empty-return">#</a>

与 [expect(locator).to_be_empty(**kwargs)](#locator-assertions-to-be-empty) 相反.

## expect(locator).not_to_be_enabled(**kwargs)<a name="locator-assertions-not-to-be-enabled">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-be-enabled-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-be-enabled-return">#</a>

与 [expect(locator).to_be_enabled(**kwargs)](#locator-assertions-to-be-enabled) 相反.

## expect(locator).not_to_be_focused(**kwargs)<a name="locator-assertions-not-to-be-focused">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-be-focused-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-be-focused-return">#</a>

与 [expect(locator).to_be_focused(**kwargs)](#locator-assertions-to-be-focused) 相反.

## expect(locator).not_to_be_hidden(**kwargs)<a name="locator-assertions-not-to-be-hidden">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-be-hidden-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-be-hidden-return">#</a>

与 [expect(locator).to_be_hidden(**kwargs)](#locator-assertions-to-be-hidden) 相反.

## expect(locator).not_to_be_visible(**kwargs)<a name="locator-assertions-not-to-be-visible">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-be-visible-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-be-visible-return">#</a>

与 [expect(locator).to_be_visible(**kwargs)](#locator-assertions-to-be-visible) 相反.

## expect(locator).not_to_contain_text(expected, **kwargs)<a name="locator-assertions-not-to-contain-text">#</a>

- `expected` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)]> 期望的子字符串或RegExp或它们的列表.<a name="locator-assertions-not-to-contain-text-option-expected">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-contain-text-option-timeout">#</a>
- `use_inner_text` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 检索DOM节点文本时使用 `element.innerText` 而不是 `element.textContent` .<a name="locator-assertions-not-to-contain-text-option-use-inner-text">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-contain-text-return">#</a>

与之相反 [expect(locator).to_contain_text(expected, **kwargs)](#locator-assertions-to-contain-text).

## expect(locator).not_to_have_attribute(name, value, **kwargs)<a name="locator-assertions-not-to-have-attribute">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 属性名.<a name="locator-assertions-not-to-have-attribute-option-name">#</a>
- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> 期望的属性值.<a name="locator-assertions-not-to-have-attribute-option-value">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-have-attribute-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-have-attribute-return">#</a>

与之相反 [expect(locator).to_have_attribute(name, value, **kwargs)](#locator-assertions-to-have-attribute).

## expect(locator).not_to_have_class(expected, **kwargs)<a name="locator-assertions-not-to-have-class">#</a>

- `expected` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)]> 期望的类或RegExp或它们的列表.<a name="locator-assertions-not-to-have-class-option-expected">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-have-class-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-have-class-return">#</a>

与之相反 [expect(locator).to_have_class(expected, **kwargs)](#locator-assertions-to-have-class).

## expect(locator).not_to_have_count(count, **kwargs)<a name="locator-assertions-not-to-have-count">#</a>

- `count` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 期望的计数.<a name="locator-assertions-not-to-have-count-option-count">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-have-count-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-have-count-return">#</a>

与之相反 [expect(locator).to_have_count(count, **kwargs)](#locator-assertions-to-have-count).

## expect(locator).not_to_have_css(name, value, **kwargs)<a name="locator-assertions-not-to-have-css">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> CSS 属性名.<a name="locator-assertions-not-to-have-css-option-name">#</a>
- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> CSS 属性值.<a name="locator-assertions-not-to-have-css-option-value">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-have-css-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-have-css-return">#</a>

与之相反 [expect(locator).to_have_css(name, value, **kwargs)](#locator-assertions-to-have-css).

## expect(locator).not_to_have_id(id, **kwargs)<a name="locator-assertions-not-to-have-id">#</a>

- `id` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)>元素 id.<a name="locator-assertions-not-to-have-id-option-id">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-have-id-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-have-id-return">#</a>

与之相反 [expect(locator).to_have_id(id, **kwargs)](#locator-assertions-to-have-id).

## expect(locator).not_to_have_js_property(name, value, **kwargs)<a name="locator-assertions-not-to-have-js-property">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 属性名.<a name="locator-assertions-not-to-have-js-property-option-name">#</a>
- `value` \<[Any](https://docs.python.org/3/library/typing.html#typing.Any)> 属性值.<a name="locator-assertions-not-to-have-js-property-option-value">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-have-js-property-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-have-js-property-return">#</a>

与之相反 [expect(locator).to_have_js_property(name, value, **kwargs)](#locator-assertions-to-have-js-property).

## expect(locator).not_to_have_text(expected, **kwargs)<a name="locator-assertions-not-to-have-text">#</a>

- `expected` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)]> 期望的子字符串或RegExp或它们的列表.<a name="locator-assertions-not-to-have-text-option-expected">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-have-text-option-timeout">#</a>
- `use_inner_text` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 检索DOM节点文本时使用 `element.innerText` 而不是 `element.textContent`.<a name="locator-assertions-not-to-have-text-option-use-inner-text">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-have-text-return">#</a>

与之相反 [expect(locator).to_have_text(expected, **kwargs)](#locator-assertions-to-have-text).

## expect(locator).not_to_have_value(value, **kwargs)<a name="locator-assertions-not-to-have-value">#</a>

- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> 期望值.<a name="locator-assertions-not-to-have-value-option-value">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-not-to-have-value-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-not-to-have-value-return">#</a>

与之相反 [expect(locator).to_have_value(value, **kwargs)](#locator-assertions-to-have-value).

## expect(locator).to_be_checked(**kwargs)<a name="locator-assertions-to-be-checked">#</a>

- `checked` \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="locator-assertions-to-be-checked-option-checked">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-be-checked-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-be-checked-return">#</a>

确保 [Locator](#locator) 指向选中的输入。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator(".subscribe")
expect(locator).to_be_checked()
```

- Async

```python
from playwright.async_api import expect

locator = page.locator(".subscribe")
await expect(locator).to_be_checked()
```



## expect(locator).to_be_disabled(**kwargs)<a name="locator-assertions-to-be-disabled">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-be-disabled-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-be-disabled-return">#</a>

确保 [Locator](#locator) 指向一个禁用的元素。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator("button.submit")
expect(locator).to_be_disabled()
```

- Async

```python
from playwright.async_api import expect

locator = page.locator("button.submit")
await expect(locator).to_be_disabled()
```



## expect(locator).to_be_editable(**kwargs)<a name="locator-assertions-to-be-editable">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-be-editable-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-be-editable-return">#</a>

确保 [Locator](#locator) 指向一个可编辑的元素。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator(".input")
expect(locator).to_be_editable()
```

- Async

```python
from playwright.async_api import expect

locator = page.locator(".input")
await expect(locator).to_be_editable()
```



## expect(locator).to_be_empty(**kwargs)<a name="locator-assertions-to-be-empty">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-be-empty-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-be-empty-return">#</a>

确保 [Locator](#locator) 指向空的可编辑元素或没有文本的DOM节点。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator("div.warning")
expect(locator).to_be_empty()
```

- Async

```python
from playwright.async_api import expect

locator = page.locator("div.warning")
await expect(locator).to_be_empty()
```



## expect(locator).to_be_enabled(**kwargs)<a name="locator-assertions-to-be-enabled">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-be-enabled-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-be-enabled-return">#</a>

确保 [Locator](#locator) 指向一个启用的元素。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator("button.submit")
expect(locator).to_be_enabled()
```

- Async

```python
from playwright.async_api import expect

locator = page.locator("button.submit")
await expect(locator).to_be_enabled()
```



## expect(locator).to_be_focused(**kwargs)<a name="locator-assertions-to-be-focused">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-be-focused-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-be-focused-return">#</a>

确保 [Locator](#locator) 指向一个集中的DOM节点。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator('input')
expect(locator).to_be_focused()
```

- Async

```python
from playwright.async_api import expect

locator = page.locator('input')
await expect(locator).to_be_focused()
```



## expect(locator).to_be_hidden(**kwargs)<a name="locator-assertions-to-be-hidden">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-be-hidden-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-be-hidden-return">#</a>

确保 [Locator](#locator) 指向一个隐藏的DOM节点，这与 [visible](https://playwright.dev/python/docs/actionability#visible)相反。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator('.my-element')
expect(locator).to_be_hidden()
```

- Async

```python
from playwright.async_api import expect

locator = page.locator('.my-element')
await expect(locator).to_be_hidden()
```



## expect(locator).to_be_visible(**kwargs)<a name="locator-assertions-to-be-visible">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-be-visible-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-be-visible-return">#</a>

确保 [Locator](#locator) 指向一个[可见 visible](https://playwright.dev/python/docs/actionability#visible) 的DOM节点。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator('.my-element')
expect(locator).to_be_visible()
```

- Async

```python
from playwright.async_api import expect

locator = page.locator('.my-element')
await expect(locator).to_be_visible()
```



## expect(locator).to_contain_text(expected, **kwargs)<a name="locator-assertions-to-contain-text">#</a>

- `expected` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)]> 期望的子字符串或RegExp或它们的列表.<a name="locator-assertions-to-contain-text-option-expected">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-contain-text-option-timeout">#</a>
- `use_inner_text` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当检索DOM节点文本时使用 `element.innerText` 而不是 `element.textContent` .<a name="locator-assertions-to-contain-text-option-use-inner-text">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-contain-text-return">#</a>

确保 [Locator](#locator) 指向包含给定文本的元素。您也可以为该值使用正则表达式。

- Sync

```python
import re
from playwright.sync_api import expect

locator = page.locator('.title')
expect(locator).to_contain_text("substring")
expect(locator).to_contain_text(re.compile(r"\d messages"))
```

- Async

```python
import re
from playwright.async_api import expect

locator = page.locator('.title')
await expect(locator).to_contain_text("substring")
await expect(locator).to_contain_text(re.compile(r"\d messages"))
```



注意，如果array是作为预期值传递的，那么整个元素列表都可以被断言:

- Sync

```python
import re
from playwright.sync_api import expect

locator = page.locator("list > .list-item")
expect(locator).to_contain_text(["Text 1", "Text 4", "Text 5"])
```

- Async

```python
import re
from playwright.async_api import expect

locator = page.locator("list > .list-item")
await expect(locator).to_contain_text(["Text 1", "Text 4", "Text 5"])
```



## expect(locator).to_have_attribute(name, value, **kwargs)<a name="locator-assertions-to-have-attribute">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>属性名.<a name="locator-assertions-to-have-attribute-option-name">#</a>
- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> 期望的属性值.<a name="locator-assertions-to-have-attribute-option-value">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-have-attribute-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-have-attribute-return">#</a>

确保 [Locator](#locator) 指向具有给定属性的元素。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator("input")
expect(locator).to_have_attribute("type", "text")
```

- Async

```python
from playwright.async_api import expect

locator = page.locator("input")
await expect(locator).to_have_attribute("type", "text")
```



## expect(locator).to_have_class(expected, **kwargs)<a name="locator-assertions-to-have-class">#</a>

- `expected` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)]> •      期望的类或RegExp或它们的列表.<a name="locator-assertions-to-have-class-option-expected">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-have-class-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-have-class-return">#</a>

确保 [Locator](#locator) 指向具有给定CSS类的元素。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator("#component")
expect(locator).to_have_class(re.compile(r"selected"))
```

- Async

```python
from playwright.async_api import expect

locator = page.locator("#component")
await expect(locator).to_have_class(re.compile(r"selected"))
```



注意，如果array是作为预期值传递的，那么整个元素列表都可以被断言:

- Sync

```python
from playwright.sync_api import expect

locator = page.locator("list > .component")
expect(locator).to_have_class(["component", "component selected", "component"])
```

- Async

```python
from playwright.async_api import expect

locator = page.locator("list > .component")
await expect(locator).to_have_class(["component", "component selected", "component"])
```



## expect(locator).to_have_count(count, **kwargs)<a name="locator-assertions-to-have-count">#</a>

- `count` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 期望的计数.<a name="locator-assertions-to-have-count-option-count">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-have-count-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-have-count-return">#</a>

确保 [Locator](#locator) 解析为精确数量的DOM节点。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator("list > .component")
expect(locator).to_have_count(3)
```

- Async

```python
from playwright.async_api import expect

locator = page.locator("list > .component")
await expect(locator).to_have_count(3)
```



## expect(locator).to_have_css(name, value, **kwargs)<a name="locator-assertions-to-have-css">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> CSS 属性名.<a name="locator-assertions-to-have-css-option-name">#</a>
- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> CSS属性值.<a name="locator-assertions-to-have-css-option-value">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-have-css-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-have-css-return">#</a>

确保 [Locator](#locator) 解析为具有给定计算的CSS样式的元素。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator("button")
expect(locator).to_have_css("display", "flex")
```

- Async

```python
from playwright.async_api import expect

locator = page.locator("button")
await expect(locator).to_have_css("display", "flex")
```



## expect(locator).to_have_id(id, **kwargs)<a name="locator-assertions-to-have-id">#</a>

- `id` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> 元素 id.<a name="locator-assertions-to-have-id-option-id">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-have-id-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-have-id-return">#</a>

确保 [Locator](#locator) 指向具有给定DOM节点ID的元素。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator("input")
expect(locator).to_have_id("lastname")
```

- Async

```python
from playwright.async_api import expect

locator = page.locator("input")
await expect(locator).to_have_id("lastname")
```



## expect(locator).to_have_js_property(name, value, **kwargs)<a name="locator-assertions-to-have-js-property">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 属性名 <a name="locator-assertions-to-have-js-property-option-name">#</a>
- `value` \<[Any](https://docs.python.org/3/library/typing.html#typing.Any)>属性值.<a name="locator-assertions-to-have-js-property-option-value">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-have-js-property-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-have-js-property-return">#</a>

确保 [Locator](#locator) 指向具有给定JavaScript属性的元素。请注意，该属性可以是基本类型，也可以是可序列化的普通JavaScript对象。

- Sync

```python
from playwright.sync_api import expect

locator = page.locator(".component")
expect(locator).to_have_js_property("loaded", True)
```

- Async

```python
from playwright.async_api import expect

locator = page.locator(".component")
await expect(locator).to_have_js_property("loaded", True)
```



## expect(locator).to_have_text(expected, **kwargs)<a name="locator-assertions-to-have-text">#</a>

- `expected` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)]> 期望的子字符串或RegExp或它们的列表.<a name="locator-assertions-to-have-text-option-expected">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-have-text-option-timeout">#</a>
- `use_inner_text` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当检索DOM节点文本时使用 `element.innerText` 而不是 `element.textContent` .<a name="locator-assertions-to-have-text-option-use-inner-text">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-have-text-return">#</a>

确保 [Locator](#locator) 指向具有给定文本的元素。您也可以为该值使用正则表达式。

- Sync

```python
import re
from playwright.sync_api import expect

locator = page.locator(".title")
expect(locator).to_have_text(re.compile(r"Welcome, Test User"))
expect(locator).to_have_text(re.compile(r"Welcome, .*"))
```

- Async

```python
import re
from playwright.async_api import expect

locator = page.locator(".title")
await expect(locator).to_have_text(re.compile(r"Welcome, Test User"))
await expect(locator).to_have_text(re.compile(r"Welcome, .*"))
```



注意，如果array是作为预期值传递的，那么整个元素列表都可以被断言:

- Sync

```python
from playwright.sync_api import expect

locator = page.locator("list > .component")
expect(locator).to_have_text(["Text 1", "Text 2", "Text 3"])
```

- Async

```python
from playwright.async_api import expect

locator = page.locator("list > .component")
await expect(locator).to_have_text(["Text 1", "Text 2", "Text 3"])
```



## expect(locator).to_have_value(value, **kwargs)<a name="locator-assertions-to-have-value">#</a>

- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> 期望值 <a name="locator-assertions-to-have-value-option-value">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="locator-assertions-to-have-value-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-assertions-to-have-value-return">#</a>

确保 [Locator](#locator) 指向具有给定输入值的元素。您也可以为该值使用正则表达式。

- Sync

```python
import re
from playwright.sync_api import expect

locator = page.locator("input[type=number]")
expect(locator).to_have_value(re.compile(r"[0-9]"))
```

- Async

```python
import re
from playwright.async_api import expect

locator = page.locator("input[type=number]")
await expect(locator).to_have_value(re.compile(r"[0-9]"))
```



## expect(page).not_to_have_title(title_or_reg_exp, **kwargs)<a name="page-assertions-not-to-have-title">#</a>

- `title_or_reg_exp` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> 期望的标题或RegExp.<a name="page-assertions-not-to-have-title-option-title-or-reg-exp">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="page-assertions-not-to-have-title-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-assertions-not-to-have-title-return">#</a>

与之相反 [expect(page).to_have_title(title_or_reg_exp, **kwargs)](#page-assertions-to-have-title).

## expect(page).not_to_have_url(url_or_reg_exp, **kwargs)<a name="page-assertions-not-to-have-url">#</a>

- `url_or_reg_exp` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> 期望的子字符串或RegExp.<a name="page-assertions-not-to-have-url-option-url-or-reg-exp">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="page-assertions-not-to-have-url-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-assertions-not-to-have-url-return">#</a>

与之相反 [expect(page).to_have_url(url_or_reg_exp, **kwargs)](#page-assertions-to-have-url).

## expect(page).to_have_title(title_or_reg_exp, **kwargs)<a name="page-assertions-to-have-title">#</a>

- `title_or_reg_exp` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)>期望的标题或RegExp.<a name="page-assertions-to-have-title-option-title-or-reg-exp">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="page-assertions-to-have-title-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-assertions-to-have-title-return">#</a>

确保 页面具有给定的标题。

- Sync

```python
import re
from playwright.sync_api import expect

# ...
expect(page).to_have_title(re.compile(r".*checkout"))
```

- Async

```python
import re
from playwright.async_api import expect

# ...
await expect(page).to_have_title(re.compile(r".*checkout"))
```



## expect(page).to_have_url(url_or_reg_exp, **kwargs)<a name="page-assertions-to-have-url">#</a>

- `url_or_reg_exp` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> 期望的子字符串或RegExp.<a name="page-assertions-to-have-url-option-url-or-reg-exp">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 重试断言的时间.<a name="page-assertions-to-have-url-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-assertions-to-have-url-return">#</a>

确保 页面被导航到给定的URL。

- Sync

```python
import re
from playwright.sync_api import expect

# ...
expect(page).to_have_url(re.compile(".*checkout"))
```

- Async

```python
import re
from playwright.async_api import expect

# ...
await expect(page).to_have_url(re.compile(".*checkout"))
```



## expect(api_response).not_to_be_ok()<a name="api-response-assertions-not-to-be-ok">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="api-response-assertions-not-to-be-ok-return">#</a>

与之相反 [expect(api_response).to_be_ok()](#api-response-assertions-to-be-ok).

## expect(api_response).to_be_ok()<a name="api-response-assertions-to-be-ok">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="api-response-assertions-to-be-ok-return">#</a>

确保 确保响应状态码在[200..299]范围。

- Sync

```python
import re
from playwright.sync_api import expect

# ...
expect(response).to_be_ok()
```

- Async

```python
from playwright.async_api import expect

# ...
await expect(response).to_be_ok()
```



# Accessibility

可访问性类提供了检查Chromium的可访问性树的方法。辅助技术(如屏幕阅读器[screen readers](https://en.wikipedia.org/wiki/Screen_reader)或开关[switches](https://en.wikipedia.org/wiki/Switch_access))使用可访问性树。

可访问性是一个非常特定于平台的东西。在不同的平台上，不同的屏幕阅读器可能会产生非常不同的输出。

Chromium、Firefox和WebKit的渲染引擎都有一个“可访问性树”的概念，然后这些概念被翻译成不同的特定于平台的api。可访问性命名空间提供对此可访问性树的访问权。

当从内部浏览器AX树转换为特定于平台的AX- tree时，或者通过辅助技术本身，大多数可访问性树都会被过滤掉。默认情况下，剧作家会尝试近似过滤，只暴露树的“有趣”节点。

- [accessibility.snapshot(**kwargs)](#accessibility-snapshot)

## accessibility.snapshot(**kwargs)<a name="accessibility-snapshot">#</a>

- `interesting_only` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 从树中删除无兴趣节点。默认值为`true`.<a name="accessibility-snapshot-option-interesting-only">#</a>
- `root` \<[ElementHandle](#elementhandle)> 快照的根DOM元素。默认为整个page.<a name="accessibility-snapshot-option-root">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="accessibility-snapshot-return">#</a>
    - `role` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 角色 [role](https://www.w3.org/TR/wai-aria/#usage_intro).
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 节点的人类可读名称.
    - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 节点的当前值.
    - `description` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个额外的人类可读的节点描述，如果适用。
    - `keyshortcuts` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 与此节点相关联的键盘快捷键，如果适用的话。
    - `roledescription` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个人类可读的角色替代者，如果适用的话。
    - `valuetext` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>  当前值的描述，如果适用的话。
    - `disabled` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 如果适用，节点是否被禁用。
    - `expanded` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 如果适用，节点是展开还是折叠。
    - `focused` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 如果适用，节点是否被聚焦。
    - `modal` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 如果适用，节点是否为模态。
    - `multiline` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 如果适用，节点文本输入是否支持多行。
    - `multiselectable` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 如果适用，是否可以选择多个子节点。
    - `readonly` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否为只读。
    - `required` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否需要该节点。
    - `selected` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否在其父节点中选中该节点。
    - `checked` \<[bool](https://docs.python.org/3/library/stdtypes.html)|"mixed"> 复选框是否选中，或是否为"mixed"(如果适用)
    - `pressed` \<[bool](https://docs.python.org/3/library/stdtypes.html)|"mixed"> 是否选中切换按钮，或如果适用，是"mixed"。
    - `level` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 标题的级别，如果适用。
    - `valuemin` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 节点中的最小值(如果适用)。
    - `valuemax` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 节点中的最大值(如果适用)。
    - `autocomplete` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 控件支持哪种类型的自动完成(如果适用)。
    - `haspopup` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 当前节点显示的是哪种类型的弹出窗口，如果适用的话。
    - `invalid` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 如果适用，该节点的值是否无效以及以何种方式无效。
    - `orientation` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>如果适用，节点是水平方向还是垂直方向。
    - `children` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]>子节点，如果有，如果适用。

捕获可访问性树的当前状态。返回的对象表示页面的根可访问节点。



> NOTE
>
> Chromium的可访问性树包含了在大多数平台和大多数屏幕阅读器上未使用的节点。playwright也会为了更容易处理树而丢弃它们，除非 `interesting_only` 被设置为 `false`.
>
> 

转储整个可访问性树的示例:

- Sync

```python
snapshot = page.accessibility.snapshot()
print(snapshot)
```

- Async

```python
snapshot = await page.accessibility.snapshot()
print(snapshot)
```

记录被关注节点名称的示例:

- Sync

```python
def find_focused_node(node):
    if (node.get("focused"))
        return node
    for child in (node.get("children") or []):
        found_node = find_focused_node(child)
        return found_node
    return None

snapshot = page.accessibility.snapshot()
node = find_focused_node(snapshot)
if node:
    print(node["name"])
```

- Async

```python
def find_focused_node(node):
    if (node.get("focused"))
        return node
    for child in (node.get("children") or []):
        found_node = find_focused_node(child)
        return found_node
    return None

snapshot = await page.accessibility.snapshot()
node = find_focused_node(snapshot)
if node:
    print(node["name"])
```



# Browser

- extends: [EventEmitter](https://pyee.readthedocs.io/en/latest/#pyee.BaseEventEmitter)

Browser 是通过 [browser_type.launch(**kwargs)](#browser-type-launch) 创建的。使用[Browser](#browser)创建[Page](#page)的例子:

- Sync

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    firefox = playwright.firefox
    browser = firefox.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    firefox = playwright.firefox
    browser = await firefox.launch()
    page = await browser.new_page()
    await page.goto("https://example.com")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

- [browser.on("disconnected")](#browser-event-disconnected)
- [browser.close()](#browser-close)
- [browser.contexts](#browser-contexts)
- [browser.is_connected()](#browser-is-connected)
- [browser.new_browser_cdp_session()](#browser-new-browser-cdp-session)
- [browser.new_context(**kwargs)](#browser-new-context)
- [browser.new_page(**kwargs)](#browser-new-page)
- [browser.start_tracing(**kwargs)](#browser-start-tracing)
- [browser.stop_tracing()](#browser-stop-tracing)
- [browser.version](#browser-version)

## browser.on("disconnected")<a name="browser-event-disconnected">#</a>

- type: \<[Browser](#browser)>

当Browser与浏览器应用程序断开连接时触发。这可能是因为以下原因之一:

- Browser 程序关闭或崩溃。
- 调用了 [browser.close()](#browser-close) 方法

## browser.close()<a name="browser-close">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-close-return">#</a>

如果使用 [browser_type.launch(**kwargs)](#browser-type-launch)获得此browser，则关闭browser及其所有page(如果有打开的page)。

如果这个浏览器连接到，清除所有创建的属于这个浏览器的上下文，并断开与浏览器服务器的连接。

[Browser](#browser) 对象本身被认为已被销毁，不能再使用。

## browser.contexts<a name="browser-contexts">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[BrowserContext](#browsercontext)]><a name="browser-contexts-return">#</a>

返回所有打开的浏览器上下文的数组。在新创建的浏览器中，这将不返回任何浏览器上下文

- Sync

```python
browser = pw.webkit.launch()
print(len(browser.contexts())) # prints `0`
context = browser.new_context()
print(len(browser.contexts())) # prints `1`
```

- Async

```python
browser = await pw.webkit.launch()
print(len(browser.contexts())) # prints `0`
context = await browser.new_context()
print(len(browser.contexts())) # prints `1`
```

## browser.is_connected()<a name="browser-is-connected">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="browser-is-connected-return">#</a>

表示浏览器已连接。

## browser.new_browser_cdp_session()<a name="browser-new-browser-cdp-session">#</a>

- returns: \<[CDPSession](#cdpsession)><a name="browser-new-browser-cdp-session-return">#</a>

> NOTE
>
> CDP会话仅支持基于chromium的浏览器。
>
> 返回新创建的浏览器会话。

## browser.new_context(**kwargs)<a name="browser-new-context">#</a>

- `accept_downloads` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否自动下载所有附件。在所有下载都被接受的地方默认为 True <a name="browser-new-context-option-accept-downloads">#</a>
- `base_url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 使用以下方法时 [page.goto(url, **kwargs)](#page-goto), [page.route(url, handler, **kwargs)](#page-route), [page.wait_for_url(url, **kwargs)](#page-wait-for-url), [page.expect_request(url_or_predicate, **kwargs)](#page-wait-for-request), or [page.expect_response(url_or_predicate, **kwargs)](#page-wait-for-response)通过使用 [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 构造函数构建相应的URL:
    - baseURL= `http://localhost:3000` 时,导航到 `/bar.html` 结果是 `http://localhost:3000/bar.html`
    - baseURL= `http://localhost:3000/foo/` 时,导航到 `./bar.html` 结果是 `http://localhost:3000/foo/bar.html`
    - baseURL= `http://localhost:3000/foo` 时,导航到(没有下划线) `./bar.html` 结果是 `http://localhost:3000/bar.html`
- `bypass_csp` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 切换绕过页面的 Content-Security-Policy.<a name="browser-new-context-option-bypass-csp">#</a>
- `color_scheme` \<"light"|"dark"|"no-preference"> 模拟`'prefers-colors-scheme'` 的媒体特性，支持的值为 `'light'`, `'dark'`, `'no-preference'`. 详情请参阅 [page.emulate_media(**kwargs)](#page-emulate-media) . 默认值为 `'light'`.<a name="browser-new-context-option-color-scheme">#</a>
- `device_scale_factor` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 指定设备比例因子(可以认为是dpr)。默认为 `1`.<a name="browser-new-context-option-device-scale-factor">#</a>
- `extra_http_headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 一个包含附加HTTP头的对象，每个请求都要发送.<a name="browser-new-context-option-extra-http-headers">#</a>
- `forced_colors` \<"active"|"none"> 模拟 `'forced-colors'` 媒体特性，支持的值为 `'active'`, `'none'`. 详情请参阅[page.emulate_media(**kwargs)](#page-emulate-media) . 默认为 `'none'`.<a name="browser-new-context-option-forced-colors">#</a>

> NOTE
>
> 它在WebKit中不支持，请在他们的问题跟踪器中查看 [here](https://bugs.webkit.org/show_bug.cgi?id=225281) .

- `geolocation` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="browser-new-context-option-geolocation">#</a>

    - `latitude` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>纬度介于-90和90之间。
    - `longitude` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 经度介于-180和180之间。
    - `accuracy` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>非负精度值。默认值为 `0`.

- `has_touch` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 指定视口是否支持触摸事件。默认值为`false`.<a name="browser-new-context-option-has-touch">#</a>

- `http_credentials` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)>  HTTP认证凭据 [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).<a name="browser-new-context-option-http-credentials">#</a>

    - `username` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
    - `password` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>

- `ignore_https_errors` \<[bool](https://docs.python.org/3/library/stdtypes.html)>发送网络请求时是否忽略HTTPS错误。默认值为 `false`.<a name="browser-new-context-option-ignore-https-errors">#</a>

- `is_mobile` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否考虑 `meta viewport` 标签，是否启用触摸事件。默认值为 `false`. Firefox中不支持.<a name="browser-new-context-option-is-mobile">#</a>

- `java_script_enabled` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否在上下文中启用JavaScript。默认值为 `true`.<a name="browser-new-context-option-java-script-enabled">#</a>

- `locale` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 指定用户的本地语言环境，例如 `en-GB`, `de-DE`, 等. 区域设置将影响导航器. `navigator.language` 的值, `Accept-Language` 请求头值以及数字和日期格式规则.<a name="browser-new-context-option-locale">#</a>

- `no_viewport` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 不强制固定viewport，允许在头部模式下调整窗口大小.<a name="browser-new-context-option-no-viewport">#</a>

- `offline` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否仿真网络离线。默认值为 `false`.<a name="browser-new-context-option-offline">#</a>

- `permissions` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 在此上下文中授予所有页面的权限列表。获取更多细节: [browser_context.grant_permissions(permissions, **kwargs)](#browser-context-grant-permissions) .<a name="browser-new-context-option-permissions">#</a>

- `proxy` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 在此上下文中使用的网络代理设置.<a name="browser-new-context-option-proxy">#</a>

    - `server` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 所有请求使用的代理。支持HTTP代理和SOCKS代理，例如: `http://myproxy.com:3128` or `socks5://myproxy.com:3128`.缩写形式 `myproxy.com:3128` 被认为是一个HTTP代理。
    - `bypass` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>可选，用逗号分隔的域，绕过代理，例如 `".com, chromium.org, .domain.com"`.
    - `username` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 可选username，当HTTP代理需要鉴权时使用。
    - `password` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 当HTTP代理需要鉴权时可选密码。

    > NOTE
    >
    > 对于Windows上的Chromium浏览器，需要使用全局代理启动该选项才能工作。如果所有上下文覆盖了代理，全局代理将永远不会被使用，可以是任何字符串，例如: `launch({ proxy: { server: 'http://per-context' } })`.

- `record_har_omit_content` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 可选设置，控制是否从HAR忽略请求内容。默认值为`false`.<a name="browser-new-context-option-record-har-omit-content">#</a>

- `record_har_path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 为文件系统中指定的 [HAR](http://www.softwareishard.com/blog/har-12-spec) 文件中所有页面启用HAR 记录,如果没有指定，则不会记录HAR。确保调用 [browser_context.close()](#browser-context-close) 来保存HAR.<a name="browser-new-context-option-record-har-path">#</a>

- `record_video_dir` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 开启进入指定目录的所有页面的视频录制,如果没有指定，则不录制视频。确保调用 [browser_context.close()](#browser-context-close) 来保存视频.<a name="browser-new-context-option-record-video-dir">#</a>

- `record_video_size` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 录制视频的尺寸。如果没有指定大小将等于 `viewport` 缩小到800x800。如果`viewport` 没有显式配置，视频大小默认为800x450。每个页面的实际图片将按比例缩小，如果需要，以适应指定的大小.<a name="browser-new-context-option-record-video-size">#</a>

    - `width` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 视频帧宽度.
    - `height` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 视频帧高度.

- `reduced_motion` \<"reduce"|"no-preference"> 模拟`'prefers-reduced-motion'` 媒体特性，支持的值为 `'reduce'`, `'no-preference'`. 详情请参阅 [page.emulate_media(**kwargs)](#page-emulate-media) . 默认值为 `'no-preference'`.<a name="browser-new-context-option-reduced-motion">#</a>

- `screen` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)>通过 `window.screen`在web页面中模拟一致的窗口屏幕大小. 仅在 `viewport` 设置时使用.<a name="browser-new-context-option-screen">#</a>

    - `width` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面宽度(px).
    - `height` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面高度(px).

- `storage_state` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)>用给定的存储状态填充上下文. 这个选项可以用来用通过 [browser_context.storage_state(**kwargs)](#browser-context-storage-state)获得的登录信息初始化上下文。可以是保存了存储空间的文件路径，也可以是包含以下字段的对象:<a name="browser-new-context-option-storage-state">#</a>

    - `cookies` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]> cookie设置上下文
        - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `domain` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> Domain和path是必需的
        - `path` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> Domain和path是必需的
        - `expires` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> Unix 时间，单位为秒.
        - `httpOnly` \<[bool](https://docs.python.org/3/library/stdtypes.html)>
        - `secure` \<[bool](https://docs.python.org/3/library/stdtypes.html)>
        - `sameSite` \<"Strict"|"Lax"|"None"> 相同站点标识
    - `origins` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]> localStorage 设置上下文
        - `origin` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `localStorage` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]>
            - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
            - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>

- `strict_selectors` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 它指定了，为这个上下文启用严格选择器模式。在严格的选择器模式中，当有多个元素匹配选择器时，所有对选择器的操作都将意味着只有一个目标DOM元素。请参阅 [Locator](#locator) 以了解更多关于严格模式.<a name="browser-new-context-option-strict-selectors">#</a>

- `timezone_id` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 修改上下文的时区。查看 [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1) 获取支持的时区id列表.<a name="browser-new-context-option-timezone-id">#</a>

- `user_agent` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 在此上下文中使用的特定用户代理.<a name="browser-new-context-option-user-agent">#</a>

- `viewport` \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 为每个页面设置一个一致的视口。默认为1280x720视口. `no_viewport` 禁用固定视口.<a name="browser-new-context-option-viewport">#</a>

    - `width` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面宽度(px).
    - `height` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面高度(px).

- returns: \<[BrowserContext](#browsercontext)><a name="browser-new-context-return">#</a>

创建一个新的浏览器上下文。它不会与其他浏览器上下文共享cookie /缓存

- Sync

```python
browser = playwright.firefox.launch() # or "chromium" or "webkit".
# create a new incognito browser context.
context = browser.new_context()
# create a new page in a pristine context.
page = context.new_page()
page.goto("https://example.com")
```

- Async

```python
browser = await playwright.firefox.launch() # or "chromium" or "webkit".
# create a new incognito browser context.
context = await browser.new_context()
# create a new page in a pristine context.
page = await context.new_page()
await page.goto("https://example.com")
```

## browser.new_page(**kwargs)<a name="browser-new-page">#</a>

- `accept_downloads` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否自动下载所有附件。在所有下载都被接受的地方默认为 True .<a name="browser-new-page-option-accept-downloads">#</a>

- `base_url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 使用以下方法时 [page.goto(url, **kwargs)](#page-goto), [page.route(url, handler, **kwargs)](#page-route), [page.wait_for_url(url, **kwargs)](#page-wait-for-url), [page.expect_request(url_or_predicate, **kwargs)](#page-wait-for-request), or [page.expect_response(url_or_predicate, **kwargs)](#page-wait-for-response)通过使用 [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 构造函数构建相应的URL:<a name="browser-new-page-option-base-url">#</a>

    - baseURL= `http://localhost:3000` 时,导航到 `/bar.html` 结果是 `http://localhost:3000/bar.html`
    - baseURL= `http://localhost:3000/foo/` 时,导航到 `./bar.html` 结果是 `http://localhost:3000/foo/bar.html`
    - baseURL= `http://localhost:3000/foo` 时,导航到(没有下划线) `./bar.html` 结果是 `http://localhost:3000/bar.html`

- `bypass_csp` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 切换绕过页面的 Content-Security-Policy.<a name="browser-new-page-option-bypass-csp">#</a>

- `color_scheme` \<"light"|"dark"|"no-preference"> 模拟`'prefers-colors-scheme'` 的媒体特性，支持的值为 `'light'`, `'dark'`, `'no-preference'`. 详情请参阅 [page.emulate_media(**kwargs)](#page-emulate-media) . 默认值为 `'light'`.<a name="browser-new-page-option-color-scheme">#</a>

- `device_scale_factor` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 指定设备比例因子(可以认为是dpr)。默认为 `1`.<a name="browser-new-page-option-device-scale-factor">#</a>

- `extra_http_headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 个包含附加HTTP头的对象，每个请求都要发送.<a name="browser-new-page-option-extra-http-headers">#</a>

- `forced_colors` \<"active"|"none">模拟 `'forced-colors'` 媒体特性，支持的值为 `'active'`, `'none'`. 详情请参阅[page.emulate_media(**kwargs)](#page-emulate-media) . 默认为 `'none'`.<a name="browser-new-page-option-forced-colors">#</a>

    > NOTE
    >
    > 它在WebKit中不支持，请在他们的问题跟踪器中查看 [here](https://bugs.webkit.org/show_bug.cgi?id=225281) .

- `geolocation` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="browser-new-page-option-geolocation">#</a>

    - `latitude` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>纬度介于-90和90之间。
    - `longitude` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 经度介于-180和180之间。
    - `accuracy` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>非负精度值。默认值为 `0`.

- `has_touch` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 指定视口是否支持触摸事件。默认值为false.<a name="browser-new-page-option-has-touch">#</a>

- `http_credentials` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> HTTP认证凭据 [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).<a name="browser-new-page-option-http-credentials">#</a>

    - `username` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
    - `password` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>

- `ignore_https_errors` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 发送网络请求时是否忽略HTTPS错误。默认值为`false`.<a name="browser-new-page-option-ignore-https-errors">#</a>

- `is_mobile` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否考虑 `meta viewport` 标签，是否启用触摸事件。默认值为 `false`. Firefox中不支持.<a name="browser-new-page-option-is-mobile">#</a>

- `java_script_enabled` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否在上下文中启用JavaScript。默认值为 `true`.<a name="browser-new-page-option-java-script-enabled">#</a>

- `locale` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 指定用户的本地语言环境，例如 `en-GB`, `de-DE`, 等. 区域设置将影响导航器. `navigator.language` 的值, `Accept-Language` 请求头值以及数字和日期格式规则.<a name="browser-new-page-option-locale">#</a>

- `no_viewport` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 不强制固定viewport，允许在头部模式下调整窗口大小.<a name="browser-new-page-option-no-viewport">#</a>

- `offline` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否仿真网络离线。默认值为 `false`.<a name="browser-new-page-option-offline">#</a>

- `permissions` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 在此上下文中授予所有页面的权限列表。获取更多细节: [browser_context.grant_permissions(permissions, **kwargs)](#browser-context-grant-permissions) .<a name="browser-new-page-option-permissions">#</a>

- `proxy` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 在此上下文中使用的网络代理设置.<a name="browser-new-page-option-proxy">#</a>

    - `server` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 所有请求使用的代理。支持HTTP代理和SOCKS代理，例如: `http://myproxy.com:3128` or `socks5://myproxy.com:3128`.缩写形式 `myproxy.com:3128` 被认为是一个HTTP代理.
    - `bypass` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>可选，用逗号分隔的域，绕过代理，例如 `".com, chromium.org, .domain.com"`.
    - `username` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 可选username，当HTTP代理需要鉴权时使用。
    - `password` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 当HTTP代理需要鉴权时可选密码。

    > NOTE
    >
    > 对于Windows上的Chromium浏览器，需要使用全局代理启动该选项才能工作。如果所有上下文覆盖了代理，全局代理将永远不会被使用，可以是任何字符串，例如: `launch({ proxy: { server: 'http://per-context' } })`.

- `record_har_omit_content` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 可选设置，控制是否从HAR忽略请求内容。默认值为`false`.<a name="browser-new-page-option-record-har-omit-content">#</a>

- `record_har_path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 为文件系统中指定的 [HAR](http://www.softwareishard.com/blog/har-12-spec) 文件中所有页面启用HAR 记录,如果没有指定，则不会记录HAR。确保调用 [browser_context.close()](#browser-context-close) 来保存HAR.<a name="browser-new-page-option-record-har-path">#</a>

- `record_video_dir` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 开启进入指定目录的所有页面的视频录制,如果没有指定，则不录制视频。确保调用 [browser_context.close()](#browser-context-close) 来保存视频.<a name="browser-new-page-option-record-video-dir">#</a>

- `record_video_size` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 录制视频的尺寸。如果没有指定大小将等于 `viewport` 缩小到800x800。如果`viewport` 没有显式配置，视频大小默认为800x450。每个页面的实际图片将按比例缩小，如果需要，以适应指定的大小.<a name="browser-new-page-option-record-video-size">#</a>

    - `width` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 视频帧宽度.
    - `height` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 视频帧高度.

- `reduced_motion` \<"reduce"|"no-preference"> 模拟`'prefers-reduced-motion'` 媒体特性，支持的值为 `'reduce'`, `'no-preference'`. 详情请参阅 [page.emulate_media(**kwargs)](#page-emulate-media) . 默认值为 `'no-preference'`.<a name="browser-new-page-option-reduced-motion">#</a>

- `screen` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 通过 `window.screen`在web页面中模拟一致的窗口屏幕大小. 仅在 `viewport` 设置时使用.<a name="browser-new-page-option-screen">#</a>

    - `width` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面宽度(px).
    - `height` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面高度(px).

- `storage_state` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 用给定的存储状态填充上下文. 这个选项可以用来用通过 [browser_context.storage_state(**kwargs)](#browser-context-storage-state)获得的登录信息初始化上下文。可以是保存了存储空间的文件路径，也可以是包含以下字段的对象:<a name="browser-new-page-option-storage-state">#</a>

    - `cookies` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]> cookie设置上下文
        - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `domain` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> Domain和path是必需的
        - `path` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> Domain和path是必需的
        - `expires` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> Unix 时间，单位为秒
        - `httpOnly` \<[bool](https://docs.python.org/3/library/stdtypes.html)>
        - `secure` \<[bool](https://docs.python.org/3/library/stdtypes.html)>
        - `sameSite` \<"Strict"|"Lax"|"None"> 相同站点标识
    - `origins` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]> localStorage 设置上下文
        - `origin` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `localStorage` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]>
            - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
            - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>

- `strict_selectors` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 它指定了，为这个上下文启用严格选择器模式。在严格的选择器模式中，当有多个元素匹配选择器时，所有对选择器的操作都将意味着只有一个目标DOM元素。请参阅 [Locator](#locator) 以了解更多关于严格模式.<a name="browser-new-page-option-strict-selectors">#</a>

- `timezone_id` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 修改上下文的时区。查看 [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1) 获取支持的时区id列表.<a name="browser-new-page-option-timezone-id">#</a>

- `user_agent` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 在此上下文中使用的特定用户代理.<a name="browser-new-page-option-user-agent">#</a>

- `viewport` \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 为每个页面设置一个一致的视口。默认为1280x720视口. `no_viewport` 禁用固定视口.

    - `width` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面宽度(px).
    - `height` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面高度(px).

- returns: \<[Page](#page)><a name="browser-new-page-return">#</a>

在新的浏览器上下文中创建一个新页面。关闭此页面也将关闭上下文。

这是一个方便的API，应该只用于单页场景和简短的片段。产品代码和测试框架应该显式地创建 [browser.new_context(**kwargs)](#browser-new-context) ,然后再创建[browser_context.new_page()](#browser-context-new-page) 来控制它们的确切生命周期。

## browser.start_tracing(**kwargs)<a name="browser-start-tracing">#</a>

- `page` \<[Page](#page)> 可选，如果指定，跟踪包含给定页面的截图.<a name="browser-start-tracing-option-page">#</a>
- `categories` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 指定要使用的自定义类别而不是默认类别.<a name="browser-start-tracing-option-categories">#</a>
- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 文件写入的路径.<a name="browser-start-tracing-option-path">#</a>
- `screenshots` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 捕获跟踪中的屏幕截图.<a name="browser-start-tracing-option-screenshots">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-start-tracing-return">#</a>

> NOTE
>
> 这个API控制 [Chromium Tracing](https://www.chromium.org/developers/how-tos/trace-event-profiling-tool) 这是一个低级别的Chromium专用调试工具。控制 [Playwright Tracing](https://playwright.dev/python/docs/trace-viewer) 的API可以在[这里](#tracing)找到.
>
> 你可以使用 [browser.start_tracing(**kwargs)](#browser-start-tracing) 和[browser.stop_tracing()](#browser-stop-tracing) 来创建一个可以在Chrome DevTools性能面板中打开的跟踪文件.

- Sync

```python
browser.start_tracing(page, path="trace.json")
page.goto("https://www.google.com")
browser.stop_tracing()
```

- Async

```python
await browser.start_tracing(page, path="trace.json")
await page.goto("https://www.google.com")
await browser.stop_tracing()
```

## browser.stop_tracing()<a name="browser-stop-tracing">#</a>

- returns: \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)><a name="browser-stop-tracing-return">#</a>

> NOTE
>
> 这个API控制 [Chromium Tracing](https://www.chromium.org/developers/how-tos/trace-event-profiling-tool) 这是一个低级别的Chromium专用调试工具。控制 [Playwright Tracing](https://playwright.dev/python/docs/trace-viewer) 的API可以在[这里](#tracing)找到.
>
> 返回带有跟踪数据的缓冲区.

## browser.version<a name="browser-version">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="browser-version-return">#</a>

返回浏览器版本



# BrowserContext

- extends: [EventEmitter](https://pyee.readthedocs.io/en/latest/#pyee.BaseEventEmitter)

BrowserContexts 提供了一种操作多个独立浏览器会话的方法。

如果一个页面打开另一个页面，例如with a `window.open` call，弹出窗口将属于父页面的浏览器上下文。

Playwright 允许使用 browser.new_context(**kwargs)方法创建“Incognito”浏览器上下文。“Incognito”浏览器上下文不会将任何浏览数据写入磁盘。

- Sync

```python
# create a new incognito browser context
context = browser.new_context()
# create a new page inside context.
page = context.new_page()
page.goto("https://example.com")
# dispose context once it is no longer needed.
context.close()
```

- Async

```python
# create a new incognito browser context
context = await browser.new_context()
# create a new page inside context.
page = await context.new_page()
await page.goto("https://example.com")
# dispose context once it is no longer needed.
await context.close()
```

## browser_context.on("backgroundpage")<a name="browser-context-event-background-page">#</a>

- type: \<[Page](#page)>

> NOTE
>
> 仅适用于Chromium 浏览器的持久上下文。



当在上下文中创建新的后台页面时触发。

- Sync

```python
background_page = context.wait_for_event("backgroundpage")
```

- Async

```python
background_page = await context.wait_for_event("backgroundpage")
```



## browser_context.on("close")<a name="browser-context-event-close">#</a>

- type: \<[BrowserContext](#browsercontext)>

当浏览器上下文关闭时触发。这可能是因为以下原因之一:

- 关闭浏览器上下文.
- 浏览器应用程序关闭或崩溃.
- 调用了 [browser.close()](#browser-close) 方法.

## browser_context.on("page")<a name="browser-context-event-page">#</a>

- type: \<[Page](#page)>

当在BrowserContext中创建一个新的Page时，会触发该事件。页面可能仍在加载中。该事件也将为弹出页面而触发。请参见[page.on("popup")](#page-event-popup) 接收与特定页面相关的关于弹出窗口的事件.

该页面可用的最早时刻是当它已导航到初始url。例如，当用`window.open('http://example.com')`, 打开一个弹出窗口时，这个事件将在网络请求"[http://example.com"](http://example.com"/) 完成并在弹出窗口中开始加载响应时触发.

- Sync

```python
with context.expect_page() as page_info:
    page.click("a[target=_blank]"),
page = page_info.value
print(page.evaluate("location.href"))
```

- Async

```python
async with context.expect_page() as page_info:
    await page.click("a[target=_blank]"),
page = await page_info.value
print(await page.evaluate("location.href"))
```

> NOTE
>
> 使用[page.wait_for_load_state(**kwargs)](#page-wait-for-load-state) 等待页面到达特定的状态(在大多数情况下不需要它).

## browser_context.on("request")<a name="browser-context-event-request">#</a>

- type: \<[Request](#request)>

当从通过此上下文创建的任何页面发出请求时触发。请求对象是只读的。要只监听来自特定页面的请求，请使用 [page.on("request")](#page-event-request).

为了拦截和修改请求，请参阅 [browser_context.route(url, handler, **kwargs)](#browser-context-route) or [page.route(url, handler, **kwargs)](#page-route).

## browser_context.on("requestfailed")<a name="browser-context-event-request-failed">#</a>

- type: \<[Request](#request)>

当请求失败时触发，例如超时。要只监听来自特定页面的失败请求，请使用 [page.on("requestfailed")](#page-event-request-failed).

> NOTE
>
> HTTP错误响应，如404或503，从HTTP的角度来看，仍然是成功的响应，因此请求将完成[browser_context.on("requestfinished")](#browser-context-event-request-finished)事件，而不是 [browser_context.on("requestfailed")](#browser-context-event-request-failed).

## browser_context.on("requestfinished")<a name="browser-context-event-request-finished">#</a>

- type: \<[Request](#request)>

在下载响应体后，请求成功完成时触发。对于一个成功的响应，事件序列是 `request`, `response` and `requestfinished`. 要监听来自特定页面的成功请求，请使用 [page.on("requestfinished")](#page-event-request-finished).

## browser_context.on("response")<a name="browser-context-event-response">#</a>

- type: \<[Response](#response)>

当收到请求的响应状态和报头时触发。对于一个成功的响应，事件序列是 `request`, `response` and `requestfinished`. 要监听来自特定页面的响应事件，请使用 [page.on("response")](#page-event-response).

## browser_context.on("serviceworker")<a name="browser-context-event-service-worker">#</a>

- type: \<[Worker](#worker)>

> NOTE
>
> Service worker只支持基于chrome的浏览器.
>
> 当在上下文中创建新的 service worker 时触发.

## browser_context.add_cookies(cookies)<a name="browser-context-add-cookies">#</a>

- `cookies` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]><a name="browser-context-add-cookies-option-cookies">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
    - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
    - `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>  完整的URL(带协议),   url 和( domain / path) 之间必选其一.
    - `domain` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 域(与path一起使用),不需要加协议.    url 和( domain / path) 之间必选其一.
    - `path` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 路径(与domain 一起使用),前面需要加`/`.     url 和( domain / path) 之间必选其一.
    - `expires` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> Unix 时间，单位为秒。可选的.
    - `httpOnly` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 可选的.
    - `secure` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 可选的.
    - `sameSite` \<"Strict"|"Lax"|"None">   <“严格”|“宽松”|“没有”>可选的.
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-add-cookies-return">#</a>

将cookie添加到此浏览器上下文中。这个上下文中的所有页面都将安装这些cookie。cookie可以通过[browser_context.cookies(**kwargs)](#browser-context-cookies) 获取.

```python
# cookie_object like
{
    'name': 'aaa', 
    'value': '132456', 
    'domain': 'httpbin.org', 
    'path': '/cookies'
}
# or
{
    'name': 'aaa', 
    'value': '132456', 
    'url': 'http://httpbin.org/cookies', 
}
```

- Sync

```python
browser_context.add_cookies([cookie_object1, cookie_object2])
```

- Async

```python
await browser_context.add_cookies([cookie_object1, cookie_object2])
```

## browser_context.add_init_script(**kwargs)<a name="browser-context-add-init-script">#</a>

- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> JavaScript 文件的路径. 如果`path` 是一个相对路径，那么它是相对于当前工作目录解析的。可选的.<a name="browser-context-add-init-script-option-path">#</a>
- `script` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 在浏览器上下文中所有页面中执行的脚本。可选的.<a name="browser-context-add-init-script-option-script">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-add-init-script-return">#</a>

添加一个脚本，该脚本将在以下场景之一中进行评估:

- 当在浏览器上下文中创建或导航页面时.
- 当在浏览器上下文中的任何页面中附加或导航一个子框架时。在这种情况下，脚本将在新附加的框架的上下文中执行.

在创建文档之后，但在运行文档的任何脚本之前，对脚本进行计算。这对于修改JavaScript环境是很有用的，例如 `Math.random`.

一个重写 `Math.random`的例子。页面加载前:

```js
// preload.js
Math.random = () => 42;
```

- Sync

```python
# in your playwright script, assuming the preload.js file is in same directory.
browser_context.add_init_script(path="preload.js")
```

- Async

```python
# in your playwright script, assuming the preload.js file is in same directory.
await browser_context.add_init_script(path="preload.js")
```

> NOTE
>
> 通过 [browser_context.add_init_script(**kwargs)](#browser-context-add-init-script) and [page.add_init_script(**kwargs)](#page-add-init-script) 安装的多个脚本的计算顺序没有定义.

## browser_context.background_pages<a name="browser-context-background-pages">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Page](#page)]><a name="browser-context-background-pages-return">#</a>

> NOTE
>
> 背景页面仅支持基于chrome的浏览器.
>
> 所有现有的背景页在上下文中.

## browser_context.browser<a name="browser-context-browser">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Browser](#browser)><a name="browser-context-browser-return">#</a>

返回上下文的浏览器实例。如果它作为持久上下文启动，则返回null.

## browser_context.clear_cookies()<a name="browser-context-clear-cookies">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-clear-cookies-return">#</a>

清除上下文 cookies.

## browser_context.clear_permissions()<a name="browser-context-clear-permissions">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-clear-permissions-return">#</a>

清除浏览器上下文的所有权限覆盖.

- Sync

```python
context = browser.new_context()
context.grant_permissions(["clipboard-read"])
# do stuff ..
context.clear_permissions()
```

- Async

```python
context = await browser.new_context()
await context.grant_permissions(["clipboard-read"])
# do stuff ..
context.clear_permissions()
```

## browser_context.close()<a name="browser-context-close">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-close-return">#</a>

关闭浏览器上下文。属于浏览器上下文的所有页面都将被关闭.

> NOTE
>
> 无法关闭默认的浏览器上下文.

## browser_context.cookies(**kwargs)<a name="browser-context-cookies">#</a>

- `urls` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 可选url列表.<a name="browser-context-cookies-option-urls">#</a>
- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]><a name="browser-context-cookies-return">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
    - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
    - `domain` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
    - `path` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
    - `expires` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> Unix 时间，单位为秒.
    - `httpOnly` \<[bool](https://docs.python.org/3/library/stdtypes.html)>
    - `secure` \<[bool](https://docs.python.org/3/library/stdtypes.html)>
    - `sameSite` \<"Strict"|"Lax"|"None">   <“严格”|“宽松”|“没有”>

如果没有指定url，则此方法返回所有cookie。如果指定了url，则只返回影响这些url的cookie.

## browser_context.expect_event(event, **kwargs)<a name="browser-context-wait-for-event">#</a>

- `event` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 事件名称，相同的一个将传递给 `browserContext.on(event)`.<a name="browser-context-wait-for-event-option-event">#</a>
- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)> 接收事件数据，并在等待应该被解析时解析为 True .<a name="browser-context-wait-for-event-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为 `30000` (30 seconds). 传入`0` 禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) 来更改.<a name="browser-context-wait-for-event-option-timeout">#</a>
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)><a name="browser-context-wait-for-event-return">#</a>

等待事件触发，并将其值传递给谓词函数。当谓词返回 True 时返回。如果上下文在触发事件之前关闭，则将抛出一个错误。返回事件数据值.

- Sync

```python
with context.expect_event("page") as event_info:
    page.click("button")
page = event_info.value
```

- Async

```python
async with context.expect_event("page") as event_info:
    await page.click("button")
page = await event_info.value
```

## browser_context.expect_page(**kwargs)<a name="browser-context-wait-for-page">#</a>

- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[Page](#page)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 接收 [Page](#page) 对象，并在等待应该解决时解析为 True .<a name="browser-context-wait-for-page-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为 `30000` (30 seconds). 传入`0` 禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) 来更改.<a name="browser-context-wait-for-page-option-timeout">#</a>
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)[[Page](#page)]><a name="browser-context-wait-for-page-return">#</a>

执行操作并等待在上下文中创建一个新的 [Page](#page) 如果提供了predicate，它将 [Page](#page) 值传递给 `predicate` 函数，并等待 `predicate(event)` 返回一个真值。如果上下文在创建新页面之前关闭，将抛出一个错误.

## browser_context.expose_binding(name, callback, **kwargs)<a name="browser-context-expose-binding">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> window对象上的函数名.<a name="browser-context-expose-binding-option-name">#</a>
- `callback` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)> 在 playwright 的上下文中被调用的回调函数.<a name="browser-context-expose-binding-option-callback">#</a>
- `handle` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否将参数作为句柄传递，而不是按值传递。当传递句柄时，只支持一个参数。当传递值时，支持多个参数.<a name="browser-context-expose-binding-option-handle">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-expose-binding-return">#</a>

该方法在上下文中每一页的每一帧的窗口对象上添加一个名为name的函数。当被调用时，函数执行回调并返回一个 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) ,该Promise解析为回调的返回值。如果回调返回一个Promise，它将被等待

`callback`函数的第一个参数包含调用者的信息: `{ browserContext: BrowserContext, page: Page, frame: Frame }`.

查看仅用于页面版本的 [page.expose_binding(name, callback, **kwargs)](#page-expose-binding).

一个将页面URL暴露给上下文中所有页面中的所有帧的例子:

- Sync

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    webkit = playwright.webkit
    browser = webkit.launch(headless=false)
    context = browser.new_context()
    context.expose_binding("pageURL", lambda source: source["page"].url)
    page = context.new_page()
    page.set_content("""
    \<script>
      async function onClick() {
        document.querySelector('div').textContent = await window.pageURL();
      }
    \</script>
    \<button onclick="onClick()">Click me\</button>
    \<div>\</div>
    """)
    page.click("button")

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    webkit = playwright.webkit
    browser = await webkit.launch(headless=false)
    context = await browser.new_context()
    await context.expose_binding("pageURL", lambda source: source["page"].url)
    page = await context.new_page()
    await page.set_content("""
    \<script>
      async function onClick() {
        document.querySelector('div').textContent = await window.pageURL();
      }
    \</script>
    \<button onclick="onClick()">Click me\</button>
    \<div>\</div>
    """)
    await page.click("button")

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

传递元素句柄的例子:

- Sync

```python
def print(source, element):
    print(element.text_content())

context.expose_binding("clicked", print, handle=true)
page.set_content("""
  \<script>
    document.addEventListener('click', event => window.clicked(event.target));
  \</script>
  \<div>Click me\</div>
  \<div>Or click me\</div>
""")
```

- Async

```python
async def print(source, element):
    print(await element.text_content())

await context.expose_binding("clicked", print, handle=true)
await page.set_content("""
  \<script>
    document.addEventListener('click', event => window.clicked(event.target));
  \</script>
  \<div>Click me\</div>
  \<div>Or click me\</div>
""")
```

## browser_context.expose_function(name, callback)<a name="browser-context-expose-function">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> window对象上的函数名.<a name="browser-context-expose-function-option-name">#</a>
- `callback` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)> 在 playwright 的上下文中被调用的回调函数.<a name="browser-context-expose-function-option-callback">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-expose-function-return">#</a>

该方法在上下文中每一页的每一帧的窗口对象上添加一个名为name的函数。当被调用时，函数执行回调并返回一个 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) ,该Promise解析为回调的返回值.

如果回调返回一个 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise),它将被等待.

查看仅页面版本的[page.expose_function(name, callback)](#page-expose-function) .

在上下文中为所有页面添加一个`sha256` 函数的例子:

- Sync

```python
import hashlib
from playwright.sync_api import sync_playwright

def sha256(text):
    m = hashlib.sha256()
    m.update(bytes(text, "utf8"))
    return m.hexdigest()


def run(playwright):
    webkit = playwright.webkit
    browser = webkit.launch(headless=False)
    context = browser.new_context()
    context.expose_function("sha256", sha256)
    page = context.new_page()
    page.set_content("""
        \<script>
          async function onClick() {
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');
          }
        \</script>
        \<button onclick="onClick()">Click me\</button>
        \<div>\</div>
    """)
    page.click("button")

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
import hashlib
from playwright.async_api import async_playwright

def sha256(text):
    m = hashlib.sha256()
    m.update(bytes(text, "utf8"))
    return m.hexdigest()


async def run(playwright):
    webkit = playwright.webkit
    browser = await webkit.launch(headless=False)
    context = await browser.new_context()
    await context.expose_function("sha256", sha256)
    page = await context.new_page()
    await page.set_content("""
        \<script>
          async function onClick() {
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');
          }
        \</script>
        \<button onclick="onClick()">Click me\</button>
        \<div>\</div>
    """)
    await page.click("button")

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

## browser_context.grant_permissions(permissions, **kwargs)<a name="browser-context-grant-permissions">#</a>

- `permissions` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 要授予的权限或权限数组。权限可以是以下值之一: <a name="browser-context-grant-permissions-option-permissions">#</a>
    - `'geolocation' `		地理位置
    - `'midi'`
    - `'midi-sysex'` (system-exclusive midi)
    - `'notifications'`      通知
    - `'camera'`        相机
    - `'microphone'`     麦克风
    - `'background-sync'`
    - `'ambient-light-sensor'`    环境光传感器
    - `'accelerometer'`       加速度计
    - `'gyroscope' `     陀螺
    - `'magnetometer'`   磁强计
    - `'accessibility-events'`
    - `'clipboard-read'`
    - `'clipboard-write'`
    - `'payment-handler'`
- `origin` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>  要授予权限的[起点](https://developer.mozilla.org/en-US/docs/Glossary/Origin)，例如: "[https://example.com"](https://example.com"/).<a name="browser-context-grant-permissions-option-origin">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-grant-permissions-return">#</a>

向浏览器上下文授予指定的权限。如果指定，则仅向给定的源授予相应的权限.

## browser_context.new_cdp_session(page)<a name="browser-context-new-cdp-session">#</a>

- `page` \<[Page](#page)|[Frame](#frame)> 创建会话的目标。为了向后兼容，这个参数被命名为 `page`, 但它可以是一个 `Page` or `Frame` 类型.<a name="browser-context-new-cdp-session-option-page">#</a>
- returns: \<[CDPSession](#cdpsession)><a name="browser-context-new-cdp-session-return">#</a>

> NOTE
>
> CDP会话仅支持基于chromium的浏览器
>
> 返回新创建的会话.

## browser_context.new_page()<a name="browser-context-new-page">#</a>

- returns: \<[Page](#page)><a name="browser-context-new-page-return">#</a>

在浏览器上下文中创建一个新页面.

## browser_context.pages<a name="browser-context-pages">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Page](#page)]><a name="browser-context-pages-return">#</a>

返回上下文中所有打开的页面.

## browser_context.route(url, handler, **kwargs)<a name="browser-context-route">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[URL](https://en.wikipedia.org/wiki/URL)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 一个glob模式、regex模式或谓词在路由时接收要匹配的 [URL](https://en.wikipedia.org/wiki/URL) ,当通过上下文选项提供了一个`base_url` 并且传递的URL是一个路径时，它会通过 [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 构造函数合并.<a name="browser-context-route-option-url">#</a>
- `handler` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[Route](#route), [Request](#request)]> handler函数路由请求.<a name="browser-context-route-option-handler">#</a>
- `times` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 一个路由应该使用的频率。默认情况下，每次都会使用.<a name="browser-context-route-option-times">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-route-return">#</a>

路由提供了修改浏览器上下文中任何页面发出的网络请求的能力。一旦路由被启用，每一个匹配url模式的请求都会停止，除非它被继续、完成或中止.

> NOTE
>
> [page.route(url, handler, **kwargs)](#page-route) 不会拦截被 Service Worker 拦截的请求. 详情查看 [这个问题](https://github.com/microsoft/playwright/issues/1090) . 我们建议在使用请求拦截时禁用 Service Workers, 通过 `await context.addInitScript(() => delete window.navigator.serviceWorker);`

一个简单的处理程序的例子，中止所有的图像请求:

- Sync

```python
context = browser.new_context()
page = context.new_page()
context.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
page.goto("https://example.com")
browser.close()
```

- Async

```python
context = await browser.new_context()
page = await context.new_page()
await context.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
await page.goto("https://example.com")
await browser.close()
```

或者使用regex模式替换相同的代码片段:

- Sync

```python
context = browser.new_context()
page = context.new_page()
context.route(re.compile(r"(\.png$)|(\.jpg$)"), lambda route: route.abort())
page = await context.new_page()
page = context.new_page()
page.goto("https://example.com")
browser.close()
```

- Async

```python
context = await browser.new_context()
page = await context.new_page()
await context.route(re.compile(r"(\.png$)|(\.jpg$)"), lambda route: route.abort())
page = await context.new_page()
await page.goto("https://example.com")
await browser.close()
```

可以通过检查请求来决定路由操作。例如，mock所有包含post数据的请求，并保留所有其他请求的原样:

- Sync

```python
def handle_route(route):
  if ("my-string" in route.request.post_data)
    route.fulfill(body="mocked-data")
  else
    route.continue_()
context.route("/api/**", handle_route)
```

- Async

```python
def handle_route(route):
  if ("my-string" in route.request.post_data)
    route.fulfill(body="mocked-data")
  else
    route.continue_()
await context.route("/api/**", handle_route)
```

当请求同时匹配两个处理程序时,[page.route(url, handler, **kwargs)](https://playwright.dev/python/docs/api/class-page#page-route) 优先于浏览器上下文路由

要移除带有处理程序的路由，你可以使用 [browser_context.unroute(url, **kwargs)](#browser-context-unroute).

> NOTE
>
> 启用路由将禁用 http 缓存.

## browser_context.service_workers<a name="browser-context-service-workers">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Worker](#worker)]><a name="browser-context-service-workers-return">#</a>

> NOTE
>
> Service worker只支持基于chrome的浏览器。
>
> 上下文中的所有现有服务工作者。

## browser_context.set_default_navigation_timeout(timeout)<a name="browser-context-set-default-navigation-timeout">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大导航时间，以毫秒为单位<a name="browser-context-set-default-navigation-timeout-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-set-default-navigation-timeout-return">#</a>

此设置将改变以下方法和相关快捷方式的默认最大导航时间:

- [page.go_back(**kwargs)](#page-go-back)
- [page.go_forward(**kwargs)](#page-go-forward)
- [page.goto(url, **kwargs)](#page-goto)
- [page.reload(**kwargs)](#page-reload)
- [page.set_content(html, **kwargs)](#page-set-content)
- [page.expect_navigation(**kwargs)](#page-wait-for-navigation)

> NOTE
>
> [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) 和 [page.set_default_timeout(timeout)](#page-set-default-timeout) 优先于 [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout).

## browser_context.set_default_timeout(timeout)<a name="browser-context-set-default-timeout">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间(毫秒)<a name="browser-context-set-default-timeout-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-set-default-timeout-return">#</a>

此设置将更改`所有`接受超时的方法的默认最大时间.

> NOTE
>
> [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout), [page.set_default_timeout(timeout)](#page-set-default-timeout) 和[browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout) 优先于 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout).

## browser_context.set_extra_http_headers(headers)<a name="browser-context-set-extra-http-headers">#</a>

- `headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 包含每个请求发送的附加HTTP头的对象。所有头文件的值必须是字符串.<a name="browser-context-set-extra-http-headers-option-headers">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-set-extra-http-headers-return">#</a>

额外的HTTP报头将与上下文中的任何页面发起的每个请求一起发送。这些标头与 [page.set_extra_http_headers(headers)](#page-set-extra-http-headers)设置的特定于页面的额外HTTP标头合并. 如果页面覆盖了特定的标题，那么将使用特定于页面的标题值，而不是浏览器上下文标题值.

> NOTE
>
> [browser_context.set_extra_http_headers(headers)](#browser-context-set-extra-http-headers) 不能保证传出请求中报头的顺序.

## browser_context.set_geolocation(geolocation)<a name="browser-context-set-geolocation">#</a>

- `geolocation` \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="browser-context-set-geolocation-option-geolocation">#</a>
    - `latitude` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 纬度介于-90和90之间.
    - `longitude` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 经度介于-180和180之间.
    - `accuracy` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 非负精度值。默认值为`0`.
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-set-geolocation-return">#</a>

设置上下文的地理位置。传递 `null` or `undefined` 将模拟位置不可用.

- Sync

```python
browser_context.set_geolocation({"latitude": 59.95, "longitude": 30.31667})
```

- Async

```python
await browser_context.set_geolocation({"latitude": 59.95, "longitude": 30.31667})
```

> NOTE
>
> 考虑使用 [browser_context.grant_permissions(permissions, **kwargs)](#browser-context-grant-permissions) 授予浏览器上下文页面读取其地理位置的权限.

## browser_context.set_offline(offline)<a name="browser-context-set-offline">#</a>

- `offline` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否为浏览器上下文模拟网络离线.<a name="browser-context-set-offline-option-offline">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-set-offline-return">#</a>

## browser_context.storage_state(**kwargs)<a name="browser-context-storage-state">#</a>

- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 存储状态保存到的文件路径. 如果`path` 是一个相对路径，那么它是相对于当前工作目录解析的。如果没有提供路径，存储状态仍然返回，但不会保存到磁盘.<a name="browser-context-storage-state-option-path">#</a>
- returns: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="browser-context-storage-state-return">#</a>
    - `cookies` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]>
        - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `domain` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `path` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `expires` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> Unix 时间，单位为秒.
        - `httpOnly` \<[bool](https://docs.python.org/3/library/stdtypes.html)>
        - `secure` \<[bool](https://docs.python.org/3/library/stdtypes.html)>
        - `sameSite` \<"Strict"|"Lax"|"None">   <“严格”|“宽松”|“没有”>
    - `origins` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]>
        - `origin` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
        - `localStorage` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]>
            - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
            - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>

返回此浏览器上下文的存储状态，包含当前cookie和本地存储快照.

## browser_context.unroute(url, **kwargs)<a name="browser-context-unroute">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[URL](https://en.wikipedia.org/wiki/URL)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 用于向[browser_context.route(url, handler, **kwargs)](#browser-context-route)注册路由的glob模式、regex模式或谓词接收url .<a name="browser-context-unroute-option-url">#</a>
- `handler` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[Route](#route), [Request](#request)]> 可选处理函数，用于向 [browser_context.route(url, handler, **kwargs)](#browser-context-route) 注册路由.<a name="browser-context-unroute-option-handler">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="browser-context-unroute-return">#</a>

移除使用 [browser_context.route(url, handler, **kwargs)](#browser-context-route) 创建的路由. 当未指定`handler` 时，删除`url`的所有路由 .

## browser_context.wait_for_event(event, **kwargs)<a name="browser-context-wait-for-event-2">#</a>

- `event` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 事件名称，与通常传递给 `*.on(event)`的名称相同.<a name="browser-context-wait-for-event-2-option-event">#</a>
- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)> 接收事件数据，并在等待应该被解析时解析为真值.<a name="browser-context-wait-for-event-2-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为 `30000` (30 seconds). 传入`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) 来更改.<a name="browser-context-wait-for-event-2-option-timeout">#</a>
- returns: \<[Any](https://docs.python.org/3/library/typing.html#typing.Any)><a name="browser-context-wait-for-event-2-return">#</a>

> NOTE
>
> 在大多数情况下，你应该使用 [browser_context.expect_event(event, **kwargs)](#browser-context-wait-for-event).
>
> 等待给定 `event` 被触发. 如果提供了 `predicate` ,它会将事件的值传递给 `predicate(event)` 并等待其返回一个真值. 如果浏览器上下文在触发事件之前关闭，则将抛出一个错误.

## browser_context.request<a name="browser-context-request">#</a>

- type: \<[APIRequestContext](#apirequestcontext)>

与此上下文关联的API测试助手。使用此API发出的请求将使用上下文 cookie.

## browser_context.tracing<a name="browser-context-tracing">#</a>

- type: \<[Tracing](#tracing)>





# BrowserType



BrowserType 提供了启动特定浏览器实例或连接到现有浏览器实例的方法。下面是一个使用Playwright 驱动自动化的典型例子:

- Sync

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    chromium = playwright.chromium
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.goto("https://example.com")
    # other actions...
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

## browser_type.connect(ws_endpoint, **kwargs)<a name="browser-type-connect">#</a>

- `ws_endpoint` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>要连接的浏览器websocket端点.<a name="browser-type-connect-option-ws-endpoint">#</a>
- `headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> websocket 连接请求发送的额外HTTP头。可选的.<a name="browser-type-connect-option-headers">#</a>
- `slow_mo` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 使 playwright 操作变慢指定的毫秒数。很有用，这样你就能知道发生了什么。默认为0.<a name="browser-type-connect-option-slow-mo">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 等待连接建立的最大时间(单位:毫秒)。默认为 `30000` (30 seconds). 传递`0` 以禁用超时.<a name="browser-type-connect-option-timeout">#</a>
- returns: \<[Browser](#browser)><a name="browser-type-connect-return">#</a>

该方法将playwright 附加到一个现有的浏览器实例.

## browser_type.connect_over_cdp(endpoint_url, **kwargs)<a name="browser-type-connect-over-cdp">#</a>

- `endpoint_url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要连接CDP的 websocket端点或 http url。例如 `http://localhost:9222/` or `ws://127.0.0.1:9222/devtools/browser/387adf4c-243f-4051-a181-46798f4a46f4`.<a name="browser-type-connect-over-cdp-option-endpoint-url">#</a>
- `headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 连接请求发送的额外HTTP头。可选的.<a name="browser-type-connect-over-cdp-option-headers">#</a>
- `slow_mo` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 使 playwright 操作变慢指定的毫秒数。很有用，这样你就能知道发生了什么。默认为0.<a name="browser-type-connect-over-cdp-option-slow-mo">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 等待连接建立的最大时间(单位:毫秒)。默认为 `30000` (30 seconds). 传递`0` 以禁用超时.<a name="browser-type-connect-over-cdp-option-timeout">#</a>
- returns: \<[Browser](#browser)><a name="browser-type-connect-over-cdp-return">#</a>

该方法使用Chrome DevTools协议将playwright附加到一个现有的浏览器实例.

默认的浏览器上下文可以通过 [browser.contexts](#browser-contexts) 访问.

> NOTE
>
> 通过Chrome DevTools协议连接仅支持基于Chrome的浏览器.

## browser_type.executable_path<a name="browser-type-executable-path">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="browser-type-executable-path-return">#</a>

Playwright 希望在这个路径中找到捆绑的浏览器可执行文件.

## browser_type.launch(**kwargs)<a name="browser-type-launch">#</a>

- `args` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 传递给浏览器实例的其他参数。Chrome的列表可以在[这里](http://peter.sh/experiments/chromium-command-line-switches/)找到 .<a name="browser-type-launch-option-args">#</a>
- `channel` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 浏览器分发通道。支持的值为 "chrome", "chrome-beta", "chrome-dev", "chrome-canary", "msedge", "msedge-beta", "msedge-dev", "msedge-canary". 阅读更多关于使用 [Google Chrome 和 Microsoft Edge](https://playwright.dev/python/docs/browsers#google-chrome--microsoft-edge) 的方式.<a name="browser-type-launch-option-channel">#</a>
- `chromium_sandbox` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启用Chromium 沙箱. 默认为 `false`.<a name="browser-type-launch-option-chromium-sandbox">#</a>
- `devtools` \<[bool](https://docs.python.org/3/library/stdtypes.html)> **Chromium-only** 是否为每个选项卡自动打开开发人员工具面板。如果该选项为 `true`, 则`headless` 选项将被设为`false`.<a name="browser-type-launch-option-devtools">#</a>
- `downloads_path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 如果指定，接受的下载将被下载到此目录, 否则，将在关闭浏览器时创建并删除临时目录。在这两种情况下，当创建下载的浏览器上下文关闭时，下载就会被删除.<a name="browser-type-launch-option-downloads-path">#</a>
- `env` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]> 指定浏览器可见的环境变量。默认为 `process.env`.<a name="browser-type-launch-option-env">#</a>
- `executable_path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 浏览器可执行文件的运行路径，而不是绑定文件. 如果`executable_path` 是一个相对路径，那么它是相对于当前工作目录进行解析的。请注意，playwright 只适用于捆绑的Chromium, Firefox或WebKit，使用风险自负.<a name="browser-type-launch-option-executable-path">#</a>
- `firefox_user_prefs` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]> Firefox用户首选项。在[`about:config`](https://support.mozilla.org/en-US/kb/about-config-editor-firefox) 了解更多关于Firefox用户首选项的信息.<a name="browser-type-launch-option-firefox-user-prefs">#</a>
- `handle_sighup` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 在SIGHUP上关闭浏览器进程。默认值为 `true`.<a name="browser-type-launch-option-handle-sighup">#</a>
- `handle_sigint` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 在Ctrl-C上关闭浏览器进程。默认值为 `true`.<a name="browser-type-launch-option-handle-sigint">#</a>
- `handle_sigterm` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 关闭SIGTERM上的浏览器进程。默认值为 `true`.<a name="browser-type-launch-option-handle-sigterm">#</a>
- `headless` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否以无头模式运行浏览器。更多关于 [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) and [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode) 的细节。默认为 `true` 除非 `devtools` 选项为`true`.<a name="browser-type-launch-option-headless">#</a>
- `ignore_default_args` \<[bool](https://docs.python.org/3/library/stdtypes.html)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 如果为`true`, Playwright 不会传递自己的配置参数，而只使用来自 `args`的配置参数. 如果给出了数组，则过滤掉给定的默认参数。危险的选择, 小心使用。默认值为 `false`.<a name="browser-type-launch-option-ignore-default-args">#</a>
- `proxy` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 网络代理设置.<a name="browser-type-launch-option-proxy">#</a>
    - `server` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 所有请求使用的代理。支持HTTP代理和SOCKS代理，例如:`http://myproxy.com:3128` or `socks5://myproxy.com:3128`. 缩写形式 `myproxy.com:3128` 被认为是一个HTTP代理.
    - `bypass` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 可选，用逗号分隔的域，绕过代理，例如 `".com, chromium.org, .domain.com"`.
    - `username` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 可选username，当HTTP代理需要鉴权时使用.
    - `password` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 当HTTP代理需要鉴权时可选密码.
- `slow_mo` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 使 playwright 操作变慢指定的毫秒数。可以让您看到正在发生什么.<a name="browser-type-launch-option-slow-mo">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 浏览器实例启动的最大等待时间(单位为毫秒)。默认为 `30000` (30 seconds). 传递`0` 以禁用超时.<a name="browser-type-launch-option-timeout">#</a>
- `traces_dir` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 如果指定，跟踪记录将被保存到该目录.<a name="browser-type-launch-option-traces-dir">#</a>
- returns: \<[Browser](#browser)><a name="browser-type-launch-return">#</a>

返回浏览器实例.

你可以使用 `ignore_default_args` 从默认参数中过滤出 `--mute-audio`:

- Sync

```python
browser = playwright.chromium.launch( # or "firefox" or "webkit".
    ignore_default_args=["--mute-audio"]
)
```

- Async

```python
browser = await playwright.chromium.launch( # or "firefox" or "webkit".
    ignore_default_args=["--mute-audio"]
)
```

> **Chromium-only** Playwright 也可以用来控制谷歌Chrome或微软Edge浏览器，但它最好的版本与 Chromium 捆绑. 不能保证它能与任何其他版本一起工作。使用 `executable_path` 选项时要特别小心.
>
> 如果 Google Chrome (而不是 Chromium) 是首选, 则建议使用 [Chrome Canary](https://www.google.com/chrome/browser/canary.html) or [Dev Channel](https://www.chromium.org/getting-involved/dev-channel) .
>
> 像 Google Chrome 和 Microsoft Edge 这样的常用浏览器适合于需要专用媒体编解码器进行视频播放的测试. Chromium and Chrome 的其他区别见[这篇文章](https://www.howtogeek.com/202825/what’s-the-difference-between-chromium-and-chrome/). [本文](https://chromium.googlesource.com/chromium/src/+/lkgr/docs/chromium_browser_vs_google_chrome.md) 描述了Linux 用户的一些差异.

## browser_type.launch_persistent_context(user_data_dir, **kwargs)<a name="browser-type-launch-persistent-context">#</a>

- `user_data_dir` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 用户数据目录的路径，用于存储浏览器会话数据，如cookie和本地存储. 更多关于 [Chromium](https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md#introduction) and [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options#User_Profile) 的细节. 注意 Chromium 的用户数据目录是父目录的“配置文件路径” `chrome://version`. 传递一个空字符串来使用临时目录.<a name="browser-type-launch-persistent-context-option-user-data-dir">#</a>

- `accept_downloads` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否自动下载所有附件。在所有下载都被接受的地方默认为 `true` .<a name="browser-type-launch-persistent-context-option-accept-downloads">#</a>

- `args` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 传递给浏览器实例的其他参数. Chromium 标志的列表可以在[这里](http://peter.sh/experiments/chromium-command-line-switches/)找到 .<a name="browser-type-launch-persistent-context-option-args">#</a>

- `base_url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 使用 [page.goto(url, **kwargs)](#page-goto), [page.route(url, handler, **kwargs)](#page-route), [page.wait_for_url(url, **kwargs)](#page-wait-for-url), [page.expect_request(url_or_predicate, **kwargs)](#page-wait-for-request), or [page.expect_response(url_or_predicate, **kwargs)](#page-wait-for-response) 通过使用`URL()`构造函数构建相应的URL来考虑基URL :<a name="browser-type-launch-persistent-context-option-base-url">#</a>

    - baseURL= `http://localhost:3000` 时,导航到 `/bar.html` 的结果为 `http://localhost:3000/bar.html`
    - baseURL= `http://localhost:3000/foo/` 时,导航到 `./bar.html` 的结果为 `http://localhost:3000/foo/bar.html`
    - baseURL= `http://localhost:3000/foo` 时,导航到(没有下划线) `./bar.html` 的结果为`http://localhost:3000/bar.html`

- `bypass_csp` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 切换绕过页面的 Content-Security-Policy.<a name="browser-type-launch-persistent-context-option-bypass-csp">#</a>

- `channel` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 浏览器分发通道。支持的值为 "chrome", "chrome-beta", "chrome-dev", "chrome-canary", "msedge", "msedge-beta", "msedge-dev", "msedge-canary". 阅读更多关于使用 [Google Chrome 和 Microsoft Edge](https://playwright.dev/python/docs/browsers#google-chrome--microsoft-edge).<a name="browser-type-launch-persistent-context-option-channel">#</a>

- `chromium_sandbox` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启用Chromium 沙箱. 默认为 `false`.<a name="browser-type-launch-persistent-context-option-chromium-sandbox">#</a>

- `color_scheme` \<"light"|"dark"|"no-preference"> 模拟`'prefers-colors-scheme'` 的媒体特性，支持的值为`'light'`, `'dark'`, `'no-preference'`. 详情请参阅 : [page.emulate_media(**kwargs)](#page-emulate-media) . 默认为 `'light'`.<a name="browser-type-launch-persistent-context-option-color-scheme">#</a>

- `device_scale_factor` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 指定设备比例因子(可以认为是dpr)。默认为`1`.<a name="browser-type-launch-persistent-context-option-device-scale-factor">#</a>

- `devtools` \<[bool](https://docs.python.org/3/library/stdtypes.html)> **Chromium-only** 是否为每个选项卡自动打开开发人员工具面板。如果该选项为 `true`, 则 `headless` 选项将被设为`false`.<a name="browser-type-launch-persistent-context-option-devtools">#</a>

- `downloads_path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 如果指定，接受的下载将被下载到此目录, 否则，将在关闭浏览器时创建并删除临时目录。在这两种情况下，当创建下载的浏览器上下文关闭时，下载就会被删除.<a name="browser-type-launch-persistent-context-option-downloads-path">#</a>

- `env` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[bool](https://docs.python.org/3/library/stdtypes.html)]> 指定浏览器可见的环境变量。默认为 `process.env`.<a name="browser-type-launch-persistent-context-option-env">#</a>

- `executable_path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 浏览器可执行文件的运行路径，而不是绑定文件. 如果`executable_path` 是一个相对路径，那么它是相对于当前工作目录进行解析的。请注意，playwright 只适用于捆绑的Chromium, Firefox或WebKit，使用风险自负.<a name="browser-type-launch-persistent-context-option-executable-path">#</a>

- `extra_http_headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 一个包含附加HTTP头的对象，每个请求都要发送.<a name="browser-type-launch-persistent-context-option-extra-http-headers">#</a>

- `forced_colors` \<"active"|"none"> 模拟`'forced-colors'` 媒体特性，支持的值为 `'active'`, `'none'`. 详情请参阅:[page.emulate_media(**kwargs)](#page-emulate-media) . 默认为 `'none'`.<a name="browser-type-launch-persistent-context-option-forced-colors">#</a>

    > NOTE
    >
    > 它在WebKit中不支持，请在他们的[问题](https://bugs.webkit.org/show_bug.cgi?id=225281)跟踪器中查看

- `geolocation` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="browser-type-launch-persistent-context-option-geolocation">#</a>

    - `latitude` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 纬度介于-90和90之间.
    - `longitude` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 经度介于-180和180之间.
    - `accuracy` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 非负精度值。默认值为`0`.

- `handle_sighup` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 在SIGHUP上关闭浏览器进程。默认值为 `true`.<a name="browser-type-launch-persistent-context-option-handle-sighup">#</a>

- `handle_sigint` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 在Ctrl-C上关闭浏览器进程。默认值为 `true`.<a name="browser-type-launch-persistent-context-option-handle-sigint">#</a>

- `handle_sigterm` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 关闭SIGTERM上的浏览器进程。默认值为 `true`.<a name="browser-type-launch-persistent-context-option-handle-sigterm">#</a>

- `has_touch` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 指定视口是否支持触摸事件。默认值为` false`.<a name="browser-type-launch-persistent-context-option-has-touch">#</a>

- `headless` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否以无头模式运行浏览器。更多关于 [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) and [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode)的细节。默认为 `true` 除非 `devtools` 选项为 `true`.<a name="browser-type-launch-persistent-context-option-headless">#</a>

- `http_credentials` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> HTTP认证凭据 [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).<a name="browser-type-launch-persistent-context-option-http-credentials">#</a>

    - `username` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>
    - `password` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>

- `ignore_default_args` \<[bool](https://docs.python.org/3/library/stdtypes.html)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 如果为`true`, 不会传递自己的配置参数，而只使用来自 `args`的配置参数。如果给出了数组，则过滤掉给定的默认参数。危险的选择, 小心使用。默认值为 `false`.<a name="browser-type-launch-persistent-context-option-ignore-default-args">#</a>

- `ignore_https_errors` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 发送网络请求时是否忽略HTTPS错误。默认值为 `false`.<a name="browser-type-launch-persistent-context-option-ignore-https-errors">#</a>

- `is_mobile` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否考虑 `meta viewport` 标签，是否启用触摸事件。默认值为`false`。Firefox中不支持.<a name="browser-type-launch-persistent-context-option-is-mobile">#</a>

- `java_script_enabled` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否在上下文中启用JavaScript。默认值为 `true`.<a name="browser-type-launch-persistent-context-option-java-script-enabled">#</a>

- `locale` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 指定用户的本地语言环境，例如 `en-GB`, `de-DE`, 等。区域设置将影响 `navigator.language` 的值, `Accept-Language` 请求头值以及数字和日期格式规则.<a name="browser-type-launch-persistent-context-option-locale">#</a>

- `no_viewport` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 不强制固定viewport，允许在头部模式下调整窗口大小.<a name="browser-type-launch-persistent-context-option-no-viewport">#</a>

- `offline` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否仿真网络离线。默认值为 `false`.<a name="browser-type-launch-persistent-context-option-offline">#</a>

- `permissions` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 在此上下文中授予所有页面的权限列表。详细常看: [browser_context.grant_permissions(permissions, **kwargs)](#browser-context-grant-permissions).<a name="browser-type-launch-persistent-context-option-permissions">#</a>

- `proxy` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 网络代理设置.<a name="browser-type-launch-persistent-context-option-proxy">#</a>

    - `server` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 所有请求使用的代理。支持HTTP代理和SOCKS代理，例如:`http://myproxy.com:3128` or `socks5://myproxy.com:3128`. 缩写 `myproxy.com:3128` 被认为是一个HTTP代理.
    - `bypass` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 可选，用逗号分隔的域，绕过代理，例如 `".com, chromium.org, .domain.com"`.
    - `username` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 可选username，当HTTP代理需要鉴权时使用.
    - `password` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 当HTTP代理需要鉴权时可选密码.

- `record_har_omit_content` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 可选设置，控制是否从HAR忽略请求内容。默认值为 `false`.<a name="browser-type-launch-persistent-context-option-record-har-omit-content">#</a>

- `record_har_path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 为文件系统中指定的 [HAR](http://www.softwareishard.com/blog/har-12-spec) 文件中所有页面启用HAR记录. 如果没有指定，则不会记录HAR。确保调用 [browser_context.close()](#browser-context-close) 来保存HAR.<a name="browser-type-launch-persistent-context-option-record-har-path">#</a>

- `record_video_dir` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 开启进入指定目录的所有页面的视频录制. 如果没有指定，则不录制视频。确保调用 [browser_context.close()](#browser-context-close) 来保存视频.<a name="browser-type-launch-persistent-context-option-record-video-dir">#</a>

- `record_video_size` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 录制视频的尺寸。如果没有指定大小将等于 `viewport` 缩小到800x800。如果 `viewport` 没有显式配置，视频大小默认为800x450。每个页面的实际图片将按比例缩小，如果需要，以适应指定的大小.<a name="browser-type-launch-persistent-context-option-record-video-size">#</a>

    - `width` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 视频帧宽度.
    - `height` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 视频帧高度.

- `reduced_motion` \<"reduce"|"no-preference"> 模拟`'prefers-reduced-motion'` 媒体特性，支持的值为 `'reduce'`, `'no-preference'`. 详情请参阅[page.emulate_media(**kwargs)](#page-emulate-media).  默认为 `'no-preference'`.<a name="browser-type-launch-persistent-context-option-reduced-motion">#</a>

- `screen` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 通过 `window.screen`.在web页面中模拟一致的窗口屏幕大小。仅在设置 `viewport` 时使用.

    - `width` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面宽度(px).
    - `height` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面高度(px).

- `slow_mo` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 使 playwright 操作变慢指定的毫秒数。可以让您看到正在发生什么.<a name="browser-type-launch-persistent-context-option-slow-mo">#</a>

- `strict_selectors` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 它指定了，为这个上下文启用严格选择器模式。在严格的选择器模式中，当有多个元素匹配选择器时，所有对选择器的操作都将意味着只有一个目标DOM元素。请参阅 [Locator](#locator) 以了解更多关于严格模式.<a name="browser-type-launch-persistent-context-option-strict-selectors">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 浏览器实例启动的最大等待时间(单位为毫秒)。默认为 `30000` (30 seconds). 传递`0` 以禁用超时.<a name="browser-type-launch-persistent-context-option-timeout">#</a>

- `timezone_id` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 修改上下文的时区。查看 [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1) 获取支持的时区id列表.<a name="browser-type-launch-persistent-context-option-timezone-id">#</a>

- `traces_dir` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 如果指定，跟踪记录将被保存到该目录.<a name="browser-type-launch-persistent-context-option-traces-dir">#</a>

- `user_agent` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 在此上下文中使用的特定用户代理.<a name="browser-type-launch-persistent-context-option-user-agent">#</a>

- `viewport` \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 为每个页面设置一个一致的视口。默认为1280x720视口. `no_viewport`禁用固定视口.<a name="browser-type-launch-persistent-context-option-viewport">#</a>

    - `width` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面宽度(px).
    - `height` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面高度(px).

- returns: \<[BrowserContext](#browsercontext)><a name="browser-type-launch-persistent-context-return">#</a>

返回持久的浏览器上下文实例.

启动浏览器，使用位于 `user_data_dir` 的持久存储，并返回唯一的上下文。关闭此上下文将自动关闭浏览器.

## browser_type.name<a name="browser-type-name">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="browser-type-name-return">#</a>

返回浏览器的名称。例如: `'chromium'`, `'webkit'` or `'firefox'`.





# CDPSession

- extends: [EventEmitter](https://pyee.readthedocs.io/en/latest/#pyee.BaseEventEmitter)

`CDPSession` 实例用于谈论原始的Chrome Devtools协议:

- 协议方法可以用会话调用 `session.send` .
- 协议事件可以通过会话订阅 `session.on` 上的方法.

有用的链接:

- DevTools协议的文档可以在这里找到: [DevTools Protocol Viewer](https://chromedevtools.github.io/devtools-protocol/).
- 开始使用DevTools协议: https://github.com/aslushnikov/getting-started-with-cdp/blob/master/README.md

- Sync

```python
client = page.context.new_cdp_session(page)
client.send("Animation.enable")
client.on("Animation.animationCreated", lambda: print("animation created!"))
response = client.send("Animation.getPlaybackRate")
print("playback rate is " + str(response["playbackRate"]))
client.send("Animation.setPlaybackRate", {
    playbackRate: response["playbackRate"] / 2
})
```

- Async

```python
client = await page.context.new_cdp_session(page)
await client.send("Animation.enable")
client.on("Animation.animationCreated", lambda: print("animation created!"))
response = await client.send("Animation.getPlaybackRate")
print("playback rate is " + str(response["playbackRate"]))
await client.send("Animation.setPlaybackRate", {
    playbackRate: response["playbackRate"] / 2
})
```

- [cdp_session.detach()](#cdp-session-detach)
- [cdp_session.send(method, **kwargs)](#cdp-session-send)

## cdp_session.detach()<a name="cdp-session-detach">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="cdp-session-detach-return">#</a>

将CDPSession与目标分离。一旦分离，CDPSession对象将不会发出任何事件，也不能用于发送消息.

## cdp_session.send(method, **kwargs)<a name="cdp-session-send">#</a>

- `method` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 协议方法名<a name="cdp-session-send-option-method">#</a>
- `params` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 可选方法参数<a name="cdp-session-send-option-params">#</a>
- returns: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="cdp-session-send-return">#</a>





# ConsoleMessage

[ConsoleMessage](#consolemessage) 对象通过 [page.on("console")](#page-event-console) 事件调度.

- [console_message.args](#console-message-args)
- [console_message.location](#console-message-location)
- [console_message.text](#console-message-text)
- [console_message.type](#console-message-type)

## console_message.args<a name="console-message-args">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[JSHandle](#jshandle)]><a name="console-message-args-return">#</a>

传递给 `console` 函数调用的参数列表。参见 [page.on("console")](#page-event-console).

## console_message.location<a name="console-message-location">#</a>

- returns: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="console-message-location-return">#</a>
    - `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 资源的url.
    - `lineNumber` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 0-based 资源的行号.
    - `columnNumber` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 0-based 资源的列号.

## console_message.text<a name="console-message-text">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="console-message-text-return">#</a>

控制台消息的文本.

## console_message.type<a name="console-message-type">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="console-message-type-return">#</a>

以下值之一: `'log'`, `'debug'`, `'info'`, `'error'`, `'warning'`, `'dir'`, `'dirxml'`, `'table'`, `'trace'`, `'clear'`, `'startGroup'`, `'startGroupCollapsed'`, `'endGroup'`, `'assert'`, `'profile'`, `'profileEnd'`, `'count'`, `'timeEnd'`.





# Dialog

[Dialog](#dialog) 对象通过 [page.on("dialog")](#page-event-dialog) 事件分配.

使用 `Dialog`类的一个例子:

- Sync

```python
from playwright.sync_api import sync_playwright

def handle_dialog(dialog):
    print(dialog.message)
    dialog.dismiss()

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.on("dialog", handle_dialog)
    page.evaluate("alert('1')")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def handle_dialog(dialog):
    print(dialog.message)
    await dialog.dismiss()

async def run(playwright):
    chromium = playwright.chromium
    browser = await chromium.launch()
    page = await browser.new_page()
    page.on("dialog", handle_dialog)
    page.evaluate("alert('1')")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

> NOTE
>
> 除非有 [page.on("dialog")](#page-event-dialog) 监听器，否则对话框会自动被驳回。当监听器存在时，它必须要么 [dialog.accept(**kwargs)](#dialog-accept) 要么[dialog.dismiss()](#dialog-dismiss) 否则页面将[冻结](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop#never_blocking)等待对话框，像click这样的动作将永远不会结束.

- [dialog.accept(**kwargs)](#dialog-accept)
- [dialog.default_value](#dialog-default-value)
- [dialog.dismiss()](#dialog-dismiss)
- [dialog.message](#dialog-message)
- [dialog.type](#dialog-type)

## dialog.accept(**kwargs)<a name="dialog-accept">#</a>

- `prompt_text` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 提示符中要输入的文本。如果对话框的类型不是提示符，则不会造成任何影响。可选的.<a name="dialog-accept-option-prompt-text">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="dialog-accept-return">#</a>

当对话框被接受时返回.

## dialog.default_value<a name="dialog-default-value">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="dialog-default-value-return">#</a>

如果对话框是提示符，则返回默认的提示值。否则，返回空字符串.

## dialog.dismiss()<a name="dialog-dismiss">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="dialog-dismiss-return">#</a>

当对话框被驳回时返回.

## dialog.message<a name="dialog-message">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="dialog-message-return">#</a>

对话框中显示的消息.

## dialog.type<a name="dialog-type">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="dialog-type-return">#</a>

返回对话框的类型，可以是`alert`, `beforeunload`, `confirm` or `prompt`.



# Download

[Download](#download) 对象通过 [page.on("download")](#page-event-download) 事件被页面分派.

当浏览器上下文关闭时，属于浏览器上下文的所有下载文件将被删除.

一旦下载开始，就会触发Download事件。下载完成后，下载路径变为可用:

- Sync

```python
with page.expect_download() as download_info:
    page.click("a")
download = download_info.value
# wait for download to complete
path = download.path()
```

- Async

```python
async with page.expect_download() as download_info:
    await page.click("a")
download = await download_info.value
# waits for download to complete
path = await download.path()
```

- [download.cancel()](#download-cancel)
- [download.delete()](#download-delete)
- [download.failure()](#download-failure)
- [download.page](#download-page)
- [download.path()](#download-path)
- [download.save_as(path)](#download-save-as)
- [download.suggested_filename](#download-suggested-filename)
- [download.url](#download-url)

## download.cancel()<a name="download-cancel">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="download-cancel-return">#</a>

取消下载。如果下载已经完成或取消，则不会失败。成功取消后, `download.failure()` 将解析为 `'canceled'`.

## download.delete()<a name="download-delete">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="download-delete-return">#</a>

删除下载的文件。如果需要，将等待下载完成.

## download.failure()<a name="download-failure">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="download-failure-return">#</a>

如果有，返回下载错误。如果需要，将等待下载完成.

## download.page<a name="download-page">#</a>

- returns: \<[Page](#page)><a name="download-page-return">#</a>

获取下载文件所属的页面.

## download.path()<a name="download-path">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[pathlib.Path](https://realpython.com/python-pathlib/)><a name="download-path-return">#</a>

如果下载成功，返回下载文件的路径。如果需要，该方法将等待下载完成。该方法在远程连接时排除.

请注意，下载的文件名是一个随机的GUID，使用 [download.suggested_filename](#download-suggested-filename) 获取建议文件名.

## download.save_as(path)<a name="download-save-as">#</a>

- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 下载应该被复制的路径.<a name="download-save-as-option-path">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="download-save-as-return">#</a>

将下载文件复制到用户指定的路径。在下载过程中调用此方法是安全的。如果需要，将等待下载完成.

## download.suggested_filename<a name="download-suggested-filename">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="download-suggested-filename-return">#</a>

返回此下载的建议文件名。它通常是由浏览器从 [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition) 响应头或下载属性计算出来的。看规范是什么。不同的浏览器可以使用不同的逻辑来计算它 .

## download.url<a name="download-url">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="download-url-return">#</a>

返回下载url.





# ElementHandle

- extends: [JSHandle](#jshandle)

ElementHandle 表示一个页面内的DOM元素。可以用页面创建 [page.query_selector(selector, **kwargs)](#page-query-selector) 方法.

> DISCOURAGED
>
> 不鼓励使用ElementHandle，而是使用 [Locator](#locator) 对象和 web优先断言.
>

- Sync

```python
href_element = page.query_selector("a")
href_element.click()
```

- Async

```python
href_element = await page.query_selector("a")
await href_element.click()
```

ElementHandle prevents DOM element from garbage collection unless the handle is disposed with [js_handle.dispose()](#js-handle-dispose). ElementHandles are auto-disposed when their origin frame gets navigated.

ElementHandle instances can be used as an argument in [page.eval_on_selector(selector, expression, **kwargs)](#page-eval-on-selector) and [page.evaluate(expression, **kwargs)](#page-evaluate) methods.

The difference between the [Locator](#locator) and ElementHandle is that the ElementHandle points to a particular element, while [Locator](#locator) captures the logic of how to retrieve an element.

In the example below, handle points to a particular DOM element on page. If that element changes text or is used by React to render an entirely different component, handle is still pointing to that very DOM element. This can lead to unexpected behaviors.

- Sync

```python
handle = page.query_selector("text=Submit")
handle.hover()
handle.click()
```

- Async

```python
handle = await page.query_selector("text=Submit")
await handle.hover()
await handle.click()
```

With the locator, every time the `element` is used, up-to-date DOM element is located in the page using the selector. So in the snippet below, underlying DOM element is going to be located twice.

- Sync

```python
locator = page.locator("text=Submit")
locator.hover()
locator.click()
```

- Async

```python
locator = page.locator("text=Submit")
await locator.hover()
await locator.click()
```

- [element_handle.bounding_box()](#element-handle-bounding-box)
- [element_handle.check(**kwargs)](#element-handle-check)
- [element_handle.click(**kwargs)](#element-handle-click)
- [element_handle.content_frame()](#element-handle-content-frame)
- [element_handle.dblclick(**kwargs)](#element-handle-dblclick)
- [element_handle.dispatch_event(type, **kwargs)](#element-handle-dispatch-event)
- [element_handle.eval_on_selector(selector, expression, **kwargs)](#element-handle-eval-on-selector)
- [element_handle.eval_on_selector_all(selector, expression, **kwargs)](#element-handle-eval-on-selector-all)
- [element_handle.fill(value, **kwargs)](#element-handle-fill)
- [element_handle.focus()](#element-handle-focus)
- [element_handle.get_attribute(name)](#element-handle-get-attribute)
- [element_handle.hover(**kwargs)](#element-handle-hover)
- [element_handle.inner_html()](#element-handle-inner-html)
- [element_handle.inner_text()](#element-handle-inner-text)
- [element_handle.input_value(**kwargs)](#element-handle-input-value)
- [element_handle.is_checked()](#element-handle-is-checked)
- [element_handle.is_disabled()](#element-handle-is-disabled)
- [element_handle.is_editable()](#element-handle-is-editable)
- [element_handle.is_enabled()](#element-handle-is-enabled)
- [element_handle.is_hidden()](#element-handle-is-hidden)
- [element_handle.is_visible()](#element-handle-is-visible)
- [element_handle.owner_frame()](#element-handle-owner-frame)
- [element_handle.press(key, **kwargs)](#element-handle-press)
- [element_handle.query_selector(selector)](#element-handle-query-selector)
- [element_handle.query_selector_all(selector)](#element-handle-query-selector-all)
- [element_handle.screenshot(**kwargs)](#element-handle-screenshot)
- [element_handle.scroll_into_view_if_needed(**kwargs)](#element-handle-scroll-into-view-if-needed)
- [element_handle.select_option(**kwargs)](#element-handle-select-option)
- [element_handle.select_text(**kwargs)](#element-handle-select-text)
- [element_handle.set_checked(checked, **kwargs)](#element-handle-set-checked)
- [element_handle.set_input_files(files, **kwargs)](#element-handle-set-input-files)
- [element_handle.tap(**kwargs)](#element-handle-tap)
- [element_handle.text_content()](#element-handle-text-content)
- [element_handle.type(text, **kwargs)](#element-handle-type)
- [element_handle.uncheck(**kwargs)](#element-handle-uncheck)
- [element_handle.wait_for_element_state(state, **kwargs)](#element-handle-wait-for-element-state)
- [element_handle.wait_for_selector(selector, **kwargs)](#element-handle-wait-for-selector)
- [js_handle.as_element()](#js-handle-as-element)
- [js_handle.dispose()](#js-handle-dispose)
- [js_handle.evaluate(expression, **kwargs)](#js-handle-evaluate)
- [js_handle.evaluate_handle(expression, **kwargs)](#js-handle-evaluate-handle)
- [js_handle.get_properties()](#js-handle-get-properties)
- [js_handle.get_property(property_name)](#js-handle-get-property)
- [js_handle.json_value()](#js-handle-json-value)

## element_handle.bounding_box()<a name="element-handle-bounding-box">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="element-handle-bounding-box-return">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 元素的 X 坐标像素.
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 元素的Y坐标，以像素为单位.
    - `width` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 元素的宽度，以像素为单位.
    - `height` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 元素的高度，以像素为单位.

此方法返回元素的边界框，如果元素不可见，则返回`null`。边界框是相对于主帧视口计算的——主帧视口通常与浏览器窗口相同.

滚动会影响返回的绑定框，类似于  [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) , 这意味着x和/或y可能是负的.

与 [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) 不同，子frame 中的元素返回相对于主frame 的边界框.

假设页面是静态的，使用边界框坐标执行输入是安全的。例如，下面的代码片段应该单击元素的中心.

- Sync

```python
box = element_handle.bounding_box()
page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
```

- Async

```python
box = await element_handle.bounding_box()
await page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
```

## element_handle.check(**kwargs)<a name="element-handle-check">#</a>

- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="element-handle-check-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="element-handle-check-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="element-handle-check-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-check-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="element-handle-check-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-check-return">#</a>

这个方法通过执行以下步骤来检查元素:

1. 确保元素是一个复选框或单选输入。如果不是，则抛出此方法。如果元素已被选中，则该方法立即返回.
2. 等待元素的[可操作性](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项.
3. 如果需要，将元素滚动到视图中.
4. 使用 [page.mouse](#page-mouse) 单击元素的中心.
5. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.
6. 确保元素现在被选中。如果不是，则排除此方法.

如果元素在动作期间的任何时刻与DOM分离，此方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## element_handle.click(**kwargs)<a name="element-handle-click">#</a>

- `button` \<"left"|"right"|"middle"> 默认左 `left`.<a name="element-handle-click-option-button">#</a>
- `click_count` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 默认为1,详情查看  [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail).<a name="element-handle-click-option-click-count">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `mousedown`和`mouseup`之间的等待时间，单位是毫秒。默认为0.<a name="element-handle-click-option-delay">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="element-handle-click-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="element-handle-click-option-modifiers">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="element-handle-click-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="element-handle-click-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-click-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="element-handle-click-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-click-return">#</a>

该方法执行以下步骤单击元素:

1. 等待元素的[可操作性](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项.
2. 如果需要，将元素滚动到视图中.
3. 使用 [page.mouse](#page-mouse) 单击元素的中心, or the specified `position`.
4. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.

如果元素在动作期间的任何时刻与DOM分离，此方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## element_handle.content_frame()<a name="element-handle-content-frame">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Frame](#frame)><a name="element-handle-content-frame-return">#</a>

Returns the content frame for element handles referencing iframe nodes, or `null` otherwise

## element_handle.dblclick(**kwargs)<a name="element-handle-dblclick">#</a>

- `button` \<"left"|"right"|"middle"> 默认左 `left`.<a name="element-handle-dblclick-option-button">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `mousedown`和`mouseup`之间的等待时间，单位是毫秒。默认为0.<a name="element-handle-dblclick-option-delay">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="element-handle-dblclick-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="element-handle-dblclick-option-modifiers">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="element-handle-dblclick-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="element-handle-dblclick-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-dblclick-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="element-handle-dblclick-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-dblclick-return">#</a>

该方法执行以下步骤双击元素:

1. 等待元素的[可操作性](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项.
2. 如果需要，将元素滚动到视图中.
3. 使用 [page.mouse](#page-mouse) 方法,双击元素中心位置.
4. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.该方法执行以下步骤双击元素, 注意，如果`dblclick()`的第一次单击触发了一个导航事件，则该方法将抛出.

如果元素在动作期间的任何时刻与DOM分离，此方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

> NOTE
>
> `elementHandle.dblclick()` dispatches two `click` events and a single `dblclick` event.

## element_handle.dispatch_event(type, **kwargs)<a name="element-handle-dispatch-event">#</a>

- `type` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> DOM事件类型:`"click"`， `"dragstart"`等.<a name="element-handle-dispatch-event-option-type">#</a>
- `event_init` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 可选的特定于事件的初始化属性.<a name="element-handle-dispatch-event-option-event-init">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-dispatch-event-return">#</a>

下面的代码片段分派元素上的`单击`事件。无论元素的可见性状态如何，单击都将被分派。这相当于调用[element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

- Sync

```python
element_handle.dispatch_event("click")
```

- Async

```python
await element_handle.dispatch_event("click")
```

在底层，它根据给定的类型创建一个事件实例，使用`event_init`属性初始化它，并在元素上分派它。默认情况下，事件是组合的、可取消的和冒泡的.

由于`event_init`是特定于事件的，请参考事件文档中的初始属性列表:

- [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
- [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
- [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
- [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
- [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
- [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
- [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)

如果你想要将活动对象传递到事件中，你也可以指定`jhandle`作为属性值:

- Sync

```python
# note you can only create data_transfer in chromium and firefox
data_transfer = page.evaluate_handle("new DataTransfer()")
element_handle.dispatch_event("#source", "dragstart", {"dataTransfer": data_transfer})
```

- Async

```python
# note you can only create data_transfer in chromium and firefox
data_transfer = await page.evaluate_handle("new DataTransfer()")
await element_handle.dispatch_event("#source", "dragstart", {"dataTransfer": data_transfer})
```

## element_handle.eval_on_selector(selector, expression, **kwargs)<a name="element-handle-eval-on-selector">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="element-handle-eval-on-selector-option-selector">#</a>
- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="element-handle-eval-on-selector-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="element-handle-eval-on-selector-option-arg">#</a>
- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="element-handle-eval-on-selector-return">#</a>

返回表达式的返回值.

The method finds an element matching the specified selector in the `ElementHandle`s subtree and passes it as a first argument to `expression`. See [Working with selectors](https://playwright.dev/python/docs/selectors) for more details. If no elements match the selector, the method throws an error.

如果`expression`返回[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)，那么 [element_handle.eval_on_selector(selector, expression, **kwargs)](#element-handle-eval-on-selector) 将等待promise解析并返回它的值.

Examples:

- Sync

```python
tweet_handle = page.query_selector(".tweet")
assert tweet_handle.eval_on_selector(".like", "node => node.innerText") == "100"
assert tweet_handle.eval_on_selector(".retweets", "node => node.innerText") = "10"
```

- Async

```python
tweet_handle = await page.query_selector(".tweet")
assert await tweet_handle.eval_on_selector(".like", "node => node.innerText") == "100"
assert await tweet_handle.eval_on_selector(".retweets", "node => node.innerText") = "10"
```

## element_handle.eval_on_selector_all(selector, expression, **kwargs)<a name="element-handle-eval-on-selector-all">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="element-handle-eval-on-selector-all-option-selector">#</a>
- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="element-handle-eval-on-selector-all-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="element-handle-eval-on-selector-all-option-arg">#</a>
- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="element-handle-eval-on-selector-all-return">#</a>

返回表达式的返回值.

The method finds all elements matching the specified selector in the `ElementHandle`'s subtree and passes an array of matched elements as a first argument to `expression`. See [Working with selectors](https://playwright.dev/python/docs/selectors) for more details.

如果`expression`返回[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)，那么 [element_handle.eval_on_selector_all(selector, expression, **kwargs)](#element-handle-eval-on-selector-all) 将等待promise解析并返回它的值.

Examples:

```html
\<div class="feed">
  \<div class="tweet">Hello!\</div>
  \<div class="tweet">Hi!\</div>
\</div>
```

- Sync

```python
feed_handle = page.query_selector(".feed")
assert feed_handle.eval_on_selector_all(".tweet", "nodes => nodes.map(n => n.innerText)") == ["hello!", "hi!"]
```

- Async

```python
feed_handle = await page.query_selector(".feed")
assert await feed_handle.eval_on_selector_all(".tweet", "nodes => nodes.map(n => n.innerText)") == ["hello!", "hi!"]
```

## element_handle.fill(value, **kwargs)<a name="element-handle-fill">#</a>

- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> Value to set for the `\<input>`, `\<textarea>` or `[contenteditable]` element.<a name="element-handle-fill-option-value">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="element-handle-fill-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="element-handle-fill-option-no-wait-after">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-fill-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-fill-return">#</a>

这个方法等待[可操作性](https://playwright.dev/python/docs/actionability)检查，聚焦元素，填充它，并在填充后触发一个输入事件。请注意，您可以传递一个空字符串来清除输入字段.

如果目标元素不是 `\<input>`, `\<textarea>` or `[contenteditable]`, 此方法将抛出一个错误。但是，如果该元素位于`\<label>`元素中，且该元素具有关联控件，则该控件将被填充.

To send fine-grained keyboard events, use [element_handle.type(text, **kwargs)](#element-handle-type).

## element_handle.focus()<a name="element-handle-focus">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-focus-return">#</a>

Calls [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on the element.

## element_handle.get_attribute(name)<a name="element-handle-get-attribute">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 属性名.<a name="element-handle-get-attribute-option-name">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="element-handle-get-attribute-return">#</a>

返回元素属性值.

## element_handle.hover(**kwargs)<a name="element-handle-hover">#</a>

- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="element-handle-hover-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="element-handle-hover-option-modifiers">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="element-handle-hover-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-hover-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="element-handle-hover-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-hover-return">#</a>

该方法通过执行以下步骤悬停在元素上:

1. 等待元素的[可操作性](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项.
2. 如果需要，将元素滚动到视图中.
3. 使鼠标停在元素中心或指定位置上.
4. 等待发起的导航成功或失败，除非设置了`noWaitAfter`选项.

如果元素在动作期间的任何时刻与DOM分离，此方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## element_handle.inner_html()<a name="element-handle-inner-html">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="element-handle-inner-html-return">#</a>

Returns the `element.innerHTML`.

## element_handle.inner_text()<a name="element-handle-inner-text">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="element-handle-inner-text-return">#</a>

Returns the `element.innerText`.

## element_handle.input_value(**kwargs)<a name="element-handle-input-value">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-input-value-option-timeout">#</a>
- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="element-handle-input-value-return">#</a>

返回输入 `\<input>` or `\<textarea>` or `\<select>`  元素的值, 排除非输入元素.

## element_handle.is_checked()<a name="element-handle-is-checked">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="element-handle-is-checked-return">#</a>

返回元素是否被选中。如果元素不是复选框或单选输入则排除.

## element_handle.is_disabled()<a name="element-handle-is-disabled">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="element-handle-is-disabled-return">#</a>

返回该元素是否被禁用，与启用[enabled](https://playwright.dev/python/docs/actionability#enabled)相反.

## element_handle.is_editable()<a name="element-handle-is-editable">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="element-handle-is-editable-return">#</a>

返回元素是否可编辑[editable](https://playwright.dev/python/docs/actionability#editable).

## element_handle.is_enabled()<a name="element-handle-is-enabled">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="element-handle-is-enabled-return">#</a>

返回元素是否被启用[enabled](https://playwright.dev/python/docs/actionability#enabled).

## element_handle.is_hidden()<a name="element-handle-is-hidden">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="element-handle-is-hidden-return">#</a>

返回元素是否隐藏，与可见 [visible](https://playwright.dev/python/docs/actionability#visible)相反.

## element_handle.is_visible()<a name="element-handle-is-visible">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="element-handle-is-visible-return">#</a>

返回元素是否可见[visible](https://playwright.dev/python/docs/actionability#visible).

## element_handle.owner_frame()<a name="element-handle-owner-frame">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Frame](#frame)><a name="element-handle-owner-frame-return">#</a>

Returns the frame containing the given element.

## element_handle.press(key, **kwargs)<a name="element-handle-press">#</a>

- `key` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要按下的`键名`或要生成的字符，如`ArrowLeft`或'a'.<a name="element-handle-press-option-key">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `keydown`和`keyup`之间的等待时间，单位是毫秒。默认为0.<a name="element-handle-press-option-delay">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="element-handle-press-option-no-wait-after">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-press-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-press-return">#</a>

聚焦元素，然后使用 [keyboard.down(key)](#keyboard-down) and [keyboard.up(key)](#keyboard-up).

key可以指定想要的 [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) 或是单个字符生成的文本,这里可以找到键值的超集。键的例子如下:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

还支持以下快捷键:`Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

按住`Shift`键将输入与大写键对应的文本.

如果`key`是单个字符，它是区分大小写的，因此值`a`和`A`将生成不同的文本.

也支持快捷键，如键:“Control+o”或键:“Control+Shift+T”。当用修饰符指定时，修饰符被按下并被保持，而随后的键被按下.

## element_handle.query_selector(selector)<a name="element-handle-query-selector">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="element-handle-query-selector-option-selector">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[ElementHandle](#elementhandle)><a name="element-handle-query-selector-return">#</a>

The method finds an element matching the specified selector in the `ElementHandle`'s subtree. See [Working with selectors](https://playwright.dev/python/docs/selectors) for more details. If no elements match the selector, returns `null`.

## element_handle.query_selector_all(selector)<a name="element-handle-query-selector-all">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="element-handle-query-selector-all-option-selector">#</a>
- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[ElementHandle](#elementhandle)]><a name="element-handle-query-selector-all-return">#</a>

The method finds all elements matching the specified selector in the `ElementHandle`s subtree. See [Working with selectors](https://playwright.dev/python/docs/selectors) for more details. If no elements match the selector, returns empty array.

## element_handle.screenshot(**kwargs)<a name="element-handle-screenshot">#</a>

- `animations` \<"disabled"> 当设置为`"disabled"`时，停止CSS动画，CSS转换和Web动画。动画根据其持续时间得到不同的处理:<a name="element-handle-screenshot-option-animations">#</a>
    - 有限动画是快进到完成，所以他们会触发`transitionend`事件.
    - 无限动画被取消到初始状态，然后在屏幕截图后播放.
- `mask` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Locator](#locator)]> 指定在截屏时应该被屏蔽的定位器。被屏蔽的元素将被一个粉红色的框覆盖#FF00FF，完全覆盖该元素.<a name="element-handle-screenshot-option-mask">#</a>
- `omit_background` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 隐藏默认的白色背景，并允许透明捕捉屏幕截图。不适用于`jpeg`图像。默认值为`false`.<a name="element-handle-screenshot-option-omit-background">#</a>
- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 保存镜像的文件路径, 屏幕截图类型将从文件扩展名推断。如果path是一个相对路径，那么它是相对于当前工作目录解析的。如果没有提供路径，映像将不会被保存到磁盘.<a name="element-handle-screenshot-option-path">#</a>
- `quality` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 图像的质量，在0-100之间。不适用于png图像.<a name="element-handle-screenshot-option-quality">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-screenshot-option-timeout">#</a>
- `type` \<"png"|"jpeg">指定截图类型，默认为`png`.<a name="element-handle-screenshot-option-type">#</a>
- returns: \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)><a name="element-handle-screenshot-return">#</a>

返回带有捕获的截图的缓冲区.

这个方法等待[可操作性](https://playwright.dev/python/docs/actionability)检查，然后在截屏之前将元素滚动到视图中。如果元素与DOM分离，该方法将抛出一个错误.

## element_handle.scroll_into_view_if_needed(**kwargs)<a name="element-handle-scroll-into-view-if-needed">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-scroll-into-view-if-needed-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-scroll-into-view-if-needed-return">#</a>

这个方法等待[可操作性](https://playwright.dev/python/docs/actionability)检查，然后尝试滚动元素到视图中，除非它是完全可见的，由 [IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)的比率定义.

Throws when `elementHandle` does not point to an element [connected](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected) to a Document or a ShadowRoot.

## element_handle.select_option(**kwargs)<a name="element-handle-select-option">#</a>

- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="element-handle-select-option-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="element-handle-select-option-option-no-wait-after">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-select-option-option-timeout">#</a>
- `element` \<[ElementHandle](#elementhandle)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[ElementHandle](#elementhandle)]> 要选择的选项。可选的.<a name="element-handle-select-option-option-element">#</a>
- `index` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)]> 按索引进行选择的选项。可选的.<a name="element-handle-select-option-option-index">#</a>
- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 按值选择的选项。如果`\<select>`具有多个属性，则选择所有给定的选项，否则只选择与传递的选项之一匹配的第一个选项。可选的.<a name="element-handle-select-option-option-value">#</a>
- `label` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 按标签进行选择的选项。如果`\<select>`具有多个属性，则选择所有给定的选项，否则只选择与传递的选项之一匹配的第一个选项。可选的.<a name="element-handle-select-option-option-label">#</a>
- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]><a name="element-handle-select-option-return">#</a>

这个方法等待[可操作性](https://playwright.dev/python/docs/actionability)检查，直到所有指定的选项都出现在`\<select>`元素中，然后选择这些选项.

如果目标元素不是`\<select>`元素，此方法将抛出一个错误。但是，如果该元素位于`\<label>`元素中，且该元素具有关联控件，则将使用该控件.

Returns the array of option values that have been successfully selected.

一旦选择了所有提供的选项，就触发一个更改和输入事件.

- Sync

```python
# single selection matching the value
handle.select_option("blue")
# single selection matching both the label
handle.select_option(label="blue")
# multiple selection
handle.select_option(value=["red", "green", "blue"])
```

- Async

```python
# single selection matching the value
await handle.select_option("blue")
# single selection matching the label
await handle.select_option(label="blue")
# multiple selection
await handle.select_option(value=["red", "green", "blue"])
```

```python
# sync

# single selection matching the value
handle.select_option("blue")
# single selection matching both the value and the label
handle.select_option(label="blue")
# multiple selection
handle.select_option("red", "green", "blue")
# multiple selection for blue, red and second option
handle.select_option(value="blue", { index: 2 }, "red")
```

## element_handle.select_text(**kwargs)<a name="element-handle-select-text">#</a>

- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="element-handle-select-text-option-force">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-select-text-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-select-text-return">#</a>

这个方法等待[可操作性](https://playwright.dev/python/docs/actionability)检查, then focuses the element and selects all its text content.

## element_handle.set_checked(checked, **kwargs)<a name="element-handle-set-checked">#</a>

- `checked` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否选中或不选中复选框.<a name="element-handle-set-checked-option-checked">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="element-handle-set-checked-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="element-handle-set-checked-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="element-handle-set-checked-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-set-checked-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="element-handle-set-checked-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-set-checked-return">#</a>

这个方法通过执行以下步骤检查或取消检查一个元素:

1. Ensure that element is a checkbox or a radio input. If not, this method throws.
2. 如果元素已经具有正确的选中状态，则该方法立即返回.
3. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
4. 如果需要，将元素滚动到视图中.
5. 使用 [page.mouse](#page-mouse) 单击元素的中心.
6. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.
7. 确保元素现在被选中或取消选中。如果不是，则抛出此方法.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## element_handle.set_input_files(files, **kwargs)<a name="element-handle-set-input-files">#</a>

- `files` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]|[List](https://docs.python.org/3/library/typing.html#typing.List)[[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]><a name="element-handle-set-input-files-option-files">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> File name
    - `mimeType` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> File type
    - `buffer` \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> File content
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="element-handle-set-input-files-option-no-wait-after">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-set-input-files-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-set-input-files-return">#</a>

This method expects `elementHandle` to point to an [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

将文件输入的值设置为这些文件路径或文件。如果某些`filepath`是相对路径，那么它们将相对于当前工作目录进行解析。对于空数组，清除选定的文件.

## element_handle.tap(**kwargs)<a name="element-handle-tap">#</a>

- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="element-handle-tap-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="element-handle-tap-option-modifiers">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="element-handle-tap-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="element-handle-tap-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-tap-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="element-handle-tap-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-tap-return">#</a>

这个方法通过执行以下步骤点击元素:

1. 等待元素的[可操作性](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项.
2. 如果需要，将元素滚动到视图中.
3. 点击页面中心或指定位置.
4. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.

如果元素在动作期间的任何时刻与DOM分离，此方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

> NOTE
>
> `elementHandle.tap()` requires that the `hasTouch` option of the browser context be set to true.

## element_handle.text_content()<a name="element-handle-text-content">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="element-handle-text-content-return">#</a>

Returns the `node.textContent`.

## element_handle.type(text, **kwargs)<a name="element-handle-type">#</a>

- `text` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要输入到焦点元素中的文本.<a name="element-handle-type-option-text">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 按键之间的等待时间，单位是毫秒。默认为0.<a name="element-handle-type-option-delay">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="element-handle-type-option-no-wait-after">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-type-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-type-return">#</a>

聚焦元素，然后为文本中的每个字符发送 `keydown`, `keypress`/`input`, and `keyup`  事件.

To press a special key, like `Control` or `ArrowDown`, use [element_handle.press(key, **kwargs)](#element-handle-press).

- Sync

```python
element_handle.type("hello") # types instantly
element_handle.type("world", delay=100) # types slower, like a user
```

- Async

```python
await element_handle.type("hello") # types instantly
await element_handle.type("world", delay=100) # types slower, like a user
```

An example of typing into a text field and then submitting the form:

- Sync

```python
element_handle = page.query_selector("input")
element_handle.type("some text")
element_handle.press("Enter")
```

- Async

```python
element_handle = await page.query_selector("input")
await element_handle.type("some text")
await element_handle.press("Enter")
```

## element_handle.uncheck(**kwargs)<a name="element-handle-uncheck">#</a>

- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="element-handle-uncheck-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="element-handle-uncheck-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="element-handle-uncheck-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-uncheck-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="element-handle-uncheck-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-uncheck-return">#</a>

这个方法通过执行以下步骤来检查元素:

1. 确保元素是一个复选框或单选输入。如果不是，则抛出此方法。如果元素已被选中，则此方法立即返回.
2. 等待元素的[可操作性](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项.
3. 如果需要，将元素滚动到视图中.
4. 使用 [page.mouse](#page-mouse) 单击元素的中心.
5. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.
6. 确保元素现在是未选中的。如果不是，则排除此方法.

如果元素在动作期间的任何时刻与DOM分离，此方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## element_handle.wait_for_element_state(state, **kwargs)<a name="element-handle-wait-for-element-state">#</a>

- `state` \<"visible"|"hidden"|"stable"|"enabled"|"disabled"|"editable"> A state to wait for, see below for more details.<a name="element-handle-wait-for-element-state-option-state">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-wait-for-element-state-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="element-handle-wait-for-element-state-return">#</a>

Returns when the element satisfies the `state`.

Depending on the `state` parameter, this method waits for one of the [actionability](https://playwright.dev/python/docs/actionability) checks to pass. This method throws when the element is detached while waiting, unless waiting for the `"hidden"` state.

- `"visible"` Wait until the element is [visible](https://playwright.dev/python/docs/actionability#visible).
- `"hidden"` Wait until the element is [not visible](https://playwright.dev/python/docs/actionability#visible) or [not attached](https://playwright.dev/python/docs/actionability#attached). Note that waiting for hidden does not throw when the element detaches.
- `"stable"` Wait until the element is both [visible](https://playwright.dev/python/docs/actionability#visible) and [stable](https://playwright.dev/python/docs/actionability#stable).
- `"enabled"` Wait until the element is [enabled](https://playwright.dev/python/docs/actionability#enabled).
- `"disabled"` Wait until the element is [not enabled](https://playwright.dev/python/docs/actionability#enabled).
- `"editable"` Wait until the element is [editable](https://playwright.dev/python/docs/actionability#editable).

If the element does not satisfy the condition for the `timeout` milliseconds, this method will throw.

## element_handle.wait_for_selector(selector, **kwargs)<a name="element-handle-wait-for-selector">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="element-handle-wait-for-selector-option-selector">#</a>
- `state` \<"attached"|"detached"|"visible"|"hidden"> 默认为`"visible"`。可以是:<a name="element-handle-wait-for-selector-option-state">#</a>
    - `'attached'` - 等待元素出现在DOM中.
    - `'detached'` - 等待元素在DOM中不存在.
    - `'visible'` - 等待元素有非空的边界框 且 没有 `visibility:hidden`.注意，没有任何内容或带有`display:none` 的元素有一个空的边界框，因此不被认为是可见的.
    - `'hidden'` - 等待元素从DOM中分离出来, 或有一个空的边界框或' visibility:hidden '。这与`“visible”`选项相反.
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="element-handle-wait-for-selector-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="element-handle-wait-for-selector-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[ElementHandle](#elementhandle)><a name="element-handle-wait-for-selector-return">#</a>

Returns element specified by selector when it satisfies `state` option. Returns `null` if waiting for `hidden` or `detached`.

Wait for the `selector` relative to the element handle to satisfy `state` option (either appear/disappear from dom, or become visible/hidden). If at the moment of calling the method `selector` already satisfies the condition, the method will return immediately. If the selector doesn't satisfy the condition for the `timeout` milliseconds, the function will throw.

- Sync

```python
page.set_content("\<div>\<span>\</span>\</div>")
div = page.query_selector("div")
# waiting for the "span" selector relative to the div.
span = div.wait_for_selector("span", state="attached")
```

- Async

```python
await page.set_content("\<div>\<span>\</span>\</div>")
div = await page.query_selector("div")
# waiting for the "span" selector relative to the div.
span = await div.wait_for_selector("span", state="attached")
```

> NOTE
>
> This method does not work across navigations, use [page.wait_for_selector(selector, **kwargs)](#page-wait-for-selector) instead.





# Error

- extends: [Exception](https://docs.python.org/3/library/exceptions.html#Exception)

当某些操作异常终止时将引发错误，例如浏览器在运行时关闭 [page.evaluate(expression, **kwargs)](#page-evaluate),  所有playwright 的 Exception都继承自这个类

- [error.message](#error-message)
- [error.name](#error-name)
- [error.stack](#error-stack)

## error.message<a name="error-message">#</a>

- type: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>

错误消息.

## error.name<a name="error-name">#</a>

- type: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>

浏览器内部抛出的错误的名称。可选的.

## error.stack<a name="error-stack">#</a>

- type: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>

浏览器内部抛出的错误堆栈。可选的.



# FileChooser

[FileChooser](#filechooser) 对象由 [page.on("filechooser")](#page-event-file-chooser) 事件中的页面调度.

- Sync

```python
with page.expect_file_chooser() as fc_info:
    page.click("upload")
file_chooser = fc_info.value
file_chooser.set_files("myfile.pdf")
```

- Async

```python
async with page.expect_file_chooser() as fc_info:
    await page.click("upload")
file_chooser = await fc_info.value
await file_chooser.set_files("myfile.pdf")
```

- [file_chooser.element](#file-chooser-element)
- [file_chooser.is_multiple()](#file-chooser-is-multiple)
- [file_chooser.page](#file-chooser-page)
- [file_chooser.set_files(files, **kwargs)](#file-chooser-set-files)

## file_chooser.element<a name="file-chooser-element">#</a>

- returns: \<[ElementHandle](#elementhandle)><a name="file-chooser-element-return">#</a>

返回与此文件选择器关联的输入元素.

## file_chooser.is_multiple()<a name="file-chooser-is-multiple">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="file-chooser-is-multiple-return">#</a>

返回此文件选择器是否接受多个文件.

## file_chooser.page<a name="file-chooser-page">#</a>

- returns: \<[Page](#page)><a name="file-chooser-page-return">#</a>

返回此文件选择器所属的页面.

## file_chooser.set_files(files, **kwargs)<a name="file-chooser-set-files">#</a>

- `files` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]|[List](https://docs.python.org/3/library/typing.html#typing.List)[[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]><a name="file-chooser-set-files-option-files">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件名
    - `mimeType` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件类型
    - `buffer` \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> 文件内容
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为 `false`.<a name="file-chooser-set-files-option-no-wait-after">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="file-chooser-set-files-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="file-chooser-set-files-return">#</a>

设置与此选择器关联的文件输入的值。如果某些 `filePaths` 是相对路径，那么它们将相对于当前工作目录进行解析。对于空数组，清除选定的文件.



# Frame

在每个时间点，页面都会通过 [page.main_frame](#page-main-frame) and [frame.child_frames](#frame-child-frames) 方法.

[Frame](#frame) 对象的生命周期由三个事件控制，在页面对象中分配:

- [page.on("frameattached")](#page-event-frame-attached) - 当框架被附加到页面时触发. 一个框架只能附加到页面一次.
- [page.on("framenavigated")](#page-event-frame-navigated) -当帧提交导航到另一个URL时触发
- [page.on("framedetached")](#page-event-frame-detached) - 当框架从页面分离时触发. Frame只能从页面分离一次.

一个倾倒框架树的例子:

- Sync

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    firefox = playwright.firefox
    browser = firefox.launch()
    page = browser.new_page()
    page.goto("https://www.theverge.com")
    dump_frame_tree(page.main_frame, "")
    browser.close()

def dump_frame_tree(frame, indent):
    print(indent + frame.name + '@' + frame.url)
    for child in frame.child_frames:
        dump_frame_tree(child, indent + "    ")

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    firefox = playwright.firefox
    browser = await firefox.launch()
    page = await browser.new_page()
    await page.goto("https://www.theverge.com")
    dump_frame_tree(page.main_frame, "")
    await browser.close()

def dump_frame_tree(frame, indent):
    print(indent + frame.name + '@' + frame.url)
    for child in frame.child_frames:
        dump_frame_tree(child, indent + "    ")

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

- [frame.add_script_tag(**kwargs)](#frame-add-script-tag)
- [frame.add_style_tag(**kwargs)](#frame-add-style-tag)
- [frame.check(selector, **kwargs)](#frame-check)
- [frame.child_frames](#frame-child-frames)
- [frame.click(selector, **kwargs)](#frame-click)
- [frame.content()](#frame-content)
- [frame.dblclick(selector, **kwargs)](#frame-dblclick)
- [frame.dispatch_event(selector, type, **kwargs)](#frame-dispatch-event)
- [frame.drag_and_drop(source, target, **kwargs)](#frame-drag-and-drop)
- [frame.eval_on_selector(selector, expression, **kwargs)](#frame-eval-on-selector)
- [frame.eval_on_selector_all(selector, expression, **kwargs)](#frame-eval-on-selector-all)
- [frame.evaluate(expression, **kwargs)](#frame-evaluate)
- [frame.evaluate_handle(expression, **kwargs)](#frame-evaluate-handle)
- [frame.expect_navigation(**kwargs)](#frame-wait-for-navigation)
- [frame.fill(selector, value, **kwargs)](#frame-fill)
- [frame.focus(selector, **kwargs)](#frame-focus)
- [frame.frame_element()](#frame-frame-element)
- [frame.frame_locator(selector)](#frame-frame-locator)
- [frame.get_attribute(selector, name, **kwargs)](#frame-get-attribute)
- [frame.goto(url, **kwargs)](#frame-goto)
- [frame.hover(selector, **kwargs)](#frame-hover)
- [frame.inner_html(selector, **kwargs)](#frame-inner-html)
- [frame.inner_text(selector, **kwargs)](#frame-inner-text)
- [frame.input_value(selector, **kwargs)](#frame-input-value)
- [frame.is_checked(selector, **kwargs)](#frame-is-checked)
- [frame.is_detached()](#frame-is-detached)
- [frame.is_disabled(selector, **kwargs)](#frame-is-disabled)
- [frame.is_editable(selector, **kwargs)](#frame-is-editable)
- [frame.is_enabled(selector, **kwargs)](#frame-is-enabled)
- [frame.is_hidden(selector, **kwargs)](#frame-is-hidden)
- [frame.is_visible(selector, **kwargs)](#frame-is-visible)
- [frame.locator(selector, **kwargs)](#frame-locator)
- [frame.name](#frame-name)
- [frame.page](#frame-page)
- [frame.parent_frame](#frame-parent-frame)
- [frame.press(selector, key, **kwargs)](#frame-press)
- [frame.query_selector(selector, **kwargs)](#frame-query-selector)
- [frame.query_selector_all(selector)](#frame-query-selector-all)
- [frame.select_option(selector, **kwargs)](#frame-select-option)
- [frame.set_checked(selector, checked, **kwargs)](#frame-set-checked)
- [frame.set_content(html, **kwargs)](#frame-set-content)
- [frame.set_input_files(selector, files, **kwargs)](#frame-set-input-files)
- [frame.tap(selector, **kwargs)](#frame-tap)
- [frame.text_content(selector, **kwargs)](#frame-text-content)
- [frame.title()](#frame-title)
- [frame.type(selector, text, **kwargs)](#frame-type)
- [frame.uncheck(selector, **kwargs)](#frame-uncheck)
- [frame.url](#frame-url)
- [frame.wait_for_function(expression, **kwargs)](#frame-wait-for-function)
- [frame.wait_for_load_state(**kwargs)](#frame-wait-for-load-state)
- [frame.wait_for_selector(selector, **kwargs)](#frame-wait-for-selector)
- [frame.wait_for_timeout(timeout)](#frame-wait-for-timeout)
- [frame.wait_for_url(url, **kwargs)](#frame-wait-for-url)

## frame.add_script_tag(**kwargs)<a name="frame-add-script-tag">#</a>

- `content` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要注入帧的原始JavaScript内容.<a name="frame-add-script-tag-option-content">#</a>
- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 要注入帧的JavaScript文件的路径,如果`path`是一个相对路径，那么它是相对于当前工作目录解析的.<a name="frame-add-script-tag-option-path">#</a>
- `type` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 脚本类型。使用“module”来加载一个Javascript ES6模块。详情请参阅 [script](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) .<a name="frame-add-script-tag-option-type">#</a>
- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要添加的脚本的url.<a name="frame-add-script-tag-option-url">#</a>
- returns: \<[ElementHandle](#elementhandle)><a name="frame-add-script-tag-return">#</a>

当脚本的onload触发或脚本内容被注入帧时，返回添加的标签.

添加一个 `\<script>` 标签到页面所需的url或内容.

## frame.add_style_tag(**kwargs)<a name="frame-add-style-tag">#</a>

- `content` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 原始的CSS内容注入到帧.<a name="frame-add-style-tag-option-content">#</a>
- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 要注入帧的CSS文件的路径, 如果path是一个相对路径，那么它是相对于当前工作目录解析的.<a name="frame-add-style-tag-option-path">#</a>
- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> `\<link>`标签的url.<a name="frame-add-style-tag-option-url">#</a>
- returns: \<[ElementHandle](#elementhandle)><a name="frame-add-style-tag-return">#</a>

当样式表的onload触发时，或者当CSS内容被注入框架时，返回添加的标签.

添加一个 `\<link rel="stylesheet">` 标签到页面所需的url或 `\<style type="text/css">`标签的内容.

## frame.check(selector, **kwargs)<a name="frame-check">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-check-option-selector">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="frame-check-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="frame-check-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="frame-check-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-check-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-check-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="frame-check-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-check-return">#</a>

这个方法通过以下步骤检查元素匹配选择器:

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 确保匹配的元素是一个复选框或单选输入。如果不是，则排除此方法。如果元素已被选中，则该方法立即返回.
3. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
4. 如果需要，将元素滚动到视图中.
5. 使用 [page.mouse](#page-mouse) 单击元素的中心.
6. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.
7. 确保元素现在被选中。如果不是，则排除此方法.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## frame.child_frames<a name="frame-child-frames">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Frame](#frame)]><a name="frame-child-frames-return">#</a>

## frame.click(selector, **kwargs)<a name="frame-click">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-click-option-selector">#</a>
- `button` \<"left"|"right"|"middle"> 默认左 `left`.<a name="frame-click-option-button">#</a>
- `click_count` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 默认为1. 查看[UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail).<a name="frame-click-option-click-count">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `mousedown`和`mouseup`之间的等待时间，单位是毫秒。默认为0.<a name="frame-click-option-delay">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="frame-click-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="frame-click-option-modifiers">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="frame-click-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="frame-click-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-click-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-click-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="frame-click-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-click-return">#</a>

这个方法通过执行以下步骤点击元素匹配选择器:

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
3. 如果需要，将元素滚动到视图中.
4. 使用 [page.mouse](#page-mouse) 单击元素的中心, or the specified `position`.
5. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## frame.content()<a name="frame-content">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="frame-content-return">#</a>

获取框架的完整HTML内容，包括文档类型.

## frame.dblclick(selector, **kwargs)<a name="frame-dblclick">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-dblclick-option-selector">#</a>
- `button` \<"left"|"right"|"middle"> 默认左 `left`.<a name="frame-dblclick-option-button">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `mousedown`和`mouseup`之间的等待时间，单位是毫秒。默认为0.<a name="frame-dblclick-option-delay">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="frame-dblclick-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="frame-dblclick-option-modifiers">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="frame-dblclick-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="frame-dblclick-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-dblclick-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-dblclick-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="frame-dblclick-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-dblclick-return">#</a>

该方法通过执行以下步骤双击元素匹配选择器:

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
3. 如果需要，将元素滚动到视图中.
4. 使用 [page.mouse](#page-mouse) 方法,双击元素中心位置.
5. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.该方法执行以下步骤双击元素, 注意，如果`dblclick()`的第一次单击触发了一个导航事件，则该方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

> NOTE
>
> `frame.dblclick()` 分发两个`click`事件和一个`dblclick`事件.

## frame.dispatch_event(selector, type, **kwargs)<a name="frame-dispatch-event">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-dispatch-event-option-selector">#</a>
- `type` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> DOM事件类型:`"click"`， `"dragstart"`等.<a name="frame-dispatch-event-option-type">#</a>
- `event_init` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 可选的特定于事件的初始化属性.<a name="frame-dispatch-event-option-event-init">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-dispatch-event-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-dispatch-event-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-dispatch-event-return">#</a>

下面的代码片段分派元素上的`单击`事件。无论元素的可见性状态如何，单击都将被分派。这相当于调用[element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

- Sync

```python
frame.dispatch_event("button#submit", "click")
```

- Async

```python
await frame.dispatch_event("button#submit", "click")
```

在底层，它根据给定的类型创建一个事件实例，使用`event_init`属性初始化它，并在元素上分派它。默认情况下，事件是组合的、可取消的和冒泡的.

由于`event_init`是特定于事件的，请参考事件文档中的初始属性列表:

- [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
- [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
- [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
- [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
- [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
- [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
- [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)

如果你想要将活动对象传递到事件中，你也可以指定`jhandle`作为属性值:

- Sync

```python
# note you can only create data_transfer in chromium and firefox
data_transfer = frame.evaluate_handle("new DataTransfer()")
frame.dispatch_event("#source", "dragstart", { "dataTransfer": data_transfer })
```

- Async

```python
# note you can only create data_transfer in chromium and firefox
data_transfer = await frame.evaluate_handle("new DataTransfer()")
await frame.dispatch_event("#source", "dragstart", { "dataTransfer": data_transfer })
```

## frame.drag_and_drop(source, target, **kwargs)<a name="frame-drag-and-drop">#</a>

- `source` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="frame-drag-and-drop-option-source">#</a>
- `target` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="frame-drag-and-drop-option-target">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="frame-drag-and-drop-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="frame-drag-and-drop-option-no-wait-after">#</a>
- `source_position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 此时相对于元素填充框的左上角单击源元素。如果没有指定，则使用元素的某个可见点.<a name="frame-drag-and-drop-option-source-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-drag-and-drop-option-strict">#</a>
- `target_position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 此时相对于元素填充框的左上角落在目标元素上。如果没有指定，则使用元素的某个可见点.<a name="frame-drag-and-drop-option-target-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-drag-and-drop-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="frame-drag-and-drop-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-drag-and-drop-return">#</a>

## frame.eval_on_selector(selector, expression, **kwargs)<a name="frame-eval-on-selector">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="frame-eval-on-selector-option-selector">#</a>
- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="frame-eval-on-selector-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="frame-eval-on-selector-option-arg">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-eval-on-selector-option-strict">#</a>
- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="frame-eval-on-selector-return">#</a>

返回表达式的返回值.

> CAUTION
>
> 此方法不等待元素通过可操作性检查，因此可能导致不稳定的测试 . 使用[locator.evaluate(expression, **kwargs)](#locator-evaluate), 其它[Locator](#locator) 方法优先断言

该方法在框架中找到与指定选择器匹配的元素，并将其作为第一个参数传递给表达式。有关详细信息，请参阅 [Working with selectors](https://playwright.dev/python/docs/selectors)。如果没有匹配该选择器的元素，该方法将抛出错误

如果`expression` 返回 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 那么[frame.eval_on_selector(selector, expression, **kwargs)](#frame-eval-on-selector) 将等待promise解析并返回它的值.

例子:

- Sync

```python
search_value = frame.eval_on_selector("#search", "el => el.value")
preload_href = frame.eval_on_selector("link[rel=preload]", "el => el.href")
html = frame.eval_on_selector(".main-container", "(e, suffix) => e.outerHTML + suffix", "hello")
```

- Async

```python
search_value = await frame.eval_on_selector("#search", "el => el.value")
preload_href = await frame.eval_on_selector("link[rel=preload]", "el => el.href")
html = await frame.eval_on_selector(".main-container", "(e, suffix) => e.outerHTML + suffix", "hello")
```

## frame.eval_on_selector_all(selector, expression, **kwargs)<a name="frame-eval-on-selector-all">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="frame-eval-on-selector-all-option-selector">#</a>
- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="frame-eval-on-selector-all-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="frame-eval-on-selector-all-option-arg">#</a>
- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="frame-eval-on-selector-all-return">#</a>

返回表达式的返回值.

> NOTE
>
> 在大多数情况下, [locator.evaluate_all(expression, **kwargs)](#locator-evaluate-all), 其它[Locator](#locator) 做得更好.

该方法在框架中查找与指定选择器匹配的所有元素，并将匹配元素的数组作为第一个参数传递给表达式。有关详细信息，请参阅[Working with selectors](https://playwright.dev/python/docs/selectors)

如果`expression` 返回 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 那么[frame.eval_on_selector(selector, expression, **kwargs)](#frame-eval-on-selector) 将等待promise解析并返回它的值.

例子:

- Sync

```python
divs_counts = frame.eval_on_selector_all("div", "(divs, min) => divs.length >= min", 10)
```

- Async

```python
divs_counts = await frame.eval_on_selector_all("div", "(divs, min) => divs.length >= min", 10)
```

## frame.evaluate(expression, **kwargs)<a name="frame-evaluate">#</a>

- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="frame-evaluate-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="frame-evaluate-option-arg">#</a>
- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="frame-evaluate-return">#</a>

返回表达式的返回值.

如果函数传递给 [frame.evaluate(expression, **kwargs)](#frame-evaluate) 返回 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 那么[frame.evaluate(expression, **kwargs)](#frame-evaluate) 将等待promise解析并返回其值.

如果函数传递给 [frame.evaluate(expression, **kwargs)](#frame-evaluate) 返回一个不可序列化的值-[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description) , 那么[frame.evaluate(expression, **kwargs)](#frame-evaluate) 返回`undefined`. Playwright 还支持传递一些附加值，不能通过`JSON`序列化 : `-0`, `NaN`, `Infinity`, `-Infinity`.

- Sync

```python
result = frame.evaluate("([x, y]) => Promise.resolve(x * y)", [7, 8])
print(result) # prints "56"
```

- Async

```python
result = await frame.evaluate("([x, y]) => Promise.resolve(x * y)", [7, 8])
print(result) # prints "56"
```

字符串也可以代替函数传入.

- Sync

```python
print(frame.evaluate("1 + 2")) # prints "3"
x = 10
print(frame.evaluate(f"1 + {x}")) # prints "11"
```

- Async

```python
print(await frame.evaluate("1 + 2")) # prints "3"
x = 10
print(await frame.evaluate(f"1 + {x}")) # prints "11"
```

可以将 [ElementHandle](#elementhandle) 实例作为参数传递给框架 [frame.evaluate(expression, **kwargs)](#frame-evaluate):

- Sync

```python
body_handle = frame.evaluate("document.body")
html = frame.evaluate("([body, suffix]) => body.innerHTML + suffix", [body_handle, "hello"])
body_handle.dispose()
```

- Async

```python
body_handle = await frame.evaluate("document.body")
html = await frame.evaluate("([body, suffix]) => body.innerHTML + suffix", [body_handle, "hello"])
await body_handle.dispose()
```

## frame.evaluate_handle(expression, **kwargs)<a name="frame-evaluate-handle">#</a>

- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="frame-evaluate-handle-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="frame-evaluate-handle-option-arg">#</a>
- returns: \<[JSHandle](#jshandle)><a name="frame-evaluate-handle-return">#</a>

返回表达式的返回值是 [JSHandle](#jshandle).

框架之间唯一的区别 [frame.evaluate(expression, **kwargs)](#frame-evaluate) 和 [frame.evaluate_handle(expression, **kwargs)](#frame-evaluate-handle) 是 [frame.evaluate_handle(expression, **kwargs)](#frame-evaluate-handle) 返回 [JSHandle](#jshandle).

如果函数，传递给 [frame.evaluate_handle(expression, **kwargs)](#frame-evaluate-handle), 返回 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 那么 [frame.evaluate_handle(expression, **kwargs)](#frame-evaluate-handle) 将等待promise解析并返它的.

- Sync

```python
a_window_handle = frame.evaluate_handle("Promise.resolve(window)")
a_window_handle # handle for the window object.
```

- Async

```python
a_window_handle = await frame.evaluate_handle("Promise.resolve(window)")
a_window_handle # handle for the window object.
```

字符串也可以代替函数传入.

- Sync

```python
a_handle = page.evaluate_handle("document") # handle for the "document"
```

- Async

```python
a_handle = await page.evaluate_handle("document") # handle for the "document"
```

[JSHandle](#jshandle) 实例可以作为参数传递给 [frame.evaluate_handle(expression, **kwargs)](#frame-evaluate-handle):

- Sync

```python
a_handle = page.evaluate_handle("document.body")
result_handle = page.evaluate_handle("body => body.innerHTML", a_handle)
print(result_handle.json_value())
result_handle.dispose()
```

- Async

```python
a_handle = await page.evaluate_handle("document.body")
result_handle = await page.evaluate_handle("body => body.innerHTML", a_handle)
print(await result_handle.json_value())
await result_handle.dispose()
```

## frame.expect_navigation(**kwargs)<a name="frame-wait-for-navigation">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>最大操作时间，单位为毫秒，默认为30秒，通过0表示禁止超时。默认值可以通过使用  [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout), [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来修改.<a name="frame-wait-for-navigation-option-timeout">#</a>
- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[URL](https://en.wikipedia.org/wiki/URL)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 一个glob模式、regex模式或谓词，在等待导航时接收匹配的url。注意，如果参数是一个不带通配符的字符串，该方法将等待导航到与该字符串完全相等的URL.<a name="frame-wait-for-navigation-option-url">#</a>
- `wait_until` \<"load"|"domcontentloaded"|"networkidle"|"commit"> 当认为操作成功时，默认为`load`。事件可以是:<a name="frame-wait-for-navigation-option-wait-until">#</a>
    - `'domcontentloaded'` - 当`domcontentloaded`事件被触发时，认为操作已经完成.
    - `'load'` - 当触发`load`事件时，认为操作已经完成.
    - `'networkidle'` - 当至少`500毫秒`没有网络连接时，认为操作已经完成.
    - `'commit'` - 当接收到网络响应并开始加载文档时，认为操作已经完成.
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)[[Response](#response)]><a name="frame-wait-for-navigation-return">#</a>

等待框架导航并返回主资源响应。在多个重定向的情况下，导航将使用最后一个重定向的响应进行解析。如果导航到一个不同的锚或导航由于历史API的使用，导航将解析为`null`.

该方法等待 frame 导航到一个新的URL。当你运行会间接导致框架导航的代码时，它很有用。考虑一下这个例子:

- Sync

```python
with frame.expect_navigation():
    frame.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
# Resolves after navigation has finished
```

- Async

```python
async with frame.expect_navigation():
    await frame.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
# Resolves after navigation has finished
```

> NOTE
>
> 使用 [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) 更改URL被视为导航.

## frame.fill(selector, value, **kwargs)<a name="frame-fill">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-fill-option-selector">#</a>
- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> Value to fill for the `\<input>`, `\<textarea>` or `[contenteditable]` element.<a name="frame-fill-option-value">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="frame-fill-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="frame-fill-option-no-wait-after">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-fill-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-fill-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-fill-return">#</a>

这个方法等待元素匹配`选择器`，等待[actionability](https://playwright.dev/python/docs/actionability)检查，聚焦元素，填充它，并在填充后触发一个输入事件。请注意，您可以`传递`一个空字符串来清除输入字段

如果目标元素不是 `\<input>`, `\<textarea>` 或者`[contenteditable]` 元素，此方法将抛出一个错误。但是，如果该元素位于 `\<label>` 元素中，且该元素具有关联控件，则该控件将被填充.

要发送细粒度的键盘事件，请使用 [frame.type(selector, text, **kwargs)](#frame-type).

## frame.focus(selector, **kwargs)<a name="frame-focus">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-focus-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-focus-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-focus-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-focus-return">#</a>

这个方法获取一个带有选择器的元素并聚焦于它。如果没有元素匹配选择器，该方法将等待，直到匹配元素出现在DOM中

## frame.frame_element()<a name="frame-frame-element">#</a>

- returns: \<[ElementHandle](#elementhandle)><a name="frame-frame-element-return">#</a>

返回与此fram相对应的fram或iframe元素句柄

这与 [element_handle.content_frame()](#element-handle-content-frame) 相反. 注意，返回的句柄实际上属于父 frame.

如果 frame 在 `frameElement()` 返回之前被分离，则此方法将抛出错误.

- Sync

```python
frame_element = frame.frame_element()
content_frame = frame_element.content_frame()
assert frame == content_frame
```

- Async

```python
frame_element = await frame.frame_element()
content_frame = await frame_element.content_frame()
assert frame == content_frame
```

## frame.frame_locator(selector)<a name="frame-frame-locator">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 解析DOM元素时使用的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-frame-locator-option-selector">#</a>
- returns: \<[FrameLocator](#framelocator)><a name="frame-frame-locator-return">#</a>

在使用iframes时，您可以创建一个 frame 定位器，该定位器将进入iframe并允许选择该iframe中的元素。下面的代码片段在id为 `my-frame`的iframe中定位到文本为"Submit"的元素，例如: `\<iframe id="my-frame">`:

- Sync

```python
locator = frame.frame_locator("#my-iframe").locator("text=Submit")
locator.click()
```

- Async

```python
locator = frame.frame_locator("#my-iframe").locator("text=Submit")
await locator.click()
```

## frame.get_attribute(selector, name, **kwargs)<a name="frame-get-attribute">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-get-attribute-option-selector">#</a>
- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 属性名.<a name="frame-get-attribute-option-name">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-get-attribute-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-get-attribute-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="frame-get-attribute-return">#</a>

返回元素属性值.

## frame.goto(url, **kwargs)<a name="frame-goto">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> frame导航到的url。url应该包括协议，例如 `https://`.<a name="frame-goto-option-url">#</a>
- `referer` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> referer头值。如果提供，它将优先于[page.set_extra_http_headers(headers)](#page-set-extra-http-headers)设置的referer头值.<a name="frame-goto-option-referer">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>最大操作时间，单位为毫秒，默认为30秒，通过0表示禁止超时。默认值可以通过使用  [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout), [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来修改.<a name="frame-goto-option-timeout">#</a>
- `wait_until` \<"load"|"domcontentloaded"|"networkidle"|"commit"> 当认为操作成功时，默认为`load`。事件可以是:<a name="frame-goto-option-wait-until">#</a>
    - `'domcontentloaded'` - 当`domcontentloaded`事件被触发时，认为操作已经完成.
    - `'load'` - 当触发`load`事件时，认为操作已经完成.
    - `'networkidle'` - 当至少`500毫秒`没有网络连接时，认为操作已经完成.
    - `'commit'` - 当接收到网络响应并开始加载文档时，认为操作已经完成.
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Response](#response)><a name="frame-goto-return">#</a>

返回主资源响应。在多个重定向的情况下，导航将使用最后一个重定向的响应进行解析

如果以下情况，该方法将抛出一个错误:

- 有一个SSL错误(例如在自签名证书的情况下).
- 目标URL无效.
- 导航过程中超时.
- 远程服务器没有响应或不可达.
- main 资源加载失败.

当远程服务器返回任何有效的HTTP状态码时，该方法不会抛出错误，包括404 " not Found"和500 "Internal server error "。这些响应的状态代码可以通过调用[response.status](#response-status)来获取.

> NOTE
>
> 该方法要么抛出错误，要么返回主资源响应。唯一的例外是导航到`空白`或导航到相同的URL与不同的哈希，这将成功并返回null.

> NOTE
>
> 无头模式不支持PDF文档的导航。参见[upstream issue](https://bugs.chromium.org/p/chromium/issues/detail?id=761295).

## frame.hover(selector, **kwargs)<a name="frame-hover">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-hover-option-selector">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="frame-hover-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="frame-hover-option-modifiers">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="frame-hover-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-hover-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-hover-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="frame-hover-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-hover-return">#</a>

该方法通过执行以下步骤悬停在元素匹配`选择器`上:

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
3. 如果需要，将元素滚动到视图中.
4. 使鼠标停在元素中心或指定位置上.
5. 等待发起的导航成功或失败，除非设置了`noWaitAfter`选项.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## frame.inner_html(selector, **kwargs)<a name="frame-inner-html">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-inner-html-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-inner-html-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-inner-html-option-timeout">#</a>
- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="frame-inner-html-return">#</a>

返回`element.innerHTML`.

## frame.inner_text(selector, **kwargs)<a name="frame-inner-text">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-inner-text-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-inner-text-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-inner-text-option-timeout">#</a>
- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="frame-inner-text-return">#</a>

返回`element.innerText`.

## frame.input_value(selector, **kwargs)<a name="frame-input-value">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-input-value-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-input-value-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-input-value-option-timeout">#</a>
- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="frame-input-value-return">#</a>

返回以下元素的输入值 `\<input>` or `\<textarea>` or `\<select>` .排除非输入元素.

## frame.is_checked(selector, **kwargs)<a name="frame-is-checked">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-is-checked-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-is-checked-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-is-checked-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="frame-is-checked-return">#</a>

返回元素是否被选中。如果元素不是复选框或单选输入则排除.

## frame.is_detached()<a name="frame-is-detached">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="frame-is-detached-return">#</a>

如果 frame 已被分离，则返回 true，否则返回 false.

## frame.is_disabled(selector, **kwargs)<a name="frame-is-disabled">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-is-disabled-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-is-disabled-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-is-disabled-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="frame-is-disabled-return">#</a>

返回该元素是否被禁用，与启用相反 [enabled](https://playwright.dev/python/docs/actionability#enabled).

## frame.is_editable(selector, **kwargs)<a name="frame-is-editable">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-is-editable-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-is-editable-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-is-editable-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="frame-is-editable-return">#</a>

返回元素是否可编辑 [editable](https://playwright.dev/python/docs/actionability#editable).

## frame.is_enabled(selector, **kwargs)<a name="frame-is-enabled">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-is-enabled-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-is-enabled-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-is-enabled-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="frame-is-enabled-return">#</a>

返回元素是否被启用 [enabled](https://playwright.dev/python/docs/actionability#enabled).

## frame.is_hidden(selector, **kwargs)<a name="frame-is-hidden">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-is-hidden-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-is-hidden-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> **DEPRECATED** 此选项将被忽略. [frame.is_hidden(selector, **kwargs)](#frame-is-hidden) 立即返回,不会等待元素被隐藏.<a name="frame-is-hidden-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="frame-is-hidden-return">#</a>

返回元素是否隐藏，与[可见](https://playwright.dev/python/docs/actionability#visible)相反。不匹配任何元素的选择器被认为是隐藏的. 

## frame.is_visible(selector, **kwargs)<a name="frame-is-visible">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-is-visible-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-is-visible-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> **DEPRECATED** 此选项将被忽略. [frame.is_visible(selector, **kwargs)](#frame-is-visible) 立即返回,不会等待元素变得可见.<a name="frame-is-visible-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="frame-is-visible-return">#</a>

返回元素是否[可见](https://playwright.dev/python/docs/actionability#visible)。不匹配任何元素的选择器被认为不可见 

## frame.locator(selector, **kwargs)<a name="frame-locator">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 解析DOM元素时使用的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-locator-option-selector">#</a>

- `has` \<[Locator](#locator)> 对selector选中的元素进行再次匹配, 匹配目标中的子元素, 例如: 匹配子元素的`text=Playwright`的元素  `\<article>\<div>Playwright\</div>\</article>`.<a name="frame-locator-option-has">#</a>

    请注意，外部和内部定位器必须属于同一个 frame. 内部定位器不能包含 [FrameLocator](#framelocator).

- `has_text` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> 匹配包含指定文本的元素，可能在子元素或后代元素中,例如:`"Playwright"` 匹配 `\<article>\<div>Playwright\</div>\</article>`.<a name="frame-locator-option-has-text">#</a>

- returns: \<[Locator](#locator)><a name="frame-locator-return">#</a>

该方法返回一个元素定位器，可用于在frame中执行操作。在执行一个操作之前，Locator被立即解析为元素，因此同一定位器上的一系列操作实际上可以在不同的DOM元素上执行。如果这些动作之间的DOM结构发生了变化，就会发生这种情况.

## frame.name<a name="frame-name">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="frame-name-return">#</a>

返回在标签中指定的 frame 的 name 属性.

如果名称为空，则返回 id 属性.

> NOTE
>
> 这个值在 frame 创建时计算一次，如果属性后来改变，这个值将不会更新.

## frame.page<a name="frame-page">#</a>

- returns: \<[Page](#page)><a name="frame-page-return">#</a>

返回包含此frame的页面.

## frame.parent_frame<a name="frame-parent-frame">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Frame](#frame)><a name="frame-parent-frame-return">#</a>

父frame，如果有的话。分离的frame和主frame返回`null`.

## frame.press(selector, key, **kwargs)<a name="frame-press">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-press-option-selector">#</a>
- `key` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要按下的`键名`或要生成的字符，如`ArrowLeft`或'a'.<a name="frame-press-option-key">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `keydown`和`keyup`之间的等待时间，单位是毫秒。默认为0.<a name="frame-press-option-delay">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="frame-press-option-no-wait-after">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-press-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-press-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-press-return">#</a>

key可以指定想要的 [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) 或是单个字符生成的文本,这里可以找到键值的超集。键的例子如下:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, 等.

还支持以下快捷键:`Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

按住`Shift`键将输入与大写键对应的文本.

如果`key`是单个字符，它是区分大小写的，因此值`a`和`A`将生成不同的文本.

也支持快捷键，如键:“Control+o”或键:“Control+Shift+T”。当用修饰符指定时，修饰符被按下并被保持，而随后的键被按下.

## frame.query_selector(selector, **kwargs)<a name="frame-query-selector">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="frame-query-selector-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-query-selector-option-strict">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[ElementHandle](#elementhandle)><a name="frame-query-selector-return">#</a>

返回指向frame元素的ElementHandle.

> CAUTION
>
> 不鼓励使用 [ElementHandle](#elementhandle)，而是使用[Locator](#locator)对象和web优先断言 

该方法在框架中查找与指定选择器匹配的元素。有关详细信息，请参阅 [Working with selectors](https://playwright.dev/python/docs/selectors)。如果没有元素匹配该选择器，则返回`null`

## frame.query_selector_all(selector)<a name="frame-query-selector-all">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="frame-query-selector-all-option-selector">#</a>
- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[ElementHandle](#elementhandle)]><a name="frame-query-selector-all-return">#</a>

返回指向frame元素的ElementHandles.

> CAUTION
>
> 不鼓励使用 [ElementHandle](#elementhandle)，而是使用[Locator](#locator)对象

该方法在框架中查找与指定选择器匹配的所有元素。有关详细信息，请参阅 [Working with selectors](https://playwright.dev/python/docs/selectors)。如果没有元素匹配该选择器，则返回`空数组`

## frame.select_option(selector, **kwargs)<a name="frame-select-option">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="frame-select-option-option-selector">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="frame-select-option-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="frame-select-option-option-no-wait-after">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-select-option-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-select-option-option-timeout">#</a>
- `element` \<[ElementHandle](#elementhandle)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[ElementHandle](#elementhandle)]> 要选择的选项。可选的.<a name="frame-select-option-option-element">#</a>
- `index` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)]> 按索引进行选择的选项。可选的.<a name="frame-select-option-option-index">#</a>
- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 按值选择的选项。如果`\<select>`具有多个属性，则选择所有给定的选项，否则只选择与传递的选项之一匹配的第一个选项。可选的.<a name="frame-select-option-option-value">#</a>
- `label` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 按标签进行选择的选项。如果`\<select>`具有多个属性，则选择所有给定的选项，否则只选择与传递的选项之一匹配的第一个选项。可选的.<a name="frame-select-option-option-label">#</a>
- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]><a name="frame-select-option-return">#</a>

这个方法等待元素匹配选择器，等待[可操作性](https://playwright.dev/python/docs/actionability)检查，直到所有指定的选项都出现在`\<select>`元素中，并选择这些选项.

如果目标元素不是`\<select>`元素，此方法将抛出一个错误。但是，如果该元素位于`\<label>`元素中，且该元素具有关联控件，则将使用该控件.

返回已成功选择的选项值的数组.

一旦选择了所有提供的选项，就触发一个更改和输入事件.

- Sync

```python
# single selection matching the value
frame.select_option("select#colors", "blue")
# single selection matching both the label
frame.select_option("select#colors", label="blue")
# multiple selection
frame.select_option("select#colors", value=["red", "green", "blue"])
```

- Async

```python
# single selection matching the value
await frame.select_option("select#colors", "blue")
# single selection matching the label
await frame.select_option("select#colors", label="blue")
# multiple selection
await frame.select_option("select#colors", value=["red", "green", "blue"])
```

## frame.set_checked(selector, checked, **kwargs)<a name="frame-set-checked">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-set-checked-option-selector">#</a>
- `checked` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否选中或不选中复选框.<a name="frame-set-checked-option-checked">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="frame-set-checked-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="frame-set-checked-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="frame-set-checked-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-set-checked-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-set-checked-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="frame-set-checked-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-set-checked-return">#</a>

这个方法通过执行以下步骤检查或取消检查元素匹配选择器:

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 确保匹配的元素是一个复选框或单选输入。如果不是，则排除此方法.
3. 如果元素已经具有正确的选中状态，则该方法立即返回.
4. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
5. 如果需要，将元素滚动到视图中.
6. 使用 [page.mouse](#page-mouse) 单击元素的中心.
7. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.
8. 确保元素现在被选中或取消选中。如果不是，则抛出此方法.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## frame.set_content(html, **kwargs)<a name="frame-set-content">#</a>

- `html` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要分配给页面的html标记.<a name="frame-set-content-option-html">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>最大操作时间，单位为毫秒，默认为30秒，通过0表示禁止超时。默认值可以通过使用  [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout), [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来修改.<a name="frame-set-content-option-timeout">#</a>
- `wait_until` \<"load"|"domcontentloaded"|"networkidle"|"commit"> 当认为操作成功时，默认为`load`。事件可以是:<a name="frame-set-content-option-wait-until">#</a>
    - `'domcontentloaded'` - 当`domcontentloaded`事件被触发时，认为操作已经完成.
    - `'load'` - 当触发`load`事件时，认为操作已经完成.
    - `'networkidle'` - 当至少`500毫秒`没有网络连接时，认为操作已经完成.
    - `'commit'` - 当接收到网络响应并开始加载文档时，认为操作已经完成.
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-set-content-return">#</a>

## frame.set_input_files(selector, files, **kwargs)<a name="frame-set-input-files">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-set-input-files-option-selector">#</a>
- `files` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]|[List](https://docs.python.org/3/library/typing.html#typing.List)[[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]><a name="frame-set-input-files-option-files">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> File name
    - `mimeType` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> File type
    - `buffer` \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> File content
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="frame-set-input-files-option-no-wait-after">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-set-input-files-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-set-input-files-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-set-input-files-return">#</a>

这个方法期望选择器指向一个[输入元素](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

将文件输入的值设置为这些文件路径或文件。如果某些`filepath`是相对路径，那么它们将相对于当前工作目录进行解析。对于空数组，清除选定的文件.

## frame.tap(selector, **kwargs)<a name="frame-tap">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-tap-option-selector">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="frame-tap-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="frame-tap-option-modifiers">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="frame-tap-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="frame-tap-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-tap-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-tap-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="frame-tap-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-tap-return">#</a>

这个方法通过执行以下步骤点击元素匹配选择器:

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
3. 如果需要，将元素滚动到视图中.
4. 点击页面中心或指定位置.
5. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

> NOTE
>
> `frame.tap()`要求浏览器上下文的`hasTouch`选项被设置为`True`.

## frame.text_content(selector, **kwargs)<a name="frame-text-content">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-text-content-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-text-content-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-text-content-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="frame-text-content-return">#</a>

返回`element.textContent`.

## frame.title()<a name="frame-title">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="frame-title-return">#</a>

返回页面标题.

## frame.type(selector, text, **kwargs)<a name="frame-type">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-type-option-selector">#</a>
- `text` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要输入到焦点元素中的文本.<a name="frame-type-option-text">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 按键之间的等待时间，单位是毫秒。默认为0.<a name="frame-type-option-delay">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="frame-type-option-no-wait-after">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-type-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-type-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-type-return">#</a>

为文本中的每个字符发送 `keydown`, `keypress`/`input`, and `keyup` 事件. `frame.type` 可用于发送细粒度键盘事件。要在表单字段中填充值，请使用 [frame.fill(selector, value, **kwargs)](#frame-fill).

要按一个特殊的键，如`Control`或`ArrowDown`，使用 [keyboard.press(key, **kwargs)](#keyboard-press).

- Sync

```python
frame.type("#mytextarea", "hello") # types instantly
frame.type("#mytextarea", "world", delay=100) # types slower, like a user
```

- Async

```python
await frame.type("#mytextarea", "hello") # types instantly
await frame.type("#mytextarea", "world", delay=100) # types slower, like a user
```

## frame.uncheck(selector, **kwargs)<a name="frame-uncheck">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-uncheck-option-selector">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="frame-uncheck-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="frame-uncheck-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="frame-uncheck-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-uncheck-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-uncheck-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="frame-uncheck-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-uncheck-return">#</a>

这个方法通过以下步骤检查元素匹配选择器::

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 确保匹配的元素是一个复选框或单选输入。如果不是，则排除此方法. If the element is already unchecked, this method returns immediately.
3. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
4. 如果需要，将元素滚动到视图中.
5. 使用 [page.mouse](#page-mouse) 单击元素的中心.
6. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.
7. 确保元素现在是未选中的。如果不是，则排除此方法.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## frame.url<a name="frame-url">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="frame-url-return">#</a>

返回 frame's url.

## frame.wait_for_function(expression, **kwargs)<a name="frame-wait-for-function">#</a>

- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="frame-wait-for-function-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="frame-wait-for-function-option-arg">#</a>
- `polling` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|"raf"> 如果`polling`是'raf'，那么表达式会在`requestAnimationFrame`回调中持续执行。如果`polling`是一个数字，那么它将被视为执行函数的毫秒间隔。默认为`raf`.<a name="frame-wait-for-function-option-polling">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，以毫秒为单位。默认为`30000`(30秒)。通过0禁用超时。默认值可以通过使用[browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout)来更改.<a name="frame-wait-for-function-option-timeout">#</a>
- returns: \<[JSHandle](#jshandle)><a name="frame-wait-for-function-return">#</a>

当表达式返回真值时，返回该值.

[frame.wait_for_function(expression, **kwargs)](#frame-wait-for-function) 可用于观察视口大小的变化:

- Sync

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    webkit = playwright.webkit
    browser = webkit.launch()
    page = browser.new_page()
    page.evaluate("window.x = 0; setTimeout(() => { window.x = 100 }, 1000);")
    page.main_frame.wait_for_function("() => window.x > 0")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    webkit = playwright.webkit
    browser = await webkit.launch()
    page = await browser.new_page()
    await page.evaluate("window.x = 0; setTimeout(() => { window.x = 100 }, 1000);")
    await page.main_frame.wait_for_function("() => window.x > 0")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

将参数传递给 `frame.waitForFunction` 函数:

- Sync

```python
selector = ".foo"
frame.wait_for_function("selector => !!document.querySelector(selector)", selector)
```

- Async

```python
selector = ".foo"
await frame.wait_for_function("selector => !!document.querySelector(selector)", selector)
```

## frame.wait_for_load_state(**kwargs)<a name="frame-wait-for-load-state">#</a>

- `state` \<"load"|"domcontentloaded"|"networkidle"> 可选加载状态，等待，默认为`load`。如果在加载当前文档时已经达到该状态，该方法将立即进行解析。可以是:<a name="frame-wait-for-load-state-option-state">#</a>
    - `'load'` - 等待`load`事件被触发.
    - `'domcontentloaded'` - 等待`domcontentloaded`事件被触发.
    - `'networkidle'` - 等待至少500毫秒没有网络连接.
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>最大操作时间，单位为毫秒，默认为30秒，通过0表示禁止超时。默认值可以通过使用  [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout), [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来修改.<a name="frame-wait-for-load-state-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-wait-for-load-state-return">#</a>

等待到达所需的加载状态.

当 frame 达到所需的加载状态时返回，默认为加载。该导航必须在调用此方法时已提交。如果当前文档已经达到了所需的状态，则立即进行解析.

- Sync

```python
frame.click("button") # click triggers navigation.
frame.wait_for_load_state() # the promise resolves after "load" event.
```

- Async

```python
await frame.click("button") # click triggers navigation.
await frame.wait_for_load_state() # the promise resolves after "load" event.
```

## frame.wait_for_selector(selector, **kwargs)<a name="frame-wait-for-selector">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="frame-wait-for-selector-option-selector">#</a>
- `state` \<"attached"|"detached"|"visible"|"hidden"> 默认为`"visible"`。可以是:<a name="frame-wait-for-selector-option-state">#</a>
    - `'attached'` - 等待元素出现在DOM中.
    - `'detached'` - 等待元素在DOM中不存在.
    - `'visible'` - 等待元素有非空的边界框 且 没有 `visibility:hidden`.注意，没有任何内容或带有`display:none` 的元素有一个空的边界框，因此不被认为是可见的.
    - `'hidden'` - 等待元素从DOM中分离出来, 或有一个空的边界框或' visibility:hidden '。这与`“visible”`选项相反.
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="frame-wait-for-selector-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="frame-wait-for-selector-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[ElementHandle](#elementhandle)><a name="frame-wait-for-selector-return">#</a>

当选择器指定的元素满足状态选项时返回。如果等待`隐藏`或`分离`，则返回null.

> NOTE
>
> Playwright 在执行操作之前，自动等待元素准备就绪. 使用[Locator](#locator)对象和web-first断言会使代码不需要等待选择器.

等待' selector '满足' state '选项(要么从dom中出现/消失，要么变成可见/隐藏)。如果在调用方法' selector '的时候已经满足条件，该方法将立即返回。如果选择器不满足' timeout '毫秒的条件，函数将排除.

此方法适用于多个导航:

- Sync

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    for current_url in ["https://google.com", "https://bbc.com"]:
        page.goto(current_url, wait_until="domcontentloaded")
        element = page.main_frame.wait_for_selector("img")
        print("Loaded image: " + str(element.get_attribute("src")))
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    chromium = playwright.chromium
    browser = await chromium.launch()
    page = await browser.new_page()
    for current_url in ["https://google.com", "https://bbc.com"]:
        await page.goto(current_url, wait_until="domcontentloaded")
        element = await page.main_frame.wait_for_selector("img")
        print("Loaded image: " + str(await element.get_attribute("src")))
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

## frame.wait_for_timeout(timeout)<a name="frame-wait-for-timeout">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 等待超时时间<a name="frame-wait-for-timeout-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-wait-for-timeout-return">#</a>

等待给定超时(以毫秒为单位).

注意，`frame.waitForTimeout()` 应该只用于调试。在生产中使用计时器的测试将是不可靠的。使用信号，如网络事件，选择器变得可见和其他方式.

## frame.wait_for_url(url, **kwargs)<a name="frame-wait-for-url">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[URL](https://en.wikipedia.org/wiki/URL)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 一个glob模式、regex模式或谓词，在等待导航时接收匹配的url。注意，如果参数是一个不带通配符的字符串，该方法将等待导航到与该字符串完全相等的URL.<a name="frame-wait-for-url-option-url">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>最大操作时间，单位为毫秒，默认为30秒，通过0表示禁止超时。默认值可以通过使用  [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout), [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来修改.<a name="frame-wait-for-url-option-timeout">#</a>
- `wait_until` \<"load"|"domcontentloaded"|"networkidle"|"commit"> 当认为操作成功时，默认为`load`。事件可以是:<a name="frame-wait-for-url-option-wait-until">#</a>
    - `'domcontentloaded'` - 当`domcontentloaded`事件被触发时，认为操作已经完成.
    - `'load'` - 当触发`load`事件时，认为操作已经完成.
    - `'networkidle'` - 当至少`500毫秒`没有网络连接时，认为操作已经完成.
    - `'commit'` - 当接收到网络响应并开始加载文档时，认为操作已经完成.
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="frame-wait-for-url-return">#</a>

等待frame导航到给定的URL.

- Sync

```python
frame.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
frame.wait_for_url("**/target.html")
```

- Async

```python
await frame.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
await frame.wait_for_url("**/target.html")
```





# FrameLocator

FrameLocator表示页面上`iframe`的视图。它捕获的逻辑足以检索`iframe`并定位该`iframe`中的元素。framellocator可以用 [page.frame_locator(selector)](#page-frame-locator) or [locator.frame_locator(selector)](#locator-frame-locator) 方法创建.

- Sync

```python
locator = page.frame_locator("my-frame").locator("text=Submit")
locator.click()
```

- Async

```python
locator = page.frame_locator("#my-frame").locator("text=Submit")
await locator.click()
```

**Strictness**

框架定位是严格的。这意味着，如果有多个元素匹配给定的选择器，那么帧定位器上的所有操作都会抛出.

- Sync

```python
# Throws if there are several frames in DOM:
page.frame_locator('.result-frame').locator('button').click()

# Works because we explicitly tell locator to pick the first frame:
page.frame_locator('.result-frame').first.locator('button').click()
```

- Async

```python
# Throws if there are several frames in DOM:
await page.frame_locator('.result-frame').locator('button').click()

# Works because we explicitly tell locator to pick the first frame:
await page.frame_locator('.result-frame').first.locator('button').click()
```

**Converting Locator to FrameLocator**

如果你有一个指向`iframe`的[Locator](#locator)对象，可以使用以下方法将其转换为 [FrameLocator](#framelocator), 使用   [`:scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/:scope) CSS 选择器:

- Sync

```python
frameLocator = locator.frame_locator(":scope");
```

- Async

```python
frameLocator = locator.frame_locator(":scope");
```

- [frame_locator.first](#frame-locator-first)
- [frame_locator.frame_locator(selector)](#frame-locator-frame-locator)
- [frame_locator.last](#frame-locator-last)
- [frame_locator.locator(selector, **kwargs)](#frame-locator-locator)
- [frame_locator.nth(index)](#frame-locator-nth)

## frame_locator.first<a name="frame-locator-first">#</a>

- returns: \<[FrameLocator](#framelocator)><a name="frame-locator-first-return">#</a>

返回第一个匹配 frame 的定位符.

## frame_locator.frame_locator(selector)<a name="frame-locator-frame-locator">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 解析DOM元素时使用的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-locator-frame-locator-option-selector">#</a>
- returns: \<[FrameLocator](#framelocator)><a name="frame-locator-frame-locator-return">#</a>

在使用iframes时，您可以创建一个frame 定位器，该定位器将进入iframe并允许选择该iframe中的元素.

## frame_locator.last<a name="frame-locator-last">#</a>

- returns: \<[FrameLocator](#framelocator)><a name="frame-locator-last-return">#</a>

返回最后一个匹配frame 的定位符.

## frame_locator.locator(selector, **kwargs)<a name="frame-locator-locator">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 解析DOM元素时使用的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="frame-locator-locator-option-selector">#</a>

- `has` \<[Locator](#locator)> 对selector选中的元素进行再次匹配, 匹配目标中的子元素, 例如: 匹配子元素的`text=Playwright`的元素  `\<article>\<div>Playwright\</div>\</article>`.<a name="frame-locator-locator-option-has">#</a>

    请注意，外部和内部定位器必须属于同一个 frame. 内部定位器不能包含 [FrameLocator](#framelocator).

- `has_text` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> 匹配包含指定文本的元素，可能在子元素或后代元素中,例如:`"Playwright"` 匹配 `\<article>\<div>Playwright\</div>\</article>`.<a name="frame-locator-locator-option-has-text">#</a>

- returns: \<[Locator](#locator)><a name="frame-locator-locator-return">#</a>

该方法在framocator的子树中找到与指定选择器匹配的元素.

## frame_locator.nth(index)<a name="frame-locator-nth">#</a>

- `index` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)><a name="frame-locator-nth-option-index">#</a>
- returns: \<[FrameLocator](#framelocator)><a name="frame-locator-nth-return">#</a>

返回第n个匹配frame 的定位符.





# JSHandle

JSHandle表示一个页内JavaScript对象。JSHandles可以用 [page.evaluate_handle(expression, **kwargs)](#page-evaluate-handle) 方法创建.

- Sync

```python
window_handle = page.evaluate_handle("window")
# ...
```

- Async

```python
window_handle = await page.evaluate_handle("window")
# ...
```

jhandle防止被引用的JavaScript对象被垃圾收集，除非该句柄被 [js_handle.dispose()](#js-handle-dispose) 指定. 当JSHandles的原始frame 被导航或者父上下文被销毁时，JSHandles会被自动销毁.

JSHandle实例可以当作 [page.eval_on_selector(selector, expression, **kwargs)](#page-eval-on-selector), [page.evaluate(expression, **kwargs)](#page-evaluate) and [page.evaluate_handle(expression, **kwargs)](#page-evaluate-handle) 方法中的一个参数.

- [js_handle.as_element()](#js-handle-as-element)
- [js_handle.dispose()](#js-handle-dispose)
- [js_handle.evaluate(expression, **kwargs)](#js-handle-evaluate)
- [js_handle.evaluate_handle(expression, **kwargs)](#js-handle-evaluate-handle)
- [js_handle.get_properties()](#js-handle-get-properties)
- [js_handle.get_property(property_name)](#js-handle-get-property)
- [js_handle.json_value()](#js-handle-json-value)

## js_handle.as_element()<a name="js-handle-as-element">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[ElementHandle](#elementhandle)><a name="js-handle-as-element-return">#</a>

如果对象句柄是[ElementHandle](#elementhandle)的实例，则返回`null`或对象句柄本身.

## js_handle.dispose()<a name="js-handle-dispose">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="js-handle-dispose-return">#</a>

`jsHandle.dispose` 方法停止引用元素句柄.

## js_handle.evaluate(expression, **kwargs)<a name="js-handle-evaluate">#</a>

- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="js-handle-evaluate-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="js-handle-evaluate-option-arg">#</a>
- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="js-handle-evaluate-return">#</a>

返回表达式的返回值.

此方法将此句柄作为第一个参数传递给表达式.

如果表达式返回[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)，则 `handle.evaluate`将等待promise解析并返回其值

例子:

- Sync

```python
tweet_handle = page.query_selector(".tweet .retweets")
assert tweet_handle.evaluate("node => node.innerText") == "10 retweets"
```

- Async

```python
tweet_handle = await page.query_selector(".tweet .retweets")
assert await tweet_handle.evaluate("node => node.innerText") == "10 retweets"
```

## js_handle.evaluate_handle(expression, **kwargs)<a name="js-handle-evaluate-handle">#</a>

- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="js-handle-evaluate-handle-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="js-handle-evaluate-handle-option-arg">#</a>
- returns: \<[JSHandle](#jshandle)><a name="js-handle-evaluate-handle-return">#</a>

返回表达式的返回值是一个 [JSHandle](#jshandle).

此方法将此句柄作为第一个参数传递给表达式.

 `jsHandle.evaluate` 和`jsHandle.evaluateHandle` 两者之间的唯一区别是: `jsHandle.evaluateHandle` 返回[JSHandle](#jshandle).

如果函数传递给 `jsHandle.evaluateHandle` 返回一个 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 则`jsHandle.evaluateHandle`将等待promise解析并返回它的值.

更多细节参考: [page.evaluate_handle(expression, **kwargs)](#page-evaluate-handle) .

## js_handle.get_properties()<a name="js-handle-get-properties">#</a>

- returns: \<[Map][[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [JSHandle](#jshandle)]><a name="js-handle-get-properties-return">#</a>

该方法返回一个映射，其中包含自己的属性名作为键，jshhandle实例作为属性值.

- Sync

```python
handle = page.evaluate_handle("{window, document}")
properties = handle.get_properties()
window_handle = properties.get("window")
document_handle = properties.get("document")
handle.dispose()
```

- Async

```python
handle = await page.evaluate_handle("{window, document}")
properties = await handle.get_properties()
window_handle = properties.get("window")
document_handle = properties.get("document")
await handle.dispose()
```

## js_handle.get_property(property_name)<a name="js-handle-get-property">#</a>

- `property_name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 属性获取<a name="js-handle-get-property-option-property-name">#</a>
- returns: \<[JSHandle](#jshandle)><a name="js-handle-get-property-return">#</a>

从被引用的对象中获取单个属性.

## js_handle.json_value()<a name="js-handle-json-value">#</a>

- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="js-handle-json-value-return">#</a>

返回对象的JSON表示。如果对象有toJSON函数，它将不会被调用.

> NOTE
>
> 如果引用的对象不是可字符串化的，该方法将返回一个空的JSON对象。如果对象有循环引用，它将抛出一个错误.





# Keyboard

Keyboard提供了一个用于管理虚拟键盘的api。高级api是 [keyboard.type(text, **kwargs)](#keyboard-type), 它接受原始字符并在页面上生成适当的keydown、keypress/input和keyup事件.

为了进行更精细的控制，可以使用 [keyboard.down(key)](#keyboard-down), [keyboard.up(key)](#keyboard-up), and [keyboard.insert_text(text)](#keyboard-insert-text) 手动触发事件，就像它们是从真正的键盘中生成的一样.

按住`Shift`键来选择和删除一些文本的例子:

- Sync

```python
page.keyboard.type("Hello World!")
page.keyboard.press("ArrowLeft")
page.keyboard.down("Shift")
for i in range(6):
    page.keyboard.press("ArrowLeft")
page.keyboard.up("Shift")
page.keyboard.press("Backspace")
# result text will end up saying "Hello!"
```

- Async

```python
await page.keyboard.type("Hello World!")
await page.keyboard.press("ArrowLeft")
await page.keyboard.down("Shift")
for i in range(6):
    await page.keyboard.press("ArrowLeft")
await page.keyboard.up("Shift")
await page.keyboard.press("Backspace")
# result text will end up saying "Hello!"
```

一个按大写字母`A`的例子

- Sync

```python
page.keyboard.press("Shift+KeyA")
# or
page.keyboard.press("Shift+A")
```

- Async

```python
await page.keyboard.press("Shift+KeyA")
# or
await page.keyboard.press("Shift+A")
```

一个用键盘触发全部选择的例子

- Sync

```python
# on windows and linux
page.keyboard.press("Control+A")
# on mac_os
page.keyboard.press("Meta+A")
```

- Async

```python
# on windows and linux
await page.keyboard.press("Control+A")
# on mac_os
await page.keyboard.press("Meta+A")
```

- [keyboard.down(key)](#keyboard-down)
- [keyboard.insert_text(text)](#keyboard-insert-text)
- [keyboard.press(key, **kwargs)](#keyboard-press)
- [keyboard.type(text, **kwargs)](#keyboard-type)
- [keyboard.up(key)](#keyboard-up)

## keyboard.down(key)<a name="keyboard-down">#</a>

- `key` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要按下的`键名`或要生成的字符，如`ArrowLeft`或'a'.<a name="keyboard-down-option-key">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="keyboard-down-return">#</a>

分派一个按键事件.

key可以指定想要的 [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) 或是单个字符生成的文本,这里可以找到键值的超集。键的例子如下:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

还支持以下快捷键:`Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

按住`Shift`键将输入与大写键对应的文本.

如果`key`是单个字符，它是区分大小写的，因此值`a`和`A`将生成不同的文本.

如果key是一个修饰键, `Shift`, `Meta`, `Control`, or `Alt`, 随后的按键将发送该修饰器激活。要释放修饰键，请使用 [keyboard.up(key)](#keyboard-up).

按下该键一次后，随后调用 [keyboard.down(key)](#keyboard-down) 将[重复](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/repeat)设置为 true. 释放键，使用 [keyboard.up(key)](#keyboard-up).

> NOTE
>
> 修改键会产生影响 `keyboard.down`. 按住 `Shift` 键将输入大写的文本.

## keyboard.insert_text(text)<a name="keyboard-insert-text">#</a>

- `text` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 设置输入为指定的文本值.<a name="keyboard-insert-text-option-text">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="keyboard-insert-text-return">#</a>

只分派输入事件，不发出 `keydown`, `keyup` or `keypress` 等事件.

- Sync

```python
page.keyboard.insert_text("嗨")
```

- Async

```python
await page.keyboard.insert_text("嗨")
```

> NOTE
>
> 修饰键不影响 `keyboard.insertText`. 按下 `Shift` 键不会输入大写的文本.

## keyboard.press(key, **kwargs)<a name="keyboard-press">#</a>

- `key` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要按下的`键名`或要生成的字符，如`ArrowLeft`或'a'.<a name="keyboard-press-option-key">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `keydown`和`keyup`之间的等待时间，单位是毫秒。默认为0.<a name="keyboard-press-option-delay">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="keyboard-press-return">#</a>

key可以指定想要的 [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) 或是单个字符生成的文本,这里可以找到键值的超集。键的例子如下:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

还支持以下快捷键:`Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

按住`Shift`键将输入与大写键对应的文本.

如果`key`是单个字符，它是区分大小写的，因此值`a`和`A`将生成不同的文本.

也支持快捷键，如键:“Control+o”或键:“Control+Shift+T”。当用修饰符指定时，修饰符被按下并被保持，而随后的键被按下.

- Sync

```python
page = browser.new_page()
page.goto("https://keycode.info")
page.keyboard.press("a")
page.screenshot(path="a.png")
page.keyboard.press("ArrowLeft")
page.screenshot(path="arrow_left.png")
page.keyboard.press("Shift+O")
page.screenshot(path="o.png")
browser.close()
```

- Async

```python
page = await browser.new_page()
await page.goto("https://keycode.info")
await page.keyboard.press("a")
await page.screenshot(path="a.png")
await page.keyboard.press("ArrowLeft")
await page.screenshot(path="arrow_left.png")
await page.keyboard.press("Shift+O")
await page.screenshot(path="o.png")
await browser.close()
```

 [keyboard.down(key)](#keyboard-down) and [keyboard.up(key) ](#keyboard-up)的快捷键.

## keyboard.type(text, **kwargs)<a name="keyboard-type">#</a>

- `text` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要输入到焦点元素中的文本.<a name="keyboard-type-option-text">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 按键之间的等待时间，单位是毫秒。默认为0.<a name="keyboard-type-option-delay">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="keyboard-type-return">#</a>

为文本中的每个字符发送  `keydown`, `keypress`/`input`, and `keyup` 事件.

要按一个特殊的键，如`Control`或`ArrowDown`，使用 [keyboard.press(key, **kwargs)](#keyboard-press).

- Sync

```python
page.keyboard.type("Hello") # types instantly
page.keyboard.type("World", delay=100) # types slower, like a user
```

- Async

```python
await page.keyboard.type("Hello") # types instantly
await page.keyboard.type("World", delay=100) # types slower, like a user
```

> NOTE
>
> 修饰键不影响 `keyboard.type`. 按下 `Shift` 键不会输入大写的文本.

> NOTE
>
> 对于非美式键盘上的字符，只会发送一个`输入`事件.

## keyboard.up(key)<a name="keyboard-up">#</a>

- `key` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要按下的`键名`或要生成的字符，如`ArrowLeft`或'a'.<a name="keyboard-up-option-key">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="keyboard-up-return">#</a>

分派一个`keyup`事件.



# Locator

`locator 定位器`是playwright 自动等待和重试能力的核心部分。简而言之，定位器表示一种随时在页面上查找元素的方法。可以使用页面创建定位器 [page.locator(selector, **kwargs)](#page-locator) .

[Learn more about locators](https://playwright.dev/python/docs/locators).

- [locator.all_inner_texts()](#locator-all-inner-texts)
- [locator.all_text_contents()](#locator-all-text-contents)
- [locator.bounding_box(**kwargs)](#locator-bounding-box)
- [locator.check(**kwargs)](#locator-check)
- [locator.click(**kwargs)](#locator-click)
- [locator.count()](#locator-count)
- [locator.dblclick(**kwargs)](#locator-dblclick)
- [locator.dispatch_event(type, **kwargs)](#locator-dispatch-event)
- [locator.drag_to(target, **kwargs)](#locator-drag-to)
- [locator.element_handle(**kwargs)](#locator-element-handle)
- [locator.element_handles()](#locator-element-handles)
- [locator.evaluate(expression, **kwargs)](#locator-evaluate)
- [locator.evaluate_all(expression, **kwargs)](#locator-evaluate-all)
- [locator.evaluate_handle(expression, **kwargs)](#locator-evaluate-handle)
- [locator.fill(value, **kwargs)](#locator-fill)
- [locator.first](#locator-first)
- [locator.focus(**kwargs)](#locator-focus)
- [locator.frame_locator(selector)](#locator-frame-locator)
- [locator.get_attribute(name, **kwargs)](#locator-get-attribute)
- [locator.highlight()](#locator-highlight)
- [locator.hover(**kwargs)](#locator-hover)
- [locator.inner_html(**kwargs)](#locator-inner-html)
- [locator.inner_text(**kwargs)](#locator-inner-text)
- [locator.input_value(**kwargs)](#locator-input-value)
- [locator.is_checked(**kwargs)](#locator-is-checked)
- [locator.is_disabled(**kwargs)](#locator-is-disabled)
- [locator.is_editable(**kwargs)](#locator-is-editable)
- [locator.is_enabled(**kwargs)](#locator-is-enabled)
- [locator.is_hidden(**kwargs)](#locator-is-hidden)
- [locator.is_visible(**kwargs)](#locator-is-visible)
- [locator.last](#locator-last)
- [locator.locator(selector, **kwargs)](#locator-locator)
- [locator.nth(index)](#locator-nth)
- [locator.page](#locator-page)
- [locator.press(key, **kwargs)](#locator-press)
- [locator.screenshot(**kwargs)](#locator-screenshot)
- [locator.scroll_into_view_if_needed(**kwargs)](#locator-scroll-into-view-if-needed)
- [locator.select_option(**kwargs)](#locator-select-option)
- [locator.select_text(**kwargs)](#locator-select-text)
- [locator.set_checked(checked, **kwargs)](#locator-set-checked)
- [locator.set_input_files(files, **kwargs)](#locator-set-input-files)
- [locator.tap(**kwargs)](#locator-tap)
- [locator.text_content(**kwargs)](#locator-text-content)
- [locator.type(text, **kwargs)](#locator-type)
- [locator.uncheck(**kwargs)](#locator-uncheck)
- [locator.wait_for(**kwargs)](#locator-wait-for)

## locator.all_inner_texts()<a name="locator-all-inner-texts">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]><a name="locator-all-inner-texts-return">#</a>

返回一个 `node.innerText` 值为所有匹配节点.

## locator.all_text_contents()<a name="locator-all-text-contents">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]><a name="locator-all-text-contents-return">#</a>

返回一个节点数组值为所有节点的 `node.textContent` .

## locator.bounding_box(**kwargs)<a name="locator-bounding-box">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-bounding-box-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="locator-bounding-box-return">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 元素的 X 坐标像素.
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 元素的Y坐标，以像素为单位.
    - `width` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 元素的宽度，以像素为单位.
    - `height` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 元素的高度，以像素为单位.

此方法返回元素的边界框，如果元素不可见，则返回`null`。边界框是相对于主帧视口计算的——主帧视口通常与浏览器窗口相同.

滚动会影响返回的绑定框，类似于  [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) , 这意味着x和/或y可能是负的.

与 [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) 不同，子frame 中的元素返回相对于主frame 的边界框.

假设页面是静态的，使用边界框坐标执行输入是安全的。例如，下面的代码片段应该单击元素的中心.

- Sync

```python
box = element.bounding_box()
page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
```

- Async

```python
box = await element.bounding_box()
await page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
```

## locator.check(**kwargs)<a name="locator-check">#</a>

- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="locator-check-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="locator-check-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="locator-check-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-check-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="locator-check-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-check-return">#</a>

这个方法通过执行以下步骤来检查元素:

1. 确保元素是一个复选框或单选输入。如果不是，则抛出此方法。如果元素已被选中，则该方法立即返回.
2. 等待元素的[可操作性](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项.
3. 如果需要，将元素滚动到视图中.
4. 使用 [page.mouse](#page-mouse) 单击元素的中心.
5. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.
6. 确保元素现在被选中。如果不是，则排除此方法.

如果元素在动作期间的任何时刻与DOM分离，此方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## locator.click(**kwargs)<a name="locator-click">#</a>

- `button` \<"left"|"right"|"middle"> 默认左 `left`.<a name="locator-click-option-button">#</a>
- `click_count` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 默认为1,详情查看  [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail).<a name="locator-click-option-click-count">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `mousedown`和`mouseup`之间的等待时间，单位是毫秒。默认为0.<a name="locator-click-option-delay">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="locator-click-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="locator-click-option-modifiers">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="locator-click-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="locator-click-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-click-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="locator-click-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-click-return">#</a>

该方法执行以下步骤单击元素:

1. 等待元素的[可操作性](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项.
2. 如果需要，将元素滚动到视图中.
3. 使用 [page.mouse](#page-mouse) 单击元素的中心, or the specified `position`.
4. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.

如果元素在动作期间的任何时刻与DOM分离，此方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## locator.count()<a name="locator-count">#</a>

- returns: \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)><a name="locator-count-return">#</a>

返回匹配给定选择器的元素数.

## locator.dblclick(**kwargs)<a name="locator-dblclick">#</a>

- `button` \<"left"|"right"|"middle"> 默认左 `left`.<a name="locator-dblclick-option-button">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `mousedown`和`mouseup`之间的等待时间，单位是毫秒。默认为0.<a name="locator-dblclick-option-delay">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="locator-dblclick-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="locator-dblclick-option-modifiers">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="locator-dblclick-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="locator-dblclick-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-dblclick-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="locator-dblclick-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-dblclick-return">#</a>

该方法执行以下步骤双击元素:

1. 等待元素的[可操作性](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项.
2. 如果需要，将元素滚动到视图中.
3. 使用 [page.mouse](#page-mouse) 方法,双击元素中心位置.
4. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.该方法执行以下步骤双击元素, 注意，如果`dblclick()`的第一次单击触发了一个导航事件，则该方法将抛出.

如果元素在动作期间的任何时刻与DOM分离，此方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

> NOTE
>
> `element.dblclick()` 分发两个 `click` 事件和一个 `dblclick` 事件.

## locator.dispatch_event(type, **kwargs)<a name="locator-dispatch-event">#</a>

- `type` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> DOM事件类型:`"click"`， `"dragstart"`等.<a name="locator-dispatch-event-option-type">#</a>
- `event_init` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 可选的特定于事件的初始化属性.<a name="locator-dispatch-event-option-event-init">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-dispatch-event-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-dispatch-event-return">#</a>

下面的代码片段分派元素上的`单击`事件。无论元素的可见性状态如何，单击都将被分派。这相当于调用[element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

- Sync

```python
element.dispatch_event("click")
```

- Async

```python
await element.dispatch_event("click")
```

在底层，它根据给定的类型创建一个事件实例，使用`event_init`属性初始化它，并在元素上分派它。默认情况下，事件是组合的、可取消的和冒泡的.

由于`event_init`是特定于事件的，请参考事件文档中的初始属性列表:

- [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
- [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
- [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
- [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
- [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
- [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
- [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)

如果你想要将活动对象传递到事件中，你也可以指定`jhandle`作为属性值:

- Sync

```python
# note you can only create data_transfer in chromium and firefox
data_transfer = page.evaluate_handle("new DataTransfer()")
element.dispatch_event("#source", "dragstart", {"dataTransfer": data_transfer})
```

- Async

```python
# note you can only create data_transfer in chromium and firefox
data_transfer = await page.evaluate_handle("new DataTransfer()")
await element.dispatch_event("#source", "dragstart", {"dataTransfer": data_transfer})
```

## locator.drag_to(target, **kwargs)<a name="locator-drag-to">#</a>

- `target` \<[Locator](#locator)> 要拖动到的元素的定位器.<a name="locator-drag-to-option-target">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="locator-drag-to-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="locator-drag-to-option-no-wait-after">#</a>
- `source_position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 此时相对于元素填充框的左上角单击源元素。如果没有指定，则使用元素的某个可见点.<a name="locator-drag-to-option-source-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `target_position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 此时相对于元素填充框的左上角落在目标元素上。如果没有指定，则使用元素的某个可见点.<a name="locator-drag-to-option-target-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-drag-to-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="locator-drag-to-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-drag-to-return">#</a>

## locator.element_handle(**kwargs)<a name="locator-element-handle">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-element-handle-option-timeout">#</a>
- returns: \<[ElementHandle](#elementhandle)><a name="locator-element-handle-return">#</a>

解析给定的定位器到第一个匹配的DOM元素。如果没有匹配查询的元素可见，等待它们直到给定的超时。如果多个元素匹配该选择器，则抛出.

## locator.element_handles()<a name="locator-element-handles">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[ElementHandle](#elementhandle)]><a name="locator-element-handles-return">#</a>

解析所有匹配的DOM元素.

## locator.evaluate(expression, **kwargs)<a name="locator-evaluate">#</a>

- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="locator-evaluate-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="locator-evaluate-option-arg">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-evaluate-option-timeout">#</a>
- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="locator-evaluate-return">#</a>

返回表达式的返回值.

此方法将此句柄作为第一个参数传递给表达式.

如果表达式返回 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 则`handle.evaluate` 将等待promise解析并返回其值.

例子:

- Sync

```python
tweets = page.locator(".tweet .retweets")
assert tweets.evaluate("node => node.innerText") == "10 retweets"
```

- Async

```python
tweets = page.locator(".tweet .retweets")
assert await tweets.evaluate("node => node.innerText") == "10 retweets"
```

## locator.evaluate_all(expression, **kwargs)<a name="locator-evaluate-all">#</a>

- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="locator-evaluate-all-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="locator-evaluate-all-option-arg">#</a>
- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="locator-evaluate-all-return">#</a>

该方法查找与指定定位器匹配的所有元素，并将匹配元素的数组作为第一个参数传递给表达式。返回表达式调用的结果.

如果表达式返回 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 则 [locator.evaluate_all(expression, **kwargs)](#locator-evaluate-all) 将等待promise解析并返回其值.

例子:

- Sync

```python
elements = page.locator("div")
div_counts = elements("(divs, min) => divs.length >= min", 10)
```

- Async

```python
elements = page.locator("div")
div_counts = await elements("(divs, min) => divs.length >= min", 10)
```

## locator.evaluate_handle(expression, **kwargs)<a name="locator-evaluate-handle">#</a>

- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="locator-evaluate-handle-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="locator-evaluate-handle-option-arg">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-evaluate-handle-option-timeout">#</a>
- returns: \<[JSHandle](#jshandle)><a name="locator-evaluate-handle-return">#</a>

返回表达式的返回值 as a [JSHandle](#jshandle).

此方法将此句柄作为第一个参数传递给表达式.

 [locator.evaluate(expression, **kwargs)](#locator-evaluate) and [locator.evaluate_handle(expression, **kwargs)](#locator-evaluate-handle) 之间唯一不同的是 [locator.evaluate_handle(expression, **kwargs)](#locator-evaluate-handle) 返回 [JSHandle](#jshandle).

如果函数传递给 [locator.evaluate_handle(expression, **kwargs)](#locator-evaluate-handle)返回一个 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 则 [locator.evaluate_handle(expression, **kwargs)](#locator-evaluate-handle) 将等待promise解析并返回其值.

详情查看 [page.evaluate_handle(expression, **kwargs)](#page-evaluate-handle).

## locator.fill(value, **kwargs)<a name="locator-fill">#</a>

- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> Value to set for the `\<input>`, `\<textarea>` or `[contenteditable]` element.<a name="locator-fill-option-value">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="locator-fill-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="locator-fill-option-no-wait-after">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-fill-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-fill-return">#</a>

这个方法等待[可操作性](https://playwright.dev/python/docs/actionability)检查，聚焦元素，填充它，并在填充后触发一个输入事件。请注意，您可以传递一个空字符串来清除输入字段.

如果目标元素不是 `\<input>`, `\<textarea>` or `[contenteditable]`, 此方法将抛出一个错误。但是，如果该元素位于`\<label>`元素中，且该元素具有关联控件，则该控件将被填充.

要发送细粒度的键盘事件，请使用 [locator.type(text, **kwargs)](#locator-type).

## locator.first<a name="locator-first">#</a>

- returns: \<[Locator](#locator)><a name="locator-first-return">#</a>

返回第一个匹配元素的定位符.

## locator.focus(**kwargs)<a name="locator-focus">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-focus-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-focus-return">#</a>

Calls [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on the element.

## locator.frame_locator(selector)<a name="locator-frame-locator">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 解析DOM元素时使用的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="locator-frame-locator-option-selector">#</a>
- returns: \<[FrameLocator](#framelocator)><a name="locator-frame-locator-return">#</a>

当使用 iframe 时，你可以创建一个frame 定位器，它将进入iframe 并允许选择该 iframe中的元素:

- Sync

```python
locator = page.frame_locator("iframe").locator("text=Submit")
locator.click()
```

- Async

```python
locator = page.frame_locator("iframe").locator("text=Submit")
await locator.click()
```

## locator.get_attribute(name, **kwargs)<a name="locator-get-attribute">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 属性名.<a name="locator-get-attribute-option-name">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-get-attribute-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="locator-get-attribute-return">#</a>

返回元素属性值.

## locator.highlight()<a name="locator-highlight">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-highlight-return">#</a>

在屏幕上突出显示相应的元素。这对调试很有用，不要提交使用 [locator.highlight()](#locator-highlight) 的代码.

## locator.hover(**kwargs)<a name="locator-hover">#</a>

- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="locator-hover-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="locator-hover-option-modifiers">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="locator-hover-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-hover-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="locator-hover-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-hover-return">#</a>

该方法通过执行以下步骤悬停在元素上:

1. 等待元素的[可操作性](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项.
2. 如果需要，将元素滚动到视图中.
3. 使鼠标停在元素中心或指定位置上.
4. 等待发起的导航成功或失败，除非设置了`noWaitAfter`选项.

如果元素在动作期间的任何时刻与DOM分离，此方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## locator.inner_html(**kwargs)<a name="locator-inner-html">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-inner-html-option-timeout">#</a>
- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="locator-inner-html-return">#</a>

Returns the `element.innerHTML`.

## locator.inner_text(**kwargs)<a name="locator-inner-text">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-inner-text-option-timeout">#</a>
- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="locator-inner-text-return">#</a>

Returns the `element.innerText`.

## locator.input_value(**kwargs)<a name="locator-input-value">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-input-value-option-timeout">#</a>
- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="locator-input-value-return">#</a>

返回输入 `\<input>` or `\<textarea>` or `\<select>`  元素的值, 排除非输入元素.

## locator.is_checked(**kwargs)<a name="locator-is-checked">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-is-checked-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="locator-is-checked-return">#</a>

返回元素是否被选中。如果元素不是复选框或单选输入则排除.

## locator.is_disabled(**kwargs)<a name="locator-is-disabled">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-is-disabled-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="locator-is-disabled-return">#</a>

返回该元素是否被禁用，与启用[enabled](https://playwright.dev/python/docs/actionability#enabled)相反.

## locator.is_editable(**kwargs)<a name="locator-is-editable">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-is-editable-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="locator-is-editable-return">#</a>

返回元素是否可编辑[editable](https://playwright.dev/python/docs/actionability#editable).

## locator.is_enabled(**kwargs)<a name="locator-is-enabled">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-is-enabled-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="locator-is-enabled-return">#</a>

返回元素是否被启用[enabled](https://playwright.dev/python/docs/actionability#enabled).

## locator.is_hidden(**kwargs)<a name="locator-is-hidden">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> **DEPRECATED** This option is ignored. [locator.is_hidden(**kwargs)](#locator-is-hidden) does not wait for the element to become hidden and returns immediately.<a name="locator-is-hidden-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="locator-is-hidden-return">#</a>

返回元素是否隐藏，与可见 [visible](https://playwright.dev/python/docs/actionability#visible)相反.

## locator.is_visible(**kwargs)<a name="locator-is-visible">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> **DEPRECATED** This option is ignored. [locator.is_visible(**kwargs)](#locator-is-visible) does not wait for the element to become visible and returns immediately.<a name="locator-is-visible-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="locator-is-visible-return">#</a>

返回元素是否可见[visible](https://playwright.dev/python/docs/actionability#visible).

## locator.last<a name="locator-last">#</a>

- returns: \<[Locator](#locator)><a name="locator-last-return">#</a>

返回最后一个匹配元素的定位符.

## locator.locator(selector, **kwargs)<a name="locator-locator">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 解析DOM元素时使用的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="locator-locator-option-selector">#</a>

- `has` \<[Locator](#locator)> 对selector选中的元素进行再次匹配, 匹配目标中的子元素, 例如: 匹配子元素的`text=Playwright`的元素  `\<article>\<div>Playwright\</div>\</article>`.<a name="locator-locator-option-has">#</a>

    请注意，外部和内部定位器必须属于同一个 frame. 内部定位器不能包含 [FrameLocator](#framelocator).

- `has_text` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> 匹配包含指定文本的元素，可能在子元素或后代元素中,例如:`"Playwright"` 匹配 `\<article>\<div>Playwright\</div>\</article>`.<a name="locator-locator-option-has-text">#</a>

- returns: \<[Locator](#locator)><a name="locator-locator-return">#</a>

该方法在`Locator`的子树中查找与指定选择器匹配的元素.

## locator.nth(index)<a name="locator-nth">#</a>

- `index` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)><a name="locator-nth-option-index">#</a>
- returns: \<[Locator](#locator)><a name="locator-nth-return">#</a>

返回第n个匹配元素的定位符.

## locator.page<a name="locator-page">#</a>

- returns: \<[Page](#page)><a name="locator-page-return">#</a>

这个定位器所属的页面.

## locator.press(key, **kwargs)<a name="locator-press">#</a>

- `key` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要按下的`键名`或要生成的字符，如`ArrowLeft`或'a'.<a name="locator-press-option-key">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `keydown`和`keyup`之间的等待时间，单位是毫秒。默认为0.<a name="locator-press-option-delay">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="locator-press-option-no-wait-after">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-press-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-press-return">#</a>

聚焦元素，然后使用 [keyboard.down(key)](#keyboard-down) and [keyboard.up(key)](#keyboard-up).

key可以指定想要的 [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) 或是单个字符生成的文本,这里可以找到键值的超集。键的例子如下:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

还支持以下快捷键:`Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

按住`Shift`键将输入与大写键对应的文本.

如果`key`是单个字符，它是区分大小写的，因此值`a`和`A`将生成不同的文本.

也支持快捷键，如键:“Control+o”或键:“Control+Shift+T”。当用修饰符指定时，修饰符被按下并被保持，而随后的键被按下.

## locator.screenshot(**kwargs)<a name="locator-screenshot">#</a>

- `animations` \<"disabled"> 当设置为`"disabled"`时，停止CSS动画，CSS转换和Web动画。动画根据其持续时间得到不同的处理:<a name="locator-screenshot-option-animations">#</a>
    - 有限动画是快进到完成，所以他们会触发`transitionend`事件.
    - 无限动画被取消到初始状态，然后在屏幕截图后播放.
- `mask` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Locator](#locator)]> 指定在截屏时应该被屏蔽的定位器。被屏蔽的元素将被一个粉红色的框覆盖#FF00FF，完全覆盖该元素.<a name="locator-screenshot-option-mask">#</a>
- `omit_background` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 隐藏默认的白色背景，并允许透明捕捉屏幕截图。不适用于`jpeg`图像。默认值为`false`.<a name="locator-screenshot-option-omit-background">#</a>
- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 保存镜像的文件路径, 屏幕截图类型将从文件扩展名推断。如果path是一个相对路径，那么它是相对于当前工作目录解析的。如果没有提供路径，映像将不会被保存到磁盘.<a name="locator-screenshot-option-path">#</a>
- `quality` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 图像的质量，在0-100之间。不适用于png图像.<a name="locator-screenshot-option-quality">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-screenshot-option-timeout">#</a>
- `type` \<"png"|"jpeg">指定截图类型，默认为`png`.<a name="locator-screenshot-option-type">#</a>
- returns: \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)><a name="locator-screenshot-return">#</a>

返回带有捕获的截图的缓冲区.

这个方法等待[可操作性](https://playwright.dev/python/docs/actionability)检查，然后在截屏之前将元素滚动到视图中。如果元素与DOM分离，该方法将抛出一个错误.

## locator.scroll_into_view_if_needed(**kwargs)<a name="locator-scroll-into-view-if-needed">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-scroll-into-view-if-needed-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-scroll-into-view-if-needed-return">#</a>

这个方法等待[可操作性](https://playwright.dev/python/docs/actionability)检查，然后尝试滚动元素到视图中，除非它是完全可见的，由 [IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)的比率定义.

## locator.select_option(**kwargs)<a name="locator-select-option">#</a>

- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="locator-select-option-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="locator-select-option-option-no-wait-after">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-select-option-option-timeout">#</a>
- `element` \<[ElementHandle](#elementhandle)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[ElementHandle](#elementhandle)]> 要选择的选项。可选的.<a name="locator-select-option-option-element">#</a>
- `index` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)]> 按索引进行选择的选项。可选的.<a name="locator-select-option-option-index">#</a>
- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 按值选择的选项。如果`\<select>`具有多个属性，则选择所有给定的选项，否则只选择与传递的选项之一匹配的第一个选项。可选的.<a name="locator-select-option-option-value">#</a>
- `label` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 按标签进行选择的选项。如果`\<select>`具有多个属性，则选择所有给定的选项，否则只选择与传递的选项之一匹配的第一个选项。可选的.<a name="locator-select-option-option-label">#</a>
- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]><a name="locator-select-option-return">#</a>

这个方法等待[可操作性](https://playwright.dev/python/docs/actionability)检查，直到所有指定的选项都出现在`\<select>`元素中，然后选择这些选项.

如果目标元素不是`\<select>`元素，此方法将抛出一个错误。但是，如果该元素位于`\<label>`元素中，且该元素具有关联控件，则将使用该控件.

返回已成功选择的选项值的数组.

一旦选择了所有提供的选项，就触发一个更改和输入事件.

- Sync

```python
# single selection matching the value
element.select_option("blue")
# single selection matching both the label
element.select_option(label="blue")
# multiple selection
element.select_option(value=["red", "green", "blue"])
```

- Async

```python
# single selection matching the value
await element.select_option("blue")
# single selection matching the label
await element.select_option(label="blue")
# multiple selection
await element.select_option(value=["red", "green", "blue"])
```

```python
# sync

# single selection matching the value
element.select_option("blue")
# single selection matching both the value and the label
element.select_option(label="blue")
# multiple selection
element.select_option("red", "green", "blue")
# multiple selection for blue, red and second option
element.select_option(value="blue", { index: 2 }, "red")
```

## locator.select_text(**kwargs)<a name="locator-select-text">#</a>

- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="locator-select-text-option-force">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-select-text-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-select-text-return">#</a>

这个方法等待[可操作性](https://playwright.dev/python/docs/actionability)检查, 然后关注元素并选择其所有文本内容

## locator.set_checked(checked, **kwargs)<a name="locator-set-checked">#</a>

- `checked` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否选中或不选中复选框.<a name="locator-set-checked-option-checked">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="locator-set-checked-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="locator-set-checked-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="locator-set-checked-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-set-checked-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="locator-set-checked-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-set-checked-return">#</a>

这个方法通过执行以下步骤检查或取消检查一个元素:

1. 确保匹配的元素是一个复选框或单选输入。如果不是，则排除此方法.
2. 如果元素已经具有正确的选中状态，则该方法立即返回.
3. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
4. 如果需要，将元素滚动到视图中.
5. 使用 [page.mouse](#page-mouse) 单击元素的中心.
6. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.
7. 确保元素现在被选中或取消选中。如果不是，则抛出此方法.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## locator.set_input_files(files, **kwargs)<a name="locator-set-input-files">#</a>

- `files` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]|[List](https://docs.python.org/3/library/typing.html#typing.List)[[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]><a name="locator-set-input-files-option-files">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件名
    - `mimeType` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 文件类型
    - `buffer` \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> 文件内容
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="locator-set-input-files-option-no-wait-after">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-set-input-files-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-set-input-files-return">#</a>

这个方法期望元素指向一个输入元素 [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

将文件输入的值设置为这些文件路径或文件。如果某些`filepath`是相对路径，那么它们将相对于当前工作目录进行解析。对于空数组，清除选定的文件.

## locator.tap(**kwargs)<a name="locator-tap">#</a>

- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="locator-tap-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="locator-tap-option-modifiers">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="locator-tap-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="locator-tap-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-tap-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="locator-tap-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-tap-return">#</a>

这个方法通过执行以下步骤点击元素:

1. 等待元素的[可操作性](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项.
2. 如果需要，将元素滚动到视图中.
3. 点击页面中心或指定位置.
4. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.

如果元素在动作期间的任何时刻与DOM分离，此方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

> NOTE
>
> `element.tap()` 要求浏览器上下文的`hasTouch`选项设置为 True.

## locator.text_content(**kwargs)<a name="locator-text-content">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-text-content-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="locator-text-content-return">#</a>

Returns the `node.textContent`.

## locator.type(text, **kwargs)<a name="locator-type">#</a>

- `text` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要输入到焦点元素中的文本.<a name="locator-type-option-text">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 按键之间的等待时间，单位是毫秒。默认为0.<a name="locator-type-option-delay">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="locator-type-option-no-wait-after">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-type-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-type-return">#</a>

聚焦元素，然后为文本中的每个字符发送 `keydown`, `keypress`/`input`, and `keyup`  事件.

要按一个特殊的键，如 `Control` or `ArrowDown`, 使用[locator.press(key, **kwargs)](#locator-press).

- Sync

```python
element.type("hello") # types instantly
element.type("world", delay=100) # types slower, like a user
```

- Async

```python
await element.type("hello") # types instantly
await element.type("world", delay=100) # types slower, like a user
```

一个在文本框中输入然后提交表单的例子:

- Sync

```python
element = page.locator("input")
element.type("some text")
element.press("Enter")
```

- Async

```python
element = page.locator("input")
await element.type("some text")
await element.press("Enter")
```

## locator.uncheck(**kwargs)<a name="locator-uncheck">#</a>

- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="locator-uncheck-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="locator-uncheck-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="locator-uncheck-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-uncheck-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="locator-uncheck-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-uncheck-return">#</a>

这个方法通过执行以下步骤来检查元素:

1. 确保元素是一个复选框或单选输入。如果不是，则抛出此方法。如果元素已被选中，则此方法立即返回.
2. 等待元素的[可操作性](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项.
3. 如果需要，将元素滚动到视图中.
4. 使用 [page.mouse](#page-mouse) 单击元素的中心.
5. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.
6. 确保元素现在是未选中的。如果不是，则排除此方法.

如果元素在动作期间的任何时刻与DOM分离，此方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

## locator.wait_for(**kwargs)<a name="locator-wait-for">#</a>

- `state` \<"attached"|"detached"|"visible"|"hidden"> 默认为`"visible"`。可以是:<a name="locator-wait-for-option-state">#</a>
    - `'attached'` - 等待元素出现在DOM中.
    - `'detached'` - 等待元素在DOM中不存在.
    - `'visible'` - 等待元素有非空的边界框 且 没有 `visibility:hidden`.注意，没有任何内容或带有`display:none` 的元素有一个空的边界框，因此不被认为是可见的.
    - `'hidden'` - 等待元素从DOM中分离出来, 或有一个空的边界框或' visibility:hidden '。这与`“visible”`选项相反.
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="locator-wait-for-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="locator-wait-for-return">#</a>

当 locator 指定的元素满足状态选项时返回.

如果目标元素已经满足条件，则该方法立即返回。否则，将等待`超时`毫秒，直到满足条件.

- Sync

```python
order_sent = page.locator("#order-sent")
order_sent.wait_for()
```

- Async

```python
order_sent = page.locator("#order-sent")
await order_sent.wait_for()
```





# Mouse

Mouse类操作的是相对于视口左上角的CSS 像素.

每个`页面`对象都有自己的鼠标，可以通过 [page.mouse](#page-mouse).

- Sync

```python
# using ‘page.mouse’ to trace a 100x100 square.
page.mouse.move(0, 0)
page.mouse.down()
page.mouse.move(0, 100)
page.mouse.move(100, 100)
page.mouse.move(100, 0)
page.mouse.move(0, 0)
page.mouse.up()
```

- Async

```python
# using ‘page.mouse’ to trace a 100x100 square.
await page.mouse.move(0, 0)
await page.mouse.down()
await page.mouse.move(0, 100)
await page.mouse.move(100, 100)
await page.mouse.move(100, 0)
await page.mouse.move(0, 0)
await page.mouse.up()
```

- [mouse.click(x, y, **kwargs)](#mouse-click)
- [mouse.dblclick(x, y, **kwargs)](#mouse-dblclick)
- [mouse.down(**kwargs)](#mouse-down)
- [mouse.move(x, y, **kwargs)](#mouse-move)
- [mouse.up(**kwargs)](#mouse-up)
- [mouse.wheel(delta_x, delta_y)](#mouse-wheel)

## mouse.click(x, y, **kwargs)<a name="mouse-click">#</a>

- `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)><a name="mouse-click-option-x">#</a>
- `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)><a name="mouse-click-option-y">#</a>
- `button` \<"left"|"right"|"middle"> 默认左 `left`.<a name="mouse-click-option-button">#</a>
- `click_count` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 默认为1,详情查看  [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail).<a name="mouse-click-option-click-count">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `mousedown`和`mouseup`之间的等待时间，单位是毫秒。默认为0.<a name="mouse-click-option-delay">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="mouse-click-return">#</a>

 [mouse.move(x, y, **kwargs)](#mouse-move), [mouse.down(**kwargs)](#mouse-down), [mouse.up(**kwargs)](#mouse-up) 的三合一快捷键

## mouse.dblclick(x, y, **kwargs)<a name="mouse-dblclick">#</a>

- `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)><a name="mouse-dblclick-option-x">#</a>
- `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)><a name="mouse-dblclick-option-y">#</a>
- `button` \<"left"|"right"|"middle"> 默认左 `left`.<a name="mouse-dblclick-option-button">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `mousedown`和`mouseup`之间的等待时间，单位是毫秒。默认为0.<a name="mouse-dblclick-option-delay">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="mouse-dblclick-return">#</a>

 [mouse.move(x, y, **kwargs)](#mouse-move), [mouse.down(**kwargs)](#mouse-down), [mouse.up(**kwargs)](#mouse-up), [mouse.down(**kwargs)](#mouse-down) and [mouse.up(**kwargs)](#mouse-up) 的快捷键

## mouse.down(**kwargs)<a name="mouse-down">#</a>

- `button` \<"left"|"right"|"middle"> 默认左 `left`.<a name="mouse-down-option-button">#</a>
- `click_count` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 默认为1,详情查看  [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail).<a name="mouse-down-option-click-count">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="mouse-down-return">#</a>

发送一个 `mousedown` 事件.

## mouse.move(x, y, **kwargs)<a name="mouse-move">#</a>

- `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)><a name="mouse-move-option-x">#</a>
- `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)><a name="mouse-move-option-y">#</a>
- `steps` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 默认为1. 发送 `mousemove` 事件.<a name="mouse-move-option-steps">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="mouse-move-return">#</a>

发送一个 `mousemove` 事件.

## mouse.up(**kwargs)<a name="mouse-up">#</a>

- `button` \<"left"|"right"|"middle"> 默认左 `left`.<a name="mouse-up-option-button">#</a>
- `click_count` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 默认为1,详情查看  [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail).<a name="mouse-up-option-click-count">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="mouse-up-return">#</a>

发送一个 `mouseup` 事件.

## mouse.wheel(delta_x, delta_y)<a name="mouse-wheel">#</a>

- `delta_x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 像素水平滚动.<a name="mouse-wheel-option-delta-x">#</a>
- `delta_y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 垂直滚动的像素.<a name="mouse-wheel-option-delta-y">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="mouse-wheel-return">#</a>

发送一个 `wheel` 事件.

> NOTE
>
> 如果Wheel事件未被处理，则可能导致滚动，并且此方法在返回之前不会等待滚动完成



# Page

- extends: [EventEmitter](https://pyee.readthedocs.io/en/latest/#pyee.BaseEventEmitter)

页面提供了与[Browser](#browser)中的单个标签交互的方法，或在Chromium的[extension background page](https://developer.chrome.com/extensions/background_pages)。一个[Browser](#browser)实例可能有多个[Page](#page)实例

这个例子创建了一个页面，将它导航到一个URL，然后保存了一个截图:

- Sync

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    webkit = playwright.webkit
    browser = webkit.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://example.com")
    page.screenshot(path="screenshot.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    webkit = playwright.webkit
    browser = await webkit.launch()
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://example.com")
    await page.screenshot(path="screenshot.png")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

Page类会发出各种各样的事件(如下所述)，这些事件可以使用Node的任何本地[`EventEmitter`](https://nodejs.org/api/events.html#events_class_eventemitter)方法来处理，比如`on`、`once`或`removeListener `.

下面的例子记录了单个页面加载事件的消息:

```python
page.once("load", lambda: print("page loaded!"))
```

要取消订阅事件，请使用 `removeListener` 方法:

```python
def log_request(intercepted_request):
    print("a request was made:", intercepted_request.url)
page.on("request", log_request)
# sometime later...
page.remove_listener("request", log_request)
```

- [page.on("close")](#page-event-close)
- [page.on("console")](#page-event-console)
- [page.on("crash")](#page-event-crash)
- [page.on("dialog")](#page-event-dialog)
- [page.on("domcontentloaded")](#page-event-dom-content-loaded)
- [page.on("download")](#page-event-download)
- [page.on("filechooser")](#page-event-file-chooser)
- [page.on("frameattached")](#page-event-frame-attached)
- [page.on("framedetached")](#page-event-frame-detached)
- [page.on("framenavigated")](#page-event-frame-navigated)
- [page.on("load")](#page-event-load)
- [page.on("pageerror")](#page-event-page-error)
- [page.on("popup")](#page-event-popup)
- [page.on("request")](#page-event-request)
- [page.on("requestfailed")](#page-event-request-failed)
- [page.on("requestfinished")](#page-event-request-finished)
- [page.on("response")](#page-event-response)
- [page.on("websocket")](#page-event-web-socket)
- [page.on("worker")](#page-event-worker)
- [page.add_init_script(**kwargs)](#page-add-init-script)
- [page.add_script_tag(**kwargs)](#page-add-script-tag)
- [page.add_style_tag(**kwargs)](#page-add-style-tag)
- [page.bring_to_front()](#page-bring-to-front)
- [page.check(selector, **kwargs)](#page-check)
- [page.click(selector, **kwargs)](#page-click)
- [page.close(**kwargs)](#page-close)
- [page.content()](#page-content)
- [page.context](#page-context)
- [page.dblclick(selector, **kwargs)](#page-dblclick)
- [page.dispatch_event(selector, type, **kwargs)](#page-dispatch-event)
- [page.drag_and_drop(source, target, **kwargs)](#page-drag-and-drop)
- [page.emulate_media(**kwargs)](#page-emulate-media)
- [page.eval_on_selector(selector, expression, **kwargs)](#page-eval-on-selector)
- [page.eval_on_selector_all(selector, expression, **kwargs)](#page-eval-on-selector-all)
- [page.evaluate(expression, **kwargs)](#page-evaluate)
- [page.evaluate_handle(expression, **kwargs)](#page-evaluate-handle)
- [page.expect_console_message(**kwargs)](#page-wait-for-console-message)
- [page.expect_download(**kwargs)](#page-wait-for-download)
- [page.expect_event(event, **kwargs)](#page-wait-for-event)
- [page.expect_file_chooser(**kwargs)](#page-wait-for-file-chooser)
- [page.expect_navigation(**kwargs)](#page-wait-for-navigation)
- [page.expect_popup(**kwargs)](#page-wait-for-popup)
- [page.expect_request(url_or_predicate, **kwargs)](#page-wait-for-request)
- [page.expect_request_finished(**kwargs)](#page-wait-for-request-finished)
- [page.expect_response(url_or_predicate, **kwargs)](#page-wait-for-response)
- [page.expect_websocket(**kwargs)](#page-wait-for-web-socket)
- [page.expect_worker(**kwargs)](#page-wait-for-worker)
- [page.expose_binding(name, callback, **kwargs)](#page-expose-binding)
- [page.expose_function(name, callback)](#page-expose-function)
- [page.fill(selector, value, **kwargs)](#page-fill)
- [page.focus(selector, **kwargs)](#page-focus)
- [page.frame(**kwargs)](#page-frame)
- [page.frame_locator(selector)](#page-frame-locator)
- [page.frames](#page-frames)
- [page.get_attribute(selector, name, **kwargs)](#page-get-attribute)
- [page.go_back(**kwargs)](#page-go-back)
- [page.go_forward(**kwargs)](#page-go-forward)
- [page.goto(url, **kwargs)](#page-goto)
- [page.hover(selector, **kwargs)](#page-hover)
- [page.inner_html(selector, **kwargs)](#page-inner-html)
- [page.inner_text(selector, **kwargs)](#page-inner-text)
- [page.input_value(selector, **kwargs)](#page-input-value)
- [page.is_checked(selector, **kwargs)](#page-is-checked)
- [page.is_closed()](#page-is-closed)
- [page.is_disabled(selector, **kwargs)](#page-is-disabled)
- [page.is_editable(selector, **kwargs)](#page-is-editable)
- [page.is_enabled(selector, **kwargs)](#page-is-enabled)
- [page.is_hidden(selector, **kwargs)](#page-is-hidden)
- [page.is_visible(selector, **kwargs)](#page-is-visible)
- [page.locator(selector, **kwargs)](#page-locator)
- [page.main_frame](#page-main-frame)
- [page.opener()](#page-opener)
- [page.pause()](#page-pause)
- [page.pdf(**kwargs)](#page-pdf)
- [page.press(selector, key, **kwargs)](#page-press)
- [page.query_selector(selector, **kwargs)](#page-query-selector)
- [page.query_selector_all(selector)](#page-query-selector-all)
- [page.reload(**kwargs)](#page-reload)
- [page.route(url, handler, **kwargs)](#page-route)
- [page.screenshot(**kwargs)](#page-screenshot)
- [page.select_option(selector, **kwargs)](#page-select-option)
- [page.set_checked(selector, checked, **kwargs)](#page-set-checked)
- [page.set_content(html, **kwargs)](#page-set-content)
- [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout)
- [page.set_default_timeout(timeout)](#page-set-default-timeout)
- [page.set_extra_http_headers(headers)](#page-set-extra-http-headers)
- [page.set_input_files(selector, files, **kwargs)](#page-set-input-files)
- [page.set_viewport_size(viewport_size)](#page-set-viewport-size)
- [page.tap(selector, **kwargs)](#page-tap)
- [page.text_content(selector, **kwargs)](#page-text-content)
- [page.title()](#page-title)
- [page.type(selector, text, **kwargs)](#page-type)
- [page.uncheck(selector, **kwargs)](#page-uncheck)
- [page.unroute(url, **kwargs)](#page-unroute)
- [page.url](#page-url)
- [page.video](#page-video)
- [page.viewport_size](#page-viewport-size)
- [page.wait_for_event(event, **kwargs)](#page-wait-for-event-2)
- [page.wait_for_function(expression, **kwargs)](#page-wait-for-function)
- [page.wait_for_load_state(**kwargs)](#page-wait-for-load-state)
- [page.wait_for_selector(selector, **kwargs)](#page-wait-for-selector)
- [page.wait_for_timeout(timeout)](#page-wait-for-timeout)
- [page.wait_for_url(url, **kwargs)](#page-wait-for-url)
- [page.workers](#page-workers)
- [page.accessibility](#page-accessibility)
- [page.keyboard](#page-keyboard)
- [page.mouse](#page-mouse)
- [page.request](#page-request)
- [page.touchscreen](#page-touchscreen)

## page.on("close")<a name="page-event-close">#</a>

- type: \<[Page](#page)>

页面关闭时触发.

## page.on("console")<a name="page-event-console">#</a>

- type: \<[ConsoleMessage](#consolemessage)>

当页面中的JavaScript调用控制台API方法之一时触发，例如`console.log`或`console.dir`。当页面抛出错误或警告时也会触发.

传递到`console.log`的参数显示为事件处理程序上的参数.

一个处理控制台事件的例子:

- Sync

```python
def print_args(msg):
    for arg in msg.args:
        print(arg.json_value())

page.on("console", print_args)
page.evaluate("console.log('hello', 5, {foo: 'bar'})")
```

- Async

```python
async def print_args(msg):
    values = []
    for arg in msg.args:
        values.append(await arg.json_value())
    print(values)

page.on("console", print_args)
await page.evaluate("console.log('hello', 5, {foo: 'bar'})")
```

## page.on("crash")<a name="page-event-crash">#</a>

- type: \<[Page](#page)>

当页面崩溃时触发。如果试图分配过多的内存，浏览器页面可能会崩溃。当页面崩溃时，将抛出正在进行的和后续的操作.

处理崩溃最常见的方法是捕获一个异常:

- Sync

```python
try:
    # crash might happen during a click.
    page.click("button")
    # or while waiting for an event.
    page.wait_for_event("popup")
except Error as e:
    # when the page crashes, exception message contains "crash".
```

- Async

```python
try:
    # crash might happen during a click.
    await page.click("button")
    # or while waiting for an event.
    await page.wait_for_event("popup")
except Error as e:
    # when the page crashes, exception message contains "crash".
```

## page.on("dialog")<a name="page-event-dialog">#</a>

- type: \<[Dialog](#dialog)>

当JavaScript对话框出现时触发，例如 `alert`, `prompt`, `confirm` or `beforeunload`. 必须要么 [dialog.accept(**kwargs)](#dialog-accept) 要么[dialog.dismiss()](#dialog-dismiss) 对话框-否则页面会冻结等待对话框，像click这样的动作将永远不会结束.



> NOTE
>
> 当没有 [page.on("dialog")](#page-event-dialog) 监听器时，所有的对话框都会被自动取消.

## page.on("domcontentloaded")<a name="page-event-dom-content-loaded">#</a>

- type: \<[Page](#page)>

当发送 JavaScript [`DOMContentLoaded`](https://developer.mozilla.org/en-US/docs/Web/Events/DOMContentLoaded) 事件时触发.

## page.on("download")<a name="page-event-download">#</a>

- type: \<[Download](#download)>

附件下载开始时发出。用户可以通过传递的 [Download](#download) 实例访问已下载内容的基本文件操作.

## page.on("filechooser")<a name="page-event-file-chooser">#</a>

- type: \<[FileChooser](#filechooser)>

当一个文件选择器应该出现时发出，例如在单击 `\<input type=file>`. Playwright 可以通过使用[file_chooser.set_files(files, **kwargs)](#file-chooser-set-files) 设置输入文件来响应它.

```python
page.on("filechooser", lambda file_chooser: file_chooser.set_files("/tmp/myfile.pdf"))
```

## page.on("frameattached")<a name="page-event-frame-attached">#</a>

- type: \<[Frame](#frame)>

附加 frame 时触发.

## page.on("framedetached")<a name="page-event-frame-detached">#</a>

- type: \<[Frame](#frame)>

分离 frame 时触发.

## page.on("framenavigated")<a name="page-event-frame-navigated">#</a>

- type: \<[Frame](#frame)>

当一个frame 导航到一个新url时触发.

## page.on("load")<a name="page-event-load">#</a>

- type: \<[Page](#page)>

当分派JavaScript加载  [`load`](https://developer.mozilla.org/en-US/docs/Web/Events/load) 事件时触发

## page.on("pageerror")<a name="page-event-page-error">#</a>

- type: \<[Error](#error)>

当页面内发生未捕获的异常时触发.

## page.on("popup")<a name="page-event-popup">#</a>

- type: \<[Page](#page)>

当页面打开新选项卡或窗口时触发。这个事件是在 [browser_context.on("page")](#browser-context-event-page)之外触发的，但只针对与该页相关的弹出窗口.

该页面可用的最早时刻是当它已导航到初始url。例如，当用 `window.open('http://example.com')`打开一个弹出窗口时，这个事件将在网络请求"[http://example.com"](http://example.com"/) 完成并在弹出窗口中开始加载响应时触发.

- Sync

```python
with page.expect_event("popup") as page_info:
    page.evaluate("window.open('https://example.com')")
popup = page_info.value
print(popup.evaluate("location.href"))
```

- Async

```python
async with page.expect_event("popup") as page_info:
    page.evaluate("window.open('https://example.com')")
popup = await page_info.value
print(await popup.evaluate("location.href"))
```

> NOTE
>
> 使用[page.wait_for_load_state(**kwargs)](#page-wait-for-load-state) 等待页面到达特定的状态(在大多数情况下不需要它).

## page.on("request")<a name="page-event-request">#</a>

- type: \<[Request](#request)>

当页面发出请求时触发。[request](#request)对象是只读的。要拦截和修改请求，请参阅页面 [page.route(url, handler, **kwargs)](#page-route) or [browser_context.route(url, handler, **kwargs)](#browser-context-route).

## page.on("requestfailed")<a name="page-event-request-failed">#</a>

- type: \<[Request](#request)>

当请求失败时触发，例如超时.

> NOTE
>
> HTTP错误响应，如404或503，从HTTP的角度来看，仍然是成功的响应，因此请求将以 [page.on("requestfinished")](#page-event-request-finished) 事件完成，而不是[page.on("requestfailed")](#page-event-request-failed). 只有当客户端无法从服务器获得HTTP响应时，请求才会被认为失败，例如由于网络错误 net::ERR_FAILED.

## page.on("requestfinished")<a name="page-event-request-finished">#</a>

- type: \<[Request](#request)>

在下载响应体后，请求成功完成时触发。对于一个成功的响应，事件序列是 `request`, `response` and `requestfinished`.

## page.on("response")<a name="page-event-response">#</a>

- type: \<[Response](#response)>

当收到请求的[Response](#response)状态和报头时触发。对于一个成功的响应，事件序列是 `request`, `response` and `requestfinished`.

## page.on("websocket")<a name="page-event-web-socket">#</a>

- type: \<[WebSocket](#websocket)>

 [WebSocket](#websocket) 请求发送时触发.

## page.on("worker")<a name="page-event-worker">#</a>

- type: \<[Worker](#worker)>

当页面生成一个专用的 [WebWorker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) 时触发.

## page.add_init_script(**kwargs)<a name="page-add-init-script">#</a>

- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> JavaScript 文件的路径. 如果path是一个相对路径，那么它是相对于当前工作目录解析的。可选的.<a name="page-add-init-script-option-path">#</a>
- `script` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 在浏览器上下文中所有页面中计算的脚本。可选的.<a name="page-add-init-script-option-script">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-add-init-script-return">#</a>

添加一个脚本，该脚本将在以下场景之一中进行评估:

- 当页面被导航时.
- 当附加或导航子框架时。在这种情况下，脚本将在新附加的框架的上下文中计算.

在创建文档之后，但在运行文档的任何脚本之前，对脚本进行计算。这对于修改JavaScript环境是很有用的，例如 `Math.random`.

一个重写 `Math.random` 的例子:

```js
// preload.js
Math.random = () => 42;
```

- Sync

```python
# in your playwright script, assuming the preload.js file is in same directory
page.add_init_script(path="./preload.js"
```

- Async

```python
# in your playwright script, assuming the preload.js file is in same directory
await page.add_init_script(path="./preload.js")
```

> NOTE
>
> 通过 [browser_context.add_init_script(**kwargs)](#browser-context-add-init-script) and [page.add_init_script(**kwargs)](#page-add-init-script)安装的多个脚本的计算顺序没有定义.

## page.add_script_tag(**kwargs)<a name="page-add-script-tag">#</a>

- `content` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要注入帧的原始JavaScript内容.<a name="page-add-script-tag-option-content">#</a>
- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 要注入帧的JavaScript文件的路径,如果`path`是一个相对路径，那么它是相对于当前工作目录解析的.<a name="page-add-script-tag-option-path">#</a>
- `type` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> JS脚本类型。使用“module”来加载一个Javascript ES6模块。详情请参阅 [script](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) .<a name="page-add-script-tag-option-type">#</a>
- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要添加的脚本的url.<a name="page-add-script-tag-option-url">#</a>
- returns: \<[ElementHandle](#elementhandle)><a name="page-add-script-tag-return">#</a>

添加一个`\<script>` 标签到页面所需的url或内容. 当脚本的onload触发或脚本内容被注入帧时，返回添加的标签.

主frame [frame.add_script_tag(**kwargs)](#frame-add-script-tag) 的快捷方式.

## page.add_style_tag(**kwargs)<a name="page-add-style-tag">#</a>

- `content` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 原始的CSS内容注入到帧.<a name="page-add-style-tag-option-content">#</a>
- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 要注入帧的CSS文件的路径, 如果path是一个相对路径，那么它是相对于当前工作目录解析的.<a name="page-add-style-tag-option-path">#</a>
- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> URL of the `\<link>` tag.<a name="page-add-style-tag-option-url">#</a>
- returns: \<[ElementHandle](#elementhandle)><a name="page-add-style-tag-return">#</a>

添加一个 `\<link rel="stylesheet">` 标签到页面所需的url 或 `\<style type="text/css">` 标签时. 当样式表的onload触发时，或者当CSS内容被注入框架时，返回添加的标签.

主框架的 [frame.add_style_tag(**kwargs)](#frame-add-style-tag) 快捷方式.

## page.bring_to_front()<a name="page-bring-to-front">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-bring-to-front-return">#</a>

将页面放到前面(激活标签).

## page.check(selector, **kwargs)<a name="page-check">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-check-option-selector">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="page-check-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="page-check-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="page-check-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-check-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-check-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="page-check-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-check-return">#</a>

这个方法通过以下步骤检查元素匹配选择器::

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 确保匹配的元素是一个复选框或单选输入。如果不是，则排除此方法。如果元素已被选中，则该方法立即返回.
3. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
4. 如果需要，将元素滚动到视图中.
5. 使用 [page.mouse](#page-mouse) 单击元素的中心.
6. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.
7. 确保元素现在被选中。如果不是，则排除此方法.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

主框架 [frame.check(selector, **kwargs)](#frame-check) 的快捷方式.

## page.click(selector, **kwargs)<a name="page-click">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-click-option-selector">#</a>
- `button` \<"left"|"right"|"middle"> 默认左 `left`.<a name="page-click-option-button">#</a>
- `click_count` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 默认为1,详情查看  [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail).<a name="page-click-option-click-count">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `mousedown`和`mouseup`之间的等待时间，单位是毫秒。默认为0.<a name="page-click-option-delay">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="page-click-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="page-click-option-modifiers">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="page-click-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="page-click-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-click-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-click-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="page-click-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-click-return">#</a>

这个方法通过执行以下步骤点击元素匹配选择器:

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
3. 如果需要，将元素滚动到视图中.
4. 使用 [page.mouse](#page-mouse) 单击元素的中心, or the specified `position`.
5. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

主框架 [frame.click(selector, **kwargs)](#frame-click) 的快捷方式.

## page.close(**kwargs)<a name="page-close">#</a>

- `run_before_unload` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 默认为`false`。是否运行卸载前页面处理程序 [before unload](https://developer.mozilla.org/en-US/docs/Web/Events/beforeunload) .<a name="page-close-option-run-before-unload">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-close-return">#</a>

如果`run_before_unload` is `false`, 则不运行任何卸载处理程序，并等待关闭页面. 如果`run_before_unload` is `true` 该方法将运行卸载处理程序，但`不会等待`页面关闭.

默认情况下, `page.close()` 不会在卸载处理程序之前运行.

> NOTE
>
> 如果`run_before_unload` 被传递为true，一个 `beforeunload` 对话框可能会被调用，并且应该通过 [page.on("dialog")](#page-event-dialog) 事件手动处理.

## page.content()<a name="page-content">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="page-content-return">#</a>

获取页面的完整HTML内容，包括文档类型.

## page.context<a name="page-context">#</a>

- returns: \<[BrowserContext](#browsercontext)><a name="page-context-return">#</a>

获取页面所属的浏览器上下文.

## page.dblclick(selector, **kwargs)<a name="page-dblclick">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-dblclick-option-selector">#</a>
- `button` \<"left"|"right"|"middle"> 默认左 `left`.<a name="page-dblclick-option-button">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `mousedown`和`mouseup`之间的等待时间，单位是毫秒。默认为0.<a name="page-dblclick-option-delay">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="page-dblclick-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="page-dblclick-option-modifiers">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="page-dblclick-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="page-dblclick-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-dblclick-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-dblclick-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="page-dblclick-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-dblclick-return">#</a>

该方法通过执行以下步骤双击元素匹配选择器:

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
3. 如果需要，将元素滚动到视图中.
4. 使用 [page.mouse](#page-mouse) 方法,双击元素中心位置.
5. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.该方法执行以下步骤双击元素, 注意，如果`dblclick()`的第一次单击触发了一个导航事件，则该方法将抛出.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

> NOTE
>
> `page.dblclick()` 分发两个 `click` 事件和一个 `dblclick` 事件.

主框架 [frame.dblclick(selector, **kwargs)](#frame-dblclick) 的快捷方式.

## page.dispatch_event(selector, type, **kwargs)<a name="page-dispatch-event">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-dispatch-event-option-selector">#</a>
- `type` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> DOM事件类型:`"click"`， `"dragstart"`等.<a name="page-dispatch-event-option-type">#</a>
- `event_init` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 可选的特定于事件的初始化属性.<a name="page-dispatch-event-option-event-init">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-dispatch-event-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-dispatch-event-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-dispatch-event-return">#</a>

下面的代码片段分派元素上的`单击`事件。无论元素的可见性状态如何，单击都将被分派。这相当于调用[element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

- Sync

```python
page.dispatch_event("button#submit", "click")
```

- Async

```python
await page.dispatch_event("button#submit", "click")
```

在底层，它根据给定的类型创建一个事件实例，使用`event_init`属性初始化它，并在元素上分派它。默认情况下，事件是组合的、可取消的和冒泡的.

由于`event_init`是特定于事件的，请参考事件文档中的初始属性列表:

- [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
- [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
- [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
- [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
- [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
- [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
- [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)

如果你想要将活动对象传递到事件中，你也可以指定`jhandle`作为属性值:

- Sync

```python
# note you can only create data_transfer in chromium and firefox
data_transfer = page.evaluate_handle("new DataTransfer()")
page.dispatch_event("#source", "dragstart", { "dataTransfer": data_transfer })
```

- Async

```python
# note you can only create data_transfer in chromium and firefox
data_transfer = await page.evaluate_handle("new DataTransfer()")
await page.dispatch_event("#source", "dragstart", { "dataTransfer": data_transfer })
```

## page.drag_and_drop(source, target, **kwargs)<a name="page-drag-and-drop">#</a>

- `source` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="page-drag-and-drop-option-source">#</a>
- `target` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="page-drag-and-drop-option-target">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="page-drag-and-drop-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="page-drag-and-drop-option-no-wait-after">#</a>
- `source_position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 此时相对于元素填充框的左上角单击源元素。如果没有指定，则使用元素的某个可见点.<a name="page-drag-and-drop-option-source-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-drag-and-drop-option-strict">#</a>
- `target_position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 此时相对于元素填充框的左上角落在目标元素上。如果没有指定，则使用元素的某个可见点.<a name="page-drag-and-drop-option-target-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-drag-and-drop-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="page-drag-and-drop-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-drag-and-drop-return">#</a>

## page.emulate_media(**kwargs)<a name="page-emulate-media">#</a>

- `color_scheme` \<[NoneType](https://docs.python.org/3/library/constants.html#None)|"light"|"dark"|"no-preference"> 模拟`'prefers-colors-scheme'` 媒体特性，支持的值为 `'light'`, `'dark'`, `'no-preference'`. 传递`null`将禁用颜色方案仿真.<a name="page-emulate-media-option-color-scheme">#</a>

- `forced_colors` \<[NoneType](https://docs.python.org/3/library/constants.html#None)|"active"|"none"> 模拟`'forced-colors'` 媒体特性，支持的值为 `'active'` and `'none'`. 传递`null`将禁用强制颜色模拟.<a name="page-emulate-media-option-forced-colors">#</a>

    > NOTE
>
    > 它在WebKit中不支持，请在他们的问题跟踪器中查看 [here](https://bugs.webkit.org/show_bug.cgi?id=225281) .

- `media` \<[NoneType](https://docs.python.org/3/library/constants.html#None)|"screen"|"print"> 修改页面的CSS媒体类型。唯一允许的值是 `'screen'`, `'print'` and `null`. 传递`null`将禁用CSS媒体模拟.<a name="page-emulate-media-option-media">#</a>

- `reduced_motion` \<[NoneType](https://docs.python.org/3/library/constants.html#None)|"reduce"|"no-preference"> 模拟`'prefers-reduced-motion'` 媒体特性，支持的值为 `'reduce'`, `'no-preference'`. 传递`null`将禁用减少的运动仿真.<a name="page-emulate-media-option-reduced-motion">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-emulate-media-return">#</a>

这个方法通过media参数改变 `CSS media type` ,或者使用`colorScheme`参数改变 `'prefers-colors-scheme'` 的媒体特性.

- Sync

```python
page.evaluate("matchMedia('screen').matches")
# → True
page.evaluate("matchMedia('print').matches")
# → False

page.emulate_media(media="print")
page.evaluate("matchMedia('screen').matches")
# → False
page.evaluate("matchMedia('print').matches")
# → True

page.emulate_media()
page.evaluate("matchMedia('screen').matches")
# → True
page.evaluate("matchMedia('print').matches")
# → False
```

- Async

```python
await page.evaluate("matchMedia('screen').matches")
# → True
await page.evaluate("matchMedia('print').matches")
# → False

await page.emulate_media(media="print")
await page.evaluate("matchMedia('screen').matches")
# → False
await page.evaluate("matchMedia('print').matches")
# → True

await page.emulate_media()
await page.evaluate("matchMedia('screen').matches")
# → True
await page.evaluate("matchMedia('print').matches")
# → False
```

- Sync

```python
page.emulate_media(color_scheme="dark")
page.evaluate("matchMedia('(prefers-color-scheme: dark)').matches")
# → True
page.evaluate("matchMedia('(prefers-color-scheme: light)').matches")
# → False
page.evaluate("matchMedia('(prefers-color-scheme: no-preference)').matches")
```

- Async

```python
await page.emulate_media(color_scheme="dark")
await page.evaluate("matchMedia('(prefers-color-scheme: dark)').matches")
# → True
await page.evaluate("matchMedia('(prefers-color-scheme: light)').matches")
# → False
await page.evaluate("matchMedia('(prefers-color-scheme: no-preference)').matches")
# → False
```

## page.eval_on_selector(selector, expression, **kwargs)<a name="page-eval-on-selector">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="page-eval-on-selector-option-selector">#</a>
- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="page-eval-on-selector-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="page-eval-on-selector-option-arg">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-eval-on-selector-option-strict">#</a>
- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="page-eval-on-selector-return">#</a>

> CAUTION
>
> 此方法不等待元素通过可操作性检查，因此可能导致不稳定的测试。使用 [locator.evaluate(expression, **kwargs)](#locator-evaluate), 其它[Locator](#locator) 其他Locator助手方法或web优先断言.

该方法在页面中找到与指定选择器匹配的元素，并将其作为第一个参数传递给表达式。如果没有匹配该选择器的元素，该方法将抛出错误。返回表达式的值.

如果expression` 返回 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 则 [page.eval_on_selector(selector, expression, **kwargs)](#page-eval-on-selector) 将等待promise解析并返回它的值.

例子:

- Sync

```python
search_value = page.eval_on_selector("#search", "el => el.value")
preload_href = page.eval_on_selector("link[rel=preload]", "el => el.href")
html = page.eval_on_selector(".main-container", "(e, suffix) => e.outer_html + suffix", "hello")
```

- Async

```python
search_value = await page.eval_on_selector("#search", "el => el.value")
preload_href = await page.eval_on_selector("link[rel=preload]", "el => el.href")
html = await page.eval_on_selector(".main-container", "(e, suffix) => e.outer_html + suffix", "hello")
```

主框架 [frame.eval_on_selector(selector, expression, **kwargs)](#frame-eval-on-selector) 的快捷方式.

## page.eval_on_selector_all(selector, expression, **kwargs)<a name="page-eval-on-selector-all">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="page-eval-on-selector-all-option-selector">#</a>
- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="page-eval-on-selector-all-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="page-eval-on-selector-all-option-arg">#</a>
- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="page-eval-on-selector-all-return">#</a>

> NOTE
>
> 在大多数情况下， [locator.evaluate_all(expression, **kwargs)](#locator-evaluate-all), 其它 [Locator](#locator) 助手方法和 web-first断言做得更好.

该方法查找页面中与指定选择器匹配的所有元素，并将匹配元素的数组作为第一个参数传递给表达式。返回表达式调用的结果.

如果`expression`返回[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)，那么 [page.eval_on_selector_all(selector, expression, **kwargs)](#page-eval-on-selector-all) 将等待promise解析并返回它的值.

例子:

- Sync

```python
div_counts = page.eval_on_selector_all("div", "(divs, min) => divs.length >= min", 10)
```

- Async

```python
div_counts = await page.eval_on_selector_all("div", "(divs, min) => divs.length >= min", 10)
```

## page.evaluate(expression, **kwargs)<a name="page-evaluate">#</a>

- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="page-evaluate-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="page-evaluate-option-arg">#</a>
- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="page-evaluate-return">#</a>

返回表达式调用的值.

如果函数传递给 [page.evaluate(expression, **kwargs)](#page-evaluate) 返回 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 那么[page.evaluate(expression, **kwargs)](#page-evaluate) 将等待promise解析并返回它的值.

如果函数传递给 [page.evaluate(expression, **kwargs)](#page-evaluate) 返回一个不可序列化( non-[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description) ) 的值, 那么 [page.evaluate(expression, **kwargs)](#page-evaluate) 解析为`undefined`. Playwright 还支持传递一些附加值，不能通过`JSON`序列化: `-0`, `NaN`, `Infinity`, `-Infinity`.

将参数传递给表达式:

- Sync

```python
result = page.evaluate("([x, y]) => Promise.resolve(x * y)", [7, 8])
print(result) # prints "56"
```

- Async

```python
result = await page.evaluate("([x, y]) => Promise.resolve(x * y)", [7, 8])
print(result) # prints "56"
```

字符串也可以代替函数传入:

- Sync

```python
print(page.evaluate("1 + 2")) # prints "3"
x = 10
print(page.evaluate(f"1 + {x}")) # prints "11"
```

- Async

```python
print(await page.evaluate("1 + 2")) # prints "3"
x = 10
print(await page.evaluate(f"1 + {x}")) # prints "11"
```

可以将 [ElementHandle](#elementhandle) 实例作为参数传递给 [page.evaluate(expression, **kwargs)](#page-evaluate):

- Sync

```python
body_handle = page.evaluate("document.body")
html = page.evaluate("([body, suffix]) => body.innerHTML + suffix", [body_handle, "hello"])
body_handle.dispose()
```

- Async

```python
body_handle = await page.evaluate("document.body")
html = await page.evaluate("([body, suffix]) => body.innerHTML + suffix", [body_handle, "hello"])
await body_handle.dispose()
```

主框架 [frame.evaluate(expression, **kwargs)](#frame-evaluate) 的快捷方式.

## page.evaluate_handle(expression, **kwargs)<a name="page-evaluate-handle">#</a>

- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="page-evaluate-handle-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="page-evaluate-handle-option-arg">#</a>
- returns: \<[JSHandle](#jshandle)><a name="page-evaluate-handle-return">#</a>

以jhandle形式返回表达式调用的值. [JSHandle](#jshandle).

 [page.evaluate(expression, **kwargs)](#page-evaluate) and [page.evaluate_handle(expression, **kwargs)](#page-evaluate-handle) 之间唯一的区别是 [page.evaluate_handle(expression, **kwargs)](#page-evaluate-handle) 返回[JSHandle](#jshandle).

如果函数传递给 [page.evaluate_handle(expression, **kwargs)](#page-evaluate-handle) 返回一个 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 那么[page.evaluate_handle(expression, **kwargs)](#page-evaluate-handle) 将等待promise解析并返回它的值.

- Sync

```python
a_window_handle = page.evaluate_handle("Promise.resolve(window)")
a_window_handle # handle for the window object.
```

- Async

```python
a_window_handle = await page.evaluate_handle("Promise.resolve(window)")
a_window_handle # handle for the window object.
```

字符串也可以代替函数传入:

- Sync

```python
a_handle = page.evaluate_handle("document") # handle for the "document"
```

- Async

```python
a_handle = await page.evaluate_handle("document") # handle for the "document"
```

[JSHandle](#jshandle) 实例可以作为参数传递给 [page.evaluate_handle(expression, **kwargs)](#page-evaluate-handle):

- Sync

```python
a_handle = page.evaluate_handle("document.body")
result_handle = page.evaluate_handle("body => body.innerHTML", a_handle)
print(result_handle.json_value())
result_handle.dispose()
```

- Async

```python
a_handle = await page.evaluate_handle("document.body")
result_handle = await page.evaluate_handle("body => body.innerHTML", a_handle)
print(await result_handle.json_value())
await result_handle.dispose()
```

## page.expect_console_message(**kwargs)<a name="page-wait-for-console-message">#</a>

- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[ConsoleMessage](#consolemessage)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 接收 [ConsoleMessage](#consolemessage) 对象，并在等待应该解决时解析为真值.<a name="page-wait-for-console-message-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为`30000`(30秒)。通过0禁用超时。默认值可以通过使用[browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout)来更改.<a name="page-wait-for-console-message-option-timeout">#</a>
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)[[ConsoleMessage](#consolemessage)]><a name="page-wait-for-console-message-return">#</a>

执行操作并等待在页面中记录一个 [ConsoleMessage](#consolemessage) , 如果提供了`predicate`，则它将 [ConsoleMessage](#consolemessage) 值传递给 `predicate` 函数,并等待 `predicate(message)` 返回一个真值。如果页面在触发 [page.on("console")](#page-event-console) 事件之前关闭，将抛出一个错误.

## page.expect_download(**kwargs)<a name="page-wait-for-download">#</a>

- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[Download](#download)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 接收`Download`对象，并在等待应该解决时解析为true值.<a name="page-wait-for-download-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为`30000`(30秒)。通过0禁用超时。默认值可以通过使用[browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout)来更改.<a name="page-wait-for-download-option-timeout">#</a>
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)[[Download](#download)]><a name="page-wait-for-download-return">#</a>

执行操作并等待新的 [Download](#download). 如果提供了 provided, 它将 [Download](#download) 的值传递给 `predicate` 函数并等待 `predicate(download)`返回一个真值。如果页面在下载事件被触发之前关闭，将抛出一个错误.

## page.expect_event(event, **kwargs)<a name="page-wait-for-event">#</a>

- `event` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 事件名称，与通常传递给`*.on(event)`的名称相同.<a name="page-wait-for-event-option-event">#</a>
- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)> 接收事件数据，并在等待应该被解析时解析为真值.<a name="page-wait-for-event-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为`30000`(30秒)。通过0禁用超时。默认值可以通过使用[browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout)来更改.<a name="page-wait-for-event-option-timeout">#</a>
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)><a name="page-wait-for-event-return">#</a>

等待事件触发，并将其值传递给 predicate 函数. 当 predicate() 返回真值时返回。如果在触发事件之前页面已关闭，则将抛出一个错误。返回事件数据值.

- Sync

```python
with page.expect_event("framenavigated") as event_info:
    page.click("button")
frame = event_info.value
```

- Async

```python
async with page.expect_event("framenavigated") as event_info:
    await page.click("button")
frame = await event_info.value
```

## page.expect_file_chooser(**kwargs)<a name="page-wait-for-file-chooser">#</a>

- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[FileChooser](#filechooser)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 接收 [FileChooser](#filechooser) 对象，并在等待应该解决时解析为true值.<a name="page-wait-for-file-chooser-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为`30000`(30秒)。通过0禁用超时。默认值可以通过使用[browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout)来更改.<a name="page-wait-for-file-chooser-option-timeout">#</a>
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)[[FileChooser](#filechooser)]><a name="page-wait-for-file-chooser-return">#</a>

执行操作并等待创建一个新的 [FileChooser](#filechooser) . 如果提供了 provided,则它将 [FileChooser](#filechooser) 值传递给 `predicate` 函数，并等待 `predicate(fileChooser)` 返回一个真值。如果在打开文件选择器之前关闭该页，则将抛出一个错误.

## page.expect_navigation(**kwargs)<a name="page-wait-for-navigation">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>最大操作时间，单位为毫秒，默认为30秒，通过0表示禁止超时。默认值可以通过使用  [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout), [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来修改.<a name="page-wait-for-navigation-option-timeout">#</a>
- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[URL](https://en.wikipedia.org/wiki/URL)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 一个glob模式、regex模式或谓词，在等待导航时接收匹配的url。注意，如果参数是一个不带通配符的字符串，该方法将等待导航到与该字符串完全相等的URL.<a name="page-wait-for-navigation-option-url">#</a>
- `wait_until` \<"load"|"domcontentloaded"|"networkidle"|"commit"> 当认为操作成功时，默认为`load`。事件可以是:<a name="page-wait-for-navigation-option-wait-until">#</a>
    - `'domcontentloaded'` - 当`domcontentloaded`事件被触发时，认为操作已经完成.
    - `'load'` - 当触发`load`事件时，认为操作已经完成.
    - `'networkidle'` - 当至少`500毫秒`没有网络连接时，认为操作已经完成.
    - `'commit'` - 当接收到网络响应并开始加载文档时，认为操作已经完成.
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)[[Response](#response)]><a name="page-wait-for-navigation-return">#</a>

等待主框架导航并返回主资源响应。在多个重定向的情况下，导航将使用最后一个重定向的响应进行解析。如果导航到一个不同的锚或导航由于历史API的使用，导航将解析为null.

当页面导航到一个新的URL或重新加载时，这个问题就会解决。当您运行将间接导致页面导航的代码时，它非常有用。例:点击目标有一个`onclick`处理程序，通过`setTimeout`触发导航。考虑一下这个例子:

- Sync

```python
with page.expect_navigation():
    page.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
# Resolves after navigation has finished
```

- Async

```python
async with page.expect_navigation():
    await page.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
# Resolves after navigation has finished
```

> NOTE
>
> 使用 [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) 更改URL被视为导航.

主框架 [frame.expect_navigation(**kwargs)](#frame-wait-for-navigation)的快捷方式.

## page.expect_popup(**kwargs)<a name="page-wait-for-popup">#</a>

- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[Page](#page)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 接收 [Page](#page)对象，并在等待应该解决时解析为true值.<a name="page-wait-for-popup-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为`30000`(30秒)。通过0禁用超时。默认值可以通过使用[browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout)来更改.<a name="page-wait-for-popup-option-timeout">#</a>
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)[[Page](#page)]><a name="page-wait-for-popup-return">#</a>

执行动作并等待弹出 [Page](#page). 如果提供了 predicate ,它将 [Popup]的值传递给 `predicate` 函数,并等待 `predicate(page)` 返回一个真值。如果页面在弹出事件被触发之前关闭，将抛出一个错误.

## page.expect_request(url_or_predicate, **kwargs)<a name="page-wait-for-request">#</a>

- `url_or_predicate` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[Request](#request)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 请求URL字符串、regex或predicate接收 [Request](#request) 对象。当通过上下文选项提供了一个 `base_url` 并且传递的URL是一个路径时，它会通过 [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 构造函数合并.<a name="page-wait-for-request-option-url-or-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒，缺省值为30秒，通过`0`表示不允许超时。默认值可以通过使用 [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-wait-for-request-option-timeout">#</a>
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)[[Request](#request)]><a name="page-wait-for-request-return">#</a>

等待匹配的请求并返回它。有关事件的更多细节，请参阅等待事件 [waiting for event](https://playwright.dev/python/docs/events#waiting-for-event) .

- Sync

```python
with page.expect_request("http://example.com/resource") as first:
    page.click('button')
first_request = first.value

# or with a lambda
with page.expect_request(lambda request: request.url == "http://example.com" and request.method == "get") as second:
    page.click('img')
second_request = second.value
```

- Async

```python
async with page.expect_request("http://example.com/resource") as first:
    await page.click('button')
first_request = await first.value

# or with a lambda
async with page.expect_request(lambda request: request.url == "http://example.com" and request.method == "get") as second:
    await page.click('img')
second_request = await second.value
```

## page.expect_request_finished(**kwargs)<a name="page-wait-for-request-finished">#</a>

- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[Request](#request)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 接收 [Request](#request) 对象，并在等待应该解决时解析为true值.<a name="page-wait-for-request-finished-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为`30000`(30秒)。通过0禁用超时。默认值可以通过使用[browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout)来更改.<a name="page-wait-for-request-finished-option-timeout">#</a>
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)[[Request](#request)]><a name="page-wait-for-request-finished-return">#</a>

执行动作并等待一个[Request](#request) 完成加载. 如果提供了 predicate ,它将 [Request](#request)的值传递给 `predicate` 函数,并等待 `predicate(request)` 返回一个真值。如果页面在[page.on("requestfinished")](#page-event-request-finished) 事件之前关闭，将抛出一个错误.

## page.expect_response(url_or_predicate, **kwargs)<a name="page-wait-for-response">#</a>

- `url_or_predicate` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[Response](#response)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 请求URL字符串、regex或predicate接收 [Response](#response) 对象。当通过上下文选项提供了一个 `base_url` 并且传递的URL是一个路径时，它会通过 [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 构造函数合并.<a name="page-wait-for-response-option-url-or-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒，缺省值为30秒，通过`0`表示不允许超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-wait-for-response-option-timeout">#</a>
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)[[Response](#response)]><a name="page-wait-for-response-return">#</a>

返回匹配的响应。有关事件的更多细节，请参阅等待事件 [waiting for event](https://playwright.dev/python/docs/events#waiting-for-event) 

- Sync

```python
with page.expect_response("https://example.com/resource") as response_info:
    page.click("input")
response = response_info.value
return response.ok

# or with a lambda
with page.expect_response(lambda response: response.url == "https://example.com" and response.status == 200) as response_info:
    page.click("input")
response = response_info.value
return response.ok
```

- Async

```python
async with page.expect_response("https://example.com/resource") as response_info:
    await page.click("input")
response = await response_info.value
return response.ok

# or with a lambda
async with page.expect_response(lambda response: response.url == "https://example.com" and response.status == 200) as response_info:
    await page.click("input")
response = await response_info.value
return response.ok
```

## page.expect_websocket(**kwargs)<a name="page-wait-for-web-socket">#</a>

- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[WebSocket](#websocket)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 接收 [WebSocket](#websocket) 对象，并在等待应该解决时解析为true值.<a name="page-wait-for-web-socket-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为`30000`(30秒)。通过0禁用超时。默认值可以通过使用[browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout)来更改.<a name="page-wait-for-web-socket-option-timeout">#</a>
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)[[WebSocket](#websocket)]><a name="page-wait-for-web-socket-return">#</a>

执行操作并等待一个新的 [WebSocket](#websocket). 如果提供了 predicate ,它将 [WebSocket](#websocket)的值传递给 `predicate` 函数,并等待 `predicate(webSocket)` 返回一个真值。如果页面在WebSocket 事件被触发之前关闭，将抛出一个错误.

## page.expect_worker(**kwargs)<a name="page-wait-for-worker">#</a>

- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[Worker](#worker)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 接收 [Worker](#worker) 对象，并在等待应该解决时解析为true值.<a name="page-wait-for-worker-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为`30000`(30秒)。通过0禁用超时。默认值可以通过使用[browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout)来更改.<a name="page-wait-for-worker-option-timeout">#</a>
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)[[Worker](#worker)]><a name="page-wait-for-worker-return">#</a>

执行动作并等待一个新的 [Worker](#worker). 如果提供了 predicate ,它将 [Worker](#worker)的值传递给 `predicate` 函数,并等待 `predicate(worker)` 返回一个真值。如果页面在触发 worker 事件之前关闭，则将抛出一个错误.

## page.expose_binding(name, callback, **kwargs)<a name="page-expose-binding">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> window 对象上的函数名.<a name="page-expose-binding-option-name">#</a>
- `callback` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)> Playwright 的上下文中被调用的回调函数.<a name="page-expose-binding-option-callback">#</a>
- `handle` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否将参数作为句柄传递，而不是按值传递。当传递句柄时，只支持一个参数。当传递值时，支持多个参数.<a name="page-expose-binding-option-handle">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-expose-binding-return">#</a>

该方法为页面中每一个 frame 的窗口对象添加一个名为 `name` 的函数。当被调用时，函数执行回调并返回一个 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) ,该Promise解析为回调的返回值。如果回调返回一个 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 它将被等待.

`callback` 函数的第一个参数包含调用者的信息: `{ browserContext: BrowserContext, page: Page, frame: Frame }`.

查看[browser_context.expose_binding(name, callback, **kwargs)](#browser-context-expose-binding) 上下文级版本.

> NOTE
>
> Functions installed via [page.expose_binding(name, callback, **kwargs)](#page-expose-binding) survive navigations.

一个将页面URL暴露给页面中所有 frame 的例子:

- Sync

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    webkit = playwright.webkit
    browser = webkit.launch(headless=false)
    context = browser.new_context()
    page = context.new_page()
    page.expose_binding("pageURL", lambda source: source["page"].url)
    page.set_content("""
    \<script>
      async function onClick() {
        document.querySelector('div').textContent = await window.pageURL();
      }
    \</script>
    \<button onclick="onClick()">Click me\</button>
    \<div>\</div>
    """)
    page.click("button")

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    webkit = playwright.webkit
    browser = await webkit.launch(headless=false)
    context = await browser.new_context()
    page = await context.new_page()
    await page.expose_binding("pageURL", lambda source: source["page"].url)
    await page.set_content("""
    \<script>
      async function onClick() {
        document.querySelector('div').textContent = await window.pageURL();
      }
    \</script>
    \<button onclick="onClick()">Click me\</button>
    \<div>\</div>
    """)
    await page.click("button")

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

传递 element handle 的例子:

- Sync

```python
def print(source, element):
    print(element.text_content())

page.expose_binding("clicked", print, handle=true)
page.set_content("""
  \<script>
    document.addEventListener('click', event => window.clicked(event.target));
  \</script>
  \<div>Click me\</div>
  \<div>Or click me\</div>
""")
```

- Async

```python
async def print(source, element):
    print(await element.text_content())

await page.expose_binding("clicked", print, handle=true)
await page.set_content("""
  \<script>
    document.addEventListener('click', event => window.clicked(event.target));
  \</script>
  \<div>Click me\</div>
  \<div>Or click me\</div>
""")
```

## page.expose_function(name, callback)<a name="page-expose-function">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> window 对象上的函数名<a name="page-expose-function-option-name">#</a>
- `callback` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)> 回调函数，将在playwright的上下文中被调用.<a name="page-expose-function-option-callback">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-expose-function-return">#</a>

该方法在页面中每一frame 的`window`对象上添加一个名为 `name` 的函数. 当被调用时，函数执行回调并返回一个 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) ,该Promise解析为回调的返回值.

如果回调返回一个[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)，它将被等待

查看[browser_context.expose_function(name, callback)](#browser-context-expose-function) 用于上下文范围的公开函数

> NOTE
>
> Functions installed via [page.expose_function(name, callback)](#page-expose-function) survive navigations.

一个在页面中添加`sha256`函数的例子:

- Sync

```python
import hashlib
from playwright.sync_api import sync_playwright

def sha256(text):
    m = hashlib.sha256()
    m.update(bytes(text, "utf8"))
    return m.hexdigest()


def run(playwright):
    webkit = playwright.webkit
    browser = webkit.launch(headless=False)
    page = browser.new_page()
    page.expose_function("sha256", sha256)
    page.set_content("""
        \<script>
          async function onClick() {
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');
          }
        \</script>
        \<button onclick="onClick()">Click me\</button>
        \<div>\</div>
    """)
    page.click("button")

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
import hashlib
from playwright.async_api import async_playwright

def sha256(text):
    m = hashlib.sha256()
    m.update(bytes(text, "utf8"))
    return m.hexdigest()


async def run(playwright):
    webkit = playwright.webkit
    browser = await webkit.launch(headless=False)
    page = await browser.new_page()
    await page.expose_function("sha256", sha256)
    await page.set_content("""
        \<script>
          async function onClick() {
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');
          }
        \</script>
        \<button onclick="onClick()">Click me\</button>
        \<div>\</div>
    """)
    await page.click("button")

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

## page.fill(selector, value, **kwargs)<a name="page-fill">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-fill-option-selector">#</a>
- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> Value to fill for the `\<input>`, `\<textarea>` or `[contenteditable]` element.<a name="page-fill-option-value">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="page-fill-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="page-fill-option-no-wait-after">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-fill-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-fill-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-fill-return">#</a>

这个方法等待元素匹配选择器，等待[可操作性](https://playwright.dev/python/docs/actionability)检查,聚焦元素，填充它，并在填充后触发一个输入事件。请注意，您可以传递一个空字符串来清除输入字段.

如果目标元素不是 `\<input>`, `\<textarea>` or `[contenteditable]`, 此方法将抛出一个错误。但是，如果该元素位于`\<label>`元素中，且该元素具有关联控件，则该控件将被填充.

要发送细粒度的键盘事件，请使用 [page.type(selector, text, **kwargs)](#page-type).

主框架 [frame.fill(selector, value, **kwargs)](#frame-fill) 快捷方式.

## page.focus(selector, **kwargs)<a name="page-focus">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-focus-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-focus-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-focus-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-focus-return">#</a>

这个方法获取一个带有选择器的元素并聚焦于它。如果没有元素匹配选择器，该方法将等待，直到匹配元素出现在DOM中.

主框架 [frame.focus(selector, **kwargs)](#frame-focus) 快捷方式.

## page.frame(**kwargs)<a name="page-frame">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 在iframe的name属性中指定的frame名。可选的.<a name="page-frame-option-name">#</a>
- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[URL](https://en.wikipedia.org/wiki/URL)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 一个glob模式，regex模式或谓词接收frame 的[URL](https://en.wikipedia.org/wiki/URL)作为url对象。可选的 .<a name="page-frame-option-url">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Frame](#frame)><a name="page-frame-return">#</a>

返回匹配指定条件的frame。必须指定`name`或`url`.

```python
frame = page.frame(name="frame-name")
```

```python
frame = page.frame(url=r".*domain.*")
```

## page.frame_locator(selector)<a name="page-frame-locator">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 解析DOM元素时使用的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-frame-locator-option-selector">#</a>
- returns: \<[FrameLocator](#framelocator)><a name="page-frame-locator-return">#</a>

在使用iframes时，您可以创建一个帧定位器，该定位器将进入iframe并允许选择该iframe中的元素。下面的代码片段在id为 `my-frame`的iframe中定位到文本为"Submit"的元素，例如 `\<iframe id="my-frame">`:

- Sync

```python
locator = page.frame_locator("#my-iframe").locator("text=Submit")
locator.click()
```

- Async

```python
locator = page.frame_locator("#my-iframe").locator("text=Submit")
await locator.click()
```

## page.frames<a name="page-frames">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Frame](#frame)]><a name="page-frames-return">#</a>

附在页面上的所有frame的数组.

## page.get_attribute(selector, name, **kwargs)<a name="page-get-attribute">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-get-attribute-option-selector">#</a>
- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 属性名.<a name="page-get-attribute-option-name">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-get-attribute-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-get-attribute-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="page-get-attribute-return">#</a>

返回元素属性值.

## page.go_back(**kwargs)<a name="page-go-back">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>最大操作时间，单位为毫秒，默认为30秒，通过0表示禁止超时。默认值可以通过使用  [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout), [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来修改.<a name="page-go-back-option-timeout">#</a>
- `wait_until` \<"load"|"domcontentloaded"|"networkidle"|"commit"> 当认为操作成功时，默认为`load`。事件可以是:<a name="page-go-back-option-wait-until">#</a>
    - `'domcontentloaded'` - 当`domcontentloaded`事件被触发时，认为操作已经完成.
    - `'load'` - 当触发`load`事件时，认为操作已经完成.
    - `'networkidle'` - 当至少`500毫秒`没有网络连接时，认为操作已经完成.
    - `'commit'` - 当接收到网络响应并开始加载文档时，认为操作已经完成.
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Response](#response)><a name="page-go-back-return">#</a>

返回主资源响应。在多个重定向的情况下，导航将使用最后一个重定向的响应进行解析。如果不能返回，返回`null`.

导航到历史记录的前一页.

## page.go_forward(**kwargs)<a name="page-go-forward">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>最大操作时间，单位为毫秒，默认为30秒，通过0表示禁止超时。默认值可以通过使用  [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout), [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来修改.<a name="page-go-forward-option-timeout">#</a>
- `wait_until` \<"load"|"domcontentloaded"|"networkidle"|"commit"> 当认为操作成功时，默认为`load`。事件可以是:<a name="page-go-forward-option-wait-until">#</a>
    - `'domcontentloaded'` - 当`domcontentloaded`事件被触发时，认为操作已经完成.
    - `'load'` - 当触发`load`事件时，认为操作已经完成.
    - `'networkidle'` - 当至少`500毫秒`没有网络连接时，认为操作已经完成.
    - `'commit'` - 当接收到网络响应并开始加载文档时，认为操作已经完成.
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Response](#response)><a name="page-go-forward-return">#</a>

返回主资源响应。在多个重定向的情况下，导航将使用最后一个重定向的响应进行解析。如果不能前进，返回null.

导航到历史记录的下一页.

## page.goto(url, **kwargs)<a name="page-goto">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 页面导航到的url。url应该包括协议，例如 `https://`.当通过上下文选项提供了一个 `base_url` 并且传递的URL是一个路径时，它会通过 [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 构造函数合并.<a name="page-goto-option-url">#</a>
- `referer` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> referer头值。如果提供，它将优先于[page.set_extra_http_headers(headers)](#page-set-extra-http-headers)设置的referer头值.<a name="page-goto-option-referer">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>最大操作时间，单位为毫秒，默认为30秒，通过0表示禁止超时。默认值可以通过使用  [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout), [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来修改.<a name="page-goto-option-timeout">#</a>
- `wait_until` \<"load"|"domcontentloaded"|"networkidle"|"commit"> 当认为操作成功时，默认为`load`。事件可以是:<a name="page-goto-option-wait-until">#</a>
    - `'domcontentloaded'` - 当`domcontentloaded`事件被触发时，认为操作已经完成.
    - `'load'` - 当触发`load`事件时，认为操作已经完成.
    - `'networkidle'` - 当至少`500毫秒`没有网络连接时，认为操作已经完成.
    - `'commit'` - 当接收到网络响应并开始加载文档时，认为操作已经完成.
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Response](#response)><a name="page-goto-return">#</a>

返回主资源响应。在多个重定向的情况下，导航将使用最后一个重定向的响应进行解析.

如果以下情况，该方法将抛出一个错误::

- 有一个SSL错误(例如在自签名证书的情况下).
- 目标URL无效.
- 导航过程中超时.
- 远程服务器没有响应或不可达.
- main 资源加载失败.

当远程服务器返回任何有效的HTTP状态码时，该方法不会抛出错误，包括404 " not Found"和500 "Internal server error "。这些响应的状态代码可以通过调用[response.status](#response-status)来获取.

> NOTE
>
> 该方法要么抛出错误，要么返回主资源响应。唯一的例外是导航到`空白`或导航到相同的URL与不同的哈希，这将成功并返回null.

> NOTE
>
> 无头模式不支持PDF文档的导航。参见[upstream issue](https://bugs.chromium.org/p/chromium/issues/detail?id=761295).

主框架 [frame.goto(url, **kwargs)](#frame-goto) 的快捷方式

## page.hover(selector, **kwargs)<a name="page-hover">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-hover-option-selector">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="page-hover-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="page-hover-option-modifiers">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="page-hover-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-hover-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-hover-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="page-hover-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-hover-return">#</a>

该方法通过执行以下步骤悬停在元素匹配选择器上:

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
3. 如果需要，将元素滚动到视图中.
4. 使鼠标停在元素中心或指定位置上.
5. 等待发起的导航成功或失败，除非设置了`noWaitAfter`选项.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

主框架 [frame.hover(selector, **kwargs)](#frame-hover) 的快捷方式.

## page.inner_html(selector, **kwargs)<a name="page-inner-html">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-inner-html-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-inner-html-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-inner-html-option-timeout">#</a>
- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="page-inner-html-return">#</a>

Returns `element.innerHTML`.

## page.inner_text(selector, **kwargs)<a name="page-inner-text">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-inner-text-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-inner-text-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-inner-text-option-timeout">#</a>
- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="page-inner-text-return">#</a>

Returns `element.innerText`.

## page.input_value(selector, **kwargs)<a name="page-input-value">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-input-value-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-input-value-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-input-value-option-timeout">#</a>
- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="page-input-value-return">#</a>

返回以下元素的输入值 `\<input>` or `\<textarea>` or `\<select>` .排除非输入元素.

## page.is_checked(selector, **kwargs)<a name="page-is-checked">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-is-checked-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-is-checked-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-is-checked-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="page-is-checked-return">#</a>

返回元素是否被选中。如果元素不是复选框或单选输入则排除.

## page.is_closed()<a name="page-is-closed">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="page-is-closed-return">#</a>

表示该页面已关闭.

## page.is_disabled(selector, **kwargs)<a name="page-is-disabled">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-is-disabled-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-is-disabled-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-is-disabled-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="page-is-disabled-return">#</a>

返回该元素是否被禁用，与启用[enabled](https://playwright.dev/python/docs/actionability#enabled)相反.

## page.is_editable(selector, **kwargs)<a name="page-is-editable">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-is-editable-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-is-editable-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-is-editable-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="page-is-editable-return">#</a>

返回元素是否可编辑[editable](https://playwright.dev/python/docs/actionability#editable).

## page.is_enabled(selector, **kwargs)<a name="page-is-enabled">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-is-enabled-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-is-enabled-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-is-enabled-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="page-is-enabled-return">#</a>

返回元素是否被启用[enabled](https://playwright.dev/python/docs/actionability#enabled).

## page.is_hidden(selector, **kwargs)<a name="page-is-hidden">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-is-hidden-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-is-hidden-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `DEPRECATED`此选项将被忽略. [page.is_hidden(selector, **kwargs)](#page-is-hidden) 不会等待元素被隐藏并立即返回.<a name="page-is-hidden-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="page-is-hidden-return">#</a>

返回元素是否隐藏，与可见 [visible](https://playwright.dev/python/docs/actionability#visible)相反. 不匹配任何元素的选择器被认为是隐藏的.

## page.is_visible(selector, **kwargs)<a name="page-is-visible">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-is-visible-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-is-visible-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> **DEPRECATED** 此选项将被忽略. [page.is_visible(selector, **kwargs)](#page-is-visible) 不会等待元素变得可见并立即返回.<a name="page-is-visible-option-timeout">#</a>
- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="page-is-visible-return">#</a>

返回元素是否可见[visible](https://playwright.dev/python/docs/actionability#visible). 不匹配任何元素的选择器被认为不可见.

## page.locator(selector, **kwargs)<a name="page-locator">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 解析DOM元素时使用的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-locator-option-selector">#</a>

- `has` \<[Locator](#locator)> 对selector选中的元素进行再次匹配, 匹配目标中的子元素, 例如: 匹配子元素的`text=Playwright`的元素  `\<article>\<div>Playwright\</div>\</article>`.<a name="page-locator-option-has">#</a>

    请注意，外部和内部定位器必须属于同一个 frame. 内部定位器不能包含 [FrameLocator](#framelocator).

- `has_text` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)> 匹配包含指定文本的元素，可能在子元素或后代元素中,例如:`"Playwright"` 匹配 `\<article>\<div>Playwright\</div>\</article>`.<a name="page-locator-option-has-text">#</a>

- returns: \<[Locator](#locator)><a name="page-locator-return">#</a>

该方法返回一个元素定位器，可用于在页面上执行操作。在执行一个操作之前，Locator被立即解析为元素，因此同一定位器上的一系列操作实际上可以在不同的DOM元素上执行。如果这些动作之间的DOM结构发生了变化，就会发生这种情况.

主框架 [frame.locator(selector, **kwargs)](#frame-locator) 的快捷方式.

## page.main_frame<a name="page-main-frame">#</a>

- returns: \<[Frame](#frame)><a name="page-main-frame-return">#</a>

页面的主框架。页面保证有一个在导航期间持久存在的主框架.

## page.opener()<a name="page-opener">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Page](#page)><a name="page-opener-return">#</a>

返回弹出页面的 opener 其他的为空 如果 opener 已经关闭，则返回`null`.

## page.pause()<a name="page-pause">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-pause-return">#</a>

暂停脚本执行. Playwright 将停止执行脚本，等待用户在页面覆盖中按下 'Resume' 按钮，或者在DevTools控制台中调用 `playwright.resume()`.

用户可以在暂停时检查选择器或执行手动步骤。Resume将从暂停的位置继续运行原始脚本.

> NOTE
>
> 这个方法要求 Playwright 以 有头模式启动, 及 [browser_type.launch(**kwargs)](#browser-type-launch) 里 `headless=False`.

## page.pdf(**kwargs)<a name="page-pdf">#</a>

- `display_header_footer` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 显示页眉和页脚。默认值为 `false`.<a name="page-pdf-option-display-header-footer">#</a>
- `footer_template` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 打印页脚的HTML模板。应该使用与`header_template`相同的格式.<a name="page-pdf-option-footer-template">#</a>
- `format` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 论文格式。如果设置，优先级高于`宽度`或`高度`选项。默认为 'Letter'.<a name="page-pdf-option-format">#</a>
- `header_template` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 打印头的HTML模板。应该是有效的HTML标记，使用以下类注入打印值:<a name="page-pdf-option-header-template">#</a>
    - `'date'` 格式化打印日期
    - `'title'`文档标题
    - `'url'` 文档的位置
    - `'pageNumber'` 当前页码
    - `'totalPages'` 文件中的总页数
- `height` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 纸张高度，接受单位标记的值.<a name="page-pdf-option-height">#</a>
- `landscape` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 纸张朝向。默认值为 `false`.<a name="page-pdf-option-landscape">#</a>
- `margin` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 纸边距，默认为 none.<a name="page-pdf-option-margin">#</a>
    - `top` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 顶部空白，接受单位标记的值。默认值为 `0`.
    - `right` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 右边距，接受单位标记的值。默认值为 `0`.
    - `bottom` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>底部边距，接受用单位标记的值。默认值为 `0`.
    - `left` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 左边距，接受带有单位标记的值。默认值为 `0`.
- `page_ranges` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 打印的纸张范围，例如:  '1-5, 8, 11-13'. 默认为空字符串，这意味着打印所有页面.<a name="page-pdf-option-page-ranges">#</a>
- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> PDF文件保存到的路径. 如果path是一个相对路径，那么它是相对于当前工作目录解析的。如果没有提供路径，PDF将不会被保存到磁盘.<a name="page-pdf-option-path">#</a>
- `prefer_css_page_size` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 指定任何在`页面`中声明的 CSS 尺寸优先于在宽度、高度或格式选项中声明的 CSS 尺寸. 默认为 `false`, 它将缩放内容以适应纸张大小.<a name="page-pdf-option-prefer-css-page-size">#</a>
- `print_background` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 打印背景图形。默认值为 `false`.<a name="page-pdf-option-print-background">#</a>
- `scale` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 网页渲染的比例。默认为`1`。刻度必须在0.1到 2 之间.<a name="page-pdf-option-scale">#</a>
- `width` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>纸张宽度，接受单位标记的值.<a name="page-pdf-option-width">#</a>
- returns: \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)><a name="page-pdf-return">#</a>

返回PDF缓冲区.

> NOTE
>
> 生成pdf目前只支持铬无头模式.

`page.pdf()` 生成一个带有打印CSS媒体的PDF页面, 在调用`page.pdf()`之前,调用[page.emulate_media(**kwargs)](#page-emulate-media) 来生成带有屏幕媒体的pdf:

> NOTE
>
> 默认情况下, `page.pdf()` 会生成一个经过修改的pdf以供打印。使用 [`-webkit-print-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-print-color-adjust) 属性强制渲染精确的颜色.

- Sync

```python
# generates a pdf with "screen" media type.
page.emulate_media(media="screen")
page.pdf(path="page.pdf")
```

- Async

```python
# generates a pdf with "screen" media type.
await page.emulate_media(media="screen")
await page.pdf(path="page.pdf")
```

宽度、高度和边距选项接受用单位标记的值。未标记的值被视为像素.

几个例子:

- `page.pdf({width: 100})` - 打印宽度设置为100像素
- `page.pdf({width: '100px'})` - 打印宽度设置为100像素
- `page.pdf({width: '10cm'})` - 打印宽度设置为10厘米.

所有可能的单位是:

- `px` - 像素
- `in` - 英寸
- `cm` - 厘米
- `mm` - 毫米

格式选项如下:

- `Letter`: 8.5in x 11in
- `Legal`: 8.5in x 14in
- `Tabloid`: 11in x 17in
- `Ledger`: 17in x 11in
- `A0`: 33.1in x 46.8in
- `A1`: 23.4in x 33.1in
- `A2`: 16.54in x 23.4in
- `A3`: 11.7in x 16.54in
- `A4`: 8.27in x 11.7in
- `A5`: 5.83in x 8.27in
- `A6`: 4.13in x 5.83in

> NOTE
>
> `header_template` and `footer_template` 标记有以下限制: > 1. 模板内的脚本标记不会被计算. > 2. 页面样式在模板中是不可见的.

## page.press(selector, key, **kwargs)<a name="page-press">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-press-option-selector">#</a>
- `key` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要按下的`键名`或要生成的字符，如`ArrowLeft`或'a'.<a name="page-press-option-key">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> `keydown`和`keyup`之间的等待时间，单位是毫秒。默认为0.<a name="page-press-option-delay">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="page-press-option-no-wait-after">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-press-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-press-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-press-return">#</a>

聚焦元素，然后使用 [keyboard.down(key)](#keyboard-down) and [keyboard.up(key)](#keyboard-up).

key可以指定想要的 [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) 或是单个字符生成的文本,这里可以找到键值的超集。键的例子如下:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

还支持以下快捷键:`Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

按住`Shift`键将输入与大写键对应的文本.

如果`key`是单个字符，它是区分大小写的，因此值`a`和`A`将生成不同的文本.

也支持快捷键，如键:“Control+o”或键:“Control+Shift+T”。当用修饰符指定时，修饰符被按下并被保持，而随后的键被按下.

- Sync

```python
page = browser.new_page()
page.goto("https://keycode.info")
page.press("body", "A")
page.screenshot(path="a.png")
page.press("body", "ArrowLeft")
page.screenshot(path="arrow_left.png")
page.press("body", "Shift+O")
page.screenshot(path="o.png")
browser.close()
```

- Async

```python
page = await browser.new_page()
await page.goto("https://keycode.info")
await page.press("body", "A")
await page.screenshot(path="a.png")
await page.press("body", "ArrowLeft")
await page.screenshot(path="arrow_left.png")
await page.press("body", "Shift+O")
await page.screenshot(path="o.png")
await browser.close()
```

## page.query_selector(selector, **kwargs)<a name="page-query-selector">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="page-query-selector-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-query-selector-option-strict">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[ElementHandle](#elementhandle)><a name="page-query-selector-return">#</a>

> CAUTION
>
> 不鼓励使用 [ElementHandle](#elementhandle) 而是使用[Locator](#locator)对象和web优先断言

该方法查找页面中与指定选择器匹配的元素。如果没有元素匹配选择器，返回值解析为 `null`.若要等待页面上的元素，请使用[locator.wait_for(**kwargs)](#locator-wait-for).

主框架 [frame.query_selector(selector, **kwargs)](#frame-query-selector) 的快捷方式.

## page.query_selector_all(selector)<a name="page-query-selector-all">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="page-query-selector-all-option-selector">#</a>
- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[ElementHandle](#elementhandle)]><a name="page-query-selector-all-return">#</a>

> CAUTION
>
> 不鼓励使用 [ElementHandle](#elementhandle) 而是使用[Locator](#locator)对象和web优先断言

该方法查找页面中与指定选择器匹配的所有元素。如果没有元素匹配选择器，返回值解析为 `[]`.

主框架 [frame.query_selector_all(selector)](#frame-query-selector-all) 的快捷方式.

## page.reload(**kwargs)<a name="page-reload">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>最大操作时间，单位为毫秒，默认为30秒，通过0表示禁止超时。默认值可以通过使用  [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout), [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来修改.<a name="page-reload-option-timeout">#</a>
- `wait_until` \<"load"|"domcontentloaded"|"networkidle"|"commit"> 当认为操作成功时，默认为`load`。事件可以是:<a name="page-reload-option-wait-until">#</a>
    - `'domcontentloaded'` - 当`domcontentloaded`事件被触发时，认为操作已经完成.
    - `'load'` - 当触发`load`事件时，认为操作已经完成.
    - `'networkidle'` - 当至少`500毫秒`没有网络连接时，认为操作已经完成.
    - `'commit'` - 当接收到网络响应并开始加载文档时，认为操作已经完成.
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Response](#response)><a name="page-reload-return">#</a>

这个方法重新加载当前页面，就像用户触发了浏览器刷新一样。返回主资源响应。在多个重定向的情况下，导航将使用最后一个重定向的响应进行解析.

## page.route(url, handler, **kwargs)<a name="page-route">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[URL](https://en.wikipedia.org/wiki/URL)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 一个glob模式、regex模式或谓词在路由时接收要匹配的 [URL](https://en.wikipedia.org/wiki/URL). 当通过上下文选项提供了一个 `base_url` 并且传递的URL是一个路径时，它会通过 [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 构造函数合并.<a name="page-route-option-url">#</a>
- `handler` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[Route](#route), [Request](#request)]> handler函数路由请求.<a name="page-route-option-handler">#</a>
- `times` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 一个路由应该使用的频率。默认情况下，每次都会使用.<a name="page-route-option-times">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-route-return">#</a>

路由提供了修改由页面发出的网络请求的功能.

一旦路由被启用，每一个匹配url模式的请求都会停止，除非它被继续、完成或中止.

> NOTE
>
> 只有当响应是重定向时，才会为第一个url调用处理程序.

> NOTE
>
> [page.route(url, handler, **kwargs)](#page-route) 不会拦截被Service Worker拦截的请求. 查看[这个问题](https://github.com/microsoft/playwright/issues/1090). 我们建议在使用请求拦截时禁用 Service Workers . 通过 `await context.addInitScript(() => delete window.navigator.serviceWorker);`

一个简单的处理程序的例子，中止所有的图像请求:

- Sync

```python
page = browser.new_page()
page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
page.goto("https://example.com")
browser.close()
```

- Async

```python
page = await browser.new_page()
await page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
await page.goto("https://example.com")
await browser.close()
```

或者使用regex模式替换相同的代码片段:

- Sync

```python
page = browser.new_page()
page.route(re.compile(r"(\.png$)|(\.jpg$)"), lambda route: route.abort())
page.goto("https://example.com")
browser.close()
```

- Async

```python
page = await browser.new_page()
await page.route(re.compile(r"(\.png$)|(\.jpg$)"), lambda route: route.abort())
await page.goto("https://example.com")
await browser.close()
```

可以通过检查请求来决定路由操作。例如，mock所有包含post数据的请求，并保留所有其他请求的原样:

- Sync

```python
def handle_route(route):
  if ("my-string" in route.request.post_data)
    route.fulfill(body="mocked-data")
  else
    route.continue_()
page.route("/api/**", handle_route)
```

- Async

```python
def handle_route(route):
  if ("my-string" in route.request.post_data)
    route.fulfill(body="mocked-data")
  else
    route.continue_()
await page.route("/api/**", handle_route)
```

当请求匹配两个处理程序时,页面路由优先于浏览器上下文路由(使用 [browser_context.route(url, handler, **kwargs)](https://playwright.dev/python/docs/api/class-browsercontext#browser-context-route)设置) 

要移除带有其处理程序的路由，你可以使用 [page.unroute(url, **kwargs)](#page-unroute).

> NOTE
>
> 启用路由将禁用http缓存.

## page.screenshot(**kwargs)<a name="page-screenshot">#</a>

- `animations` \<"disabled"> 当设置为`"disabled"`时，停止CSS动画，CSS转换和Web动画。动画根据其持续时间得到不同的处理:<a name="page-screenshot-option-animations">#</a>
    - 有限动画是快进到完成，所以他们会触发`transitionend`事件.
    - 无限动画被取消到初始状态，然后在屏幕截图后播放.
- `clip` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)>指定对结果图像进行剪辑的对象。应该有以下字段:<a name="page-screenshot-option-clip">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 剪辑区域左上角的X坐标
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 剪辑区域左上角的Y坐标
    - `width` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 剪辑区域的宽度
    - `height` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 剪辑区域的高度
- `full_page` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，获取完整的可滚动页面的截图，而不是当前可见的视口。默认值为 `false`.<a name="page-screenshot-option-full-page">#</a>
- `mask` \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Locator](#locator)]> 指定在截屏时应该被屏蔽的定位器。被屏蔽的元素将被一个粉红色的框覆盖#FF00FF，完全覆盖该元素.<a name="page-screenshot-option-mask">#</a>
- `omit_background` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 隐藏默认的白色背景，并允许透明捕捉屏幕截图。不适用于`jpeg`图像。默认值为`false`.<a name="page-screenshot-option-omit-background">#</a>
- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 保存镜像的文件路径, 屏幕截图类型将从文件扩展名推断。如果path是一个相对路径，那么它是相对于当前工作目录解析的。如果没有提供路径，映像将不会被保存到磁盘.<a name="page-screenshot-option-path">#</a>
- `quality` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 图像的质量，在0-100之间。不适用于png图像.<a name="page-screenshot-option-quality">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-screenshot-option-timeout">#</a>
- `type` \<"png"|"jpeg">指定截图类型，默认为`png`.<a name="page-screenshot-option-type">#</a>
- returns: \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)><a name="page-screenshot-return">#</a>

返回带有捕获的截图的缓冲区.

## page.select_option(selector, **kwargs)<a name="page-select-option">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-select-option-option-selector">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="page-select-option-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="page-select-option-option-no-wait-after">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-select-option-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-select-option-option-timeout">#</a>
- `element` \<[ElementHandle](#elementhandle)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[ElementHandle](#elementhandle)]> 要选择的选项。可选的.<a name="page-select-option-option-element">#</a>
- `index` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)]> 按索引进行选择的选项。可选的.<a name="page-select-option-option-index">#</a>
- `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 按值选择的选项。如果`\<select>`具有多个属性，则选择所有给定的选项，否则只选择与传递的选项之一匹配的第一个选项。可选的.<a name="page-select-option-option-value">#</a>
- `label` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 按标签进行选择的选项。如果`\<select>`具有多个属性，则选择所有给定的选项，否则只选择与传递的选项之一匹配的第一个选项。可选的.<a name="page-select-option-option-label">#</a>
- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]><a name="page-select-option-return">#</a>

这个方法等待元素匹配选择器，等待[可操作性](https://playwright.dev/python/docs/actionability)检查，直到所有指定的选项都出现在`\<select>`元素中，并选择这些选项.

如果目标元素不是`\<select>`元素，此方法将抛出一个错误。但是，如果该元素位于`\<label>`元素中，且该元素具有关联控件，则将使用该控件.

返回已成功选择的选项值的数组.

一旦选择了所有提供的选项，就触发一个更改和输入事件.

- Sync

```python
# single selection matching the value
page.select_option("select#colors", "blue")
# single selection matching both the label
page.select_option("select#colors", label="blue")
# multiple selection
page.select_option("select#colors", value=["red", "green", "blue"])
```

- Async

```python
# single selection matching the value
await page.select_option("select#colors", "blue")
# single selection matching the label
await page.select_option("select#colors", label="blue")
# multiple selection
await page.select_option("select#colors", value=["red", "green", "blue"])
```

主框架 [frame.select_option(selector, **kwargs)](#frame-select-option) 的快捷方式.

## page.set_checked(selector, checked, **kwargs)<a name="page-set-checked">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-set-checked-option-selector">#</a>
- `checked` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否选中或不选中复选框.<a name="page-set-checked-option-checked">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="page-set-checked-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="page-set-checked-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="page-set-checked-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-set-checked-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-set-checked-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="page-set-checked-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-set-checked-return">#</a>

这个方法通过执行以下步骤检查或取消检查元素匹配选择器:

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 确保匹配的元素是一个复选框或单选输入。如果不是，则排除此方法.
3. 如果元素已经具有正确的选中状态，则该方法立即返回.
4. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
5. 如果需要，将元素滚动到视图中.
6. 使用 [page.mouse](#page-mouse) 单击元素的中心.
7. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.
8. 确保元素现在被选中或取消选中。如果不是，则抛出此方法.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

主框架 [frame.set_checked(selector, checked, **kwargs)](#frame-set-checked) 的快捷方式.

## page.set_content(html, **kwargs)<a name="page-set-content">#</a>

- `html` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要分配给页面的html标记.<a name="page-set-content-option-html">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>最大操作时间，单位为毫秒，默认为30秒，通过0表示禁止超时。默认值可以通过使用  [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout), [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来修改.<a name="page-set-content-option-timeout">#</a>
- `wait_until` \<"load"|"domcontentloaded"|"networkidle"|"commit"> 当认为操作成功时，默认为`load`。事件可以是:<a name="page-set-content-option-wait-until">#</a>
    - `'domcontentloaded'` - 当`domcontentloaded`事件被触发时，认为操作已经完成.
    - `'load'` - 当触发`load`事件时，认为操作已经完成.
    - `'networkidle'` - 当至少`500毫秒`没有网络连接时，认为操作已经完成.
    - `'commit'` - 当接收到网络响应并开始加载文档时，认为操作已经完成.
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-set-content-return">#</a>

## page.set_default_navigation_timeout(timeout)<a name="page-set-default-navigation-timeout">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大导航时间，以毫秒为单位<a name="page-set-default-navigation-timeout-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-set-default-navigation-timeout-return">#</a>

此设置将改变以下方法和相关快捷方式的默认最大导航时间:

- [page.go_back(**kwargs)](#page-go-back)
- [page.go_forward(**kwargs)](#page-go-forward)
- [page.goto(url, **kwargs)](#page-goto)
- [page.reload(**kwargs)](#page-reload)
- [page.set_content(html, **kwargs)](#page-set-content)
- [page.expect_navigation(**kwargs)](#page-wait-for-navigation)
- [page.wait_for_url(url, **kwargs)](#page-wait-for-url)

> NOTE
>
> [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout)优先于 [page.set_default_timeout(timeout)](#page-set-default-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) 和[browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout).

## page.set_default_timeout(timeout)<a name="page-set-default-timeout">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间(毫秒)<a name="page-set-default-timeout-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-set-default-timeout-return">#</a>

此设置将更改所有接受超时的方法的默认最大时间.

> NOTE
>
> [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) 优先于 [page.set_default_timeout(timeout)](#page-set-default-timeout).

## page.set_extra_http_headers(headers)<a name="page-set-extra-http-headers">#</a>

- `headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 包含每个请求发送的附加HTTP头的对象。所有头文件的值必须是字符串.<a name="page-set-extra-http-headers-option-headers">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-set-extra-http-headers-return">#</a>

额外的HTTP报头将随页面发起的每个请求一起发送.

> NOTE
>
> [page.set_extra_http_headers(headers)](#page-set-extra-http-headers) 不能保证传出请求中报头的顺序.

## page.set_input_files(selector, files, **kwargs)<a name="page-set-input-files">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-set-input-files-option-selector">#</a>
- `files` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]|[List](https://docs.python.org/3/library/typing.html#typing.List)[[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)|[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]><a name="page-set-input-files-option-files">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> File name
    - `mimeType` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> File type
    - `buffer` \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> File content
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="page-set-input-files-option-no-wait-after">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-set-input-files-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-set-input-files-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-set-input-files-return">#</a>

这个方法期望选择器指向一个[输入元素](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

将文件输入的值设置为这些文件路径或文件。如果某些`filepath`是相对路径，那么它们将相对于当前工作目录进行解析。对于空数组，清除选定的文件.

## page.set_viewport_size(viewport_size)<a name="page-set-viewport-size">#</a>

- `viewport_size` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="page-set-viewport-size-option-viewport-size">#</a>
    - `width` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面宽度(像素).
    - `height` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面高度(像素).
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-set-viewport-size-return">#</a>

在一个浏览器中有多个页面的情况下，每个页面可以有自己的视口大小。然而，[browser.new_context(**kwargs)](#browser-new-context) 允许在上下文中一次为所有页面设置视口大小(和更多).

[page.set_viewport_size(viewport_size)](#page-set-viewport-size) 将调整页面的大小. 很多网站不希望手机改变大小，所以你应该在导航到页面之前设置viewport的大小. [page.set_viewport_size(viewport_size)](#page-set-viewport-size) 也将重置屏幕大小，如果你需要更好地控制这些属性，使用 [browser.new_context(**kwargs)](#browser-new-context) 与屏幕和viewport参数.

- Sync

```python
page = browser.new_page()
page.set_viewport_size({"width": 640, "height": 480})
page.goto("https://example.com")
```

- Async

```python
page = await browser.new_page()
await page.set_viewport_size({"width": 640, "height": 480})
await page.goto("https://example.com")
```

## page.tap(selector, **kwargs)<a name="page-tap">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-tap-option-selector">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="page-tap-option-force">#</a>
- `modifiers` \<[List](https://docs.python.org/3/library/typing.html#typing.List)["Alt"|"Control"|"Meta"|"Shift"]> modifiers按键要按。确保在操作期间只按下这些修饰符，然后恢复当前的修饰符。如果未指定，则使用当前按下的修饰符.<a name="page-tap-option-modifiers">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="page-tap-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="page-tap-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-tap-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-tap-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="page-tap-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-tap-return">#</a>

这个方法通过执行以下步骤点击元素匹配选择器:

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
3. 如果需要，将元素滚动到视图中.
4. 点击页面中心或指定位置.
5. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

> NOTE
>
> [page.tap(selector, **kwargs)](#page-tap) 需要将浏览器上下文的 `has_touch` 选项设置为  true.

主框架 [frame.tap(selector, **kwargs)](#frame-tap) 的快捷方式.

## page.text_content(selector, **kwargs)<a name="page-text-content">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-text-content-option-selector">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-text-content-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-text-content-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="page-text-content-return">#</a>

Returns `element.textContent`.

## page.title()<a name="page-title">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="page-title-return">#</a>

返回页面标题. 主框架 [frame.title()](#frame-title) 的快捷方式.

## page.type(selector, text, **kwargs)<a name="page-type">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-type-option-selector">#</a>
- `text` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要输入到焦点元素中的文本.<a name="page-type-option-text">#</a>
- `delay` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 按键之间的等待时间，单位是毫秒。默认为0.<a name="page-type-option-delay">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="page-type-option-no-wait-after">#</a>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-type-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-type-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-type-return">#</a>

为文本中的每个字符发送  `keydown`, `keypress`/`input`, and `keyup` 事件. `page.type` can be used to send fine-grained keyboard events. To fill values in form fields, use [page.fill(selector, value, **kwargs)](#page-fill).

要按一个特殊的键，如`Control`或`ArrowDown`，使用 [keyboard.press(key, **kwargs)](#keyboard-press).

- Sync

```python
page.type("#mytextarea", "hello") # types instantly
page.type("#mytextarea", "world", delay=100) # types slower, like a user
```

- Async

```python
await page.type("#mytextarea", "hello") # types instantly
await page.type("#mytextarea", "world", delay=100) # types slower, like a user
```

主框架 [frame.type(selector, text, **kwargs)](#frame-type) 的快捷方式.

## page.uncheck(selector, **kwargs)<a name="page-uncheck">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 一个搜索元素的选择器。如果有多个元素满足选择器，将使用第一个元素。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors) .<a name="page-uncheck-option-selector">#</a>
- `force` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否绕过[actionability](https://playwright.dev/python/docs/actionability)检查。默认值为`false`.<a name="page-uncheck-option-force">#</a>
- `no_wait_after` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 启动导航的操作正在等待这些导航发生，并等待页面开始加载。你可以通过设置这个标志来选择不等待。只有在特殊情况下才需要这个选项，比如导航到不可访问的页面。默认值为`false`.<a name="page-uncheck-option-no-wait-after">#</a>
- `position` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)> 相对于元素填充框的左上角使用的一个点。如果没有指定，则使用元素的某个可见点.<a name="page-uncheck-option-position">#</a>
    - `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
    - `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-uncheck-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-uncheck-option-timeout">#</a>
- `trial` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 设置后，该方法只执行[actionability](https://playwright.dev/python/docs/actionability) 检查，并跳过操作。默认值为`false`。在元素准备好时再执行动作是很有用的.<a name="page-uncheck-option-trial">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-uncheck-return">#</a>

这个方法通过执行以下步骤取消对元素匹配选择器的检查:

1. 找到一个元素匹配选择器。如果没有，则等待直到匹配的元素被附加到DOM.
2. 确保匹配的元素是一个复选框或单选输入。如果不是，则排除此方法. If the element is already unchecked, this method returns immediately.
3. 等待匹配元素的[actionability](https://playwright.dev/python/docs/actionability)检查，除非设置了强制选项。如果在检查期间分离了元素，则会重试整个操作.
4. 如果需要，将元素滚动到视图中.
5. 使用 [page.mouse](#page-mouse) 单击元素的中心.
6. 等待已启动的导航成功或失败，除非设置了`no_wait_after`选项.
7. 确保元素现在是未选中的。如果不是，则排除此方法.

如果在指定的超时期间，所有步骤组合都没有完成，则该方法将抛出一个[TimeoutError](#timeouterror)。传递零超时将禁用此功能.

主框架 [frame.uncheck(selector, **kwargs)](#frame-uncheck) 的快捷方式.

## page.unroute(url, **kwargs)<a name="page-unroute">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[URL](https://en.wikipedia.org/wiki/URL)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 一个glob Pattern, regex Pattern或predicate在路由时接收要匹配的url.<a name="page-unroute-option-url">#</a>
- `handler` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[Route](#route), [Request](#request)]> Optional handler函数路由请求.<a name="page-unroute-option-handler">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-unroute-return">#</a>

移除使用 [page.route(url, handler, **kwargs)](#page-route) 创建的路由. 当未指定handler时，删除url的所有路由.

## page.url<a name="page-url">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="page-url-return">#</a>

主框架 [frame.url](#frame-url) 的快捷方式.

## page.video<a name="page-video">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Video](#video)><a name="page-video-return">#</a>

与此页相关联的视频对象.

## page.viewport_size<a name="page-viewport-size">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="page-viewport-size-return">#</a>
    - `width` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面宽度(像素).
    - `height` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 页面高度(像素).

## page.wait_for_event(event, **kwargs)<a name="page-wait-for-event-2">#</a>

- `event` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 事件名称，与通常传递给`*.on(event)`的名称相同.<a name="page-wait-for-event-2-option-event">#</a>
- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)> 接收事件数据，并在等待应该被解析时解析为真值.<a name="page-wait-for-event-2-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为`30000`(30秒)。通过0禁用超时。默认值可以通过使用[browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout)来更改.<a name="page-wait-for-event-2-option-timeout">#</a>
- returns: \<[Any](https://docs.python.org/3/library/typing.html#typing.Any)><a name="page-wait-for-event-2-return">#</a>

> NOTE
>
> 在大多数情况下，您应该使用 [page.expect_event(event, **kwargs)](#page-wait-for-event).

等待给定事件被触发. 如果提供了 predicate ,它将 event's的值传递给 `predicate` 函数,并等待 `predicate(event)` 返回一个真值。如果触发事件之前页面已关闭，则将抛出一个错误.

## page.wait_for_function(expression, **kwargs)<a name="page-wait-for-function">#</a>

- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="page-wait-for-function-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="page-wait-for-function-option-arg">#</a>
- `polling` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)|"raf"> 如果`polling`是'raf'，那么表达式会在`requestAnimationFrame`回调中持续执行。如果`polling`是一个数字，那么它将被视为执行函数的毫秒间隔。默认为`raf`.<a name="page-wait-for-function-option-polling">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，以毫秒为单位。默认为30000(30秒)。通过0禁用超时。默认值可以通过使用[browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout)来更改.<a name="page-wait-for-function-option-timeout">#</a>
- returns: \<[JSHandle](#jshandle)><a name="page-wait-for-function-return">#</a>

当表达式返回真值时返回。它解析为真值的`jshhandle`.

[page.wait_for_function(expression, **kwargs)](#page-wait-for-function) 可用于观察视口大小的变化:

- Sync

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    webkit = playwright.webkit
    browser = webkit.launch()
    page = browser.new_page()
    page.evaluate("window.x = 0; setTimeout(() => { window.x = 100 }, 1000);")
    page.wait_for_function("() => window.x > 0")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    webkit = playwright.webkit
    browser = await webkit.launch()
    page = await browser.new_page()
    await page.evaluate("window.x = 0; setTimeout(() => { window.x = 100 }, 1000);")
    await page.wait_for_function("() => window.x > 0")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

将参数传递给[page.wait_for_function(expression, **kwargs)](#page-wait-for-function)函数的 predicate :

- Sync

```python
selector = ".foo"
page.wait_for_function("selector => !!document.querySelector(selector)", selector)
```

- Async

```python
selector = ".foo"
await page.wait_for_function("selector => !!document.querySelector(selector)", selector)
```

主框架 [frame.wait_for_function(expression, **kwargs)](#frame-wait-for-function) 的快捷方式.

## page.wait_for_load_state(**kwargs)<a name="page-wait-for-load-state">#</a>

- `state` \<"load"|"domcontentloaded"|"networkidle"> 可选加载状态，等待，默认为`load`。如果在加载当前文档时已经达到该状态，该方法将立即进行解析。可以是:<a name="page-wait-for-load-state-option-state">#</a>
    - `'load'` - 等待`load`事件被触发.
    - `'domcontentloaded'` - 等待`domcontentloaded`事件被触发.
    - `'networkidle'` - 等待至少500毫秒没有网络连接.
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>最大操作时间，单位为毫秒，默认为30秒，通过0表示禁止超时。默认值可以通过使用  [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout), [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来修改.<a name="page-wait-for-load-state-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-wait-for-load-state-return">#</a>

当达到所需的加载状态时返回

当页面达到所需的加载状态时，此问题将被解决，默认情况下加载。该导航必须在调用此方法时已提交。如果当前文档已经达到了所需的状态，则立即进行解析.

- Sync

```python
page.click("button") # click triggers navigation.
page.wait_for_load_state() # the promise resolves after "load" event.
```

- Async

```python
await page.click("button") # click triggers navigation.
await page.wait_for_load_state() # the promise resolves after "load" event.
```

- Sync

```python
with page.expect_popup() as page_info:
    page.click("button") # click triggers a popup.
popup = page_info.value
 # Following resolves after "domcontentloaded" event.
popup.wait_for_load_state("domcontentloaded")
print(popup.title()) # popup is ready to use.
```

- Async

```python
async with page.expect_popup() as page_info:
    await page.click("button") # click triggers a popup.
popup = await page_info.value
 # Following resolves after "domcontentloaded" event.
await popup.wait_for_load_state("domcontentloaded")
print(await popup.title()) # popup is ready to use.
```

主框架 [frame.wait_for_load_state(**kwargs)](#frame-wait-for-load-state) 的快捷方式.

## page.wait_for_selector(selector, **kwargs)<a name="page-wait-for-selector">#</a>

- `selector` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要查询的选择器。有关更多细节，请参阅[working with selectors](https://playwright.dev/python/docs/selectors).<a name="page-wait-for-selector-option-selector">#</a>
- `state` \<"attached"|"detached"|"visible"|"hidden"> 默认为`"visible"`。可以是:<a name="page-wait-for-selector-option-state">#</a>
    - `'attached'` - 等待元素出现在DOM中.
    - `'detached'` - 等待元素在DOM中不存在.
    - `'visible'` - 等待元素有非空的边界框 且 没有 `visibility:hidden`.注意，没有任何内容或带有`display:none` 的元素有一个空的边界框，因此不被认为是可见的.
    - `'hidden'` - 等待元素从DOM中分离出来, 或有一个空的边界框或' visibility:hidden '。这与`“visible”`选项相反.
- `strict` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 当为true时，调用要求选择器解析为单个元素。如果给定的选择器解析为多于一个元素，调用将抛出一个异常.<a name="page-wait-for-selector-option-strict">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大时间，单位为毫秒，默认为30秒，通过`0`禁用超时。默认值可以通过使用 [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来更改.<a name="page-wait-for-selector-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[ElementHandle](#elementhandle)><a name="page-wait-for-selector-return">#</a>

当选择器指定的元素满足状态选项时返回。如果等待隐藏或分离，则返回`null`.

> NOTE
>
> Playwright 在执行动作前,会自动等待元素准备好。使用 [Locator](#locator) 对象和web-first断言可以使代码不需要等待选择器.

等待选择器满足状态选项 (要么从dom中出现/消失，要么变成可见/隐藏). 如果在调用方法选择器的时刻已经满足条件，则该方法将立即返回。如果选择器不满足超时毫秒的条件，函数将抛出.

此方法适用于多个导航:

- Sync

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    for current_url in ["https://google.com", "https://bbc.com"]:
        page.goto(current_url, wait_until="domcontentloaded")
        element = page.wait_for_selector("img")
        print("Loaded image: " + str(element.get_attribute("src")))
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    chromium = playwright.chromium
    browser = await chromium.launch()
    page = await browser.new_page()
    for current_url in ["https://google.com", "https://bbc.com"]:
        await page.goto(current_url, wait_until="domcontentloaded")
        element = await page.wait_for_selector("img")
        print("Loaded image: " + str(await element.get_attribute("src")))
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

## page.wait_for_timeout(timeout)<a name="page-wait-for-timeout">#</a>

- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 等待超时时间<a name="page-wait-for-timeout-option-timeout">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-wait-for-timeout-return">#</a>

等待给定超时(以毫秒为单位).

注意，`page.waitForTimeout()` 应该只用于调试。在生产中使用计时器的测试将是不可靠的。使用信号，如网络事件，选择器变得可见和其他.

- Sync

```python
# wait for 1 second
page.wait_for_timeout(1000)
```

- Async

```python
# wait for 1 second
await page.wait_for_timeout(1000)
```

主框架 [frame.wait_for_timeout(timeout)](#frame-wait-for-timeout)的快捷方式.

## page.wait_for_url(url, **kwargs)<a name="page-wait-for-url">#</a>

- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[Pattern](https://docs.python.org/3/library/re.html)|[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[URL](https://en.wikipedia.org/wiki/URL)]:[bool](https://docs.python.org/3/library/stdtypes.html)> 一个glob模式、regex模式或谓词，在等待导航时接收匹配的url。注意，如果参数是一个不带通配符的字符串，该方法将等待导航到与该字符串完全相等的URL.<a name="page-wait-for-url-option-url">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>最大操作时间，单位为毫秒，默认为30秒，通过0表示禁止超时。默认值可以通过使用  [browser_context.set_default_navigation_timeout(timeout)](#browser-context-set-default-navigation-timeout), [browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout), [page.set_default_navigation_timeout(timeout)](#page-set-default-navigation-timeout) or [page.set_default_timeout(timeout)](#page-set-default-timeout) 方法来修改.<a name="page-wait-for-url-option-timeout">#</a>
- `wait_until` \<"load"|"domcontentloaded"|"networkidle"|"commit"> 当认为操作成功时，默认为`load`。事件可以是:<a name="page-wait-for-url-option-wait-until">#</a>
    - `'domcontentloaded'` - 当`domcontentloaded`事件被触发时，认为操作已经完成.
    - `'load'` - 当触发`load`事件时，认为操作已经完成.
    - `'networkidle'` - 当至少`500毫秒`没有网络连接时，认为操作已经完成.
    - `'commit'` - 当接收到网络响应并开始加载文档时，认为操作已经完成.
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="page-wait-for-url-return">#</a>

等待主框架导航到给定的URL.

- Sync

```python
page.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
page.wait_for_url("**/target.html")
```

- Async

```python
await page.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
await page.wait_for_url("**/target.html")
```

主框架 [frame.wait_for_url(url, **kwargs)](#frame-wait-for-url) 的快捷方式.

## page.workers<a name="page-workers">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Worker](#worker)]><a name="page-workers-return">#</a>

此方法返回与该页面关联的所有专用 [WebWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) .

> NOTE
>
> 它不包含 ServiceWorkers

## page.accessibility<a name="page-accessibility">#</a>

- type: \<[Accessibility](#accessibility)>

## page.keyboard<a name="page-keyboard">#</a>

- type: \<[Keyboard](#keyboard)>

## page.mouse<a name="page-mouse">#</a>

- type: \<[Mouse](#mouse)>

## page.request<a name="page-request">#</a>

- type: \<[APIRequestContext](#apirequestcontext)>

与此页面相关的API测试助手。使用此API发出的请求将使用页面cookie.

## page.touchscreen<a name="page-touchscreen">#</a>

- type: \<[Touchscreen](#touchscreen)>





# Request

当页面向网络资源发送请求时，会触发以下事件序列 [Page](#page):

- [page.on("request")](#page-event-request) 当页面发出请求时.
- [page.on("response")](#page-event-response) 在/如果收到请求的响应状态和报头时触发.
- [page.on("requestfinished")](#page-event-request-finished) 在下载响应体并完成请求时触发.

如果请求在某一时刻失败，则会触发 [page.on("requestfailed")](#page-event-request-failed) 而不是'requestfinished'事件(可能也不是'response'事件).

> NOTE
>
> HTTP错误响应，如404或503，从HTTP的角度来看仍然是成功的响应，所以请求将通过'requestfinished'事件完成.

如果请求得到了一个“重定向”响应，该请求就会通过“requestfinished”事件成功完成，并向一个重定向url发出一个新请求.

- [request.all_headers()](#request-all-headers)
- [request.failure](#request-failure)
- [request.frame](#request-frame)
- [request.header_value(name)](#request-header-value)
- [request.headers](#request-headers)
- [request.headers_array()](#request-headers-array)
- [request.is_navigation_request()](#request-is-navigation-request)
- [request.method](#request-method)
- [request.post_data](#request-post-data)
- [request.post_data_buffer](#request-post-data-buffer)
- [request.post_data_json](#request-post-data-json)
- [request.redirected_from](#request-redirected-from)
- [request.redirected_to](#request-redirected-to)
- [request.resource_type](#request-resource-type)
- [request.response()](#request-response)
- [request.sizes()](#request-sizes)
- [request.timing](#request-timing)
- [request.url](#request-url)

## request.all_headers()<a name="request-all-headers">#</a>

- returns: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]><a name="request-all-headers-return">#</a>

一个包含与此请求相关的所有请求HTTP头的对象。头属性名称是小写的.

## request.failure<a name="request-failure">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="request-failure-return">#</a>

该方法返回`null`，除非请求失败，如requestfailed事件所报告的那样.

所有失败请求的日志记录示例:

```python
page.on("requestfailed", lambda request: print(request.url + " " + request.failure))
```

## request.frame<a name="request-frame">#</a>

- returns: \<[Frame](#frame)><a name="request-frame-return">#</a>

返回发起此请求的[Frame](#frame) .

## request.header_value(name)<a name="request-header-value">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 请求头名称.<a name="request-header-value-option-name">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="request-header-value-return">#</a>

返回与名称匹配的头的值。名称不区分大小写.

## request.headers<a name="request-headers">#</a>

- returns: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]><a name="request-headers-return">#</a>

**DEPRECATED** **由渲染引擎看到的不完整的头文件列表。**使用 [request.all_headers()](#request-all-headers) .

## request.headers_array()<a name="request-headers-array">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]><a name="request-headers-array-return">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 请求头名称.
    - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 请求头值.

包含与此请求相关的所有请求HTTP头的数组。与 [request.all_headers()](#request-all-headers)不同，头属性名称不是小写的。具有多个条目的头属性，例如`Set-Cookie`，在数组中会出现多次

## request.is_navigation_request()<a name="request-is-navigation-request">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="request-is-navigation-request-return">#</a>

这个请求是否驱动框架的导航.

## request.method<a name="request-method">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="request-method-return">#</a>

请求的方法(GET、POST等)

## request.post_data<a name="request-post-data">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="request-post-data-return">#</a>

请求的post body，如果有的话

## request.post_data_buffer<a name="request-post-data-buffer">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)><a name="request-post-data-buffer-return">#</a>

请求体以二进制形式(如果有的话)表示

## request.post_data_json<a name="request-post-data-json">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="request-post-data-json-return">#</a>

返回url编码的`form-urlencoded`和 JSON 解析后的请求体作为备用

当响应是 `application/x-www-form-urlencoded` 时，值的键/值对象将被返回。否则它将被解析为JSON

## request.redirected_from<a name="request-redirected-from">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Request](#request)><a name="request-redirected-from-return">#</a>

请求被服务器重定向到这个，如果有的话

当服务器响应重定向时， Playwright 创建一个新的[Request](#request) 对象。这两个请求由 `redirectedFrom()` and `redirectedTo()` 方法连接。当发生多个服务器重定向时，可以通过重复调用 `redirectedFrom()`来构造整个重定向链.

例如， `http://example.com` 网站跳转到 `https://example.com`:

- Sync

```python
response = page.goto("http://example.com")
print(response.request.redirected_from.url) # "http://example.com"
```

- Async

```python
response = await page.goto("http://example.com")
print(response.request.redirected_from.url) # "http://example.com"
```

如果网站 `https://google.com`没有重定向:

- Sync

```python
response = page.goto("https://google.com")
print(response.request.redirected_from) # None
```

- Async

```python
response = await page.goto("https://google.com")
print(response.request.redirected_from) # None
```

## request.redirected_to<a name="request-redirected-to">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Request](#request)><a name="request-redirected-to-return">#</a>

如果服务器响应重定向，浏览器发出的新请求.

这个方法与 [request.redirected_from](#request-redirected-from) 相反:

```python
assert request.redirected_from.redirected_to == request
```

## request.resource_type<a name="request-resource-type">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="request-resource-type-return">#</a>

包含呈现引擎感知到的请求资源类型. ResourceType 将是以下其中之一: `document`, `stylesheet`, `image`, `media`, `font`, `script`, `texttrack`, `xhr`, `fetch`, `eventsource`, `websocket`, `manifest`, `other`.

## request.response()<a name="request-response">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Response](#response)><a name="request-response-return">#</a>

返回匹配的[Response](#response) 对象，如果由于错误没有接收到响应，则返回`null`

## request.sizes()<a name="request-sizes">#</a>

- returns: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="request-sizes-return">#</a>
    - `requestBodySize` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 请求正文(POST数据负载)的大小，以字节为单位。如果没有正文，则设置为0.
    - `requestHeadersSize` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 从HTTP请求消息开始直到(包括)正文前的双CRLF的总字节数
    - `responseBodySize` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 接收到的响应体大小(编码后)，单位为字节
    - `responseHeadersSize` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 从HTTP响应消息开始到(包括)正文前的双CRLF的总字节数

返回给定请求的资源大小信息

## request.timing<a name="request-timing">#</a>

- returns: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="request-timing-return">#</a>
    - `startTime` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 请求开始时间，单位是毫秒，自UTC 1月1日1970 00:00:00开始
    - `domainLookupStart` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 浏览器启动资源域名查找的紧接时间。该值以相对于`startTime`的毫秒为单位给出，如果不可用则为-1.
    - `domainLookupEnd` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 浏览器启动资源域名查找后的即时时间。该值以相对于`startTime`的毫秒为单位给出，如果不可用则为-1.
    - `connectStart` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 用户代理开始建立与服务器的连接以检索资源之前的时间。该值以相对于`startTime`的毫秒为单位给出，如果不可用则为-1.
    - `secureConnectionStart` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 浏览器启动握手进程以确保当前连接安全的时间。该值以相对于`startTime`的毫秒为单位给出，如果不可用则为-1.
    - `connectEnd` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>用户代理开始建立与服务器的连接以检索资源之前的时间。该值以相对于`startTime`的毫秒为单位给出，如果不可用则为-1.
    - `requestStart` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 浏览器从服务器、缓存或本地资源开始请求资源的时间。该值以相对于`startTime`的毫秒为单位给出，如果不可用则为-1
    - `responseStart` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>浏览器从服务器、缓存或本地资源开始请求资源的时间。该值以相对于`startTime`的毫秒为单位给出，如果不可用则为-1
    - `responseEnd` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>浏览器接收到资源的最后一个字节后或传输连接关闭前的时间，以先到的那个为例。该值以相对于`startTime`的毫秒为单位给出，如果不可用则为-1

返回给定请求的资源计时信息。大多数计时值在响应时可用, `responseEnd` 在请求完成时可用. 详情查看 [Resource Timing API](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming).

- Sync

```python
with page.expect_event("requestfinished") as request_info:
    page.goto("http://example.com")
request = request_info.value
print(request.timing)
```

- Async

```python
async with page.expect_event("requestfinished") as request_info:
    await page.goto("http://example.com")
request = await request_info.value
print(request.timing)
```

## request.url<a name="request-url">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="request-url-return">#</a>

请求的URL.



# Response

[Response](#response) 表示页面接收的响应.

- [response.all_headers()](#response-all-headers)
- [response.body()](#response-body)
- [response.finished()](#response-finished)
- [response.frame](#response-frame)
- [response.header_value(name)](#response-header-value)
- [response.header_values(name)](#response-header-values)
- [response.headers](#response-headers)
- [response.headers_array()](#response-headers-array)
- [response.json()](#response-json)
- [response.ok](#response-ok)
- [response.request](#response-request)
- [response.security_details()](#response-security-details)
- [response.server_addr()](#response-server-addr)
- [response.status](#response-status)
- [response.status_text](#response-status-text)
- [response.text()](#response-text)
- [response.url](#response-url)

## response.all_headers()<a name="response-all-headers">#</a>

- returns: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]><a name="response-all-headers-return">#</a>

具有与此响应关联的所有响应HTTP头的对象

## response.body()<a name="response-body">#</a>

- returns: \<[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)><a name="response-body-return">#</a>

返回带有响应体的缓冲区

## response.finished()<a name="response-finished">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="response-finished-return">#</a>

等待此响应完成，总是返回`null`

## response.frame<a name="response-frame">#</a>

- returns: \<[Frame](#frame)><a name="response-frame-return">#</a>

返回发起此响应的 [Frame](#frame) .

## response.header_value(name)<a name="response-header-value">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 请求头名称.<a name="response-header-value-option-name">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="response-header-value-return">#</a>

返回与名称匹配的头的值。名称不区分大小写。如果多个报头有相同的名称(除了 `set-cookie`), 它们将被返回一个由`,`分隔的列表。对于 `set-cookie`, 使用`\n`分隔符. 如果没有找到对应的响应头，则返回`null`.

## response.header_values(name)<a name="response-header-values">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 请求头名称.<a name="response-header-values-option-name">#</a>
- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]><a name="response-header-values-return">#</a>

返回与名称匹配的头的所有值，例如 `set-cookie`. 名称不区分大小写

## response.headers<a name="response-headers">#</a>

- returns: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]><a name="response-headers-return">#</a>

**由渲染引擎看到的不完整的响应头列表。**建议使用 [response.all_headers()](#response-all-headers) .

## response.headers_array()<a name="response-headers-array">#</a>

- returns: \<[List](https://docs.python.org/3/library/typing.html#typing.List)[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)]><a name="response-headers-array-return">#</a>
    - `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 请求头名称.
    - `value` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 请求头值.

包含与此响应关联的所有请求HTTP头的数组。与 [response.all_headers()](#response-all-headers)不同，头文件名称不是小写的。具有多个条目的头文件，例如 `Set-Cookie`, 在数组中出现多次

## response.json()<a name="response-json">#</a>

- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="response-json-return">#</a>

返回响应体的JSON表示

如果响应体不能通过JSON.parse进行解析，则该方法将抛出.

## response.ok<a name="response-ok">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="response-ok-return">#</a>

包含一个布尔值，说明响应是否成功(状态在200-299之间).

## response.request<a name="response-request">#</a>

- returns: \<[Request](#request)><a name="response-request-return">#</a>

返回匹配的 [Request](#request) 对象.

## response.security_details()<a name="response-security-details">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="response-security-details-return">#</a>
    - `issuer` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> issuer字段的Common Name组件。从证书。这应该只用于信息目的。可选的
    - `protocol` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 所使用的TLS协议。(如TLS 1.3)。可选的
    - `subjectName` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> Subject字段的Common Name组件。这应该只用于信息目的。可选的。
    - `validFrom` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> Unix时间戳(以秒为单位)，指定此证书何时生效。可选的。
    - `validTo` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> Unix时间戳(以秒为单位)，指定证书何时失效。可选的

返回SSL和其他安全信息

## response.server_addr()<a name="response-server-addr">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)><a name="response-server-addr-return">#</a>
    - `ipAddress` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 服务器IPv4或IPV6地址
    - `port` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)>

返回服务器的IP地址和端口

## response.status<a name="response-status">#</a>

- returns: \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)><a name="response-status-return">#</a>

包含响应的状态码(例如，200表示成功)

## response.status_text<a name="response-status-text">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="response-status-text-return">#</a>

包含响应的状态文本(例如，通常一个“OK”表示成功)

## response.text()<a name="response-text">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="response-text-return">#</a>

返回响应体的文本表示形式

## response.url<a name="response-url">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="response-url-return">#</a>

包含响应的URL



# Route

当一个网络路由页面被设置为 [page.route(url, handler, **kwargs)](#page-route) or [browser_context.route(url, handler, **kwargs)](#browser-context-route),  route对象允许处理该路由

- [route.abort(**kwargs)](#route-abort)
- [route.continue_(**kwargs)](#route-continue)
- [route.fulfill(**kwargs)](#route-fulfill)
- [route.request](#route-request)

## route.abort(**kwargs)<a name="route-abort">#</a>

- `error_code` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 可选错误码。默认为 `failed`, 可能是以下其中之一:<a name="route-abort-option-error-code">#</a>
    - `'aborted'` - 操作被中止(由于用户操作)
    - `'accessdenied'` - 访问资源的权限，而不是网络，被拒绝
    - `'addressunreachable'` - IP地址不可达。这通常意味着没有到指定主机或网络的路由
    - `'blockedbyclient'` - 客户端选择阻塞请求
    - `'blockedbyresponse'` - 请求失败，因为响应是与不满足的需求一起交付的(例如'X-Frame-Options'和'Content-Security-Policy'祖先检查)
    - `'connectionaborted'` - 由于没有收到ACK而导致的连接超时.
    - `'connectionclosed'` - 连接被关闭(对应于一个TCP FIN).
    - `'connectionfailed'` - 连接尝试失败.
    - `'connectionrefused'` - 连接请求被拒绝.
    - `'connectionreset'` - 连接被重置(对应于TCP RST).
    - `'internetdisconnected'` - 网络连接中断.
    - `'namenotresolved'` - 无法解析主机名.
    - `'timedout'` - 操作超时.
    - `'failed'` - 发生了一个普遍的故障.
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="route-abort-return">#</a>

中止路由的请求

## route.continue_(**kwargs)<a name="route-continue">#</a>

- `headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 改变请求的HTTP头。头文件的值将被转换为字符串.<a name="route-continue-option-headers">#</a>
- `method` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 改变请求的方法(例如GET或POST)<a name="route-continue-option-method">#</a>
- `post_data` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> 改变请求的post数据<a name="route-continue-option-post-data">#</a>
- `url` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 如果设置改变请求的url。新URL必须具有与原始URL相同的协议.<a name="route-continue-option-url">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="route-continue-return">#</a>

用可选的覆盖继续路由的请求

- Sync

```python
def handle(route, request):
    # override headers
    headers = {
        **request.headers,
        "foo": "bar" # set "foo" header
        "origin": None # remove "origin" header
    }
    route.continue_(headers=headers)
}
page.route("**/*", handle)
```

- Async

```python
async def handle(route, request):
    # override headers
    headers = {
        **request.headers,
        "foo": "bar" # set "foo" header
        "origin": None # remove "origin" header
    }
    await route.continue_(headers=headers)
}
await page.route("**/*", handle)
```

## route.fulfill(**kwargs)<a name="route-fulfill">#</a>

- `body` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> 响应正文.<a name="route-fulfill-option-body">#</a>
- `content_type` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 设置`Content-Type`响应头.<a name="route-fulfill-option-content-type">#</a>
- `headers` \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)]> 响应头。头文件的值将被转换为字符串.<a name="route-fulfill-option-headers">#</a>
- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 响应的文件路径. 内容类型将从文件扩展名推断出来。如果path是一个相对路径，那么它是相对于当前工作目录解析的.<a name="route-fulfill-option-path">#</a>
- `response` \<[APIResponse](#apiresponse)> [APIResponse](#apiresponse) 满足路由的请求。响应的各个字段(如报头)可以使用fill选项覆盖.<a name="route-fulfill-option-response">#</a>
- `status` \<[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 响应状态码，默认为`200`.<a name="route-fulfill-option-status">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="route-fulfill-return">#</a>

用给定的响应来满足路由的请求

用`404`响应来完成所有请求的例子:

- Sync

```python
page.route("**/*", lambda route: route.fulfill(
    status=404,
    content_type="text/plain",
    body="not found!"))
```

- Async

```python
await page.route("**/*", lambda route: route.fulfill(
    status=404,
    content_type="text/plain",
    body="not found!"))
```

An example of serving static file:

- Sync

```python
page.route("**/xhr_endpoint", lambda route: route.fulfill(path="mock_data.json"))
```

- Async

```python
await page.route("**/xhr_endpoint", lambda route: route.fulfill(path="mock_data.json"))
```

## route.request<a name="route-request">#</a>

- returns: \<[Request](#request)><a name="route-request-return">#</a>

A request to be routed.



# Selectors

选择器可用于安装自定义选择器引擎。有关更多信息，请参见使用选择器 [Working with selectors](https://playwright.dev/python/docs/selectors) 

- [selectors.register(name, **kwargs)](#selectors-register)

## selectors.register(name, **kwargs)<a name="selectors-register">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 在选择器中作为前缀使用的名称，例如 `{name: 'foo'}` 启用`foo=myselectorbody` 选择器。只能包含 `[a-zA-Z0-9_]` 字符.<a name="selectors-register-option-name">#</a>
- `content_script` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否在独立的JavaScript环境中运行该选择器引擎。这个环境可以访问相同的DOM，但不能访问框架脚本中的任何JavaScript对象。默认值为 `false`. 请注意，当这个引擎与其他已注册的引擎一起使用时，不能保证作为一个内容脚本运行.<a name="selectors-register-option-content-script">#</a>
- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> JavaScript文件的路径. 如果path是一个相对路径，那么它是相对于当前工作目录解析的.<a name="selectors-register-option-path">#</a>
- `script` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>原始脚本内容.<a name="selectors-register-option-script">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="selectors-register-return">#</a>

注册选择器引擎的一个例子，它根据标签名查询元素:

- Sync

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    tag_selector = """
      {
          // Returns the first element matching given selector in the root's subtree.
          query(root, selector) {
              return root.querySelector(selector);
          },
          // Returns all elements matching given selector in the root's subtree.
          queryAll(root, selector) {
              return Array.from(root.querySelectorAll(selector));
          }
      }"""

    # Register the engine. Selectors will be prefixed with "tag=".
    playwright.selectors.register("tag", tag_selector)
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.set_content('\<div>\<button>Click me\</button>\</div>')

    # Use the selector prefixed with its name.
    button = page.locator('tag=button')
    # Combine it with other selector engines.
    page.click('tag=div >> text="Click me"')
    # Can use it in any methods supporting selectors.
    button_count = page.locator('tag=button').count()
    print(button_count)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    tag_selector = """
      {
          // Returns the first element matching given selector in the root's subtree.
          query(root, selector) {
              return root.querySelector(selector);
          },
          // Returns all elements matching given selector in the root's subtree.
          queryAll(root, selector) {
              return Array.from(root.querySelectorAll(selector));
          }
      }"""

    # Register the engine. Selectors will be prefixed with "tag=".
    await playwright.selectors.register("tag", tag_selector)
    browser = await playwright.chromium.launch()
    page = await browser.new_page()
    await page.set_content('\<div>\<button>Click me\</button>\</div>')

    # Use the selector prefixed with its name.
    button = await page.query_selector('tag=button')
    # Combine it with other selector engines.
    await page.click('tag=div >> text="Click me"')
    # Can use it in any methods supporting selectors.
    button_count = await page.locator('tag=button').count()
    print(button_count)
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
```



# TimeoutError

- extends: [Error](#error)

每当某些操作因超时而终止时，就会触发TimeoutError，例如 [locator.wait_for(**kwargs)](#locator-wait-for) or [browser_type.launch(**kwargs)](#browser-type-launch).

- Sync

```python
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    try:
      page.click("text=Example", timeout=100)
    except PlaywrightTimeoutError:
      print("Timeout!")
    browser.close()
```

- Async

```python
import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

async def run(playwright):
    browser = await playwright.chromium.launch()
    page = await browser.new_page()
    try:
      await page.click("text=Example", timeout=100)
    except PlaywrightTimeoutError:
      print("Timeout!")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
```



# Touchscreen

触摸屏类操作的是相对于视口左上角CSS像素。触屏上的方法只能在已经初始化并设置为true的浏览器上下文中使用

- [touchscreen.tap(x, y)](#touchscreen-tap)

## touchscreen.tap(x, y)<a name="touchscreen-tap">#</a>

- `x` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)><a name="touchscreen-tap-option-x">#</a>
- `y` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)><a name="touchscreen-tap-option-y">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="touchscreen-tap-return">#</a>

在位置(x,y)分派一个触摸开始和触摸结束事件.



# Tracing

API用于收集和保存 Playwright的痕迹. Playwright 跟踪可以在 Playwright 脚本运行后在 [Trace Viewer](https://playwright.dev/python/docs/trace-viewer) 中打开 

在执行操作之前开始记录跟踪。最后，停止跟踪并将其保存到一个文件中

- Sync

```python
browser = chromium.launch()
context = browser.new_context()
context.tracing.start(screenshots=True, snapshots=True)
page = context.new_page()
page.goto("https://playwright.dev")
context.tracing.stop(path = "trace.zip")
```

- Async

```python
browser = await chromium.launch()
context = await browser.new_context()
await context.tracing.start(screenshots=True, snapshots=True)
page = await context.new_page()
await page.goto("https://playwright.dev")
await context.tracing.stop(path = "trace.zip")
```

- [tracing.start(**kwargs)](#tracing-start)
- [tracing.start_chunk(**kwargs)](#tracing-start-chunk)
- [tracing.stop(**kwargs)](#tracing-stop)
- [tracing.stop_chunk(**kwargs)](#tracing-stop-chunk)

## tracing.start(**kwargs)<a name="tracing-start">#</a>

- `name` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)>如果指定了，跟踪将被保存到[browser_type.launch(**kwargs)](#browser-type-launch) 中指定的`traces_dir`文件夹中的文件中.<a name="tracing-start-option-name">#</a>
- `screenshots` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 跟踪时是否截图。截图是用来构建时间线预览的.<a name="tracing-start-option-screenshots">#</a>
- `snapshots` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 如果该选项为true，跟踪将<a name="tracing-start-option-snapshots">#</a>
    - 在每个动作上捕获DOM快照
    - 记录网络活动
- `sources` \<[bool](https://docs.python.org/3/library/stdtypes.html)> 是否包含跟踪动作的源文件.<a name="tracing-start-option-sources">#</a>
- `title` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要显示在跟踪查看器中的跟踪名称.<a name="tracing-start-option-title">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="tracing-start-return">#</a>

开始跟踪

- Sync

```python
context.tracing.start(name="trace", screenshots=True, snapshots=True)
page = context.new_page()
page.goto("https://playwright.dev")
context.tracing.stop(path = "trace.zip")
```

- Async

```python
await context.tracing.start(name="trace", screenshots=True, snapshots=True)
page = await context.new_page()
await page.goto("https://playwright.dev")
await context.tracing.stop(path = "trace.zip")
```

## tracing.start_chunk(**kwargs)<a name="tracing-start-chunk">#</a>

- `title` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要显示在跟踪查看器中的跟踪名称.<a name="tracing-start-chunk-option-title">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="tracing-start-chunk-return">#</a>

启动一个新的跟踪块。如果你想在同一个 [BrowserContext](#browsercontext), 上记录多个跟踪，只使用一次 [tracing.start(**kwargs)](#tracing-start) 然后使用 [tracing.start_chunk(**kwargs)](#tracing-start-chunk) and [tracing.stop_chunk(**kwargs)](#tracing-stop-chunk) 创建多个跟踪块.

- Sync

```python
context.tracing.start(name="trace", screenshots=True, snapshots=True)
page = context.new_page()
page.goto("https://playwright.dev")

context.tracing.start_chunk()
page.click("text=Get Started")
# Everything between start_chunk and stop_chunk will be recorded in the trace.
context.tracing.stop_chunk(path = "trace1.zip")

context.tracing.start_chunk()
page.goto("http://example.com")
# Save a second trace file with different actions.
context.tracing.stop_chunk(path = "trace2.zip")
```

- Async

```python
await context.tracing.start(name="trace", screenshots=True, snapshots=True)
page = await context.new_page()
await page.goto("https://playwright.dev")

await context.tracing.start_chunk()
await page.click("text=Get Started")
# Everything between start_chunk and stop_chunk will be recorded in the trace.
await context.tracing.stop_chunk(path = "trace1.zip")

await context.tracing.start_chunk()
await page.goto("http://example.com")
# Save a second trace file with different actions.
await context.tracing.stop_chunk(path = "trace2.zip")
```

## tracing.stop(**kwargs)<a name="tracing-stop">#</a>

- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 将跟踪导出到指定路径下的文件中.<a name="tracing-stop-option-path">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="tracing-stop-return">#</a>

停止跟踪

## tracing.stop_chunk(**kwargs)<a name="tracing-stop-chunk">#</a>

- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 将上次 [tracing.start_chunk(**kwargs)](#tracing-start-chunk) 调用后收集的跟踪信息导出到指定路径的文件中.<a name="tracing-stop-chunk-option-path">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="tracing-stop-chunk-return">#</a>

停止跟踪块。有关多个跟踪块的详细信息，请参阅 [tracing.start_chunk(**kwargs)](#tracing-start-chunk) 



# Video

当使用recordVideo选项创建浏览器上下文时，每个页面都有一个与之关联的视频对象

- Sync

```python
print(page.video.path())
```

- Async

```python
print(await page.video.path())
```

- [video.delete()](#video-delete)
- [video.path()](#video-path)
- [video.save_as(path)](#video-save-as)

## video.delete()<a name="video-delete">#</a>

- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="video-delete-return">#</a>

删除视频文件。如有必要，将等待视频完成

## video.path()<a name="video-path">#</a>

- returns: \<[pathlib.Path](https://realpython.com/python-pathlib/)><a name="video-path-return">#</a>

返回视频录制到的文件系统路径。在关闭浏览器上下文时，保证视频被写入文件系统。此方法在远程连接时抛出

## video.save_as(path)<a name="video-save-as">#</a>

- `path` \<[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [pathlib.Path](https://realpython.com/python-pathlib/)]> 视频应该保存的路径.<a name="video-save-as-option-path">#</a>
- returns: \<[NoneType](https://docs.python.org/3/library/constants.html#None)><a name="video-save-as-return">#</a>

将视频保存到用户指定的路径。在视频仍在播放或页面已关闭时调用此方法是安全的。此方法将一直等待，直到页面关闭并完全保存视频



# WebSocket

[WebSocket](#websocket) 表示页面中的WebSocket连接

- [web_socket.on("close")](#web-socket-event-close)
- [web_socket.on("framereceived")](#web-socket-event-frame-received)
- [web_socket.on("framesent")](#web-socket-event-frame-sent)
- [web_socket.on("socketerror")](#web-socket-event-socket-error)
- [web_socket.expect_event(event, **kwargs)](#web-socket-wait-for-event)
- [web_socket.is_closed()](#web-socket-is-closed)
- [web_socket.url](#web-socket-url)
- [web_socket.wait_for_event(event, **kwargs)](#web-socket-wait-for-event-2)

## web_socket.on("close")<a name="web-socket-event-close">#</a>

- type: \<[WebSocket](#websocket)>

websocket关闭时触发

## web_socket.on("framereceived")<a name="web-socket-event-frame-received">#</a>

- type: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)>
    - `payload` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> frame 有效负载

当websocket接收到一个frame 时触发.

## web_socket.on("framesent")<a name="web-socket-event-frame-sent">#</a>

- type: \<[Dict](https://docs.python.org/3/library/typing.html#typing.Dict)>
    - `payload` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)|[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)> frame 有效负载

当websocket发送一个frame 时触发

## web_socket.on("socketerror")<a name="web-socket-event-socket-error">#</a>

- type: \<[String]>

当websocket有错误时触发

## web_socket.expect_event(event, **kwargs)<a name="web-socket-wait-for-event">#</a>

- `event` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 事件名称，相同的将传递到 `webSocket.on(event)`.<a name="web-socket-wait-for-event-option-event">#</a>
- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)> 接收事件数据，并在等待应该被解析时解析为真值.<a name="web-socket-wait-for-event-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为`30000`(30秒)。通过0禁用超时。默认值可以通过使用[browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout)来更改.<a name="web-socket-wait-for-event-option-timeout">#</a>
- returns: \<[EventContextManager](https://docs.python.org/3/reference/datamodel.html#context-managers)><a name="web-socket-wait-for-event-return">#</a>

等待事件触发，并将其值传递给 predicate 函数.当 predicate 返回真值时返回。如果webSocket在事件被触发之前关闭，将抛出一个错误。返回事件数据值

## web_socket.is_closed()<a name="web-socket-is-closed">#</a>

- returns: \<[bool](https://docs.python.org/3/library/stdtypes.html)><a name="web-socket-is-closed-return">#</a>

web socket已经关闭

## web_socket.url<a name="web-socket-url">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="web-socket-url-return">#</a>

包含WebSocket的URL

## web_socket.wait_for_event(event, **kwargs)<a name="web-socket-wait-for-event-2">#</a>

- `event` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 事件名称，与通常传递给`*.on(event)`的名称相同.<a name="web-socket-wait-for-event-2-option-event">#</a>
- `predicate` \<[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)> 接收事件数据，并在等待应该被解析时解析为真值.<a name="web-socket-wait-for-event-2-option-predicate">#</a>
- `timeout` \<[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)> 最大等待时间，单位为毫秒。默认为`30000`(30秒)。通过0禁用超时。默认值可以通过使用[browser_context.set_default_timeout(timeout)](#browser-context-set-default-timeout)来更改.<a name="web-socket-wait-for-event-2-option-timeout">#</a>
- returns: \<[Any](https://docs.python.org/3/library/typing.html#typing.Any)><a name="web-socket-wait-for-event-2-return">#</a>

> NOTE
>
> 在大多数情况下，你应该使用 [web_socket.expect_event(event, **kwargs)](#web-socket-wait-for-event).

等待给定事件被触发. 如果提供了 predicate ,它将 event's的值传递给 `predicate` 函数,并等待 `predicate(event)` 返回一个真值。如果套接字在触发事件之前关闭，则将抛出一个错误



# Worker

Worker 类代表一个 [WebWorker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API). 在页面对象上发出Worker事件，以通知一个Worker创建。关闭事件在worker对象消失时被触发

```python
def handle_worker(worker):
    print("worker created: " + worker.url)
    worker.on("close", lambda: print("worker destroyed: " + worker.url))

page.on('worker', handle_worker)

print("current workers:")
for worker in page.workers:
    print("    " + worker.url)
```

- [worker.on("close")](#worker-event-close)
- [worker.evaluate(expression, **kwargs)](#worker-evaluate)
- [worker.evaluate_handle(expression, **kwargs)](#worker-evaluate-handle)
- [worker.url](#worker-url)

## worker.on("close")<a name="worker-event-close">#</a>

- type: \<[Worker](#worker)>

当这个专用的[WebWorker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) 被终止时触发.

## worker.evaluate(expression, **kwargs)<a name="worker-evaluate">#</a>

- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="worker-evaluate-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="worker-evaluate-option-arg">#</a>
- returns: \<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)><a name="worker-evaluate-return">#</a>

返回表达式的返回值.

如果函数传递给 [worker.evaluate(expression, **kwargs)](#worker-evaluate) 返回一个 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 则[worker.evaluate(expression, **kwargs)](#worker-evaluate) 将等待promise解析并返回它的值.

如果函数传递给 [worker.evaluate(expression, **kwargs)](#worker-evaluate) 返回一个不可序列化 non-[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description) 的值, 则[worker.evaluate(expression, **kwargs)](#worker-evaluate) 返回`undefined`. Playwright 还支持传递一些附加值，不能通过JSON序列化: `-0`, `NaN`, `Infinity`, `-Infinity`.

## worker.evaluate_handle(expression, **kwargs)<a name="worker-evaluate-handle">#</a>

- `expression` \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)> 要在浏览器上下文中计算的`JavaScript`表达式。如果它看起来像一个函数声明，它会被解释为一个函数。否则，作为表达式求值.<a name="worker-evaluate-handle-option-expression">#</a>
- `arg` \<[EvaluationArgument](https://playwright.dev/python/docs/evaluating#evaluation-argument)> 传递给`expression`的可选参数.<a name="worker-evaluate-handle-option-arg">#</a>
- returns: \<[JSHandle](#jshandle)><a name="worker-evaluate-handle-return">#</a>

返回表达式的返回值是一个 [JSHandle](#jshandle).

[worker.evaluate(expression, **kwargs)](#worker-evaluate) and [worker.evaluate_handle(expression, **kwargs)](#worker-evaluate-handle) 之间唯一的区别是 [worker.evaluate_handle(expression, **kwargs)](#worker-evaluate-handle) 返回[JSHandle](#jshandle).

如果函数传递给 [worker.evaluate_handle(expression, **kwargs)](#worker-evaluate-handle) 返回一个 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), 则[worker.evaluate_handle(expression, **kwargs)](#worker-evaluate-handle) 将等待promise解析并返回它的值.

## worker.url<a name="worker-url">#</a>

- returns: \<[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)><a name="worker-url-return">#</a>

