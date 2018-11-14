import urllib, json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    j = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=8RmXLa9SUmJOSTLZfpSB8rQQDBV0Sq6hpmumfL6y")
    d = json.loads(json_data.read())
    print(d["url"])
    return render_template('main.html', url = d["url"], planet = d["resource"]["planet"])


if __name__ == '__main__':
    app.debug = True
app.run()
