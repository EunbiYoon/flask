from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:Ella135!@localhost/quotes"
#app.config['SQLALCHEMY_DATABASE_URI']="postgres://coozucqfvwbane:032e72f45f8b14e1a1d5620bb49d22297fd90b468f2cf7d9bf9ea41c2a0a0b9d@ec2-44-197-128-108.compute-1.amazonaws.com:5432/dabfqcjnh2gj8b"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # event notification - track resources
#app.debug=True

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

#instead of db.create_all() just run this
with app.app_context(): 
    db.create_all()


@app.route('/')
def index():
    result=Favquotes.query.all()
    return render_template('index.html',result=result)

@app.route('/quotes')
def quotes():
	 return render_template('quotes.html')

@app.route('/process', methods =['POST'])
def process():
    author=request.form['author']
    quote=request.form['quote']
    quotedata=Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()


    return redirect(url_for('index')) #index function return
