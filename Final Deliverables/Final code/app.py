from flask import Flask,render_template, request, redirect, url_for, session

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT= 32286;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=njl44200;PWD=4txG25Bx3uVKEQVg",'','')
app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')


@app.route('/addcustomer',methods = ['POST', 'GET'])
def addcus():
  if request.method == 'POST':

    a = request.form['cname']
    b = request.form['email']
    c = request.form['phone']
    d = request.form['country']
    e = request.form['city']
    f = request.form['address']
    g= request.form['desc']
    # h = request.form['description']
    # i = request.form['tax']
    # j = request.form['price']
 
    # sql = "SELECT * FROM register WHERE mail =?"
    # stmt = ibm_db.prepare(conn, sql)
    # ibm_db.bind_param(stmt,1,mail)
    # ibm_db.execute(stmt)
    # account = ibm_db.fetch_assoc(stmt)

    # if account:
    #   return render_template('register.html', msg="You are already a member, please login using your details")
    # else:
    insert_sql = "INSERT INTO addcustomer VALUES (?,?,?,?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, a)
    ibm_db.bind_param(prep_stmt, 2,b)
    ibm_db.bind_param(prep_stmt, 3, c)
    ibm_db.bind_param(prep_stmt, 4, d)
    ibm_db.bind_param(prep_stmt, 5, e)
    ibm_db.bind_param(prep_stmt, 6, f)
    ibm_db.bind_param(prep_stmt, 7, g)
    #   ibm_db.bind_param(prep_stmt, 8, h)
    #   ibm_db.bind_param(prep_stmt, 9, i)
    #   ibm_db.bind_param(prep_stmt, 10, j)
    #   ibm_db.bind_param(prep_stmt, 11 d)
    ibm_db.execute(prep_stmt)
    
    return render_template('index.html', msg="Data saved successfuly..Please login using your details")

@app.route('/newuser',methods = ['POST', 'GET'])
def newusr():
  if request.method == 'POST':

    a = request.form['uname']
    b = request.form['mobile']
    c = request.form['ppic ']
    d = request.form['email']
    e = request.form['role']
    f = request.form['pwd']
    g= request.form['cpwd']
    # h = request.form['description']
    # i = request.form['tax']
    # j = request.form['price']
 
    # sql = "SELECT * FROM register WHERE mail =?"
    # stmt = ibm_db.prepare(conn, sql)
    # ibm_db.bind_param(stmt,1,mail)
    # ibm_db.execute(stmt)
    # account = ibm_db.fetch_assoc(stmt)

    # if account:
    #   return render_template('register.html', msg="You are already a member, please login using your details")
    # else:
    insert_sql = "INSERT INTO newuser VALUES (?,?,?,?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, a)
    ibm_db.bind_param(prep_stmt, 2,b)
    ibm_db.bind_param(prep_stmt, 3, c)
    ibm_db.bind_param(prep_stmt, 4, d)
    ibm_db.bind_param(prep_stmt, 5, e)
    ibm_db.bind_param(prep_stmt, 6, f)
    ibm_db.bind_param(prep_stmt, 7, g)
      # ibm_db.bind_param(prep_stmt, 4, h)
      # ibm_db.bind_param(prep_stmt, 4, i)
      # ibm_db.bind_param(prep_stmt, 4, j)
      # ibm_db.bind_param(prep_stmt, 4, d)
    ibm_db.execute(prep_stmt)
    
    return render_template('index.html', msg="Data saved successfuly..Please login using your details")

