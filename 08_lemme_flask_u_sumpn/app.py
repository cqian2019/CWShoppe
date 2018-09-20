#Cheryl Qian
#SoftDev1 pd8
#K08 -- Fill Yer Flask
#2018-09-19


from flask import Flask
app = Flask(__name__) #instantiates the Flask class using a constructor



@app.route('/')
def home():
 return "<a href='/ingredient'> Click here for the <b>secret ingredient</b> </a>"

@app.route('/ingredient')
def ingredient():
 return "The secret ingredient is <b>tomato</b> <br> <a href='/recipe'> Click here for a recipe </a> <br> <a href='/'> Click here to go home </a>"

@app.route('/recipe')
def recipe():
 return "1 tbsp tomatoes, 1 cup water <br> <a href='/'> Go home. </a> <br> <a href='/ingredient'> View the ingredient again. </a>"

 
app.debug = True
app.run()
