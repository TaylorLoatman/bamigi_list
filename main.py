from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import security
from modules.sms_alert import SMSAlert


app = Flask(__name__)
app.config['SECRET_KEY'] = security.app_key

# Connect Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bamigi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Configure Tables
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    birthday = db.Column(db.String(10))
    phone = db.Column(db.Integer, unique=True)


db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    sms_alert = SMSAlert()

    if request.method == "POST":
        name = request.form['name']
        phone = request.form['phone']
        birthday = request.form['birthday']

        existing_phone = User.query.filter_by(phone=request.form['phone']).first()
        if name == "" or phone == "" or birthday == "":
            flash("Oooooppps, looks like we're missing some information to get you plugged in.", category=error)
        elif existing_phone:
            flash("User phone number already exist. Please choose a different one.", category=error)
        else:
            new_user = User(
                name=name,
                phone=phone,
                birthday=birthday
            )
            db.session.add(new_user)
            db.session.commit()

            sms_alert.send_msg(name, phone)


    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
