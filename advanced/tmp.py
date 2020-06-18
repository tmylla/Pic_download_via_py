from urllib import request
import json

url = 'https://huaban.com/search/?q=%E7%9F%B3%E5%8E%9F%E9%87%8C%E7%BE%8E&kbk95lmu&page=9&per_page=20&wfl=1'
t = request.urlopen(url).read()
# d = json.loads(t)['data']

print(t)