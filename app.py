from flask import Flask, flash,jsonify, redirect, render_template, request, session, abort,url_for
import os
import json
from com.awssupport.athenalab import athenaQueryExecutor
from datetime import date, datetime

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
        return render_template('exercises/exercise1.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    error = None
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        error = 'Invalid username/password'
        flash('wrong password!')
    return render_template('login.html',error=error)

@app.route('/runquery/<number>',methods=['POST'])
def run_query(number):
    print(number)
    out=athenaQueryExecutor.executeQuery()
    return json.dumps({'status':'OK','result':'success','message':out},default=json_serial);

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/exercise/<number>')
def do_exercise(number):
    expath="exercises/exercise{}.html".format(number)
    return render_template(expath)


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
