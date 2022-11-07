from flask import Flask,render_template, request, redirect, url_for, session

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=32286;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=njl44200;PWD=4txG25Bx3uVKEQVg",'','')
app = Flask(__name__)



@app.route("/")
def logs():
    return render_template('home.html')


@app.route('/register',methods = ['POST', 'GET'])
def register():
  if request.method == 'POST':

    name = request.form['name']
    mail = request.form['mail']
    pwd = request.form['pwd']
    cpwd = request.form['cpwd']
 
    sql = "SELECT * FROM register WHERE mail =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,mail)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('register.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO register VALUES (?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, mail)
      ibm_db.bind_param(prep_stmt, 3, pwd)
      ibm_db.bind_param(prep_stmt, 4, cpwd)
      ibm_db.execute(prep_stmt)
    
    return render_template('home.html', msg="Data saved successfuly..Please login using your details")

@app.route('/login',methods=['POST'])
def login():
  mail=request.form['mail']
  pwd=request.form['pwd']
  sql = "SELECT * FROM register WHERE mail =? AND pwd=?"
  stmt = ibm_db.prepare(conn, sql)
  ibm_db.bind_param(stmt,1,mail)
  ibm_db.bind_param(stmt,2,pwd)
  ibm_db.execute(stmt)
  account = ibm_db.fetch_assoc(stmt)
  if account:
    #return redirect(url_for('home'))
    return render_template('homepage.html', pred="login") 
  else:
    return render_template('register.html', pred="Login unsuccessful. Incorrect username / password !") 

