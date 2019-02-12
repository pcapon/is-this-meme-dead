
from datetime import datetime
from flask_cors import CORS
from flask_api import status
from flask import Flask, flash, request, redirect, url_for,send_from_directory,after_this_request, g
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)


@app.route("/hello")
@app.route("/")
def hello():
    return "Hello World!"

def parse_url(url):
    parseResult = {}
    infos = ["Year", "Origin"]

    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    header = soup.find("header", class_="rel c")
    dl = soup.select_one("#entry_body > aside > dl")
    parseResult["image url"] = header.find("img")["data-src"]
    parseResult["title"] = header.select_one("h1 > a").string
    dlinfos = dl.find_all("a")[-2:]

    for i in range(2):
        parseResult[infos[i]] = dlinfos[i].string

    return parseResult




@app.route('/addmeme', methods=['POST'])
def add_meme():
    link = request.json["link"]
    parse_url(link)
    return link, status.HTTP_200_OK

if __name__ == "__main__":
    app.run(debug=True)
