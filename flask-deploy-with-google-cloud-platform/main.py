# import required packages
# Create constructor object
# Creating routing
# Running web app


from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello !!"

@app.route("/<string:username>")
def name(username):
    return "<html><h1> Welcome {} </h1></html>".format(username)

@app.route("/html_page")
def html():
    return render_template("demo.html")

@app.route("/css")  
def css():
    return render_template("css.html")

if __name__ == "__main__":
    app.run(port=8080)



