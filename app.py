

from email import message
from enum import unique
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail


app=Flask(__name__,template_folder='template')

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:221022@localhost/beelaboo'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dbgmfrzbiesrgm:9d88f6ef95171d9501a2166263a951800b56ba13ea7384bfac690412539b592e@ec2-52-73-155-171.compute-1.amazonaws.com:5432/d9ugts1k4i1gpq'

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key = True)
    customer = db.Column(db.String(200), unique=True)
    pattern_name = db.Column(db.String(200), unique=True)
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

def  __init__ (self, customer,  pattern,  rating , comments): 
     self.customer = customer
     self.pattern = pattern
     self.rating = rating
     self.comments = comments



@app.route('/')

def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        pattern = request.form['pattern']
        rating = request.form['rating']
        comments = request.form['comments']

        #print(customer,pattern_name,rating,comments) 
        # #print in console and then render in success page

       
        if customer =='' :
            return render_template('index.html', message='Please fill required fields')

         #I do not want to get feedback from same customer in the same order

        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer,pattern,rating,comments)
            db.session.add(Feedback.data)
            db.session.commit()
            return render_template('success.html')

        return render_template('index.html', message='You have already submitted feedback')

        send_mail(customer,pattern,rating,comments)

if __name__ == '__main__':
    
    app.run()
