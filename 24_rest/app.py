import urllib.request, json, ssl

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    ctxt = ssl._create_unverified_context()
    j = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=6SpISNmlk1rhPfAoxzNkcS3af2BU1EIZlmtWSnbJ", context = ctxt)
    d = json.loads(j.read())
    print(d["url"])
    return render_template('index.html',planet= d["title"],url = d["url"])


if __name__ == '__main__':
    app.debug = True
    app.run()
