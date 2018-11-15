import requests, json, ssl, urllib.request

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    ctxt = ssl._create_unverified_context()

    nasaJson = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=6SpISNmlk1rhPfAoxzNkcS3af2BU1EIZlmtWSnbJ", context = ctxt)
    nasaDict = json.loads(nasaJson.read())
    
    app_id = '8f413c03'
    app_key = '2cb56b8263b8c86ff4cd0c2a998c9acc'
    language = 'en'
    word_id = 'comet'
    
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    oxJson = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

    oxDict = json.loads(oxJson.text)
    return render_template('index.html', title = nasaDict['title'], defs = oxDict['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0], url = nasaDict['url'])

if __name__ == '__main__':
    app.debug = True
    app.run()
