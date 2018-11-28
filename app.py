from flask import Flask, flash, render_template, request, session, abort,url_for
import os
import json
from com.awssupport.athenalab import queryvalidation
from datetime import date, datetime
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy.orm import sessionmaker
from tabledef import *
import cleanup,mockdataCreation,dummy

engine = create_engine('sqlite:///dbathena.db', echo=True,poolclass=SingletonThreadPool)

Base = declarative_base()

app = Flask(__name__)

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()

@app.errorhandler(404)
def page_not_found(e):
    return home()

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        Session = sessionmaker(bind=engine)
        s = Session()
        options = []
        query = s.query(Exercise).filter(Exercise.groupid.__eq__('q1'))
        # {"id":"q11","groupid":"q1","desc":"Hive Schema mismatch error","run":"","result":""}
        for row in query:
            dict = {}
            dict['id'] = row.id
            dict['desc'] = row.desc
            dict['query'] = row.query
            dict['result'] = row.result
            dict['editable'] = row.editable
            options.append(dict)
        return render_template('exercises/exercise1.html',options=options)


@app.route('/login', methods=['POST','GET'])
def do_admin_login():
    """ password validation"""
    error = None
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
        result = query.first()
        if result:
            session['logged_in'] = True
        else:
            error = 'Invalid username/password'
            flash('wrong password!')
            return render_template('login.html',error=error)
    return home()

@app.route('/runquery/<number>',methods=['POST'])
def run_query(number):
    """ Ajax call for execution"""
    Session = sessionmaker(bind=engine)
    s = Session()
    if not session.get('s3bucket'):
        query=s.query(Exercise).filter(Exercise.id.__eq__(number))
        rrow=query.first()
        query=s.query(ExerciseTopic).filter(ExerciseTopic.id.__eq__(rrow.groupid))
        prop=json.loads(query.first().property);
        session['s3bucket']=prop['s3bucket']
    row=s.query(Exercise).filter(Exercise.id.__eq__(number))
    out=queryvalidation.query_validation(number,session.get('s3bucket'),row.first().query)
    row.update({'comments':json.dumps(out,default=json_serial),'result':out['status']})
    s.commit()
    return json.dumps(out)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route("/updatequery/<number>",methods=['POST'])
def updatequery(number):

    Session = sessionmaker(bind=engine)
    s = Session()
    row = s.query(Exercise).filter(Exercise.id.__eq__(number.replace('u','')))
    print(row.first().query)
    row.update({'query':str(request.get_json()['ddl'])})
    s.commit()
    return "{'sucess':'ok'}"

@app.route('/exercise/<number>')
def do_exercise(number):
    Session = sessionmaker(bind=engine)
    s = Session()
    options=[]
    query = s.query(Exercise).filter(Exercise.groupid.__eq__(number))
    for row in query:
        dict={}
        dict['id']=row.id
        dict['desc']=row.desc
        dict['result']=row.result
        dict['query']=row.query
        dict['result']=row.result
        dict['editable']=row.editable
        options.append(dict)

    return render_template('exercises/exercise1.html',options=options)


@app.route('/cleanup')
def cleandata():
    Session = sessionmaker(bind=engine)
    s = Session()
    options = []
    query = s.query(ExerciseTopic)
    # {"id":"q11","groupid":"q1","desc":"Hive Schema mismatch error","run":"","result":""}
    for row in query:
        dict=json.loads(row.property)
        for key in dict.keys():
            print(key,dict[key],)
            cleanup.cleanup(key,dict[key])
        #session.delete(row)
        options.append(dict)

    return render_template('exercises/removesuccess.html',options=options)

@app.route('/createData')
def createData():
    Session = sessionmaker(bind=engine)
    s = Session()
    #dummy.exerciseData(s)
    mockdataCreation.sample_data(s)
    return home()



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=80)
