"""Crawl food materials."""
import codecs
from icrawler.builtin import BaiduImageCrawler
from icrawler.builtin import BingImageCrawler

IS_DEMO = False  # change to False if doing actual crawling
""" list_file = "food_mat.txt"  """
list_file = "bing_food_mat.txt"
if IS_DEMO:
    examples_per_category = 1000
else:
    examples_per_category = 1000

""" img_dir = 'images/baidu/'  """
img_dir = 'images/bing/'

with codecs.open(list_file, 'rb', 'utf-8') as categories:
    for category in categories:
        category = category.strip().encode('utf-8')
        """
        baidu_crawler = BaiduImageCrawler(
            downloader_threads=4, storage={'root_dir': img_dir + category}
        )
        baidu_crawler.crawl(category, max_num=examples_per_category)
        """
        bing_crawler = BingImageCrawler(
            downloader_threads=4, storage={'root_dir': img_dir + category}
        )
        bing_crawler.crawl(category, max_num=examples_per_category)
