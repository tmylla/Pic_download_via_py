# Pic_download_via_py
本仓库包含下载网络图片的python代码，根据下载任务的复杂程度，依次提供：

- 已知pic_url
- 正则re解析html
- bs4解析html


​	

### 已知pic_url

dl_imgurl.py：已知图片url，无需解析html，例如“http://xyz.com/series-*.jpg”的批量下载。

```
	# 使用时修改以下两行信息即可
	prefix_url = 'http://xyz.com/series-'  # 同一类目下的图片url前缀
	n = 6  # 该类目下的图片总数
```

​	

### 通过re正则获取pic_url

dl_re_url.py：未知图片url，通过正则表达式获得pic_urls列表pic_list，然后依次下载图片。

```
    # 使用时修改url
    url = 'http://xyz.com/series'
    
    # 本正则式得到.jpg结尾的url,根据自己需要修改正则式
    picre = re.compile(r'[a-zA-z]+://[^\s]*\.jpg')  
```

​	

### 通过bs4获取pic_url

dl_bs4_url.py：未知图片url，Beautiful Soup解析获得pic_urls列表pic_list，然后依次下载图片。

**TO BE CONTINUED!**

​	

### 可能遇到的问题

- 网站反爬虫机制
- 常用正则式匹配
- js渲染的页面get不到完整页面源码
- 待解决...