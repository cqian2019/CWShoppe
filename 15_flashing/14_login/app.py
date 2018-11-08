#Team xD -- Joan Chirinos, Cheryl Qian
#SoftDev pd8 
#K14 -- Do I Know You?
#2018-10-02

from flask import Flask, render_template, request, session, url_for, redirect
import os
app = Flask(__name__) #create instance of class Flask



@app.route('/')
def login_screen():
    return render_template(newTemp.html)


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run()
