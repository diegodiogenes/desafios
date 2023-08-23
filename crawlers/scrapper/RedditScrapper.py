from bs4 import BeautifulSoup

from scrapper.BaseScrapper import BaseScrapper
from utils import base_url


class RedditScrapper(BaseScrapper):

    def __init__(self, upvote_criteria: int = 5000):
        self._upvote_criteria = upvote_criteria
        self.__thread_content = None

    def __extract_score(self, thread_html):
        score = thread_html.find('div', {'class': 'score unvoted'})
        try:
            return int(score.text.replace("k", "00").replace(".", "")) if score else 0
        except ValueError:
            return 0

    def __extract_title(self, thread_html):
        info_title = thread_html.find("a", {'class': 'title'})

        title = info_title.text
        title_link = info_title.get('href') if 'https://' in info_title.get(
            'href') else f"{base_url[:-3]}{info_title.get('href')}"

        return title, title_link

    def __extract_comments(self, thread_html):
        return thread_html.find("a", {"class": "comments"}).get('href')

    def __extract_infos(self, threads):
        dict_resp = {}
        for thread_html in threads:
            if 'thing' not in thread_html.get('class'):
                continue

            subreddit = thread_html.get('data-subreddit-prefixed')
            score = self.__extract_score(thread_html)
            if score < self._upvote_criteria:
                continue

            title, title_link = self.__extract_title(thread_html)
            comments_link = self.__extract_comments(thread_html)

            dict_resp[title] = {'score': score, 'title': title, 'title_link': title_link,
                                'comments_link': comments_link, 'subreddit': subreddit}

        return dict_resp

    def scrape(self, base_html):
        soup = BeautifulSoup(base_html, 'html.parser')
        threads_content = soup.find('div', {'id': 'siteTable'})

        return self.__extract_infos(threads_content)
