from flask import Flask,render_template, request, redirect, url_for, session

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT= 32286;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=njl44200;PWD=4txG25Bx3uVKEQVg",'','')
app = Flask(__name__)



@app.route("/")
def logs():
    return render_template('index.html')


@app.route('/addpurchase',methods = ['POST', 'GET'])
def addpurchase():
  if request.method == 'POST':

    a = request.form['sname']
    b = request.form['pdate']
    c = request.form['pname']
    d = request.form['rno']
    e = request.form['pname']
    # f = request.form['sku']
    # g= request.form['minimum quantity']
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
    insert_sql = "INSERT INTO addpurchase VALUES (?,?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, a)
    ibm_db.bind_param(prep_stmt, 2,b)
    ibm_db.bind_param(prep_stmt, 3, c)
    ibm_db.bind_param(prep_stmt, 4, d)
    ibm_db.bind_param(prep_stmt, 5, e)
    #   ibm_db.bind_param(prep_stmt, 6, f)
    #   ibm_db.bind_param(prep_stmt, 4, g)
    #   ibm_db.bind_param(prep_stmt, 4, h)
    #   ibm_db.bind_param(prep_stmt, 4, i)
    #   ibm_db.bind_param(prep_stmt, 4, j)
    #   ibm_db.bind_param(prep_stmt, 4, d)
    #   ibm_db.execute(prep_stmt)
    
    return render_template('index.html', msg="Data saved successfuly..Please login using your details")

@app.route('/addquotation',methods = ['POST', 'GET'])
def addquotation():
  if request.method == 'POST':

    a = request.form['cname']
    b = request.form['qdate']
    c = request.form['rno ']
    d = request.form['pname']
    # e = request.form['unit']
    # f = request.form['sku']
    # g= request.form['minimum quantity']
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
    insert_sql = "INSERT INTO addquotation VALUES (?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, a)
    ibm_db.bind_param(prep_stmt, 2,b)
    ibm_db.bind_param(prep_stmt, 3, c)
    ibm_db.bind_param(prep_stmt, 4, d)
      # ibm_db.bind_param(prep_stmt, 4, e)
      # ibm_db.bind_param(prep_stmt, 4, f)
      # ibm_db.bind_param(prep_stmt, 4, g)
      # ibm_db.bind_param(prep_stmt, 4, h)
      # ibm_db.bind_param(prep_stmt, 4, i)
      # ibm_db.bind_param(prep_stmt, 4, j)
      # ibm_db.bind_param(prep_stmt, 4, d)
    ibm_db.execute(prep_stmt)
    
    return render_template('index.html', msg="Data saved successfuly..Please login using your details")

@app.route('/addtransfer',methods = ['POST', 'GET'])
def addtransfer():
  if request.method == 'POST':

    a = request.form['date']
    b = request.form['from']
    c = request.form['to ']
    d = request.form['product name']
    # e = request.form['unit']
    # f = request.form['sku']
    # g= request.form['minimum quantity']
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
    insert_sql = "INSERT INTO addtransfer VALUES (?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, a)
    ibm_db.bind_param(prep_stmt, 2,b)
    ibm_db.bind_param(prep_stmt, 3, c)
    ibm_db.bind_param(prep_stmt, 4, d)
      # ibm_db.bind_param(prep_stmt, 4, e)
      # ibm_db.bind_param(prep_stmt, 4, f)
      # ibm_db.bind_param(prep_stmt, 4, g)
      # ibm_db.bind_param(prep_stmt, 4, h)
      # ibm_db.bind_param(prep_stmt, 4, i)
      # ibm_db.bind_param(prep_stmt, 4, j)
      # ibm_db.bind_param(prep_stmt, 4, d)
    ibm_db.execute(prep_stmt)
    
    return render_template('index.html', msg="Data saved successfuly..Please login using your details")

