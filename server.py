import HTML_Crawler as parser
from flask import Flask, render_template, redirect, url_for
import json

server = Flask(__name__)


@server.route('/')
def main():
    url = 'https://ria.ru/world/'
    html_page = parser.get_html_page(url)
    articles = parser.find_articles(html_page)
    json_file_path = parser.publish_report('./articles.json', url,  articles)
    file = open('./articles.json', encoding='UTF-8')
    json_string = file.read()
    file.close()
    dictionary_json = json.loads(json_string)
    return render_template('html_template.html', data=dictionary_json, page_url=url)


@server.route('/refresh_page', methods=['POST'])
def refresh():
    return redirect(url_for('main'))


if __name__ == '__main__':
    server.run()
