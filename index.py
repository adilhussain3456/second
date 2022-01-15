from distutils.log import debug
from tensorflow  import keras

#from turtle import home
#from turtle import home
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)

