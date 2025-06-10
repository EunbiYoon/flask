from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from random import randint
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    name=StringField("NAME", validators=[DataRequired('A full name is required'), Length(min=5, max=30)])
    email=StringField("EMAIL", validators=[DataRequired('A correct email is required'), Email()])
    message=TextAreaField("MESSAGE", validators=[DataRequired('A message is required'), Length(min=5, max=500)])
    submit=SubmitField('SEND')
    

app=Flask(__name__)
app.config["SECRET_KEY"]="thisisasecretkeyhereisasecret"

#sqlalchemy - sqlite
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///C:\\Users\\eunbi1.yoon\\Desktop\\Newer Folder\\sqlite\\test.db"

db=SQLAlchemy()
class Clients(db.Model):
    clientid=db.Column(db.Integer(),primary_key=True)
    clientname=db.Column(db.String(40))
    clientemail=db.Column(db.String(40))
    clientmessage=db.Column(db.String(500))
    def __repr__(self):
        return f"Clinets('(self.clientid)','(self.clientname)','(self.clientemail)','(self.clientmessage)')"

db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.route("/",methods=["POST","GET"])
@app.route("/home",methods=["POST","GET"])
def hello_world():
    form=ContactForm()
    if request.method=="POST":
        name=form.name.data
        email=form.email.data
        message=form.message.data

        #2- SEND Information to SQLite
        db.session.add(
            Clients(
                clientid=randint(0,1000000),
                clientname=name,
                clientemail=email,
                clientmessage=message
            )            
        )
        db.session.commit()
        #SEND Information to SQLite

                
        print(name,email,message)
        form.name.data, form.email.data, form.message.data="","",""
        return render_template("index.html",form=form, success=True)
    return render_template("index.html",form=form)


@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/components")
def components():
    return render_template("components.html")

#2- sqllite
@app.route("/database")
def database():
    return render_template("database.html",clients=Clients.query.all())
    # filter --> return render_template("database.html",clinets=Clients.query.first(clientid="adfa"))


if __name__ =="__main__":
    app.run()