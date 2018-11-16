#Cheryl Qian
#SoftDev pd8
#K26 -- Getting More REST
#2018-11-15

import json, urllib.request, ssl

from flask import Flask, render_template, request, Markup

app = Flask(__name__)

@app.route("/")
def index():
    ctxt = ssl._create_unverified_context()
    
    nycUrl = 'https://data.cityofnewyork.us/resource/xtra-f75s.json'
    metUrl = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/2222'
    nytUrl = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
    nytHdr = {'api-key': "07d075f144584e4a96a48aaa77771104"}
    nytReq = urllib.request.Request(nytUrl,headers=nytHdr)
    
    nycData = json.load(urllib.request.urlopen(nycUrl, context=ctxt))
    metData = json.load(urllib.request.urlopen(metUrl, context=ctxt))
    nytData = json.load(urllib.request.urlopen(nytReq, context=ctxt))

    mI =metData['primaryImage']
    mF = metData['artistDisplayName']
    mT =metData['title']

    nytRet = '<b>' + nytData['response']['docs'][1]['headline']['main'] + '</b><br>'+ nytData['response']['docs'][1]['web_url'] + '<br>' + nytData['response']['docs'][1]['snippet']

    return render_template('index.html', nyc=displayDict(nycData[0]), metTitle = mT, metImg = mI, metInfo = mF, nyt= Markup(nytRet))

def displayDict(dict):
    s = ''
    for key in dict:
        s = s + '<br>' + '<b>' + key + '</b>' + ': ' + str(dict[key])
    return Markup(s)



app.debug = True
app.run()
