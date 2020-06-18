# 在pd_bs4_url.py中提到，requests.get直接访问原图地址无法会引发ET('edge rule triggered')
# 即b'{"code":"40310999","msg":"edge rule triggered"}'，无法访问到原图内容
# 原因在于每个原图需要带着该图前中等缩略图链接作为referer，为此手动添加reference即可下载原图

import os
import time
import requests
from bs4 import BeautifulSoup
from tqdm import trange


def get_html(url):
    """
    获取url页面html内容
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    html = requests.get(url, headers=headers).text

    return html


def parse_html(html_text):
    """
    BeautifulSoup解析单页html，将html页面包含的pic_url存入列表
    """
    soup = BeautifulSoup(html_text, 'html.parser')
    li = soup.find_all('div', attrs={'class':'cover'})
    # li中的一个元素如下：（每页共30张图片）
    # <div class="cover">
    # <a class="" href="https://movie.douban.com/celebrity/1016930/photo/2390809639/">
    # <img class="" src="https://img1.doubanio.com/view/photo/m/public/p2390809639.jpg"/>
    # </a>
    # </div>

    pic_list = []
    ref_list = []
    for link in li:
        pic_url = link.find('img').get('src')
        # 每一个pic_url形如：“https://img3.doubanio.com/view/photo/m/public/p2392209693.jpg”
        # 其中“/m/”表示中等缩略图，将其改为“/l/”变成较大的图进行保存；若改为“raw”则成为原图地址，但requests.get直接访问原图地址无法会引发ET('edge rule triggered')，
        # 无法访问到原图内容，本py程序为对此深入探究
        pic_url = pic_url.replace('/m/', '/raw/')
        pic_list.append(pic_url)

        ref_url = link.find('a').get('href')
        # 每一个ref_url形如：“https://movie.douban.com/celebrity/1016930/photo/2390809639/”，作为对应原图请求头“referer”
        ref_list.append(ref_url)

    return pic_list, ref_list


def download(referer, file_path, pic_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
        }
    headers['referer'] = referer
    r = requests.get(pic_url, headers=headers)
    with open(file_path, 'wb') as f:
        f.write(r.content)


def main():
    '从豆瓣下载石原里美图片，观察发现每页包含30张图片，其url按30递增，如下所示'
    pic_list = []
    ref_list = []
    for i in range(30,50):  # 总页数，本次下载前2页
        if i%5==0:
            time.sleep(20)


        url = 'https://movie.douban.com/celebrity/1016930/photos/?type=C&start=' + str(30*i) + '&sortby=like&size=a&subtype=a'
        html_text = get_html(url)
        pic_list = parse_html(html_text)[0]
        ref_list = parse_html(html_text)[1]


        os.makedirs('./pic/', exist_ok=True)  # 输出目录
        print('正在下载第%s页，本页共%s张图片。'%(i+1, len(pic_list)))

        for j in trange(len(pic_list)):
            pic_url = pic_list[j]

            file_name = pic_url.split('/')[-1].split('.')[0] + '.jpg'
            file_path = './pic/' + file_name

            referer = ref_list[j]
            download(referer, file_path, pic_url)


if __name__ == '__main__':
    main()