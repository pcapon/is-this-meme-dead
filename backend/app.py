
from datetime import datetime
from flask_cors import CORS
from flask_api import status
from flask import Flask, request, jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)
CORS(app)

cred = credentials.Certificate('./isthismemedead-firebase-adminsdk-y09hw-f48f0b916b.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://isthismemedead.firebaseio.com/'
})

@app.route("/hello")
@app.route("/")
def hello():
    return "Hello World!"

def check_meme_exist(id):
    ref = db.reference('memes')
    check = ref.child(id).get()
    return check

def save_to_firebase(infos):
    ref = db.reference('memes')
    ref.child(infos['id']).set(infos)
    return 1

def get_id(url):
    parseUrl = urlparse(url)

    return parseUrl.path.split('/')[-1]

def parse_url(url):
    parseResult = {}
    infos = ["Year", "Origin"]

    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    header = soup.find("header", class_="rel c")
    dl = soup.select_one("#entry_body > aside > dl")
    parseResult['url'] = url
    parseResult["image url"] = header.find("img")["data-src"]
    parseResult["title"] = header.select_one("h1 > a").string
    dlinfos = dl.find_all("a")[-2:]

    for i in range(2):
        parseResult[infos[i]] = dlinfos[i].string

    return parseResult

@app.route('/addmeme', methods=['POST'])
def add_meme():
    link = request.json["link"]
    id = get_id(link)
    if check_meme_exist(id):
        return jsonify({
                            "error": "Meme already exist"
                       }), status.HTTP_403_FORBIDDEN

    infos = parse_url(link)
    infos["id"] = id
    infos["status"] = 1
    infos["yes"] = 0
    infos["no"] = 0
    save_to_firebase(infos)
    print(infos)

    return jsonify(infos), status.HTTP_200_OK

@app.route('/search', methods=['GET'])
def search():
    endquery = {}
    stringQuery = request.args.get('q')
    print(stringQuery)
    ref = db.reference('memes')
    results = ref.order_by_key().start_at(stringQuery).end_at(stringQuery+"\uf8ff").get()
    for key in results:
        endquery[key] = ref.child(key).get()
    return jsonify(endquery)

if __name__ == "__main__":
    app.run(debug=True)
