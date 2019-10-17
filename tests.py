import unittest
import json
import requests
from datetime import datetime, date
import HTML_Crawler as crawler
from HTML_Crawler import articles


class CrawlerTestCase(unittest.TestCase):
    def test_checkJson(self):
        url = 'https://ria.ru/world/'
        html_page = crawler.get_html_page(url)
        articles = crawler.find_articles(html_page)
        print(articles)
        path = './articles.json'
        crawler.publish_report(path, url, articles)
        fh = open('articles.json', 'r')
        data = json.load(fh)
        fh.close()
        date0 = datetime.now()
        date1 = str(date0.date())
        self.assertEqual(data['url'] == '', False)
        self.assertEqual(data['articles'] == '', False)
        for i in data['articles']:
            self.assertEqual(i['title'] == '', False)
        self.assertEqual(data['creationDate'] == '', False)
        self.assertEqual(data['creationDate'] == date1, True)

    def test_checkPage(self):
        self.assertEqual(articles[0] == '', False)

    def test_checkUrl(self):
        url = 'https://ria.ru/world/'
        news_request = requests.get(url)
        self.assertEqual(news_request.status_code == 200, True)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(CrawlerTestCase('test_checkJson'))
    suite.addTest(CrawlerTestCase('test_checkPage'))
    suite.addTest(CrawlerTestCase('test_checkUrl'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
