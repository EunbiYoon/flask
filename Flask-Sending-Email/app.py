from flask import *
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config.update(
    DEBUG=False,
    # EMAIL SETTINGS
    MAIL_SERVER='lgekrhqmh01.lge.com',
    MAIL_PORT=25,
    MAIL_DEFAULT_SENDER=('CostReview', 'eunbi1.yoon@lge.com'),

)

mail = Mail(app)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/send_mail", methods=['POST'])
def send_mail():
    email = request.form['email'].strip()
    subject = 'Hello'
    msg = Message(
        subject=subject,
        recipients=[email],
        html=render_template('graph.html')
    )

    with app.open_resource("static/images/img_1.jpg") as fp:
        msg.attach("image.jpg", "image/jpg", fp.read())
    mail.send(msg)

    # return 
    return render_template("thank.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)