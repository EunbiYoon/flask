from flask import Flask,render_template
app=Flask(__name__)


@app.route("/")
def index():
    fruits=["apple","grapes","berries","oranges"]
    return render_template('index.html', quote="sdfsfsdf", fruits=fruits)

@app.route("/about")
def about():
    return '<h1> Hello World from about page</h1>'

@app.route("/quotes")
def quotes():
    return '<h1> Hello World </h1>'

