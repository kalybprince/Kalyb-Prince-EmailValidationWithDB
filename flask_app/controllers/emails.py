from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email

@app.route('/')
def index():
    print('/')
    if session['email']:
        return render_template('index.html', session=session['email'])
    else:
        session['email'] = 0

@app.route('/validate_email', methods=["POST"])
def validate_email():
    print('*'*80)
    data = {
        'email': request.form['email'],
    }
    if Email.validate_email(data):
        session['email'] = request.form['email']
        Email.save(data)
        return redirect('/')
    return redirect('/')