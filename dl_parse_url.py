# 未知图片url，通过正则表达式获得pic_urls

import os
import re
import requests
from tqdm import tqdm

def get_html(url):
    """
    获取url页面html内容
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
        }
    html = requests.get(url, headers=headers).text

    return html

def parse_html(html_text):
    """
    正则解析html，将html页面包含的pic_url存入列表
    """
    picre = re.compile(r'[a-zA-z]+://[^\s]*\.jpg')  # 本正则式得到.jpg结尾的url,根据自己需要修改正则式
    pic_list = re.findall(picre, html_text)

    return pic_list

def download(file_path, pic_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
        }
    r = requests.get(pic_url, headers=headers)
    with open(file_path, 'wb') as f:
        f.write(r.content)

def main():
    html_text = get_html('http://xyz.com/series')
    pic_list = parse_html(html_text)

    os.makedirs('./pic/', exist_ok=True)  # 输出目录
    for pic_url in tqdm(pic_list[:10]):
        file_name = pic_url.split('/')[-1]
        file_path = './pic/' + file_name

        download(file_path, pic_url)


if __name__ == '__main__':
    main()