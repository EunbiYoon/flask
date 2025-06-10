from flask import Flask, request, render_template
from flask_mail import Mail,Message
import smtplib
from flask_sqlalchemy import SQLAlchemy
from random import randint
from flask_mysqldb import MySQL 
import psycopg2

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

# #1- mail
# app.config['MAIL_SERVER']='mail.eunbiyoon.com'
# app.config['MAIL_PORT']='465'
# app.config['MAIL_USER_SSL']=True
# app.config['MAIL_USERNAME']='admin@eunbiyoon.com'
# app.config['MAIL_PASSWORD']='Ella135!'
# mail=Mail()
# mail.init_app(app)

# #2- sqlalchemy - sqlite
# app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///C:\\Users\\eunbi1.yoon\\Desktop\\Newer Folder\\sqlite\\test.db"
# db=SQLAlchemy()
# class Clients(db.Model):
#     clientid=db.Column(db.Integer(),primary_key=True)
#     clientname=db.Column(db.String(40))
#     clientemail=db.Column(db.String(40))
#     clientmessage=db.Column(db.String(500))
#     def __repr__(self):
#         return f"Clinets('(self.clientid)','(self.clientname)','(self.clientemail)','(self.clientmessage)')"
# db.init_app(app)
# with app.app_context():
#     db.create_all()
# db=SQLAlchemy()


#3- mysql
app.config['MYSQL_USER']='root'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_DB']='mydatabase'
mysql=MySQL()
mysql.init_app(app)
# #create database - if you cannot make table in workbench 
# with app.app_context():
#      cur=mysql.connection.cursor()
#      cur.execute('''
#          CREATE TABLE 
#      ''')
#      cur.close()



@app.route("/",methods=["POST","GET"])
@app.route("/home",methods=["POST","GET"])
def hello_world():
    form=ContactForm()
    if request.method=="POST":
        name=form.name.data
        email=form.email.data
        message=form.message.data

        # #1- send mail#
        # print(name,email,message)
        # msg=Message('Email from customer {}'.format(form.name.data), sender="admin@eunbiyoon.com", recipients=['yinyinbei0717@gmail.com'])
        # msg.body='''Message from {} <{}>
        #     this is a test. Here is the content of the message: {}
        # '''.format(form.name.data, form.email.data, form.message.data)
        # mail.send(msg)
        
        # server=smtplib.SMTP_SSL('smtp.gmail.com:465')
        # server.connect('smtp.googlemail.com',587)
        # server.ehlo()
        # server.login('emily.yoon717','Ella135!!!')
        # msg='''Message form {} <{}>
        # # This is a test. Here is the content of the message: {}
        # # '''.format(form.name.data, form.email.data, form.message.data)
        # server.sendmail("emily.yoon717@gmail.com","yinyinbei0717@gmail.com",msg)
        # server.close()
        # #send mail#

        # #2- SEND Information to SQLite
        # db.session.add(
        #     Clients(
        #         clientid=randint(0,1000000),
        #         clientname=name,
        #         clientemail=email,
        #         clientmessage=message
        #     )            
        # )
        # db.session.commit()
        # #SEND Information to SQLite


        # #3- send information into mysql
        # cur=mysql.connection.cursor()
        # cur.execute('''
        #     INSERT INTO clients(clientid, clientname, clientemail, clientmessage)
        #     VALUES(%s,%s,%s,%s);
        # ''', (randint(0,1000000),name,email,message))
        # mysql.connection.commit() #before closing this
        # cur.close()


        #4- postgresql 
        
                
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
# @app.route("/database")
# def database():
#     return render_template("database.html",clients=Clients.query.all())
#     # filter --> return render_template("database.html",clinets=Clients.query.first(clientid="adfa"))

#3- Mysql
@app.route("/database")
def database():
    cur=mysql.connection.cursor()
    cur.execute('''
        SELECT clientmessage FROM clients;
    ''')
    data=cur.fetchall()
    cur.close()
    return "%s" % data

if __name__ =="__main__":
    app.run()