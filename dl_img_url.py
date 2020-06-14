# 已知图片url，无需解析html，例如http://xyz.com/series-*(1,2..N).jpg

import os
import requests
import random
import time
from tqdm import tqdm


def download(file_path, picture_url):
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE",
		}
	r = requests.get(picture_url, headers=headers)
	with open(file_path, 'wb') as f:
		f.write(r.content)


def main():
	os.makedirs('./pic/', exist_ok=True)  # 输出目录

	# 修改以下两行信息即可
	prefix_url = 'http://xyz.com/series-'  # 同一类目下的图片url前缀
	n = 6  # 该类目下的图片总数

	tmp = prefix_url.split('/')[-1]
	pbar = tqdm(range(1, n + 1))
	for i in pbar:
		file_path = './pic/' + tmp + str(i) + '.jpg'

		picture_url = prefix_url + str(i) + '.jpg'
		download(file_path, picture_url)

		pbar.set_description('download %s' % i)
		time.sleep(random.randint(6, 10))


if __name__ == '__main__':
	main()
