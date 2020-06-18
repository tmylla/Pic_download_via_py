# Pic_download_via_py
本仓库包含下载网络图片的python代码，根据下载任务的复杂程度，依次提供：

- 已知pic_url
- 正则re解析html
- bs4解析html


​	

### 已知pic_url

[pd_img_url.py](https://github.com/tmylla/Pic_download_via_py/blob/master/pd_img_url.py)：已知图片url，无需解析html，例"http://xyz.com/series-*.jpg"的批量下载。

```
	# 使用时修改以下两行信息即可
	prefix_url = 'http://xyz.com/series-'  # 同一类目下的图片url前缀
	n = 6  # 该类目下的图片总数
```

​	

### 通过re正则获取pic_url

[pd_re_url.py](https://github.com/tmylla/Pic_download_via_py/blob/master/pd_re_url.py)：未知图片url，通过正则表达式获得`pic_urls`列表`pic_list`，然后依次下载图片。

```
    # 使用时修改url
    url = 'http://xyz.com/series'
    
    # 本正则式得到.jpg结尾的url,根据自己需要修改正则式
    picre = re.compile(r'[a-zA-z]+://[^\s]*\.jpg')  
```

​	

### 通过bs4获取pic_url

[pd_bs4_url.py](https://github.com/tmylla/Pic_download_via_py/blob/master/pd_bs4_url.py)：未知图片url，Beautiful Soup解析获得`pic_urls`列表`pic_list`，然后依次下载图片。

不同网站解析方式有所不同，[pd_bs4_url.py](https://github.com/tmylla/Pic_download_via_py/blob/master/pd_bs4_url.py)以豆瓣图片下载为例。

​	

### 可能遇到的问题

- 网站反爬虫机制

  1. User-Agent：模拟浏览器访问，添加后，服务器会认为是浏览器正常的请求。
  2. Referer：浏览器以此来判断你从哪一个网页跳转过来。
  3. ip伪装：构建ip池。
  4. Cookie伪装：cookie是服务器用来辨别你此时的状态的，每一次向服务器请求cookie都会随之更新。

- 常用正则式匹配

  - 强烈推荐[正则表达式30分钟入门教程](https://www.jb51.net/tools/zhengze.html)

- 网页的数据采用异步加载，如js渲染的页面或ajax加载的数据通过get不到完整页面源码

  - 一种方案是采用一些第三方的工具，模拟浏览器的行为加载数据，如Selenium、PhantomJs等。

  - 另外可以通过分析页面，找到请求借口，加载页面。其核心就是跟踪页面的交互行为 JS 触发调度，分析出有价值、有意义的核心调用（一般都是通过 JS 发起一个 HTTP 请求），然后我们使用 Python 直接访问逆向到的链接获取价值数据。通过"F12”进行分析，例如对于花瓣网，可以获得其链接"https://huaban.com/search/?q=%E7%9F%B3%E5%8E%9F%E9%87%8C%E7%BE%8E&kbk95lmw&page=4&per_page=20&wfl=1"，如下图所示，更改“page=*”得到其他页面，`request.urlopen(url).read()`读取网页。

    ![](https://i.loli.net/2020/06/18/kdWIXVEYfwPi4s3.png)

- 其他问题...