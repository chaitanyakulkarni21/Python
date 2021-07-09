from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    title = 'Flask'
    return render_template('index.html',title1 = title)

@app.route('/about')
def Chaitanya():
    name =  'Chaitanya'
    return render_template('about.html',name2 = name)

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')
    

app.run(debug = True)