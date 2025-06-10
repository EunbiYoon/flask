from flask import Flask, request, render_template
import psycopg2
from random import randint

#forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email
import email_validator
class ContactForm(FlaskForm):
    name=StringField('NAME',validators=[DataRequired('A full name is required'),Length(min=5, max=30)])
    email=StringField('EMAIL',validators=[DataRequired('A correct email is required'),Email()])
    message=TextAreaField('MESSAGE',validators=[DataRequired('A message is required'),Length(min=5, max=500)])
    submit=SubmitField('SEND')
#forms.py

app=Flask(__name__)
app.config["SECRET_KEY"]="c54c76d0f1643a531b2109e24933bc59c20a3e06ab23d096"


@app.route("/",methods=["POST","GET"])
@app.route("/home",methods=["POST","GET"])
def hello_world():
    form=ContactForm()
    if request.method=="POST":
        name=form.name.data
        email=form.email.data
        message=form.message.data

        #4- postgresql 
        conn=psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            password="Ella135!",
            database="mydatabase"
        )
        cursor=conn.cursor()
        cursor.execute('''
            INSERT INTO clients(clientid, clientname, clientemail, clientmessage)
                VALUES(%s,%s,%s,%s);
            ''', (randint(0,1000000),name,email,message))
        conn.commit()
        cursor.close()
        conn.close()

                
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

#4- postgresql
@app.route("/database")
def database():
    conn=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="Ella135!",
    database="mydatabase"
    )
    cursor=conn.cursor()
    cursor.execute('''
        SELECT * FROM clients;
        ''')
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    #return "%s" % data

    #datatype change 
    data=str(list(data)).replace("),",")<br/>")
    data=data.replace("[", "")
    data=data.replace("]", "")
    return data

if __name__ =="__main__":
    app.run()