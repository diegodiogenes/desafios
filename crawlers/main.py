import argparse
from pprint import pprint

from client.client import Client
from scrapper.RedditScrapper import RedditScrapper
from utils import base_url

parser = argparse.ArgumentParser(description='Formatter for Strings, wrap, align and save texts.')
parser.add_argument('--subs', dest='subs', type=str, help="Subredits to crawler", required=True)

if __name__ == '__main__':
    args = parser.parse_args()

    threads = args.subs.split(";")
    urls = [f"{base_url}{thread}/hot" for thread in threads]
    scrapper = RedditScrapper()
    crawler = Client(urls, scrapper)
    pprint(crawler.run(), indent=2)
