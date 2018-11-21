from flask import Flask, flash, render_template, request, session, abort,url_for
import os
import json
from com.awssupport.athenalab import queryvalidation
from datetime import date, datetime

from com.awssupport.athenalab.dao import exerciseinput



app = Flask(__name__)

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        print(exerciseinput.getQuery('q11'))
        return render_template('exercises/exercise1.html',options=exerciseinput.getQuery('q11'))


@app.route('/login', methods=['POST'])
def do_admin_login():
    """ password validation"""
    error = None
    if request.form['password'] == 'athenalab#2018' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        error = 'Invalid username/password'
        flash('wrong password!')
        return render_template('login.html',error=error)
    return home()

@app.route('/runquery/<number>',methods=['POST'])
def run_query(number):
    """ Ajax call for execution"""
    print(number)
    return json.dumps(queryvalidation.query_validation(number))

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/exercise/<number>')
def do_exercise(number):
    return render_template('exercises/exercise1.html',options=exerciseinput.getQuery(number))


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=8080)
